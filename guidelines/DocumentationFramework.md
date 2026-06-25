# Documentation Framework

**Version:** 1.0.0
**Status:** Draft

---

# Vision

The Documentation Framework is an offline-first, authoring-first framework created to standardize the way Immersive Games authors, organizes, maintains, and renders documentation.

Its primary purpose is to define how documentation knowledge is written and organized as renderer-independent Markdown. It establishes a shared editorial model that human authors and AI agents can use to create structured, maintainable documentation consistently across projects.

The framework also defines architecture, standards, navigation contracts, semantic Components, terminology, and rendering contracts. These concerns allow the same authored documentation to be transformed into multiple output formats while preserving its meaning and structure.

Offline HTML is the first Renderer. It is not the framework's central goal and does not define the authoring model. Future Renderers may produce PDF or other formats from the same Markdown source.

---

# Purpose

Provide a reusable documentation ecosystem that defines how knowledge is authored, organizes that knowledge consistently, enables AI agents to produce structured documentation, and renders the same authoritative Markdown into HTML and future formats.

---

# Core Principles

## Offline First

Every documentation package must work without an internet connection.

No web server should be required.

No external CDN should be required.

No online dependencies should exist.

---

## Content First

Documentation content is more important than presentation.

The documentation framework must separate:

- Authoring.
- Rendering.
- Presentation.
- Navigation.

Markdown documents are the source of truth. Generated output is derivative.

Projects should replace or revise authored content without modifying Renderer implementation.

---

## Authoring First

Documentation should be organized through an editorial hierarchy that is natural to technical authors:

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
Content Blocks
```

The Content System defines this authoring model. The Rendering System consumes it to produce output-specific structures.

---

## Reusability

Every visual component should be reusable.

Every documentation project should share the same layout and interaction patterns.

Examples include:

- User Manuals
- Technical Documentation
- API Documentation
- Game Design Documents
- Internal Wikis
- Production Documentation

---

## Consistency

Users should immediately recognize documentation produced by Immersive Games regardless of the project being documented.

Navigation, colors, typography, spacing and interaction patterns should remain consistent.

---

## Maintainability

The framework should be easy to extend.

Adding new sections or features should not require redesigning the entire documentation.

---

# Documentation Types

The framework should support different categories of documentation.

## Technical Documentation

- Architecture
- Systems
- Frameworks
- SDKs
- Libraries
- Tools
- Plugins

---

## User Manual

- Installation
- Configuration
- Tutorials
- Quick Start
- Troubleshooting
- Workflow Guides

---

## Game Design Documentation

- Game Vision
- Core Gameplay
- Mechanics
- Narrative
- Characters
- World Building
- Art Direction
- Audio Direction
- Production
- Roadmap

---

## Internal Documentation

- Coding Standards
- Architecture Decisions
- Development Guidelines
- Team Processes
- Production Pipelines

---

# Architecture

The framework transforms knowledge into human-readable output through independent layers:

```text
Knowledge
        |
        v
Authoring
        |
        v
Structured Markdown
        |
        v
Rendering
        |
        v
