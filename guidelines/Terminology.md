# Terminology

**Project:** `com.immersivegames.docs`  
**Document Type:** Terminology Standard  
**Status:** Draft  
**Version:** 0.1.0

---

## Purpose

This document defines the official terminology used by the Immersive Games Documentation Framework.

The definitions in this document establish a shared vocabulary for guidelines, specifications, implementations, project documentation, and contributions made by human authors or AI agents.

## Responsibilities

This document is responsible for:

- Defining the canonical meaning of framework terms.
- Distinguishing terms that represent architecture, documentation structure, and implementation.
- Reducing ambiguity across guidelines and subsystem specifications.
- Providing a terminology reference for contributors and AI agents.

## Out of Scope

This document does not:

- Define complete architectural contracts.
- Replace subsystem specifications.
- Define project-specific glossary terms.
- Prescribe HTML, CSS, JavaScript, template, renderer, or tooling implementation details.

## Usage Rules

Framework documents must use the terms in this document consistently.

When a new architectural concept requires a stable name, its owning specification must define the concept and update this document with the canonical term. Project-specific terminology belongs to the Glossary System of the relevant Documentation Project rather than to this framework terminology standard.

## Official Terms

### Documentation Framework

**Term:** Documentation Framework

**Definition:** The complete renderer-independent system for defining, organizing, validating, navigating, rendering, distributing, and maintaining documentation across Immersive Games projects.

**Notes:** The Documentation Framework includes architectural contracts, standards, subsystem specifications, semantic models, and renderer contracts. It is not synonymous with an HTML template.

### Documentation Project

**Term:** Documentation Project

**Definition:** The root entity representing a complete documentation package for a specific product, system, tool, asset, game, discipline, or internal process.

**Notes:** A Documentation Project contains one or more Markdown Documents and may also contain or reference Metadata, Components, glossary terms, assets, search configuration, Theme configuration, and output configuration.

### Guideline

**Term:** Guideline

**Definition:** A normative document that defines shared principles, conventions, quality expectations, or authoring rules that apply across multiple framework areas.

**Notes:** A guideline governs how work should be performed but does not necessarily define the complete contract of a subsystem.

### Specification

**Term:** Specification

**Definition:** A normative document that defines the purpose, responsibilities, boundaries, contracts, design decisions, and expected behavior of a framework entity or subsystem.

**Notes:** An implementation must conform to its applicable specifications.

### Content System

**Term:** Content System

**Definition:** The framework subsystem that defines the renderer-independent editorial model used to author and organize documentation knowledge.

**Notes:** It owns Documents, Chapters, recursively nested Sections, Content Blocks, Markdown authoring rules, and content composition. It does not own final presentation.

### Document

**Term:** Document

**Definition:** The highest editorial unit inside a Documentation Project, representing an independent publication with its own subject, title, structure, and intended audience.

**Notes:** Examples include a User Manual, Game Design Document, Engineering Documentation, API Reference, or Changelog. A Renderer determines how a Document is presented in an output.

### Chapter

**Term:** Chapter

**Definition:** A major editorial subject division within a Document.

**Notes:** A Chapter contains Sections and Content Blocks. The HTML Renderer may present Chapters as primary sidebar entries, but that presentation is not part of the Content System.

### Navigation System

**Term:** Navigation System

**Definition:** The framework subsystem that consumes rendered structure and defines how users move through the resulting documentation output.

**Notes:** It may expose document navigation, ordering, breadcrumbs, tables of contents, rendered content targets, and previous or next relationships. It does not redefine the authored editorial hierarchy.

### Component Library

**Term:** Component Library

**Definition:** The official renderer-independent catalog of reusable semantic documentation Components, their categories, support levels, intended usage, and Renderer Expectations.

**Notes:** Components are defined by purpose and meaning before visual treatment. The Component Library is not an HTML component library.

### Core Component

**Term:** Core Component

**Definition:** A Component required for any Renderer claiming basic framework compatibility.

**Notes:** Core Components establish the minimum semantic component set that Renderers must understand and preserve.

### Extended Component

**Term:** Extended Component

