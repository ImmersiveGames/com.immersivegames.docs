# Component Usage Reference

**Project:** `com.immersivegames.docs`  
**Document Type:** Authoring Reference  
**Status:** Draft  
**Version:** 0.1.0

---

## Purpose

This document is a practical authoring reference for every official Component listed in the Immersive Games Documentation Framework Component Library.

It explains what each Component means, when an authoring agent should use it, which Markdown Usage pattern is approved, and what semantic behavior a Renderer should preserve.

This document is not an implementation guide. It does not define HTML, CSS, JavaScript, visual styling, parser internals, or Renderer-specific layout.

## Source of Truth

The authoritative Component definitions are maintained in [ComponentLibrary.md](../guidelines/ComponentLibrary.md).

This document summarizes practical authoring usage for testing and documentation workflows. If this reference conflicts with the Component Library, the Component Library takes precedence.

## Authoring Rules

Authors and AI agents must follow these rules when using Components:

- Use Standard Markdown for Basic Components.
- Use Callout Syntax for Information Components.
- Use Structured Block Syntax for Extended or structured Components.
- Use uppercase snake case for callout types.
- Use lowercase kebab case for Structured Block names.
- Do not invent Component names, callout types, aliases, or renderer-specific markup.
- Do not write raw HTML for presentation.

## Support Levels

| Support Level | Meaning |
|---------------|---------|
| Core | Required for any Renderer claiming basic framework compatibility. |
| Extended | Optional but recommended for richer documentation. Unsupported Extended Components should degrade gracefully to readable Markdown. |
| Listed | Officially listed in the Component Library category catalog, but not currently included in the initial Core or Extended support sets. |

## Markdown Usage Patterns

### Standard Markdown

Use Standard Markdown whenever the content can be expressed clearly without semantic extensions.

```md
## Chapter

Regular paragraph.

- Item
- Item

| Field | Value |
|-------|-------|
| Status | Draft |
```

### Callout Syntax

Use blockquote-style callouts for Information Components.

```md
> [!TYPE] Optional Title
> Content goes here.
```

### Structured Block Syntax

Use fenced semantic blocks for structured Components.

```md
:::component-name
**Field:** Value

Content goes here.
:::
```

## Basic Components

Basic Components represent standard Markdown content structures and common authored content units.

| Component | Support Level | Markdown Usage | Purpose | When to Use | Expected Rendering |
|-----------|---------------|----------------|---------|-------------|--------------------|
| Heading | Core | Standard Markdown | Defines the editorial hierarchy of a Document, Chapter, Section, or Subsection. | Use to structure content, not to create visual emphasis. | Preserve hierarchy and enable navigation, outlines, and references. |
| Paragraph | Listed | Standard Markdown | Represents regular explanatory prose. | Use for normal written explanation. | Preserve readable text flow. |
| List | Core | Standard Markdown | Represents unordered related items. | Use when item order is not meaningful. | Preserve each item as a readable list entry. |
| Ordered List | Listed | Standard Markdown | Represents sequenced items. | Use when order, priority, or procedure sequence matters. | Preserve item order and numbering. |
| Checklist | Listed | Standard Markdown | Represents trackable tasks or completion states. | Use for task lists, validation steps, or acceptance checklists. | Preserve checked and unchecked state where supported. |
| Table | Core | Standard Markdown | Represents structured tabular data. | Use for compact comparison, field lists, or matrices. | Preserve rows, columns, headings, and cell meaning. |
| Quote | Core | Standard Markdown | Represents quoted or externally attributed text. | Use for citations, preserved statements, or quoted context. | Preserve quoted relationship and attribution if present. |
| Code Block | Core | Standard Markdown | Represents multi-line literal code or command examples. | Use for code, terminal output, configuration snippets, or data samples. | Preserve literal formatting and language metadata where supported. |
| Inline Code | Listed | Standard Markdown | Represents short literal identifiers inside prose. | Use for filenames, commands, symbols, values, or API names. | Preserve literal distinction inside text. |
| Horizontal Rule | Listed | Standard Markdown | Represents a semantic break between content blocks. | Use sparingly to separate major content shifts inside a section. | Preserve separation without changing hierarchy. |
| Link | Listed | Standard Markdown | References another document, section, asset, or external resource. | Use for cross references and external references. | Preserve destination and readable label. |
| Image | Core | Standard Markdown | Embeds or references visual content. | Use when a visual asset directly supports understanding. | Preserve alt text, source reference, and image meaning. |

### Basic Component Examples

````md
# Document Title

## Chapter

### Section

This paragraph explains the section.

- First related item
- Second related item

