# Immersive Games Documentation Framework

`com.immersivegames.docs` is the documentation framework used to define how Immersive Games documentation is designed, structured, written, rendered, distributed, and maintained.

The project provides a shared foundation for technical documentation, user manuals, Unity Asset Store package documentation, Game Design Documents, internal production documents, architecture specifications, glossaries, roadmaps, and related documentation types.

The framework is offline-first and renderer-independent. HTML is planned as its first renderer, but HTML is not the framework itself.

## Documentation Methodology

The project follows a specification-first methodology:

```text
Vision
    |
    v
Architecture
    |
    v
Standards
    |
    v
Subsystem Specifications
    |
    v
Implementation
```

### Vision

Vision defines why the framework exists, the documentation problems it addresses, and the experience it intends to provide across Immersive Games projects.

See [DocumentationFramework.md](guidelines/DocumentationFramework.md).

### Architecture

Architecture defines what the framework is, its root entities and boundaries, and how its modules relate to one another.

See [FrameworkArchitecture.md](guidelines/FrameworkArchitecture.md).

### Standards

Standards define how documentation must be written, structured, referenced, reviewed, and maintained.

See [DocumentationStandards.md](guidelines/DocumentationStandards.md) and [Terminology.md](guidelines/Terminology.md).

### Subsystem Specifications

Subsystem Specifications define each independent framework module, including its purpose, responsibilities, boundaries, contracts, design decisions, and relationships with other modules.

Planned specifications include the Content System, Navigation System, Component Library, Theme System, Rendering System, Search System, Glossary System, and Asset System.

### Implementation

Implementation creates the actual templates, tools, renderers, integrations, and examples that conform to the approved specifications.

Implementation work must not begin before the relevant guideline or subsystem specification exists. This requirement ensures that implementation choices follow the framework architecture instead of defining it implicitly.

## Current Status

The project is currently establishing its documentation foundation. Framework vision, architecture, standards, and terminology are being defined before implementation begins.

No template, renderer, or tooling implementation should be treated as authoritative until its governing specification has been approved.

## Guidelines

The `guidelines/` directory contains the authoritative framework guidance and specifications. Every document in that directory follows the structure and maintenance rules defined by the Documentation Standards.