**Definition:** An optional Component recommended for richer documentation but not required for basic framework compatibility.

**Notes:** A Renderer may support all Extended Components, selected Extended Components, or none of them, provided unsupported Components degrade gracefully.

### Theme System

**Term:** Theme System

**Definition:** The framework subsystem that defines portable visual identity through semantic design tokens and presentation policies.

**Notes:** It does not define content meaning, hierarchy, or navigation logic.

### Rendering System

**Term:** Rendering System

**Definition:** The framework subsystem that consumes the Content System's editorial model and transforms a valid Documentation Project into one or more output formats.

**Notes:** It owns renderer contracts, capability handling, output lifecycle, and fallback expectations rather than a specific output implementation.

### Renderer

**Term:** Renderer

**Definition:** An implementation of the Rendering System that consumes the authoring model of a valid Documentation Project and produces a specific distributed output format.

**Notes:** Renderers depend on framework contracts. The Content System's authoring model must not depend on a Renderer.

### HTML Renderer

**Term:** HTML Renderer

**Definition:** The first planned renderer of the Documentation Framework, responsible for producing a portable offline HTML documentation package.

**Notes:** The HTML Renderer is one implementation of the Rendering System and is not the Documentation Framework itself.

### Search System

**Term:** Search System

**Definition:** The framework subsystem that defines offline-capable indexing, query, ranking, and search-result contracts for a Documentation Project.

**Notes:** It must not require an online service or server-side search provider.

### Glossary System

**Term:** Glossary System

**Definition:** The framework subsystem that manages project-specific terms, definitions, aliases, relationships, and usage references.

**Notes:** Framework-wide architectural vocabulary belongs in this terminology standard. Subject-specific vocabulary belongs to each Documentation Project.

### Asset System

**Term:** Asset System

**Definition:** The framework subsystem that registers, describes, validates, references, and packages documentation-owned assets.

**Notes:** Assets may include images, diagrams, icons, screenshots, local media, and downloadable files.

### Page

**Term:** Page

**Definition:** An addressable unit created or exposed by a Renderer for a specific output format.

**Notes:** Page is a rendering and navigation concept, not a primary editorial authoring unit. A Renderer may map a Document, Chapter, Section, or other supported structure to a Page.

### Section

**Term:** Section

**Definition:** A specific editorial subject within a Chapter or another Section.

**Notes:** A Section organizes related content under a heading and may contain Content Blocks, Components, and nested Sections. When nested inside another Section, it is also described as a Subsection.

### Subsection

**Term:** Subsection

**Definition:** A Section nested inside another Section.

**Notes:** Subsection describes relative editorial position and is not a separate entity type. No fixed nesting limit exists.

### Content Block

**Term:** Content Block

**Definition:** An atomic information unit authored within a Section, Subsection, or another context permitted by the Content System.

**Notes:** Examples include a paragraph, list, table, image, diagram, quote, Code Block, Video Reference, or Download Link. A Content Block never contains a Document, Chapter, Section, or Subsection.

### Component

**Term:** Component

**Definition:** A reusable semantic documentation structure with a defined purpose, data contract, validation rules, and renderer-specific presentation.

**Notes:** Examples include warnings, procedures, parameter definitions, API methods, timelines, and feature comparisons.

### Governance Component

**Term:** Governance Component

**Definition:** A Component that records project reasoning, decisions, alternatives, trade-offs, constraints, assumptions, dependencies, risks, objectives, requirements, or open questions.

**Notes:** Governance Components help preserve architectural and project context that might otherwise be repeated or lost.

### Renderer Expectation

**Term:** Renderer Expectation

**Definition:** A semantic behavior or compatibility requirement that a Renderer should preserve when transforming authored documentation into an output format.

**Notes:** Renderer Expectations describe expected behavior without prescribing HTML, CSS, JavaScript, visual styling, or internal Renderer implementation.

### Theme

**Term:** Theme

**Definition:** A named set of semantic design tokens and presentation policies that controls the visual identity of rendered documentation.

**Notes:** Changing a Theme must not change content meaning or information hierarchy.

### Metadata

**Term:** Metadata

