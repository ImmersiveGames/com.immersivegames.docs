# Documentation Standards

**Project:** `com.immersivegames.docs`  
**Document Type:** Documentation Standard  
**Status:** Draft  
**Version:** 0.1.0

---

## Purpose

This document defines the authoring and maintenance standards for all guideline and specification documents inside `guidelines/`.

Its rules apply to human contributors and AI agents. Documents in this directory must comply with this standard unless a documented exception is required by the specific purpose of a document.

## Responsibilities

This standard is responsible for defining:

- The required language and file format for guideline and specification documents.
- The responsibility and scope boundaries expected from each document.
- The required structure of architectural documents.
- The rules for references, diagrams, implementation details, and revision records.
- The mandatory final sections for every document in `guidelines/`.

## Out of Scope

This standard does not define:

- The architecture of the documentation framework.
- The content model, navigation model, component library, theme system, or rendering system.
- HTML, CSS, or JavaScript implementation details.
- Templates, build tooling, or renderer behavior.
- Project-specific documentation content.

## General Authoring Rules

All guideline and specification documents must:

- Use Markdown.
- Be written in English.
- Have a single, clear responsibility.
- Avoid duplicating information defined by another document.
- Reference the owning document when a topic belongs elsewhere instead of repeating its content.
- Use terminology consistently with the architecture and other applicable guidelines.
- Keep normative requirements distinguishable from examples and explanatory text.

## Required Architecture Structure

Architectural documents must clearly separate the following concerns:

- **Purpose:** Why the documented system or module exists.
- **Responsibilities:** What the documented system or module owns and must provide.
- **Out of Scope:** What the documented system or module explicitly does not own.
- **Design Decisions:** The significant decisions, their rationale, and relevant consequences.
- **Related Documents:** References to other relevant guideline or specification files.
- **Revision History:** A chronological record of document revisions.

Additional sections may be included when they support the document's single responsibility.

## Cross-Document References

Documents must reference related guideline files by repository-relative Markdown links.

References must:

- Point to the document that owns the relevant topic.
- Describe the relationship when the filename alone is not sufficiently clear.
- Avoid restating substantial content from the referenced document.
- Be updated when files are renamed or responsibilities move.

## Diagrams

Diagrams may be used to clarify architecture, structure, relationships, dependencies, or flows.

Diagrams must complement the written specification and must not replace it. All requirements, responsibilities, boundaries, and decisions represented by a diagram must remain understandable from the surrounding text.

## Separation from Implementation

Architecture documents must not mix HTML, CSS, or JavaScript implementation details into framework architecture.

Renderer- or implementation-specific details are permitted only when the document is specifically responsible for a renderer or implementation concern. Such documents must preserve the distinction between framework contracts and technology-specific implementation choices.

## Mandatory Final Sections

Every document inside `guidelines/` must end with these sections, in this order:

1. `# Related Documents`
2. `# Revision History`

`Related Documents` must list other relevant guideline files as repository-relative Markdown links. When no related document exists, the section must state that explicitly.

`Revision History` must use the following Markdown table structure:

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 0.1.0 | 2026-06-25 | Immersive Games | Initial draft. |

Revision dates must use ISO 8601 calendar format: `YYYY-MM-DD`.

New revision entries must preserve the document's existing history and use a version appropriate to the significance of the change.

## Design Decisions

### Markdown as the Standard Format

Markdown is the required format because it is portable, readable as source text, compatible with version control, and independent from a particular renderer.

### English as the Standard Language

English is the required language to provide a consistent technical vocabulary across projects, contributors, tools, and AI agents.

### Single Responsibility per Document

Each document owns one clearly defined subject. This reduces conflicting requirements, improves discoverability, and makes individual specifications easier to evolve.

### References Instead of Duplication

Information is defined in the document that owns the topic and referenced elsewhere. This prevents multiple sources of truth and inconsistent revisions.

### Standardized Closing Sections

Related-document references and revision history are mandatory closing sections so contributors can identify dependencies and document evolution consistently.

# Documentation Governance

This section defines the governance rules for the evolution of the Immersive Games Documentation Framework.

## Terminology First

Before introducing any new architectural concept, subsystem, component, or documentation entity, contributors must verify whether the term already exists in [Terminology.md](Terminology.md).

If the concept does not exist, it must be added to `Terminology.md` before it is referenced by any other guideline document.

All guideline documents must use the official terminology defined in `Terminology.md`.

Contributors must avoid creating synonyms for existing concepts.

The terminology document is the single source of truth for the framework vocabulary.

## Architecture Before Implementation

New features must first be described in the appropriate guideline document before implementation begins.

Implementation must never define architecture.

Architecture defines implementation.

## Single Responsibility

Each guideline document should describe one architectural concern only.

Contributors must avoid mixing responsibilities across documents.

When a topic belongs to another document, the owning document must be referenced instead of duplicating its information.

## Progressive Refinement

The framework should evolve incrementally.

Architecture must be established first.

Subsystem specifications should follow.

Implementation must always be the final step.

## Backward Compatibility

When possible, architectural changes should preserve compatibility with existing Documentation Projects.

Breaking changes must be documented explicitly in the Revision History of each affected document.

## Living Documentation

Guideline documents are living specifications.

Whenever architecture changes, the affected guideline documents must be updated.

Documentation must always reflect the current architecture.

## AI Collaboration

AI-generated documentation must follow the same standards as human-written documentation.

AI agents must never invent terminology when an official term already exists.

When introducing a new concept, AI agents should recommend updating `Terminology.md` before using the new term throughout the documentation.

# Related Documents

- [DocumentationFramework.md](DocumentationFramework.md) — Defines the framework vision, principles, and intended documentation experience.
- [FrameworkArchitecture.md](FrameworkArchitecture.md) — Defines the root architecture governed by these documentation standards.
- [Terminology.md](Terminology.md) — Defines the official vocabulary used by guideline and specification documents.
- [ContentSystem.md](ContentSystem.md) — Applies these standards to the framework's editorial authoring model.

# Revision History

| Version | Date       | Author          | Description                     |
|---------|------------|-----------------|---------------------------------|
| 0.2.2   | 2026-06-25 | Immersive Games | Validated governance against the authoring-first architecture. |
| 0.2.1   | 2026-06-25 | Immersive Games | Added the Content System reference. |
| 0.2.0   | 2026-06-25 | Immersive Games | Added Documentation Governance principles. |
| 0.1.2   | 2026-06-25 | Immersive Games | Added the terminology reference. |
| 0.1.1   | 2026-06-25 | Immersive Games | Normalized Markdown formatting. |
| 0.1.0   | 2026-06-25 | Immersive Games | Initial draft.                  |