1. First ordered step
2. Second ordered step

- [ ] Draft the document
- [x] Review terminology

| Field | Value |
|-------|-------|
| Status | Draft |

> Quoted material or preserved statement.

```text
literal content
```

Use `InlineCode` for literal identifiers.

---

See [Component Library](../guidelines/ComponentLibrary.md).

![Diagram alt text](assets/diagram.png)
````

## Information Components

Information Components highlight explanatory, advisory, cautionary, or example-based content.

| Component | Support Level | Markdown Usage | Purpose | When to Use | Expected Rendering |
|-----------|---------------|----------------|---------|-------------|--------------------|
| Note | Core | `> [!NOTE]` | Adds neutral contextual information. | Use for helpful context that is not urgent or advisory. | Preserve informational emphasis without implying risk. |
| Info | Core | `> [!INFO]` | Adds explanatory or clarifying information. | Use when the reader needs extra background to interpret content. | Preserve informational meaning and optional title. |
| Tip | Core | `> [!TIP]` | Provides a useful recommendation or shortcut. | Use for workflow improvements or practical suggestions. | Preserve advisory meaning as optional guidance. |
| Warning | Core | `> [!WARNING]` | Communicates possible damage, breakage, or misuse. | Use before actions that can cause errors, data loss, or broken references. | Preserve cautionary meaning with high visibility. |
| Important | Core | `> [!IMPORTANT]` | Marks information the reader must not miss. | Use for required constraints or critical knowledge. | Preserve required-attention meaning. |
| Success | Listed | `> [!SUCCESS]` | Confirms a desired state or outcome. | Use after successful validation, setup, or completion criteria. | Preserve positive confirmation meaning. |
| Example | Core | `> [!EXAMPLE]` | Presents a representative usage sample. | Use when an example supports nearby explanation. | Preserve example relationship to the surrounding topic. |
| Best Practice | Listed | `> [!BEST_PRACTICE]` | Records preferred authoring or engineering practice. | Use when guidance should be repeated consistently across projects. | Preserve recommendation as a practice, not a requirement unless stated. |

### Information Component Examples

```md
> [!NOTE]
> Markdown remains the source of truth.

> [!INFO] Renderer Compatibility
> Unsupported Extended Components should remain readable in raw Markdown.

> [!TIP]
> Prefer Standard Markdown when it expresses the content clearly.

> [!WARNING]
> Do not use raw HTML to force presentation.

> [!IMPORTANT]
> Callout types must use uppercase snake case.

> [!SUCCESS]
> The document follows the official heading hierarchy.

> [!EXAMPLE]
> Use `> [!WARNING]` before a destructive workflow step.

> [!BEST_PRACTICE]
> Reference the owning specification instead of duplicating substantial content.
```

## Technical Components

Technical Components describe software, APIs, configuration, runtime concepts, and engineering reference material.

| Component | Support Level | Markdown Usage | Purpose | When to Use | Expected Rendering |
|-----------|---------------|----------------|---------|-------------|--------------------|
| API | Extended | `:::api` | Groups reference material for an API surface. | Use for a coherent API entry or module-level reference. | Preserve API identity, description, members, and related metadata. |
| Method | Extended | `:::method` | Documents callable behavior. | Use for functions, methods, commands, or operations. | Preserve signature, purpose, parameters, return value, and examples. |
| Property | Extended | `:::property` | Documents readable or writable data exposed by an API. | Use for fields, properties, settings, or exposed values. | Preserve name, type, access, default, and meaning. |
| Parameter | Extended | `:::parameter` | Documents an input accepted by a Method, API, or Configuration. | Use when a parameter needs description, type, requirement, or constraints. | Preserve name, type, requirement, allowed values, and description. |
| Return Value | Listed | `:::return-value` | Documents the output produced by a Method or operation. | Use when return data needs type, meaning, or edge-case description. | Preserve returned type, value meaning, and conditions. |
| Event | Listed | `:::event` | Documents a signal emitted by a system or API. | Use for callbacks, notifications, hooks, or observable events. | Preserve trigger, payload, timing, and subscribers. |
| Enumeration | Listed | `:::enumeration` | Documents a finite set of named values. | Use for enum types, modes, states, or option sets. | Preserve values, labels, descriptions, and defaults. |
| Interface | Listed | `:::interface` | Documents a formal contract implemented by classes or modules. | Use for API contracts and required members. | Preserve contract name, purpose, members, and implementation expectations. |
| Class | Listed | `:::class` | Documents a concrete type or object abstraction. | Use for classes or equivalent type constructs. | Preserve class identity, responsibility, members, and relationships. |
| Namespace | Listed | `:::namespace` | Documents a logical grouping of API elements. | Use for namespaces, packages, modules, or scoped API groups. | Preserve grouping and child API relationships. |
| Configuration | Extended | `:::configuration` | Documents configurable behavior or settings. | Use for options, files, environment values, or project settings. | Preserve setting names, defaults, accepted values, and impact. |