**Definition:** Structured information that identifies, describes, versions, classifies, or configures a Documentation Project or one of its entities.

**Notes:** Examples include project title, identifier, documentation version, subject version, author, status, locale, and update date.

### Markdown

**Term:** Markdown

**Definition:** The official authoring language and source-of-truth format for Documentation Framework content.

**Notes:** The Rendering System consumes Markdown structure and semantics to produce HTML, PDF, or future formats. Generated output does not replace the Markdown source.

### Markdown Usage

**Term:** Markdown Usage

**Definition:** The approved way a Component or documentation structure is authored in Markdown.

**Notes:** Markdown Usage for Components is defined by the Component Library so authors and AI agents use consistent notation.

### Standard Markdown

**Term:** Standard Markdown

**Definition:** The common Markdown syntax used for basic authored structures such as headings, paragraphs, lists, tables, code blocks, links, and images.

**Notes:** Standard Markdown should be preferred whenever it can express the content clearly.

### Callout Syntax

**Term:** Callout Syntax

**Definition:** The blockquote-style Markdown convention used to author Information Components through uppercase callout types such as `[!NOTE]` or `[!WARNING]`.

**Notes:** Callout Syntax remains readable as raw Markdown and must not require raw HTML.

### Structured Block Syntax

**Term:** Structured Block Syntax

**Definition:** The fenced semantic Markdown convention used to author Extended or structured Components with lowercase kebab-case Component names.

**Notes:** Structured Block Syntax is used when a Component needs fields, Metadata, or multi-part content.

### Structured Block

**Term:** Structured Block

**Definition:** A fenced semantic Markdown block that represents an Extended or structured Component.

**Notes:** Unsupported Structured Blocks should degrade gracefully into readable content.

### Component Naming Rule

**Term:** Component Naming Rule

**Definition:** A naming convention that defines how Component names, callout types, and Structured Block names must be written.

**Notes:** Component Naming Rules prevent unofficial aliases, inconsistent casing, and invented synonyms.

### Related Documents

**Term:** Related Documents

**Definition:** The mandatory final-reference section that identifies other guideline or specification files relevant to the current document.

**Notes:** It must use repository-relative Markdown links and immediately precede Revision History.

### Revision History

**Term:** Revision History

**Definition:** The mandatory final section that records the version, date, author, and description of significant document revisions.

**Notes:** Dates use the ISO `YYYY-MM-DD` format, and entries are maintained in a Markdown table.

## Design Decisions

### Canonical Vocabulary

Framework-wide terminology is maintained in one document to prevent competing definitions and inconsistent wording across specifications.

### Architecture Before Implementation

Terms describe renderer-independent concepts unless their names explicitly identify an implementation, such as HTML Renderer.

### Project Glossaries Remain Independent

The framework terminology standard defines the vocabulary of the Documentation Framework. Each Documentation Project remains responsible for terminology specific to its documented subject.

# Related Documents

- [DocumentationFramework.md](DocumentationFramework.md) — Defines the framework vision, principles, and intended documentation experience.
- [FrameworkArchitecture.md](FrameworkArchitecture.md) — Defines the root architecture and module relationships.
- [DocumentationStandards.md](DocumentationStandards.md) — Defines the authoring and maintenance rules applied to this document.
- [ContentSystem.md](ContentSystem.md) — Defines the editorial hierarchy and Markdown authoring model.
- [ComponentLibrary.md](ComponentLibrary.md) — Defines the official semantic documentation Components and support levels.

# Revision History

| Version | Date       | Author          | Description                |
|---------|------------|-----------------|----------------------------|
| 0.2.3   | 2026-06-26 | Immersive Games | Added Markdown component authoring terminology. |
| 0.2.2   | 2026-06-26 | Immersive Games | Added Component Library support terminology. |
| 0.2.1   | 2026-06-25 | Immersive Games | Clarified Section terminology for the editorial model. |
| 0.2.0   | 2026-06-25 | Immersive Games | Added the editorial authoring terminology. |
| 0.1.0   | 2026-06-25 | Immersive Games | Initial terminology draft. |