Human-readable Output
```

The framework exists to guide how humans and AI agents author and organize knowledge as structured Markdown. The Rendering System transforms that source into an output format, and each Renderer determines the appropriate presentation for that format.

HTML is the first supported output format. It is not the central purpose or architectural definition of the framework.

---

# Responsibilities

The framework is responsible for:

- Visual identity
- Layout
- Navigation
- Search
- Glossary
- Responsive behavior
- Theme
- UI components
- Cross references

---

# Project Responsibilities

Each project should provide only its own content.

Examples:

- Overview
- Architecture
- Workflow
- API
- Glossary
- Examples
- Images
- Videos
- References

---

# Out of Scope

The framework is not responsible for:

- Defining project-specific knowledge.
- Replacing source code comments or API metadata.
- Acting as a general-purpose website builder or content management system.
- Requiring an online service or server-side platform.
- Embedding Renderer-specific implementation details into the authoring model.

Project-specific content belongs to each Documentation Project. Detailed framework boundaries are defined in [FrameworkArchitecture.md](FrameworkArchitecture.md).

---

# Design Philosophy

Documentation should explain:

- What the system is.
- Why it exists.
- How it works.
- How to use it.
- How to extend it.
- Why specific decisions were made.

Documentation is not intended to mirror source code.

It should communicate knowledge rather than implementation details.

---

# Information Architecture

Every documentation project should organize information into logical sections.

Recommended sections include:

- Overview
- Getting Started
- Architecture
- Core Concepts
- Workflow
- Configuration
- API Reference
- Examples
- Best Practices
- Troubleshooting
- Glossary
- Changelog

Sections should remain optional.

The framework must support projects of different sizes.

---

# Navigation Philosophy

Navigation should minimize user effort.

The framework should provide:

- Sidebar navigation
- Sticky navigation
- Search
- Breadcrumbs
- Table of Contents
- Previous/Next page navigation
- Back to Top button

Navigation should remain predictable throughout the documentation.

---

# Search

The search system should work entirely offline.

It should support searching by:

- Titles
- Headings
- Keywords
- Glossary terms
- Body text

Search should provide instant results.

---

# Glossary

Every documentation project should be able to define its own glossary.

Glossary entries should be linked throughout the documentation whenever possible.

The glossary should become the central place for terminology.

---

# Visual Identity

The Documentation Framework defines a common visual language.

It includes:

- Color palette
- Typography
- Icons
- Cards
- Alerts
- Tables
- Code blocks
- Buttons
- Navigation
- Spacing
- Responsive behavior

Visual rules are documented separately in the HTML Style Guide.

---

# Extensibility

The framework should support future features such as:

- Multiple themes
- PDF export
- Mermaid diagrams
- Markdown import
- Documentation versioning
- Multi-language support
- Automatic index generation
- AI-assisted documentation generation

The architecture should anticipate these features without requiring major redesign.

---

# AI Integration

The framework is designed to work alongside AI-assisted development.

AI agents should be capable of:

- Generating documentation
- Updating documentation
- Maintaining glossary entries
- Creating navigation
- Organizing content
- Preserving visual consistency

All generated documentation should follow the standards defined by this framework.

---

# Long-Term Vision

The Documentation Framework should become the standard documentation framework for every Immersive Games project.

Whether documenting a Unity Asset Store package, a game, an internal framework, or a Game Design Document, users should experience the same navigation, presentation, and documentation quality.

The framework should evolve over time while preserving backward compatibility whenever possible.

---

# Success Criteria

The framework is considered successful when:

- Documentation can be created quickly.
- New projects require little setup.
- Users can navigate large documentation effortlessly.
- Documentation remains readable offline.
- Multiple projects share the same visual identity.
- AI agents can generate high-quality documentation consistently.
- The framework can evolve without breaking existing projects.

---

# Design Decisions

The root architectural decisions for the framework are maintained in [FrameworkArchitecture.md](FrameworkArchitecture.md). This vision document establishes the following guiding decisions:

- Documentation is structured knowledge rather than renderer-specific output.
- Markdown is the official authoring language and source of truth.
- The Content System defines an editorial hierarchy for human authors and AI agents.
- Offline operation is a mandatory framework constraint.
- Authoring remains separate from rendering, presentation, and navigation.
- Reusable semantic patterns provide consistency across documentation types.
- HTML is the first Renderer, not the framework architecture or its primary purpose.

# Related Documents

- [DocumentationStandards.md](DocumentationStandards.md) — Defines the standards governing documents in this directory.
- [FrameworkArchitecture.md](FrameworkArchitecture.md) — Defines the authoritative root architecture of the framework.
- [Terminology.md](Terminology.md) — Defines the official vocabulary used by the framework.
- [ContentSystem.md](ContentSystem.md) — Defines the editorial hierarchy and Markdown authoring model.

# Revision History

| Version | Date       | Author          | Description                                          |
|---------|------------|-----------------|------------------------------------------------------|
| 1.1.1   | 2026-06-25 | Immersive Games | Replaced the legacy HTML-centered architecture diagram. |
| 1.1.0   | 2026-06-25 | Immersive Games | Established the authoring-first, Markdown source-of-truth philosophy. |
| 1.0.2   | 2026-06-25 | Immersive Games | Added the framework terminology reference.           |
| 1.0.1   | 2026-06-25 | Immersive Games | Normalized Markdown formatting and renamed the file. |
| 1.0.0   | 2026-06-25 | Immersive Games | Initial draft.                                       |
