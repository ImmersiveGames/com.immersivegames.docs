# Rendering System

**Project:** `com.immersivegames.docs`  
**Document Type:** Subsystem Specification  
**Status:** Draft  
**Version:** 0.1.0

---

## Purpose

The Rendering System defines how structured Markdown documentation is transformed into standardized offline documentation output.

The first official Renderer target is a single-page offline HTML documentation package inspired by the Face System documentation layout. HTML is the first Renderer target, not the Documentation Framework itself.

The Rendering System does not define documentation content, editorial hierarchy, visual theme, or authoring rules. Those responsibilities belong to the Content System, Navigation System, Component Library, and Theme System.

The Rendering System defines Renderer responsibilities, standard input expectations, output structure, semantic output mapping, local asset organization, fallback behavior, and expected offline behavior.

## Core Philosophy

The Rendering System exists to make authored documentation readable, navigable, consistent, and distributable.

Documentation authors and AI agents write Markdown.

The Rendering System transforms that Markdown into human-readable output.

The default output is an offline HTML documentation package.

The Renderer must preserve the structure and intent defined by the Content System, Navigation System, and Component Library, while providing the structural hooks required by the Theme System.

The Renderer must not become the source of truth.

Markdown remains the source of truth.

## Responsibilities

The Rendering System is responsible for defining:

- Standard Renderer input expectations.
- Standard Renderer output structure.
- Offline HTML output requirements.
- Document-to-tab mapping for the default HTML Renderer.
- Chapter and Section navigation output.
- Sidebar output expectations.
- Table of Contents output expectations.
- Component-to-output semantic mapping.
- Local asset handling.
- Search and glossary output integration points.
- Back-to-top support.
- Fallback behavior for unsupported Components.
- Separation between structure, style, and behavior.

The Rendering System is not responsible for:

- Writing documentation content.
- Defining editorial hierarchy.
- Defining official Markdown component syntax.
- Defining visual colors, fonts, spacing, or icons.
- Defining CSS theme details.
- Defining JavaScript implementation internals.
- Managing project planning.
- Replacing the Theme System.

## Core Model

The default rendering flow is:

```text
Structured Markdown
        |
        v
Renderer
        |
        v
Offline HTML Package
        |
        v
Human-readable Documentation
```

The Renderer consumes Markdown that follows the official documentation rules.

The Renderer produces a standardized offline output that can be opened locally without a web server.

## Standard Input

The Renderer expects Markdown files organized according to the framework.

Each Markdown file represents a Document.

Each Document uses the heading hierarchy defined by the Content System:

```text
# Document Title
## Chapter
### Section
#### Subsection
##### Additional nesting
```

The Renderer must support:

- Standard Markdown.
- Callout Syntax.
- Structured Block Syntax.
- Standard Markdown links.
- Local asset references.

The Renderer must not require authors to write raw HTML for visual presentation.

## Standard Output

The default Renderer output is a complete offline HTML documentation package.

Recommended output structure:

```text
output/
|-- index.html
|-- css/
|   |-- variables.css
|   |-- typography.css
|   |-- layout.css
|   `-- components.css
|-- js/
|   |-- navigation.js
|   |-- search.js
|   |-- glossary.js
|   `-- ui.js
`-- assets/
    |-- images/
    |-- icons/
    `-- downloads/
```

The Renderer may generate this structure directly or use an equivalent internal process, but the final output must remain portable and offline-friendly.

## Offline-First Requirement

The default HTML output must work offline.

Requirements:

- No web server required.
- No external CDN required.
- No remote JavaScript dependencies.
- No remote CSS dependencies.
- No remote font dependencies.
- All required assets must use local relative paths.
- The documentation must be openable through `index.html`.

External links may exist as documentation references, but the documentation itself must remain functional without internet access.

## HTML Output Layout

The default HTML Renderer should produce a layout inspired by the Face System documentation.

Recommended layout:

```text
Header
Document Tabs
Main Documentation Shell
    Sidebar
    Main Content
    Local Table of Contents
Footer
Back to Top
```

Conceptual structure:

