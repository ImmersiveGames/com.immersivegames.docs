from __future__ import annotations

import html
import re
import shutil
import unicodedata
from pathlib import Path

from docx import Document
from docx.document import Document as DocxDocument
from docx.oxml.ns import qn
from docx.table import Table
from docx.text.paragraph import Paragraph
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DOCX = ROOT / "Exemplos" / "GDD PEGA.docx"
TEMPLATE = ROOT / "templates" / "html-default"
OUTPUT = ROOT / "PEGA"
ASSET_DIR = OUTPUT / "assets" / "documents" / "gdd"
SOURCE_OUT = OUTPUT / "source" / "gdd.md"


def iter_block_items(parent: DocxDocument):
    body = parent.element.body
    for child in body.iterchildren():
        if child.tag == qn("w:p"):
            yield Paragraph(child, parent)
        elif child.tag == qn("w:tbl"):
            yield Table(child, parent)


def slugify(value: str, used: set[str]) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^\w\s-]", "", value, flags=re.UNICODE)
    value = re.sub(r"\s+", "-", value.strip().lower())
    value = value or "section"
    base = value
    index = 2
    while value in used:
        value = f"{base}-{index}"
        index += 1
    used.add(value)
    return value


def clean_text(value: str) -> str:
    value = value.replace("\x0b", " ")
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def paragraph_style(paragraph: Paragraph) -> str:
    return paragraph.style.name if paragraph.style is not None else ""


def heading_level(paragraph: Paragraph) -> int | None:
    style = paragraph_style(paragraph)
    if style == "Title":
        return 0
    match = re.match(r"Heading\s+(\d+)", style, re.IGNORECASE)
    if not match:
        return None
    return int(match.group(1))


def paragraph_image_ids(paragraph: Paragraph) -> list[str]:
    ids: list[str] = []
    for blip in paragraph._p.xpath(".//a:blip"):
        rid = blip.get(qn("r:embed")) or blip.get(qn("r:link"))
        if rid:
            ids.append(rid)
    return ids


def extract_image(doc: Document, rid: str, written: dict[str, str]) -> str | None:
    if rid in written:
        return written[rid]
    part = doc.part.related_parts.get(rid)
    if part is None:
        return None
    content_type = getattr(part, "content_type", "image/png")
    extension = content_type.split("/")[-1].lower().replace("jpeg", "jpg")
    if extension not in {"png", "jpg", "gif", "bmp", "webp", "svg"}:
        extension = "png"
    filename = f"gdd-image-{len(written) + 1:02d}.{extension}"
    target = ASSET_DIR / filename
    target.write_bytes(part.blob)
    try:
        with Image.open(target) as image:
            width, height = image.size
        if width <= 1 and height <= 1:
            target.unlink(missing_ok=True)
            written[rid] = ""
            return None
    except Exception:
        target.unlink(missing_ok=True)
        written[rid] = ""
        return None
    relative = f"assets/documents/gdd/{filename}"
    written[rid] = relative
    return relative


def list_level(paragraph: Paragraph) -> int | None:
    ppr = paragraph._p.pPr
    if ppr is None or ppr.numPr is None:
        return None
    ilvl = ppr.numPr.ilvl
    if ilvl is None:
        return 0
    try:
        return int(ilvl.val)
    except (TypeError, ValueError):
        return 0


def inline_runs(paragraph: Paragraph) -> str:
    parts: list[str] = []
    for run in paragraph.runs:
        text = run.text
        if not text:
            continue
        escaped = html.escape(text)
        if run.bold:
            escaped = f"<strong>{escaped}</strong>"
        if run.italic:
            escaped = f"<em>{escaped}</em>"
        if run.underline:
            escaped = f"<u>{escaped}</u>"
        parts.append(escaped)
    if not parts:
        return inline_markdown(paragraph.text)
    return "".join(parts).strip()


def inline_markdown(value: str) -> str:
    value = html.escape(clean_text(value))
    value = re.sub(r"`([^`]+)`", r"<code>\1</code>", value)
    return value


def paragraph_to_markdown(paragraph: Paragraph, image_refs: list[str]) -> list[str]:
    text = clean_text(paragraph.text)
    level = heading_level(paragraph)
    lines: list[str] = []
    if level == 0 and text:
        lines.append(f"# {text}")
    elif level and text:
        lines.append(f"{'#' * (level + 1)} {text}")
    elif text:
        indent_level = list_level(paragraph)
        if indent_level is not None:
            lines.append(f"{'  ' * indent_level}- {text}")
        else:
            lines.append(text)

    for image_ref in image_refs:
        lines.append(f"![GDD image]({image_ref})")
    return lines


