# HTML Default Template

**Project:** `com.immersivegames.docs`  
**Template:** Default static HTML documentation template  
**Status:** Prototype  
**Version:** 0.1.0

---

## Purpose

This folder contains the first functional static HTML template for the Immersive Games Documentation Framework.

It demonstrates the default generated documentation experience that future agents and tools will use when converting structured Markdown documentation into readable offline HTML.

This template is not a Markdown renderer or generator yet.

## Current Status

This is the first functional static template prototype.

It is self-contained, offline-friendly, and can be opened directly from:

```text
templates/html-default/index.html
```

No server, package manager, build pipeline, CDN, remote font service, or external dependency is required.

## File Structure

```text
templates/html-default/
|-- README.md
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
    |-- icons/
    `-- images/
```

## CSS Responsibilities

- `variables.css` defines Theme Tokens, dark and light Theme Modes, spacing, radius, typography, layout, breakpoint, and z-index tokens.
- `typography.css` defines text, headings, links, code, tables, captions, and metadata typography.
- `layout.css` defines the documentation shell, Header, Document Tabs, Sidebar, Main Content, Local Table of Contents, Footer, Back to Top, and responsive behavior.
- `components.css` defines callouts, structured blocks, tables, figures, badges, glossary terms, search results, empty states, navigation cards, and related-document blocks.

## JavaScript Responsibilities

- `navigation.js` handles Document tab switching, sidebar and Local Table of Contents state, current section highlighting, keyboard-friendly tab navigation, and Back to Top.
- `search.js` implements offline client-side active Document Search and a lightweight Global Search result list.
- `glossary.js` implements simple glossary filtering and related-term navigation.
- `ui.js` handles Theme toggle, mobile Sidebar toggle, mobile Table of Contents toggle, and small UI behavior.

## Framework Mapping

- Content System: sample Documents are represented by static HTML panels.
- Navigation System: Document Tabs, Sidebar, Local Table of Contents, and Back to Top demonstrate navigation behavior.
- Component Library: Basic Components, callouts, and Structured Blocks are represented with semantic `docs-*` classes.
- Rendering System: the template follows the default offline HTML layout structure.
- Theme System: visual styling uses Theme Tokens and supports Dark Theme and Light Theme.
- Search System: offline active Document Search follows the Face System baseline behavior.
- Glossary System: the Glossary tab demonstrates term anchors and filtering.
- Asset System: local placeholder assets are referenced through relative paths.

## Limitations

- This template uses handwritten static HTML content.
- It does not parse Markdown.
- It does not generate HTML from Markdown.
- It does not create a Search Index file.
- It does not include build tooling.
- It does not include package manager configuration.

Future agents and tools should use this template as the base structure for generated documentation output.