```text
+------------------------------------------------+
| Header                                         |
| Project name | Version | Search                |
+------------------------------------------------+
| Document Tabs                                  |
| GDD | Engineering | Art Bible | Marketing      |
+---------------+--------------------+-----------+
| Sidebar       | Main Content       | TOC       |
| Chapters      | Rendered Markdown  | Current   |
| Sections      | Components         | Content   |
+---------------+--------------------+-----------+
| Footer                                         |
+------------------------------------------------+
```

This layout defines structure only.

Visual appearance belongs to the Theme System.

## Header

The Header provides global documentation context.

Expected content:

- Project title.
- Documentation title, when different from project title.
- Documentation version.
- Search entry point.

Optional content:

- Last updated date.
- Framework version.
- Project version.
- Repository or project link.

The Header should remain consistent across all rendered Documentation Projects.

## Document Tabs

Document Tabs provide primary navigation between Documents.

Mapping:

```text
Document = Top-level tab
```

Examples:

- Game Design Document.
- Engineering Documentation.
- Art Bible.
- Narrative Bible.
- Marketing Guide.
- Production Guide.
- User Manual.
- API Reference.

The Renderer should display the active Document clearly.

Tabs are the default HTML representation. Other Renderers may represent Documents differently.

## Sidebar

The Sidebar represents the editorial hierarchy of the active Document.

Mapping:

```text
Chapter = Primary sidebar item
Section = Nested sidebar item
Subsection = Deeper nested sidebar item
```

The Sidebar must show only the active Document.

Navigation between Documents belongs to Document Tabs.

The Sidebar must preserve the order of headings in the source Markdown.

## Main Content

The Main Content area displays the rendered content of the active Document or the currently selected rendered content unit.

The Main Content area must support:

- Standard Markdown.
- Information callouts.
- Structured Blocks.
- Code Blocks.
- Tables.
- Images.
- Links.
- Local asset references.

The Main Content area must remain readable even when advanced Components degrade to simpler representations.

## Local Table of Contents

The local Table of Contents provides navigation inside the currently displayed rendered content.

The Table of Contents is separate from the Sidebar.

Rules:

- Sidebar represents the active Document hierarchy.
- Table of Contents represents the current rendered content.
- Table of Contents should reflect local headings.
- Table of Contents should help users jump within long content sections.

The Renderer may omit the Table of Contents in constrained layouts, but the default HTML Renderer should include it when space allows.

## Footer

The Footer provides documentation Metadata.

Expected content:

- Project name.
- Documentation version.
- Last updated date, when available.
- Generated with `com.immersivegames.docs`.

Optional content:

- Copyright notice.
- Repository link.
- License reference.
- Build or generation timestamp.

## Back to Top

The default HTML output should provide a quick way to return to the top of the current rendered content.

The Rendering System defines the need for this capability.

The Theme System and implementation decide whether this appears as:

- A floating button.
- A footer link.
- An inline control.
- Another accessible navigation shortcut.

## Component Rendering

The Renderer must understand the Component categories defined by the Component Library.

The Renderer must support:

- Standard Markdown for Basic Components.
- Callout Syntax for Information Components.
- Structured Block Syntax for Extended or structured Components.

The Renderer must not require authors to write raw HTML to produce visual Components.

## Standard Markdown Rendering

Basic Components should be rendered using normal semantic output for the target format.

For the default HTML Renderer, expected semantic output includes:

| Markdown Element | Expected Semantic Output                     |
|------------------|----------------------------------------------|
| Heading          | Heading element with stable anchor           |
| Paragraph        | Paragraph block                              |
| List             | List block                                   |
| Table            | Table block                                  |
| Quote            | Quote block                                  |
| Code Block       | Code block with language hint when available |
| Inline Code      | Inline code element                          |
| Link             | Link element                                 |
| Image            | Image or figure element                      |

The exact styling belongs to the Theme System.

## Callout Rendering

Information Components use Callout Syntax.

Example Markdown:

```md
> [!WARNING]
> Changing this ID may break existing animation references.
```

Expected semantic class pattern for the default HTML Renderer:

```text
docs-callout
docs-callout-warning
```

Supported callout types:

- `NOTE`
- `INFO`
- `TIP`
- `WARNING`
- `IMPORTANT`
- `SUCCESS`
- `EXAMPLE`
- `BEST_PRACTICE`

The Renderer should preserve:

- Callout type.
- Optional title.
- Callout content.
- Readable fallback when styling is unavailable.

The Renderer must not define the final callout colors, icons, or spacing. Those belong to the Theme System.

## Structured Block Rendering

Structured Components use fenced semantic blocks.

Example Markdown:

```md
:::decision
**Decision:** Use Markdown as the source of truth.

**Reason:** Markdown is easy to edit, review, version, and render.

**Status:** Approved
:::
```

Expected semantic class pattern for the default HTML Renderer:

```text
docs-block
docs-block-decision
```

Structured Block names must use `lowercase-kebab-case`.

The Renderer should preserve:

- Component type.
- Structured content.
- Field labels, when present.
- Readable fallback when no specialized rendering exists.

## Component Fallback

Unsupported Extended Components must degrade gracefully.

Fallback behavior:

- Preserve all readable content.
- Preserve the Component name when useful.
- Avoid breaking the Document.
- Avoid hiding information.
- Avoid requiring raw HTML.

Example fallback:

```text
[decision]

Decision: Use Markdown as the source of truth.

Reason: Markdown is easy to edit, review, version, and render.

Status: Approved.
```

A Renderer that does not implement a specialized visual representation must still produce readable documentation.

## Semantic Class Expectations

The default HTML Renderer should emit semantic classes that allow the Theme System to style Components consistently.

Recommended class naming convention:

```text
docs-[element]
docs-[element]-[variant]
```

Examples:

```text
docs-header
docs-tabs
docs-sidebar
docs-main
docs-toc
docs-footer
docs-callout
docs-callout-warning
docs-block
docs-block-decision
docs-code
docs-table
docs-figure
```

These class names define semantic structure only.

The Theme System defines visual appearance.

## Search Integration

The Rendering System should provide output hooks for offline search.

The Search System defines indexing, query behavior, ranking, and search result contracts.

The Renderer is responsible for providing the output structure and local assets needed to expose search in the output.

Expected search entry point:

- Header search field.

Expected search destinations:

- Documents.
- Chapters.
- Sections.
- Subsections.
- Glossary terms.

Search must remain offline.

## Glossary Integration

The Rendering System should provide output hooks for glossary display.

The Glossary System defines glossary data, term rules, definitions, aliases, and relationships.

The Renderer may expose glossary content as:

- A dedicated tab.
- A modal or panel.
- An integrated section.
- A searchable glossary view.

The default HTML output should support an integrated glossary experience similar to the Face System documentation.

## Asset Handling

The Renderer must preserve local asset references.

Supported asset types may include:

- Images.
- Icons.
- Downloads.
- Diagrams.
- Local video files.
- Reference files.

Assets must be copied or referenced using stable relative paths.

The Renderer must not depend on remote assets for core documentation functionality.

## JavaScript Behavior

The default HTML Renderer may use local JavaScript for:

- Document tab switching.
- Sidebar navigation.
- Collapsible navigation groups.
- Search UI.
- Glossary UI.
- Back-to-top behavior.
- Current location highlighting.
- Local Table of Contents behavior.

JavaScript must remain local.

The Rendering System defines allowed behavior categories, not implementation internals.

## CSS Responsibility Boundary

The Renderer may emit semantic classes and structural wrappers.

The Renderer must not define visual identity.

The Theme System owns:

- Colors.
- Fonts.
- Spacing.
- Shadows.
- Borders.
- Visual hierarchy.
- Responsive styling.
- Component appearance.
- Dark or light Theme decisions.

The Rendering System owns:

- Output structure.
- Semantic class names.
- Component placement.
- Required layout regions.
- Local file organization.

## Default Visual Direction

The default HTML output should be visually inspired by the Face System documentation.

Expected direction:

- Dark documentation Theme.
- Strong Header area.
- Clear Document Tabs.
- Left Sidebar for Document navigation.
- Central content area.
- Right local Table of Contents.
- Visible callouts.
- Readable Code Blocks.
- Legible Tables.
- Integrated glossary.
- Offline search.
- Footer with version Metadata.

Exact visual design belongs to the Theme System.

## Design Decisions

### Single Offline HTML Entry Point

**Decision:** The default Renderer should generate a single `index.html` entry point.

**Rationale:** A single offline entry point is easy to distribute, open locally, package with tools, and ship with assets.

**Consequence:** Document navigation should be handled inside the generated documentation shell rather than through multiple independent HTML pages.

### Documents Become Top-Level Tabs

**Decision:** Documents are represented as the primary navigation level in the default HTML Renderer.

**Rationale:** A Documentation Project may contain multiple independent Documents, such as a Game Design Document, Engineering Documentation, Art Bible, User Manual, and API Reference.

**Consequence:** Users can switch between major documentation areas without losing the project context.

### Sidebar Is Scoped to Active Document

**Decision:** The Sidebar displays the hierarchy of the active Document only.

**Rationale:** Showing every Document hierarchy at once would create noisy navigation.

**Consequence:** Document navigation and Document-internal navigation remain separate.

### Theme Is Separate from Rendering

**Decision:** The Rendering System emits structure and semantic classes, while the Theme System defines visual styling.

**Rationale:** This allows the same Renderer structure to support different visual Themes in the future.

**Consequence:** CSS details must not be treated as Rendering System architecture.

### Components Render Semantically

**Decision:** Components are rendered according to their semantic meaning.

**Rationale:** A Warning, Decision, Timeline, or Risk should preserve meaning regardless of visual Theme.

**Consequence:** Unsupported Components must degrade to readable content rather than failing.

## Out of Scope

The Rendering System does not define:

- Documentation content.
- Project-specific writing.
- Editorial hierarchy rules.
- Official Component list.
- Final visual Theme.
- Color palette.
- Typography choices.
- CSS styling details.
- Bootstrap usage.
- Raw HTML authoring.
- Parser implementation details.
- External hosting.
- Server-side rendering.

## Future Extensions

Possible future extensions:

- Multiple HTML output modes.
- Multi-page HTML output.
- Print-friendly output.
- PDF export.
- EPUB export.
- Version selector.
- Theme selector.
- Renderer compatibility reports.
- Component support matrix.
- Automatic link validation.
- Build-time diagnostics.
- Generated search index.
- Generated glossary index.

These extensions must preserve the source-of-truth Markdown workflow.

# Related Documents

- [DocumentationFramework.md](DocumentationFramework.md) - Defines the framework vision, principles, and intended documentation experience.
- [FrameworkArchitecture.md](FrameworkArchitecture.md) - Defines the root architecture and subsystem relationships.
- [DocumentationStandards.md](DocumentationStandards.md) - Defines the documentation standards used by this specification.
- [Terminology.md](Terminology.md) - Defines the official vocabulary used by this specification.
- [ContentSystem.md](ContentSystem.md) - Defines the editorial hierarchy consumed by the Renderer.
- [NavigationSystem.md](NavigationSystem.md) - Defines the navigation concepts represented by the Renderer.
- [ComponentLibrary.md](ComponentLibrary.md) - Defines the Components and Markdown usage conventions supported by the Renderer.
- [AssetSystem.md](AssetSystem.md) - Defines local asset organization, references, validation, and packaging expectations.
- [ThemeSystem.md](ThemeSystem.md) - Defines visual identity, Theme Modes, typography direction, and Component styling responsibilities.
- [SearchSystem.md](SearchSystem.md) - Defines offline search behavior, Search Results, and Search Index expectations.
- [GlossarySystem.md](GlossarySystem.md) - Defines Glossary Terms, definitions, and glossary output expectations.

# Revision History

| Version | Date       | Author          | Description                             |
|---------|------------|-----------------|-----------------------------------------|
| 0.1.0   | 2026-06-30 | Immersive Games | Initial Rendering System specification. |