### Technical Component Examples

```md
:::api
**Name:** Face Animation API

**Purpose:** Provides animation playback operations.
:::

:::method
**Name:** PlayAnimation

**Signature:** `PlayAnimation(string animationId)`

**Purpose:** Starts a named animation.
:::

:::parameter
**Name:** `animationId`

**Type:** `string`

**Required:** Yes

**Description:** Identifier of the animation to play.
:::

:::return-value
**Type:** `bool`

**Description:** Returns `true` when playback starts successfully.
:::

:::configuration
**Name:** Default Transition Duration

**Default:** `0.2`

**Description:** Controls the default blend duration between animation states.
:::
```

## Architecture Components

Architecture Components describe structural, behavioral, or temporal relationships in systems and documentation.

| Component | Support Level | Markdown Usage | Purpose | When to Use | Expected Rendering |
|-----------|---------------|----------------|---------|-------------|--------------------|
| Flow | Extended | `:::flow` | Describes directional movement of data, control, or responsibility. | Use for data flow, user flow, or system flow. | Preserve ordered movement and participating entities. |
| Process | Listed | `:::process` | Describes a repeatable set of activities. | Use for workflows, production processes, or maintenance routines. | Preserve steps, actors, inputs, outputs, and completion criteria. |
| Timeline | Extended | `:::timeline` | Describes events across time. | Use for roadmaps, histories, release plans, or lifecycle milestones. | Preserve chronological order and milestone meaning. |
| Sequence | Listed | `:::sequence` | Describes ordered interactions. | Use for message exchange, runtime interaction, or ordered operations. | Preserve order, participants, and interaction meaning. |
| Pipeline | Extended | `:::pipeline` | Describes staged transformation from input to output. | Use for build, asset, rendering, authoring, or processing pipelines. | Preserve stages, inputs, outputs, and transitions. |
| State | Listed | `:::state` | Describes a named condition of a system or entity. | Use for state machines, lifecycle states, or mode documentation. | Preserve state name, meaning, transitions, and constraints. |
| Lifecycle | Listed | `:::lifecycle` | Describes the complete life of an entity from creation to retirement. | Use for assets, documents, features, objects, or release artifacts. | Preserve phases and transition rules. |
| Decision Tree | Listed | `:::decision-tree` | Describes conditional branching logic. | Use for troubleshooting, selection logic, or decision support. | Preserve choices, conditions, and outcomes. |

### Architecture Component Examples

```md
:::flow
**Name:** Markdown Rendering Flow

1. Author writes Markdown.
2. Renderer consumes Markdown.
3. Renderer produces human-readable output.
:::

:::timeline
**Name:** Documentation Rollout

| Date | Milestone |
|------|-----------|
| 2026-06-26 | Component authoring conventions drafted |
:::

:::pipeline
**Input:** Markdown Documents

**Stages:** Validate, parse, render, package

**Output:** Offline documentation package
:::

:::decision-tree
**Question:** Can Standard Markdown express the content clearly?

**Yes:** Use Standard Markdown.

**No:** Use an official Callout or Structured Block Component.
:::
```

## Reference Components

Reference Components connect authored content to related documentation, external resources, assets, or glossary entries.

| Component | Support Level | Markdown Usage | Purpose | When to Use | Expected Rendering |
|-----------|---------------|----------------|---------|-------------|--------------------|
| Glossary Reference | Listed | Standard Markdown link | References a glossary term. | Use when a term has an official glossary definition. | Preserve term label and destination. |
| Cross Reference | Listed | Standard Markdown link | References another part of the same Documentation Project. | Use for related sections, chapters, documents, or anchors. | Preserve readable navigation target. |
| Related Documents | Core | Markdown section with links | Lists documents relevant to the current document. | Use as a final reference section or local related-material block. | Preserve relationships and link labels. |
| External Link | Listed | Standard Markdown link | References resources outside the Documentation Project. | Use for official external resources or cited material. | Preserve external destination and readable label. |
| Asset Reference | Listed | Standard Markdown link or image | References a documentation-owned asset. | Use for files, diagrams, screenshots, or media assets. | Preserve asset relationship and path. |
| Download | Listed | Standard Markdown link | References a downloadable file. | Use when the reader should retrieve a file. | Preserve download target and description. |

