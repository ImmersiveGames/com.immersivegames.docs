# Navigation System

**Project:** `com.immersivegames.docs`  
**Document Type:** Subsystem Specification  
**Status:** Draft  
**Version:** 0.1.0

---

## Purpose

The Navigation System defines how users locate, browse, and traverse documentation within a Documentation Project.

The Navigation System describes navigation concepts only. It does not define HTML, CSS, JavaScript, visual Components, icons, layout, animations, or renderer-specific implementation details.

Navigation is independent from presentation technology. A Renderer may present navigation differently for HTML, PDF, EPUB, wiki, or another output format while preserving the same navigation model.

## Core Philosophy

The Navigation System allows users to efficiently move through the knowledge contained within a Documentation Project.

Navigation derives from the editorial hierarchy defined by the Content System and from the rendered structure produced by the Rendering System. It never defines or modifies authored content.

The Content System owns the editorial model. The Rendering System transforms that model into output-specific structures. The Navigation System defines the conceptual navigation relationships that users need in order to move through those structures.

## Responsibilities

The Navigation System is responsible for defining:

- Document navigation.
- Chapter navigation.
- Section navigation.
- Subsection navigation.
- Current location.
- Navigation state.
- Deep links.
- Cross references.
- Table of Contents behavior.
- Breadcrumbs.
- Quick navigation.
- Search entry points.

The Navigation System is not responsible for rendering, visual presentation, theme design, or search implementation.

## Navigation Model

Navigation follows the editorial hierarchy defined by the Content System.

```text
Documentation Project
        |
        v
Document Navigation
        |
        v
Editorial Tree
        |
        v
Current Content
        |
        v
Navigation Shortcuts
```

The Documentation Project provides the root navigation context. Documents provide the primary navigation level. Chapters, Sections, and Subsections provide the traversable editorial tree inside the active Document. Current Content identifies the user's active location. Navigation Shortcuts provide optional paths for moving to related or adjacent locations.

The Navigation System must preserve the meaning and order of the editorial hierarchy. It may expose navigation relationships derived from rendered output, but it must not redefine Documents, Chapters, Sections, Subsections, or Content Blocks.

## Navigation Elements

### Document Navigation

Document Navigation allows users to switch between Documents within the same Documentation Project.

Examples include:

- Game Design Document.
- Engineering Documentation.
- User Manual.
- API Reference.
- Art Bible.
- Marketing Guide.

Documents are intended to become the primary navigation tabs in HTML Renderers. This is an expected renderer mapping, not a requirement that all Renderers use tabs or that tab behavior belongs to the Content System.

### Sidebar Navigation

Sidebar Navigation provides access to the editorial hierarchy of the currently selected Document.

The sidebar represents:

- Chapters.
- Sections.
- Subsections.

Only the active Document is displayed in a Document sidebar. Navigation between Documents belongs to Document Navigation.

The Navigation System defines which editorial entities may appear in the sidebar. It does not define the sidebar's visual layout, styling, icons, animation, or interaction implementation.

### Tree Navigation

Tree Navigation represents the nested structure of the active Document.

Tree Navigation may include:

- Expandable Chapters.
- Nested Sections.
- Recursive hierarchy.

The Navigation System defines the hierarchy and navigation relationships. The Rendering System and each Renderer determine how expandable controls, indentation, disclosure behavior, or fallback presentation appear in a specific output format.

### Table of Contents

The Table of Contents allows quick navigation within the currently displayed content.

The Table of Contents:

- Reflects headings in the current content.
- Is local to the current rendered content.
- Is independent from the sidebar hierarchy.

The sidebar helps users move through the active Document. The Table of Contents helps users move within the currently displayed content. A Renderer may present both, one, or neither depending on output capabilities, but the concepts remain separate.

### Breadcrumb

A Breadcrumb provides contextual awareness by representing the current navigation path.

Example:

```text
Engineering > Systems > Face System > Runtime
```

