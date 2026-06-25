# Content System

**Project:** `com.immersivegames.docs`  
**Document Type:** Subsystem Specification  
**Status:** Draft  
**Version:** 0.1.0

---

## Purpose

The Content System defines how documentation authors organize knowledge.

It is an editorial model. It is not an HTML model, a Page model, or a renderer-specific file model. The Content System remains independent from every Renderer.

Markdown documents are the authoritative source of authored content. The Rendering System consumes the editorial structure defined by this specification and transforms it into HTML, PDF, or another supported output format.

## Core Philosophy

Documentation should be authored in the same conceptual form used by technical books and structured technical documents.

Authors organize information through the following editorial hierarchy:

```text
Documentation Project
        |
        v
Documents
        |
        v
Chapters
        |
        v
Sections
        |
        v
Subsections
        |
        v
Content Blocks
```

The hierarchy expresses editorial meaning. It does not prescribe output files, routes, screens, tabs, sidebars, or visual layout.

The Rendering System is responsible for interpreting this hierarchy for a target format. A Renderer may map the same structure differently according to the capabilities and conventions of HTML, PDF, or another output.

## Editorial Hierarchy

### Documentation Project

A Documentation Project represents the complete documentation for a product, system, organization, or other documented subject.

Examples include:

- A Unity Asset.
- A complete game project.
- An internal framework.
- An SDK.
- Company documentation.

A Documentation Project contains one or more Documents.

### Document

A Document is the highest editorial unit inside a Documentation Project. Each Document is an independent publication with its own subject, title, structure, and intended audience.

Examples include:

- Game Design Document.
- Engineering Documentation.
- User Manual.
- Technical Documentation.
- API Reference.
- Narrative Bible.
- Art Bible.
- Audio Guide.
- Marketing Guide.
- Production Guide.
- Changelog.

Documents are intended to become primary navigation tabs in the HTML Renderer. This mapping is a Renderer decision and does not make tabs part of the Content System.

### Chapter

A Chapter is a major subject division within a Document.

For Engineering Documentation, Chapters may include:

- Architecture.
- Systems.
- Runtime.
- Performance.

For a Game Design Document, Chapters may include:

- Vision.
- Gameplay.
- Progression.
- Economy.

For a User Manual, Chapters may include:

- Installation.
- Quick Start.
- Workflow.

Chapters are intended to become primary entries in a Document sidebar in the HTML Renderer. This expected mapping does not make sidebar behavior part of the Content System.

### Section

A Section explains a specific subject within a Chapter or another Section.

An Architecture Chapter may contain Sections such as:

- Overview.
- Responsibilities.
- Runtime Flow.
- Data Flow.

A Workflow Chapter may contain Sections such as:

- Creating Atlases.
- Creating FaceStates.
- Creating FaceAnimations.

Sections may recursively contain nested Sections. A nested Section may be described as a Subsection for editorial clarity.

No fixed Section nesting limit exists in the Content System. Authors should use only the depth required to communicate the subject clearly. Renderers may impose presentation constraints or fallback behavior without changing the underlying hierarchy.

### Subsection

A Subsection is a Section nested inside another Section.

The term describes a Section's relative editorial position rather than a separate entity type. A Subsection may contain additional nested Sections and Content Blocks.

### Content Block

A Content Block is an atomic information unit within a Section, Subsection, or another context explicitly permitted by the Content System.

Examples include:

- Paragraph.
- List.
- Table.
- Image.
- Diagram.
- Quote.
- Code Block.
- Video Reference.
- Download Link.

Content Blocks contain information. They never contain Documents, Chapters, Sections, or Subsections.

### Component

A Component is a reusable semantic structure built from one or more Content Blocks.

Examples include:

- Note.
- Warning.
- Tip.
- Callout.
- API Method.
- Parameter Table.
- Timeline.
- Step List.
- Feature Card.

The Component Library defines all official Components, their data contracts, composition rules, and fallback behavior. The Content System defines where Components participate in the editorial hierarchy but does not redefine individual Component contracts.

## Markdown Authoring Model

Markdown is the official authoring language and the source of truth for framework content.

The standard heading hierarchy is:

```markdown
# Document Title

## Chapter

### Section

#### Subsection

##### Additional nesting
```