def table_to_markdown(table: Table) -> list[str]:
    rows = []
    for row in table.rows:
        rows.append([clean_text(cell.text) for cell in row.cells])
    if not rows:
        return []
    width = max(len(row) for row in rows)
    normalized = [row + [""] * (width - len(row)) for row in rows]
    lines = ["| " + " | ".join(normalized[0]) + " |"]
    lines.append("| " + " | ".join("---" for _ in range(width)) + " |")
    for row in normalized[1:]:
        lines.append("| " + " | ".join(row) + " |")
    return lines


def table_to_html(table: Table) -> str:
    rows = []
    for row in table.rows:
        rows.append([clean_text(cell.text) for cell in row.cells])
    if not rows:
        return ""
    width = max(len(row) for row in rows)
    normalized = [row + [""] * (width - len(row)) for row in rows]
    out = ['<div class="docs-table-wrap"><table class="docs-table">']
    out.append("<thead><tr>")
    for cell in normalized[0]:
        out.append(f"<th>{inline_markdown(cell)}</th>")
    out.append("</tr></thead><tbody>")
    for row in normalized[1:]:
        out.append("<tr>")
        for cell in row:
            out.append(f"<td>{inline_markdown(cell)}</td>")
        out.append("</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)


def render_docx() -> tuple[str, str, str, int, int]:
    doc = Document(SOURCE_DOCX)
    ASSET_DIR.mkdir(parents=True, exist_ok=True)

    written_images: dict[str, str] = {}
    markdown_lines: list[str] = []
    html_out: list[str] = []
    sections: list[dict[str, str]] = []
    used_ids: set[str] = set()
    title = "PEGA Game Design Document"
    open_section = False
    list_stack: list[int] = []

    def close_lists(to_level: int = -1) -> None:
        while list_stack and list_stack[-1] > to_level:
            list_stack.pop()
            html_out.append("</ul>")

    def close_section() -> None:
        nonlocal open_section
        close_lists()
        if open_section:
            html_out.append("</section>")
            open_section = False

    for block in iter_block_items(doc):
        if isinstance(block, Table):
            close_lists()
            markdown_lines.extend(table_to_markdown(block))
            markdown_lines.append("")
            html_out.append(table_to_html(block))
            continue

        text = clean_text(block.text)
        image_refs: list[str] = []
        for rid in paragraph_image_ids(block):
            ref = extract_image(doc, rid, written_images)
            if ref:
                image_refs.append(ref)

        markdown_block = paragraph_to_markdown(block, image_refs)
        if markdown_block:
            markdown_lines.extend(markdown_block)
            markdown_lines.append("")

        level = heading_level(block)
        if level == 0 and text:
            title = text
            continue

        if level is not None and level > 0:
            if not text:
                close_lists()
                for image_ref in image_refs:
                    html_out.append(render_figure(image_ref))
                continue
            close_section()
            section_id = slugify(text, used_ids)
            sections.append({"id": section_id, "title": text})
            html_level = min(level + 2, 6)
            html_out.append(
                f'<section class="docs-section" id="{section_id}" data-title="{html.escape(text)}">'
                f"<h{html_level}>{inline_runs(block)}</h{html_level}>"
            )
            open_section = True
            for image_ref in image_refs:
                html_out.append(render_figure(image_ref))
            continue

        indent_level = list_level(block)
        if text and indent_level is not None:
            while list_stack and list_stack[-1] > indent_level:
                list_stack.pop()
                html_out.append("</ul>")
            if not list_stack or list_stack[-1] < indent_level:
                html_out.append("<ul>")
                list_stack.append(indent_level)
            html_out.append(f"<li>{inline_runs(block)}</li>")
        elif text:
            close_lists()
            html_out.append(f"<p>{inline_runs(block)}</p>")

        for image_ref in image_refs:
            close_lists()
            html_out.append(render_figure(image_ref))

    close_section()
    image_count = sum(1 for value in written_images.values() if value)
    return title, "\n".join(markdown_lines).strip() + "\n", "\n".join(html_out), image_count, len(sections)


def render_figure(src: str) -> str:
    match = re.search(r"(\d+)", Path(src).stem)
    label = f"GDD image {int(match.group(1))}" if match else "GDD image"
    return (
        f'<figure class="docs-figure docs-gdd-figure">'
        f'<img src="{html.escape(src)}" alt="{html.escape(label)}" loading="lazy">'
        f"<figcaption>{html.escape(label)}</figcaption>"
        f"</figure>"
    )


def build_html(title: str, body: str, image_count: int) -> str:
    intro = "Game Design Document renderizado como um pacote HTML offline a partir do documento Word original de PEGA."
    return f"""<!doctype html>
<html lang="pt-BR" data-theme="dark">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" href="css/variables.css">
  <link rel="stylesheet" href="css/typography.css">
  <link rel="stylesheet" href="css/layout.css">
  <link rel="stylesheet" href="css/components.css">
  <link rel="stylesheet" href="css/pega.css">
</head>
<body>
  <a class="docs-skip-link" href="#docs-main">Pular para o conteúdo</a>

  <div class="docs-topbar">
    <header class="docs-header">
      <div class="docs-header__brand">
        <span class="docs-header__logo-set" aria-hidden="true">
          <img class="docs-header__logo docs-header__logo--dark" src="assets/images/immersive-games-logo-full-white.png" alt="" width="180" height="65">
          <img class="docs-header__logo docs-header__logo--light" src="assets/images/immersive-games-logo-full-black.png" alt="" width="180" height="65">
        </span>
        <div>
          <h1>PEGA</h1>
        </div>
      </div>

      <div class="docs-header__tools">
        <label class="docs-search-label" for="docs-search-input">Buscar documentação</label>
        <input id="docs-search-input" class="docs-search-input" type="search" placeholder="Buscar no documento ativo..." autocomplete="off">
        <button class="docs-button docs-button--ghost" type="button" data-action="toggle-search-mode" aria-pressed="false">Global</button>
        <button class="docs-button docs-button--ghost" type="button" data-action="toggle-theme" aria-label="Alternar tema claro ou escuro">Tema</button>
        <button class="docs-button docs-button--ghost docs-mobile-only" type="button" data-action="toggle-sidebar" aria-expanded="false" aria-controls="docs-sidebar">Menu</button>
      </div>
    </header>

    <nav class="docs-tabs" role="tablist" aria-label="Document tabs">
      <button id="docs-tab-gdd" class="docs-tab is-active" type="button" role="tab" data-document-target="gdd" aria-selected="true" aria-controls="docs-panel-gdd">Game Design Document</button>
    </nav>
  </div>

  <div class="docs-search-status" id="docs-search-status" role="status" aria-live="polite">Busca pronta.</div>

  <div class="docs-shell">
    <aside class="docs-sidebar" id="docs-sidebar" aria-label="Navegação do documento">
      <div class="docs-sidebar__header">
        <span>Navegação</span>
      </div>
      <nav class="docs-sidebar__nav" data-sidebar-nav></nav>
      <div class="docs-sidebar__footer">
        <button class="docs-back-to-top" type="button" data-action="back-to-top">&uarr; Voltar ao topo</button>
      </div>
    </aside>

    <main class="docs-main" id="docs-main" tabindex="-1">
      <section class="docs-search-panel docs-content" data-search-panel hidden aria-labelledby="docs-search-panel-title">
        <div class="docs-search-panel__header">
          <p class="docs-kicker">Resultados de Busca</p>
          <h2 id="docs-search-panel-title">Resultados de busca</h2>
          <p data-search-summary>Digite no campo de busca para pesquisar no documento ativo.</p>
        </div>
        <div class="docs-search-results" data-search-results></div>
        <div class="docs-empty-state" data-search-empty hidden>
          <h2>Nenhum resultado encontrado.</h2>
          <p>Tente outro termo ou limpe a busca.</p>
        </div>
      </section>

      <section id="docs-panel-gdd" class="docs-document is-active" role="tabpanel" aria-labelledby="docs-tab-gdd" data-document="gdd" data-document-title="Game Design Document">
        <article class="docs-content">
          <header id="gdd-title" class="docs-page-header docs-gdd-hero">
            <p class="docs-kicker">Game Design Document</p>
            <h2>{html.escape(title)}</h2>
            <p>{html.escape(intro)}</p>
            <div class="docs-gdd-meta" aria-label="Document metadata">
              <span class="docs-badge">Português brasileiro</span>
              <span class="docs-badge">Fonte DOCX</span>
              <span class="docs-badge">Offline HTML</span>
              <span class="docs-badge">{image_count} imagens extraídas</span>
            </div>
          </header>

          <section class="docs-section" id="gdd-overview" data-title="Visão Geral">
            <h3>Visão Geral</h3>
            <div class="docs-callout docs-callout-info">
              <p class="docs-callout__title">Fonte principal</p>
              <p>Este HTML foi gerado a partir de <code>Exemplos/GDD PEGA.docx</code>. A versão Markdown normalizada está em <code>source/gdd.md</code>.</p>
            </div>
          </section>

          {body}
        </article>
      </section>
    </main>
  </div>

  <footer class="docs-footer">
    <p>PEGA GDD documentation package. Generated with <code>com.immersivegames.docs</code>.</p>
    <nav aria-label="Footer links">
      <a href="source/gdd.md">Markdown source</a>
      <a href="#gdd-title">Voltar ao topo</a>
    </nav>
  </footer>

  <script src="js/navigation.js"></script>
  <script src="js/search.js"></script>
  <script src="js/glossary.js"></script>
  <script src="js/ui.js"></script>
</body>
</html>
"""


def write_project_css() -> None:
    css = """/* PEGA GDD project additions. The default template remains the base theme. */
.docs-gdd-hero {
  background:
    linear-gradient(135deg, color-mix(in srgb, var(--docs-color-accent) 18%, transparent), transparent 45%),
    linear-gradient(135deg, var(--docs-color-surface-raised), var(--docs-color-surface));
}

.docs-gdd-meta {
  display: flex;
  flex-wrap: wrap;
  gap: var(--docs-spacing-sm);
  margin-top: var(--docs-spacing-md);
}

.docs-gdd-figure img {
  background: var(--docs-color-surface-soft);
  border: var(--docs-border-width) solid var(--docs-color-border);
  height: auto;
  margin: 0 auto;
  max-height: 34rem;
  object-fit: contain;
  width: auto;
}

.docs-table-wrap {
  overflow-x: auto;
}
"""
    (OUTPUT / "css" / "pega.css").write_text(css, encoding="utf-8")


def copy_template_assets() -> None:
    for folder in ("css", "js"):
        destination = OUTPUT / folder
        if destination.exists():
            shutil.rmtree(destination)
        shutil.copytree(TEMPLATE / folder, destination)

    images_destination = OUTPUT / "assets" / "images"
    icons_destination = OUTPUT / "assets" / "icons"
    images_destination.mkdir(parents=True, exist_ok=True)
    icons_destination.mkdir(parents=True, exist_ok=True)
    for file in (TEMPLATE / "assets" / "images").glob("*"):
        if file.is_file():
            shutil.copy2(file, images_destination / file.name)
    for file in (TEMPLATE / "assets" / "icons").glob("*"):
        if file.is_file():
            shutil.copy2(file, icons_destination / file.name)


def clear_document_assets() -> None:
    if ASSET_DIR.exists():
        shutil.rmtree(ASSET_DIR)
    ASSET_DIR.mkdir(parents=True, exist_ok=True)


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    (OUTPUT / "source").mkdir(parents=True, exist_ok=True)
    clear_document_assets()
    copy_template_assets()
    title, markdown, body, image_count, section_count = render_docx()
    SOURCE_OUT.write_text(markdown, encoding="utf-8")
    write_project_css()
    html_output = build_html(title, body, image_count)
    (OUTPUT / "index.html").write_text(html_output, encoding="utf-8")
    refs = re.findall(r'(?:src|href)="([^"]+)"', html_output)
    missing = []
    for ref in refs:
        if ref.startswith(("#", "http://", "https://", "mailto:")):
            continue
        if not (OUTPUT / ref).exists():
            missing.append(ref)
    print(f"Generated {OUTPUT / 'index.html'}")
    print(f"Source: {SOURCE_DOCX}")
    print(f"Extracted {image_count} images")
    print(f"Rendered {section_count} DOCX heading sections")
    print(f"HTML sections: open={html_output.count('<section')} close={html_output.count('</section>')}")
    print(f"Missing local references: {len(missing)}")
    if missing:
        for ref in missing[:20]:
            print(f"  - {ref}")


if __name__ == "__main__":
    main()