Breadcrumbs help users understand where the current content sits within the Documentation Project, active Document, and editorial hierarchy.

### Current Location

The Navigation System must always identify the currently active navigation element when the output format supports interactive or addressable navigation.

Current Location may identify:

- The active Document.
- The active Chapter.
- The active Section or Subsection.
- The active rendered content unit.

Clear Current Location improves orientation, reduces cognitive load, and helps users understand the relationship between the content they are reading and the broader Documentation Project.

### Navigation State

Navigation State describes persistent or recoverable navigation context.

Examples include:

- Active Document.
- Expanded Chapters.
- Current Section.
- Reading Position, when supported by the output format.

The Navigation System defines the concept of Navigation State. It does not define storage, browser behavior, local files, scripting, or any specific implementation mechanism.

### Deep Links

Every navigable heading should expose a stable anchor.

Deep links allow users to navigate directly to specific documentation locations, share precise references, and preserve access to important knowledge even when the rendered output is reorganized.

Deep-link stability depends on stable identifiers and predictable heading interpretation. Renderers are responsible for producing output-specific anchor representations.

### Cross References

Documentation may reference:

- Other Documents.
- Chapters.
- Sections.
- Subsections.
- Glossary terms.
- Assets.
- Rendered content units, when a Renderer exposes them.

The Navigation System defines the navigation relationships created by cross references. Reference validation and target resolution belong to the Cross-Reference Module or a possible future CrossReferenceSystem specification. Rendering is responsible for displaying the references in each output format.

### Quick Navigation

Quick Navigation defines optional shortcuts that help users move through adjacent or important locations.

Examples include:

- Back to Top.
- Previous Section.
- Next Section.
- Previous Chapter.
- Next Chapter.
- Jump to Table of Contents.

The Navigation System defines these navigation capabilities. It does not define buttons, icons, keyboard shortcuts, visual placement, animation, or layout.

### Search Entry Points

Search Entry Points define where search results may navigate users.

Search results may target:

- Documents.
- Chapters.
- Sections.
- Subsections.
- Rendered content units exposed by a Renderer.
- Glossary terms.

The Navigation System defines the valid navigation destinations for search results. Indexing, query behavior, ranking, and search-result generation belong to the Search System.

## Navigation Mapping

| Editorial Element     | Navigation Element | Purpose             |
|-----------------------|--------------------|---------------------|
| Documentation Project | Root Context       | Overall scope       |
| Document              | Primary Navigation | Switch publications |
| Chapter               | Sidebar            | Major topics        |
| Section               | Sidebar Child      | Topic navigation    |
| Subsection            | Nested Navigation  | Detailed navigation |
| Content Block         | None               | Readable content    |

Content Blocks are not primary navigation elements. A Renderer may create anchors or references to specific Content Blocks when supported by a separate contract, but the Navigation System does not require Content Blocks to appear in primary navigation structures.

## Accessibility

Navigation must support predictable, understandable movement through documentation.

Navigation principles include:

- Predictable hierarchy.
- Consistent navigation behavior.
- Keyboard navigability where the output format supports interaction.
- Stable anchors.
- Clear Current Location.
- Meaningful navigation labels.
- Preservation of editorial order.

These principles define accessibility expectations without prescribing HTML, CSS, JavaScript, ARIA attributes, focus behavior, or other renderer-specific implementation details.

## Renderer Independence

The Navigation System defines navigation concepts. The Rendering System determines how those concepts are represented in each output format.

Supported or future outputs may include:

- HTML.
- PDF.
- EPUB.
- Wiki.

Each output may present navigation differently while following the same navigation model. For example, an HTML Renderer may expose tabs, sidebars, breadcrumbs, and local tables of contents, while a PDF Renderer may expose bookmarks, section headings, internal links, and a printed table of contents.

Renderer-specific controls must remain derivative. They must not become the source of the Documentation Project's editorial hierarchy or content structure.

