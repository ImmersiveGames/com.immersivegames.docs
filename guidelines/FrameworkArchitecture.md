# Framework Architecture

**Project:** `com.immersivegames.docs`  
**Document Type:** Root Architecture Specification  
**Status:** Draft  
**Version:** 0.1.0

---

## 1. Vision

`com.immersivegames.docs` is an offline-first documentation framework for designing, organizing, rendering, distributing, and maintaining documentation across Immersive Games projects.

The framework establishes a shared documentation model, information architecture, navigation model, semantic component system, visual language, and set of quality standards. Its purpose is to make documentation consistent and portable without coupling project-specific knowledge to a particular presentation technology.

The framework is not an HTML template. Offline HTML is the first renderer of the framework and one implementation of its rendering contracts. The architecture must remain capable of supporting other renderers without requiring the documentation model to be redesigned.

---

## 2. Purpose

This document defines the root architecture of `com.immersivegames.docs`. It establishes:

- The primary architectural concepts and terminology.
- The root entity from which documentation is composed.
- The framework layers and their dependency direction.
- The core modules and their responsibilities.
- The boundaries between framework-owned and project-owned concerns.
- The architectural decisions that future specifications and implementations must preserve.
- The sequence of architecture documents required to refine this specification.

This document is the primary architectural reference for developers and AI agents contributing to the project. More specific architecture documents may refine the contracts defined here, but they must not contradict them without an explicit architecture decision and a corresponding update to this document.

The framework must support documentation such as:

- Technical documentation.
- User manuals and workflow guides.
- Unity Asset Store package documentation.
- API and integration references.
- Game Design Documents.
- Narrative, art, and audio direction documents.
- Internal production and engineering documentation.
- Architecture specifications and decision records.
- Glossaries, roadmaps, and changelogs.

---

## 3. Responsibilities

This specification is responsible for defining:

- The framework's vision and architectural purpose.
- The Documentation Project as the root entity.
- The framework's architectural layers and dependency direction.
- The core modules and their ownership boundaries.
- The design decisions that all module specifications and renderers must preserve.
- The constraints that apply to human and AI contributors.
- The roadmap for more specific architecture documents.

Detailed module contracts belong to their respective architecture documents and must reference this specification rather than duplicate its root-level decisions.

---

## 4. Core Concepts

### 3.1 Documentation as Structured Knowledge

Documentation is treated as structured knowledge rather than as a collection of presentation files. Content must communicate what a subject is, why it exists, how it works, how it is used, how it can be extended, and why relevant decisions were made.

The framework does not require every content source to use the same authoring format. It requires every supported source to be representable through a stable documentation model before rendering.

### 3.2 Content and Presentation Separation

Project-specific content must remain independent from layout, styling, and output technology. Content structures describe meaning. Themes describe visual identity. Renderers translate the model into an output format.

A project must be able to replace or revise its content without modifying framework presentation logic. A renderer or theme must be replaceable without rewriting project knowledge.

### 3.3 Offline-First Operation

Published documentation must remain usable without an internet connection, external service, external content delivery network, or application server.

Offline-first is an architectural constraint, not an optional renderer feature. Features such as search, navigation, glossary access, cross-references, and required assets must remain functional in the distributed offline package.

### 3.4 Semantic Components

Documentation components are semantic structures before they are visual elements. A warning, parameter definition, procedure, API method, timeline, or feature comparison must be represented by its meaning and required data rather than by renderer-specific markup.

Renderers determine how semantic components appear in each output format.

### 3.5 Predictable Navigation

Navigation must be derived from explicit project structure whenever possible. Page hierarchy, ordering, breadcrumbs, local tables of contents, and sequential relationships must remain predictable across documentation projects.

### 3.6 First-Class Terminology

Project terminology is part of the documentation model. Glossary entries, aliases, relationships, and usage references must be maintainable independently from their rendered presentation.

### 3.7 Renderer Independence

The documentation model must not depend on HTML, CSS, JavaScript, browser APIs, or renderer-specific file structures. Renderers depend on the model; the model does not depend on renderers.

---

## 5. Documentation Project as the Root Entity

The root entity of the framework is the **Documentation Project**.

A Documentation Project represents a complete documentation package for a specific product, system, tool, asset, game, discipline, or internal process. It owns the information required to validate, navigate, render, and distribute that package.

Examples include:

- Face System Documentation.
- Save System User Manual.
- Inventory System Technical Documentation.
- A Game Design Document.
- A Narrative Bible.
- An Art Direction Guide.

A Documentation Project contains or references:

- Project identity and metadata.
- Documentation type and version.
- Content pages and semantic content blocks.
- Information hierarchy and navigation order.
- Glossary terms and terminology relationships.
- Documentation assets and stable asset references.
- Theme selection and supported theme configuration.
- Searchable data.
- Cross-references.
- Renderer and output configuration.

Conceptually, the entity is structured as follows:

```text
DocumentationProject
|-- metadata
|-- content
|-- navigation
|-- components
|-- glossary
|-- assets
|-- search configuration
|-- theme configuration
`-- output configuration
```

The Documentation Project is the source boundary for a documentation build. It must contain enough information for a compatible renderer to produce a complete output without deriving project knowledge from renderer code.

### 4.1 Root Entity Invariants

Every valid Documentation Project must:

- Have a stable identity, title, and documentation version.
- Define or reference at least one content entry point.
- Use stable identifiers for pages, terms, components, and cross-references where identity is required.
- Resolve all required local assets through portable paths or framework-defined asset references.
- Remain valid independently from any single renderer.
- Declare renderer-specific settings only inside isolated output configuration.
- Preserve project content when theme or renderer configuration changes.

---

## 6. Architectural Layers

The framework is organized into layers with a one-way dependency direction:

```text
Documentation Sources
        |
        v
Documentation Model
        |
        v
Information Architecture
        |
        v
Navigation, Glossary, Search, and Cross-References
        |
        v
Semantic Components and Theme Tokens
        |
        v
Renderer
        |
        v