Regular Markdown elements become Content Blocks. Semantic extensions recognized by the framework may become Components when they conform to the Component Library.

This model allows human authors and AI agents to produce documentation naturally while giving the Rendering System sufficient structure to derive rendered organization. Renderers must consume Markdown semantics without making generated output authoritative.

### Heading Interpretation

The first-level heading identifies the Document title.

Second-level headings identify Chapters.

Third-level and deeper headings identify recursively nested Sections. The term Subsection may be used for any Section nested beneath another Section.

Heading levels must not be skipped when doing so would make the editorial hierarchy ambiguous.

## Responsibilities

The Content System is responsible for:

- Defining the editorial hierarchy.
- Defining Document organization.
- Defining Markdown authoring rules.
- Defining the structural role of Content Blocks.
- Defining how Components participate in authored content.
- Preserving authored knowledge independently from any Renderer.
- Providing the authoring model consumed by the Rendering System.

## Out of Scope

The Content System does not define:

- HTML.
- CSS.
- JavaScript.
- Output Pages or routes.
- Navigation behavior.
- Search behavior.
- Themes or visual identity.
- Rendering behavior.
- Visual layout.
- Renderer-specific file structures.
- Individual Component contracts.

These concerns belong to their respective subsystem specifications.

## Design Decisions

### Documentation Uses an Editorial Hierarchy

**Decision:** Documentation is modeled as Documents, Chapters, recursively nested Sections, and Content Blocks.

**Rationale:** This structure matches how authors naturally organize technical books and long-form technical documents. It keeps authoring concepts stable when output formats change.

**Consequence:** Renderers translate editorial units into output-specific structures instead of requiring authors to write for a particular presentation.

### Markdown Is the Source of Truth

**Decision:** Markdown is the official authoring language and authoritative content source.

**Rationale:** Markdown is portable, human-readable, version-control friendly, and natural for both human authors and AI agents.

**Consequence:** Generated HTML, PDF, or other output is derivative and must not replace the Markdown source.

### HTML Is Only a Renderer

**Decision:** HTML does not define the Content System.

**Rationale:** Coupling authored content to HTML would make the editorial model dependent on browser presentation and obstruct future output formats.

**Consequence:** HTML concepts such as tabs, sidebars, routes, and files are mappings performed by the HTML Renderer.

### Documents Are Independent Authoring Units

**Decision:** A Documentation Project may contain multiple independent Documents.

**Rationale:** A product may require publications for different audiences, disciplines, and purposes while remaining part of one Documentation Project.

**Consequence:** Each Document can maintain its own title, Chapters, Sections, and editorial focus while sharing project-level Metadata and framework standards.

### Sections Are Recursive

**Decision:** Sections may contain nested Sections without a fixed architectural depth limit.

**Rationale:** Documentation subjects vary in complexity, and a fixed depth would constrain large or specialized publications.

**Consequence:** The editorial model scales without introducing new entity types for every nesting depth. Renderers remain responsible for presenting deep structures accessibly.

## Future Extensions

The Content System may later support:

- Reusable Document templates.
- Document inheritance.
- Shared content.
- Localization.
- Conditional content.
- Transclusion.

These extensions must preserve the established editorial hierarchy and keep Markdown content independent from Renderer implementation.

# Related Documents

- [DocumentationFramework.md](DocumentationFramework.md) — Defines the framework vision and authoring-first philosophy.
- [FrameworkArchitecture.md](FrameworkArchitecture.md) — Defines the root architecture and subsystem relationships.
- [DocumentationStandards.md](DocumentationStandards.md) — Defines the standards and governance rules applied to this specification.
- [Terminology.md](Terminology.md) — Defines the official vocabulary used by this specification.
- [ComponentLibrary.md](ComponentLibrary.md) — Planned specification for official semantic Components.
- [NavigationSystem.md](NavigationSystem.md) — Planned specification for navigation derived from rendered structure.
- [RenderingSystem.md](RenderingSystem.md) — Planned specification for consuming the editorial model and producing outputs.

# Revision History

| Version | Date       | Author          | Description                          |
|---------|------------|-----------------|--------------------------------------|
| 0.1.1   | 2026-06-25 | Immersive Games | Validated consistency with the authoring-first architecture. |
| 0.1.0   | 2026-06-25 | Immersive Games | Initial Content System specification. |