## Design Decisions

### Navigation Consumes Content Structure

**Decision:** Navigation derives from the editorial hierarchy defined by the Content System and from structures produced by the Rendering System.

**Rationale:** Users need navigation that reflects authored knowledge, but navigation must remain separate from content authoring and output implementation.

**Consequence:** Navigation can adapt to each Renderer without redefining Documents, Chapters, Sections, Subsections, or Content Blocks.

### Documents Are the Primary Navigation Level

**Decision:** Documents provide the primary navigation level inside a Documentation Project.

**Rationale:** A Documentation Project may contain multiple independent publications for different audiences, disciplines, or purposes.

**Consequence:** Users can switch between major publications without treating Chapters or rendered content units as project-level roots.

### Sidebar Navigation Is Scoped to the Active Document

**Decision:** Sidebar Navigation represents the editorial hierarchy of the active Document only.

**Rationale:** Showing every Chapter and Section from every Document would make navigation noisy and reduce orientation.

**Consequence:** Document Navigation and Sidebar Navigation remain separate concerns.

### Table of Contents Is Independent from Sidebar Navigation

**Decision:** The Table of Contents is local to the currently displayed content and independent from the sidebar hierarchy.

**Rationale:** The sidebar supports movement through a Document, while the Table of Contents supports movement within the current rendered content.

**Consequence:** Renderers can present both structures without forcing them to duplicate each other.

### Quick Navigation Belongs to Navigation

**Decision:** Quick Navigation is part of the Navigation System rather than a rendering-only concern.

**Rationale:** Previous, next, back-to-top, and jump relationships express movement through documentation, even when their visual controls differ by Renderer.

**Consequence:** Renderers choose presentation, but the navigation capabilities and their meaning remain stable.

### Rendering Remains Independent

**Decision:** The Navigation System must not define visual controls or renderer-specific implementation details.

**Rationale:** Navigation concepts must remain portable across HTML, PDF, EPUB, wiki, and future outputs.

**Consequence:** Renderer implementations may differ while preserving shared navigation semantics.

## Out of Scope

The Navigation System does not define:

- HTML.
- CSS.
- JavaScript.
- Icons.
- Animations.
- Theme design.
- Visual Components.
- Rendering implementation.
- Search indexing.
- Search ranking.
- Markdown authoring rules.
- Content structure ownership.

These concerns belong to their respective subsystem specifications.

## Future Extensions

The Navigation System may later support:

- Recently Visited.
- Favorites.
- Reading Progress.
- Multiple Navigation Modes.
- Version Navigation.
- User Bookmarks.
- Navigation History.

These extensions must preserve the established navigation model and must not make navigation responsible for authoring content or rendering presentation.

# Related Documents

- [DocumentationFramework.md](DocumentationFramework.md) — Defines the framework vision, principles, and intended documentation experience.
- [FrameworkArchitecture.md](FrameworkArchitecture.md) — Defines the root architecture and subsystem relationships.
- [DocumentationStandards.md](DocumentationStandards.md) — Defines the authoring and maintenance standards applied to this specification.
- [Terminology.md](Terminology.md) — Defines the official vocabulary used by this specification.
- [ContentSystem.md](ContentSystem.md) — Defines the editorial hierarchy consumed by the Navigation System.
- [ComponentLibrary.md](ComponentLibrary.md) — Defines the reusable semantic documentation components consumed by Renderers.
- [RenderingSystem.md](RenderingSystem.md) — Planned specification for Renderer contracts and output lifecycle.
- [SearchSystem.md](SearchSystem.md) — Planned specification for search indexing, query behavior, and result contracts.

# Revision History

| Version | Date       | Author          | Description                              |
|---------|------------|-----------------|------------------------------------------|
| 0.1.1   | 2026-06-25 | Immersive Games | Refined renderer-independent navigation terminology. |
| 0.1.0   | 2026-06-25 | Immersive Games | Initial Navigation System specification. |
