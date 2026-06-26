# immersive-docs-authoring

## Mission

This skill teaches AI agents how to author documentation using the Immersive Games Documentation Framework.

Its purpose is to produce documentation that is:

* Consistent
* Structured
* Maintainable
* Renderer-independent
* Easy for humans to read
* Predictable for automated tools

The agent authors Markdown only.

Markdown is always the source of truth.

The agent never generates HTML unless explicitly requested.

---

# Primary Workflow

For every documentation task, follow this workflow.

## 1. Understand the Request

Identify:

* What is being documented.
* Whether the documentation already exists.
* Whether the task updates existing documentation or creates new documentation.

When the request is ambiguous, ask for clarification before authoring.

---

## 2. Identify the Documentation Project

Determine which Documentation Project owns the requested documentation.

Never mix documentation belonging to different projects.

---

## 3. Identify the Correct Document

Choose the appropriate Document.

Examples:

* Game Design Document
* Engineering Documentation
* User Manual
* API Reference
* Technical Documentation
* Narrative Bible
* Art Bible
* Audio Guide
* Marketing Guide

Create a new Document only when the information does not belong to an existing one.

---

## 4. Organize the Content

Follow the official editorial hierarchy.

Documentation Project

↓

Document

↓

Chapter

↓

Section

↓

Subsection

↓

Content Blocks

Never introduce additional hierarchy levels.

---

## 5. Verify Terminology

Before introducing a new architectural concept:

Consult:

`Terminology.md`

If the concept already exists:

Use the official terminology.

If the concept does not exist:

Recommend updating `Terminology.md` before introducing the new term.

Do not invent synonyms.

---

## 6. Verify Existing Documentation

Before writing:

Check whether similar information already exists.

Prefer references over duplication.

Maintain a single source of truth.

---

## 7. Author Markdown

Use Markdown only.

Official heading mapping:

# Document Title

## Chapter

### Section

#### Subsection

##### Additional nesting when required

Never use headings for visual formatting.

Use headings only to represent document structure.

---

## 8. Update Cross References

Whenever necessary:

* Update Related Documents.
* Update Revision History.
* Keep architectural references consistent.

---

# Authoring Principles

Documentation represents knowledge.

Do not think in HTML pages.

Do not think in visual layout.

Think like the author of a technical book.

The Rendering System is responsible for presentation.

---

# Decision Rules

When documenting architecture:

Consult:

* DocumentationFramework.md
* FrameworkArchitecture.md
* DocumentationStandards.md

When organizing documentation:

Consult:

* ContentSystem.md

When introducing terminology:

Consult:

* Terminology.md

When describing reusable UI structures:

Consult:

* ComponentLibrary.md

When describing rendering behavior:

Consult:

* RenderingSystem.md

When uncertain:

Always prefer the official guideline over assumptions.

---

# AI Behavior

The agent should:

* Preserve consistency.
* Preserve terminology.
* Preserve architectural decisions.
* Prefer clarity over verbosity.
* Avoid duplication.
* Recommend architectural improvements when inconsistencies are detected.
* Never silently change architectural concepts.

---

# Validation Checklist

Before completing any documentation task verify:

✓ The correct Documentation Project was identified.

✓ The correct Document was selected.

✓ Chapters are logically organized.

✓ Sections follow the editorial hierarchy.

✓ Markdown hierarchy is valid.

✓ Official terminology was used.

✓ Existing documentation was reused whenever possible.

✓ Related Documents were updated.

✓ Revision History was updated.

✓ No HTML assumptions were introduced.

---

# Success Criteria

The task is successful when the produced Markdown:

* Follows the Immersive Games Documentation Framework.
* Can be rendered without structural changes.
* Is understandable by humans.
* Is predictable for AI agents.
* Is independent of presentation technology.

---

# Responsibilities

This skill defines **how an AI agent works**.

It does not redefine the framework architecture.

The framework specifications remain the single source of truth.

Whenever this skill conflicts with an official guideline document, the official guideline document takes precedence.