### Reference Component Examples

```md
See [Markdown](../guidelines/Terminology.md#markdown).

See [Content System](../guidelines/ContentSystem.md).

# Related Documents

- [ComponentLibrary.md](../guidelines/ComponentLibrary.md) - Defines official Components.

See [CommonMark](https://commonmark.org/).

See [Architecture Diagram](assets/architecture-diagram.png).

Download [Example Package](downloads/example-package.zip).
```

## Media Components

Media Components represent authored use of visual, audiovisual, or compact visual-reference content.

| Component | Support Level | Markdown Usage | Purpose | When to Use | Expected Rendering |
|-----------|---------------|----------------|---------|-------------|--------------------|
| Figure | Listed | Standard Markdown image plus caption text | Presents one visual with explanatory context. | Use for diagrams, illustrations, or visual explanations. | Preserve image, alt text, caption, and relationship to surrounding text. |
| Gallery | Extended | `:::gallery` | Groups multiple related visuals. | Use for asset sets, UI states, screenshots, or visual comparisons. | Preserve collection order, labels, and captions. |
| Screenshot | Listed | Standard Markdown image or `:::screenshot` when fields are needed | Shows a captured UI or runtime state. | Use to document visual state, interface, editor view, or output. | Preserve image, context, and alt text. |
| Video | Listed | Standard Markdown link or `:::video` when fields are needed | References audiovisual documentation. | Use for tutorials, demonstrations, or captured behavior. | Preserve media target, title, description, and fallback link. |
| Icon | Listed | Standard Markdown image or inline reference | Represents a compact visual identifier. | Use when an icon itself must be documented or referenced. | Preserve icon identity and alt text. |
| Badge | Extended | `:::badge` | Represents compact status or classification metadata. | Use for status, support level, compatibility, or classification. | Preserve label and semantic status without requiring visual styling. |

### Media Component Examples

```md
![Authoring flow diagram](assets/authoring-flow.png)

Figure: The authoring flow from Markdown source to rendered output.

:::gallery
**Name:** Renderer Output States

- ![Desktop output](assets/desktop-output.png)
- ![Mobile output](assets/mobile-output.png)
:::

:::screenshot
**Title:** Component Library Section

**Image:** `assets/component-library-section.png`

**Alt:** Screenshot of the Component Library section.
:::

:::video
**Title:** Documentation Authoring Walkthrough

**Source:** `media/authoring-walkthrough.mp4`

**Description:** Demonstrates the authoring workflow.
:::

:::badge
**Label:** Core

**Meaning:** Required for basic Renderer compatibility.
:::
```

## Governance Components

Governance Components preserve project reasoning and reduce repeated discussions by recording decisions, alternatives, assumptions, risks, and unresolved questions.

| Component | Support Level | Markdown Usage | Purpose | When to Use | Expected Rendering |
|-----------|---------------|----------------|---------|-------------|--------------------|
| Requirement | Extended | `:::requirement` | Records a required capability, behavior, or constraint. | Use for must-have product, system, or documentation requirements. | Preserve requirement statement, status, and rationale. |
| Objective | Extended | `:::objective` | Records a desired outcome or goal. | Use for goals that guide design or project direction. | Preserve objective, measurement, and status. |
| Decision | Extended | `:::decision` | Records an approved or proposed decision. | Use when preserving reasoning matters for future contributors. | Preserve decision, rationale, status, and consequences. |
| Alternative | Extended | `:::alternative` | Records an option considered but not necessarily chosen. | Use when documenting choices and rejected approaches. | Preserve option, evaluation, and relationship to a decision. |
| Trade-off | Extended | `:::trade-off` | Records a balance between competing concerns. | Use when a choice improves one concern while weakening another. | Preserve benefits, costs, and accepted consequences. |
| Constraint | Listed | `:::constraint` | Records a limitation that bounds possible solutions. | Use for technical, business, platform, or policy constraints. | Preserve constraint, source, and impact. |
| Assumption | Extended | `:::assumption` | Records something believed true but requiring validation. | Use when work depends on unverified context. | Preserve assumption, confidence, validation path, and status. |
| Dependency | Listed | `:::dependency` | Records reliance on another system, team, asset, or decision. | Use when progress or behavior depends on an external factor. | Preserve dependency target, owner if known, and impact. |
| Risk | Extended | `:::risk` | Records a possible future problem and mitigation. | Use when uncertainty may affect quality, schedule, compatibility, or correctness. | Preserve risk, impact, likelihood, mitigation, and status. |
| Open Question | Extended | `:::open-question` | Records unresolved questions. | Use when a decision is pending or more information is needed. | Preserve question, owner if known, and current status. |

