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

# Related Documents

- [FrameworkArchitecture.md](FrameworkArchitecture.md) — Defines the root architecture governed by these documentation standards.

# Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 0.1.0 | 2026-06-25 | Immersive Games | Initial draft. |