Distributed Output
```

### 5.1 Documentation Sources

Documentation Sources are the author-controlled inputs from which the project model is assembled. Sources may include Markdown, structured data, metadata files, or future supported formats.

This layer owns authoring convenience, not output presentation.

### 5.2 Documentation Model

The Documentation Model is the renderer-independent representation of a Documentation Project. It defines project identity, pages, sections, semantic blocks, assets, glossary terms, relationships, and configuration.

This layer is the architectural source of truth.

### 5.3 Information Architecture

The Information Architecture layer defines how knowledge is grouped, ordered, classified, and related. It gives the content a coherent project-wide structure without prescribing how that structure is visually rendered.

### 5.4 Discovery and Relationship Services

Navigation, Glossary, Search, and Cross-Reference services make project knowledge discoverable and connected. These services consume the Documentation Model and Information Architecture.

They must not become alternate stores for project content.

### 5.5 Semantic Components and Theme Tokens

Semantic Components define reusable documentation patterns and their data contracts. Theme Tokens define presentation values such as color roles, typography roles, spacing scales, and other renderer-consumable design decisions.

Components must not contain final renderer markup. Theme Tokens must not alter content meaning or hierarchy.

### 5.6 Renderer

A Renderer transforms a valid Documentation Project into a specific output format. It maps semantic structures and theme tokens to the capabilities of that format.

Offline HTML is the first renderer. It does not define the framework model or architectural boundaries.

### 5.7 Distributed Output

Distributed Output is the portable artifact delivered to documentation users. It may be an offline HTML package, PDF, EPUB, Markdown export, static wiki package, or another supported format.

Output artifacts are products of the framework and are not authoritative sources for project content.

### 5.8 Dependency Rules

The following dependency rules are mandatory:

- Lower-level source and model layers must not import or require renderer concerns.
- Discovery services may consume the model but must not redefine it.
- Themes may provide presentation tokens but must not control content structure.
- Renderers may depend on model, service, component, and theme contracts.
- Generated output must not be required to reconstruct the authoritative model.
- Renderer-specific extensions must be isolated and must degrade safely when another renderer does not support them.

---

## 7. Core Modules and Responsibilities

### 6.1 Project and Metadata Module

The Project and Metadata Module defines project-level identity and configuration.

Responsibilities:

- Store the project identifier and title.
- Store documentation and subject versions.
- Store author, organization, status, and update information.
- Declare the documentation type.
- Declare supported locales and outputs when applicable.
- Provide renderer-independent project configuration.

It does not render metadata, author content, or generate navigation.

### 6.2 Content Module

The Content Module defines the semantic structure of documentation knowledge.

Responsibilities:

- Define pages, sections, headings, and content blocks.
- Define text, code, tables, images, links, procedures, and callouts.
- Define reusable semantic content patterns.
- Preserve content hierarchy and stable identities.
- Provide the source of truth for documentation information.

It does not define final styling, execute search, or emit HTML directly.

### 6.3 Information Architecture Module

The Information Architecture Module organizes content at project scale.

Responsibilities:

- Define documentation sections and classifications.
- Define page hierarchy and grouping.
- Define required and optional structures for documentation types.
- Express relationships between related areas of knowledge.
- Support projects of different sizes without requiring unused sections.

It does not decide final navigation controls or visual layout.

### 6.4 Navigation Module

The Navigation Module defines movement through a Documentation Project.

Responsibilities:

- Define sidebar and primary navigation structures.
- Define page ordering and hierarchy.
- Produce breadcrumb relationships.
- Produce page and section tables of contents.
- Define previous and next page relationships.
- Expose stable navigation data to renderers.

It does not author content, style controls, or perform full-text search.

### 6.5 Component Module

The Component Module defines reusable semantic documentation components.

Responsibilities:

- Define component types and purposes.
- Define required and optional fields.
- Define validation rules.
- Define nesting and composition rules.
- Define accessible semantic intent.
- Define supported fallback behavior.

Examples include alerts, warnings, cards, API methods, parameter definitions, timelines, step lists, badges, and feature comparisons.

It does not contain final CSS, renderer-specific markup, or project-specific copy.

### 6.6 Theme Module

The Theme Module defines portable visual identity through semantic design tokens and presentation policies.

Responsibilities:

- Define color, typography, spacing, border, shadow, and icon roles.
- Define light and dark theme variants.
- Define responsive presentation policies where applicable.
- Provide a default Immersive Games visual identity.
- Expose renderer-consumable tokens without changing content semantics.

It does not define navigation logic, content hierarchy, or search indexing.

### 6.7 Glossary Module

The Glossary Module manages project terminology.

Responsibilities:

- Store terms, definitions, aliases, and related terms.
- Provide stable term identifiers.
- Associate terms with relevant content references.
- Support glossary indexes and dedicated term views.
- Enable validated cross-linking between content and terminology.

It does not replace complete conceptual documentation or publish unreviewed inferred definitions.

### 6.8 Search Module

The Search Module provides renderer-consumable, offline-capable discovery data.

Responsibilities:

- Index page titles, headings, keywords, body text, and glossary terms.
- Define searchable fields and result metadata.
- Rank and return relevant results.
- Support matched-term highlighting where a renderer permits it.
- Produce or expose a portable local index.

It does not depend on online services, external search providers, or server-side execution.

### 6.9 Asset Module

The Asset Module manages documentation-owned assets and references.

Responsibilities:

- Register images, diagrams, icons, screenshots, local media, and downloads.
- Define stable asset identifiers and portable relative paths.
- Store accessibility and descriptive metadata.
- Validate required asset availability.
- Expose asset-copy requirements to renderers.

It does not edit media, create project art, or manage the source assets of the documented product.

### 6.10 Cross-Reference Module

The Cross-Reference Module defines validated relationships among documentation entities.

Responsibilities:

- Resolve links to pages, sections, glossary terms, components, and assets.
- Preserve references when output paths differ between renderers.
- Detect broken or ambiguous internal references.
- Provide renderer-neutral link targets.

It does not define external website availability or replace source-control history.

### 6.11 Validation Module

The Validation Module evaluates a Documentation Project against framework contracts.

Responsibilities:

- Validate required metadata and structural rules.
- Validate identifiers, assets, and cross-references.
- Validate component data contracts.
- Report errors, warnings, and quality guidance.
- Support deterministic validation for both humans and AI agents.

It does not rewrite content silently or make undocumented architectural decisions.

### 6.12 Rendering Module

The Rendering Module transforms a valid Documentation Project into a target output.

Responsibilities:

- Map model entities and semantic components to output constructs.
- Apply supported theme tokens.
- Generate navigation, glossary, and search artifacts.
- Resolve and copy required assets.
- Produce portable output files.
- Report unsupported features and rendering diagnostics.

It does not define project knowledge, terminology, information hierarchy, or architecture decisions for the documented subject.

---

## 8. Out of Scope

### 8.1 Framework-Owned Concerns

The framework owns:

- Documentation model contracts.
- Information architecture conventions.
- Semantic components.
- Navigation, glossary, search, and cross-reference contracts.
- Theme token contracts.
- Validation rules.
- Renderer interfaces and output requirements.
- Documentation quality and contribution standards.

### 8.2 Documentation Project-Owned Concerns

Each Documentation Project owns:

- Subject-specific knowledge.
- Project metadata and versioning information.
- Page content and examples.
- Project terminology.
- Project assets.
- Project-specific navigation choices within framework rules.
- Theme and output selections supported by the framework.

### 8.3 Non-Goals

The framework is not intended to become:

- A general-purpose website builder.
- A content management system.
- A blog or marketing-site engine.
- A server-side documentation platform.
- A project management or issue-tracking tool.
- A replacement for source code comments or API metadata.
- A source asset manager for games or tools.
- An automatic authority on project facts.
- A requirement that every documentation type use identical sections.

The framework may integrate with external authoring, validation, or publishing tools, but those integrations must not compromise offline output, renderer independence, or ownership boundaries.

---

## 9. Design Decisions

### 8.1 Documentation Project Is the Root Entity

**Decision:** The framework uses Documentation Project as its root entity.

**Rationale:** Documentation requires identity, content, metadata, hierarchy, terminology, assets, navigation, and output configuration. Treating individual pages or HTML files as the root would fragment these concerns and make multi-format rendering difficult.

**Consequence:** All modules operate within or against an explicit Documentation Project boundary.

### 8.2 The Model Is Renderer-Independent

**Decision:** The Documentation Model must not depend on HTML or another output technology.

**Rationale:** Renderer independence permits future outputs and prevents presentation constraints from becoming content constraints.

**Consequence:** Renderer-specific markup and behavior must remain outside authoritative project content, except for explicitly isolated extensions with defined fallback behavior.

### 8.3 HTML Is the First Renderer

**Decision:** Offline HTML is the first supported renderer, not the framework itself.

**Rationale:** HTML provides portable, interactive, and widely accessible documentation while supporting offline navigation and search.

**Consequence:** The initial implementation may prioritize HTML capabilities, but architecture contracts must remain meaningful for non-HTML renderers.

### 8.4 Offline-First Is Mandatory

**Decision:** Distributed documentation must function without network access or a server.

**Rationale:** Documentation may ship with Unity packages, downloadable assets, local tools, internal builds, and archived production material.

**Consequence:** Required runtime dependencies, search data, themes, scripts, fonts, and assets must be included locally or replaced with offline-safe alternatives.

### 8.5 Content, Structure, and Presentation Are Separate

**Decision:** Content meaning, information structure, navigation, and presentation are distinct architectural concerns.

**Rationale:** Separation permits reuse, controlled evolution, theme replacement, and renderer portability.

**Consequence:** A module must not absorb another module's responsibility for implementation convenience.

### 8.6 Components Are Semantic

**Decision:** Reusable components are defined by purpose and data contracts before visual treatment.

**Rationale:** Semantic components can be validated, rendered accessibly, and translated across output formats.

**Consequence:** Component specifications must define required information, usage rules, and fallback behavior.

### 8.7 Glossary and Cross-References Are First-Class

**Decision:** Terminology and internal relationships are part of the project model.

**Rationale:** Technical, game design, and production documentation depend on stable language and discoverable relationships.

**Consequence:** Terms and targets require stable identifiers and validation.

### 8.8 Generated Output Is Not Authoritative

**Decision:** Rendered artifacts are derivative outputs.

**Rationale:** Editing generated files would bypass model validation and create renderer-specific sources of truth.

**Consequence:** Changes must be made in project sources or model data and then rendered again.

### 8.9 AI Agents Follow the Same Contracts as Human Contributors

**Decision:** AI-generated and AI-modified documentation must comply with the same architecture, validation, terminology, and review requirements as human-authored work.

**Rationale:** A shared contract preserves consistency and prevents automation from introducing hidden structural conventions.

**Consequence:** AI agents must consult this specification and the relevant module specifications before creating or changing framework artifacts.

---

## 10. HTML Renderer Position

The first implementation of the Rendering Module is an offline HTML renderer. Its expected output may include:

- An `index.html` entry point.
- Local stylesheets and scripts.
- Documentation assets.
- Generated navigation data.
- A local search index.
- Glossary views.
- Responsive layouts.

The HTML renderer must:

- Work from local files without a web server.
- Avoid external CDNs and required online services.
- Use portable links and paths.
- Package all required runtime resources.
- Consume framework contracts rather than define them.
- Represent unsupported semantics through documented fallback behavior.

HTML-specific file structures, CSS conventions, JavaScript modules, browser behavior, and build mechanics belong in the HTML renderer architecture and implementation documents, not in this root architecture specification.

---

## 11. Future Extensions

The architecture must permit controlled extension in the following areas:

- Markdown and structured-data import pipelines.
- PDF, print, EPUB, static wiki, and Markdown renderers.
- Mermaid and other diagram integrations.
- Multiple themes and organization-specific theme presets.
- Localization and multi-language projects.
- Documentation version selection and version-aware cross-references.
- Automatic index and changelog generation.
- Link, terminology, accessibility, and content-quality validation.
- AI-assisted generation, review, migration, and maintenance.
- Unity package integration.
- Plugin-defined semantic components.
- Incremental builds and reusable content packages.

Future extensions must preserve the root entity, dependency direction, offline-first requirement, renderer independence, and separation of concerns defined by this document. Any extension that requires changing those constraints must be introduced through an explicit architecture decision.

---

## 12. Success Criteria

The architecture is successful when:

- New Documentation Projects can be created with minimal framework setup.
- Projects of different types can share framework behavior without sharing project-specific content.
- Content can be revised without modifying renderer or theme implementation.
- Themes and renderers can evolve without changing content meaning.
- Navigation and terminology remain predictable across projects.
- Required documentation features remain functional offline.
- Assets and cross-references remain portable and valid.
- The HTML renderer produces a self-contained, usable package.
- Additional renderers can be introduced without redesigning the Documentation Model.
- Module boundaries are sufficiently explicit to support independent implementation and testing.
- Developers and AI agents can determine where a change belongs and which contracts it must preserve.
- Generated or modified documentation can be validated consistently.

---

## 13. Roadmap for Architecture Documents

The following documents should refine this root specification in order:

1. `DocumentationProject.md`  
   Defines the root schema, identity rules, lifecycle, configuration, and project invariants.

2. `ContentSystem.md`  
   Defines pages, sections, semantic content blocks, source formats, identifiers, and composition rules.

3. `InformationArchitecture.md`  
   Defines classification, hierarchy, documentation-type profiles, and project-scale organization.

4. `NavigationSystem.md`  
   Defines navigation models, ordering, breadcrumbs, tables of contents, and sequential relationships.

5. `ComponentLibrary.md`  
   Defines semantic component contracts, validation rules, composition, accessibility intent, and fallbacks.

6. `ThemeSystem.md`  
   Defines semantic design tokens, visual identity contracts, variants, and renderer responsibilities.

7. `GlossarySystem.md`  
   Defines terminology entities, aliases, relationships, references, and glossary validation.

8. `CrossReferenceSystem.md`  
   Defines target identity, reference resolution, portability, and broken-link validation.

9. `SearchSystem.md`  
   Defines indexing inputs, result records, ranking expectations, and offline index contracts.

10. `AssetSystem.md`  
    Defines asset registration, metadata, stable paths, validation, and packaging.

11. `ValidationSystem.md`  
    Defines validation levels, diagnostics, deterministic rules, and quality gates.

12. `RenderingSystem.md`  
    Defines renderer interfaces, capability negotiation, fallback behavior, and output lifecycle.

13. `HtmlRenderer.md`  
    Defines the architecture of the first renderer, including offline packaging and browser-specific concerns.

14. `AIGuidelines.md`  
    Defines how AI agents interpret, create, update, validate, and review documentation within the framework.

Each document must identify the contracts it owns, the modules it may depend on, and the concerns that remain outside its scope.

---

## 14. Architectural Authority

This document governs the architecture of `com.immersivegames.docs`.

Contributors must preserve the following foundational constraints:

1. Documentation Project is the root entity.
2. The Documentation Model is independent from renderers.
3. Offline HTML is the first renderer, not the framework.
4. Published documentation is offline-first.
5. Content, structure, discovery services, presentation, and rendering remain separate concerns.
6. Semantic components, glossary terms, assets, and cross-references use explicit contracts.
7. Generated output is derivative and must not become the source of truth.
8. Human and AI contributors follow the same architectural and validation rules.

Changes to these constraints require an explicit architectural review and an update to this specification before dependent implementations are changed.

# Related Documents

- [DocumentationStandards.md](DocumentationStandards.md) — Defines the authoring and maintenance requirements for guideline documents.
- [ContentSystem.md](ContentSystem.md) — Planned specification for pages, sections, semantic content blocks, and composition rules.
- [NavigationSystem.md](NavigationSystem.md) — Planned specification for navigation structures and relationships.
- [ComponentLibrary.md](ComponentLibrary.md) — Planned specification for semantic documentation components.
- [ThemeSystem.md](ThemeSystem.md) — Planned specification for themes and semantic design tokens.
- [RenderingSystem.md](RenderingSystem.md) — Planned specification for renderer contracts and output lifecycle.
- [SearchSystem.md](SearchSystem.md) — Planned specification for offline indexing and search contracts.
- [GlossarySystem.md](GlossarySystem.md) — Planned specification for terminology and glossary relationships.
- [AIGuidelines.md](AIGuidelines.md) — Planned guidance for AI agents contributing to documentation.

# Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 0.1.0 | 2026-06-25 | Immersive Games | Initial draft. |