### Governance Component Examples

```md
:::requirement
**Requirement:** Markdown must remain the source of truth.

**Status:** Active
:::

:::objective
**Objective:** Make authored documentation predictable for AI agents.

**Measure:** Agents use official Component syntax without inventing aliases.
:::

:::decision
**Decision:** Use Callout Syntax for Information Components.

**Rationale:** It remains readable in raw Markdown.

**Status:** Approved
:::

:::alternative
**Alternative:** Use raw HTML alert blocks.

**Outcome:** Rejected

**Reason:** Raw HTML would couple authoring to a Renderer.
:::

:::trade-off
**Trade-off:** Structured Blocks are more explicit than plain prose but require Renderer support for rich presentation.

**Accepted Consequence:** Unsupported blocks must degrade gracefully.
:::

:::constraint
**Constraint:** Documentation authors must not define visual styling.

**Source:** Component Library
:::

:::assumption
**Assumption:** Future Renderers will support at least readable fallback for Structured Blocks.

**Validation:** Renderer compatibility testing.
:::

:::dependency
**Dependency:** Renderer Expectations

**Impact:** Components rely on Renderers preserving semantic meaning.
:::

:::risk
**Risk:** Authors may invent unofficial Component aliases.

**Impact:** Inconsistent rendering and validation.

**Mitigation:** Validate Component names against the Component Library.
:::

:::open-question
**Question:** Should project-specific Components be allowed in v1?

**Status:** Open
:::
```

## Navigation Components

Navigation Components support user movement through documentation but do not replace the Navigation System.

| Component | Support Level | Markdown Usage | Purpose | When to Use | Expected Rendering |
|-----------|---------------|----------------|---------|-------------|--------------------|
| See Also | Core | Standard Markdown list or section | Points readers to related local topics. | Use near content that naturally leads to other sections or documents. | Preserve related navigation options. |
| Previous | Listed | Standard Markdown link or `:::previous` when fields are needed | Points to the previous logical topic. | Use when authoring an explicit sequence. | Preserve backward movement relationship. |
| Next | Listed | Standard Markdown link or `:::next` when fields are needed | Points to the next logical topic. | Use when authoring an explicit sequence. | Preserve forward movement relationship. |
| Back to Top | Listed | Standard Markdown anchor link | Points back to the top of the current document or section. | Use in long documents when explicit return navigation is useful. | Preserve return target without redefining global navigation. |

### Navigation Component Examples

```md
## See Also

- [Content System](../guidelines/ContentSystem.md)
- [Component Library](../guidelines/ComponentLibrary.md)

:::previous
**Label:** Content System

**Target:** `../guidelines/ContentSystem.md`
:::

:::next
**Label:** Navigation System

**Target:** `../guidelines/NavigationSystem.md`
:::

[Back to Top](#component-usage-reference)
```

## Component Selection Guide

Use this guide when deciding which Component syntax to author.

| Need | Use |
|------|-----|
| Normal prose, lists, tables, links, images, and code | Standard Markdown |
| Context, advice, warnings, examples, or practices | Callout Syntax |
| API, configuration, architecture, media collections, or governance records | Structured Block Syntax |
| Cross-document movement or related material | Reference or Navigation Components |
| Visual or audiovisual assets | Media Components |

## Validation Checklist

Before using this document as a Component authoring reference, verify:

- The Component exists in [ComponentLibrary.md](../guidelines/ComponentLibrary.md).
- Basic Components use Standard Markdown.
- Information Components use supported callout types.
- Structured Blocks use official lowercase kebab-case names.
- Content remains readable in raw Markdown.
- No raw HTML, CSS, JavaScript, or Renderer-specific presentation rules were introduced.
- Related Documents and Revision History are present.

# Related Documents

- [ComponentLibrary.md](../guidelines/ComponentLibrary.md) - Defines the official semantic documentation Components, categories, support levels, Markdown Usage patterns, and Renderer Expectations.
- [DocumentationFramework.md](../guidelines/DocumentationFramework.md) - Defines the framework vision and authoring-first principles.
- [DocumentationStandards.md](../guidelines/DocumentationStandards.md) - Defines authoring and maintenance standards.
- [ContentSystem.md](../guidelines/ContentSystem.md) - Defines the editorial hierarchy where Components participate.
- [Terminology.md](../guidelines/Terminology.md) - Defines official framework terminology.

# Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 0.1.0 | 2026-06-26 | Codex | Initial Component usage reference generated from the Component Library. |
