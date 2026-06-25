# ADR-0003 - Editorial Hierarchy

**Status:** Accepted  
**Date:** 2026-06-25  
**Project:** com.immersivegames.docs

## Context

The framework requires a canonical structure for organizing documentation knowledge independently from output-specific concepts such as HTML files, routes, tabs, Pages, or sidebars.

Technical books and long-form technical documents naturally organize knowledge into publications, major subjects, nested subjects, and atomic authored content. A shared editorial hierarchy gives humans, AI agents, subsystem specifications, and Renderers a consistent structural contract.

## Decision

The official editorial hierarchy is:

```text
Documentation Project
        |
        v
Document
        |
        v
Chapter
        |
        v
Section
        |
        v
Subsection
        |
        v
Content Block
```

The following principles apply:

- The hierarchy follows how authors naturally structure technical documents.
- A Documentation Project contains one or more Documents.
- Documents are independent top-level editorial publications inside a Documentation Project.
- Chapters represent major subjects inside a Document.
- Sections organize specific subjects inside Chapters.
- A Subsection is a Section nested inside another Section.
- Subsections may be recursive without a fixed architectural depth limit.
- Content Blocks are atomic authored units.
- Rendering may choose how to display the hierarchy without redefining its editorial meaning.

## Consequences

- Markdown heading levels can represent the editorial hierarchy consistently.
- Different publications for different audiences can coexist in one Documentation Project.
- Deep subjects can scale through recursively nested Sections.
- Content Blocks cannot contain Documents, Chapters, Sections, or Subsections.
- Renderers may map editorial units to Pages, tabs, sidebars, printable divisions, or other output structures.
- Navigation must derive from rendered structure while preserving the authored hierarchy.

## Related Documents

- [ContentSystem.md](../guidelines/ContentSystem.md) — Defines the complete editorial hierarchy and authoring rules.
- [Terminology.md](../guidelines/Terminology.md) — Defines the official terms used by the hierarchy.
- [FrameworkArchitecture.md](../guidelines/FrameworkArchitecture.md) — Places the editorial hierarchy within the root architecture.

## Revision History

| Version | Date       | Author          | Description                |
|---------|------------|-----------------|----------------------------|
| 0.1.0   | 2026-06-25 | Immersive Games | Initial accepted decision. |
