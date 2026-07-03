# Component Library

**Project:** `com.immersivegames.docs`  
**Document Type:** Subsystem Specification  
**Status:** Draft  
**Version:** 0.1.0

---

## Purpose

The Component Library defines the official semantic documentation Components of the Immersive Games Documentation Framework.

It is the official reference for semantic documentation Components, Component categories, support levels, approved Markdown usage patterns, and expected Renderer interpretation.

It is not an HTML component library. It is a renderer-independent semantic component catalog that defines what documentation Components an authoring agent may use in Markdown and what a Renderer should understand when generating output.

## Core Philosophy

Components represent meaning, not appearance.

Documentation agents write Components in Markdown as part of the authored source of truth. Renderers decide how those Components are presented in each output format.

Components must be reusable across Game Design Documents, technical documentation, API references, user manuals, project documentation, and other Documentation Project types. A Component should describe an authoring intent that remains useful even when rendered as HTML, PDF, EPUB, wiki content, or another output.

The Component Library may define Markdown syntax for authoring Components. It must not define visual styling, HTML structure, CSS, JavaScript, or layout.

## Responsibilities

The Component Library is responsible for:

- Defining official Component categories.
- Defining official Component names.
- Defining when each Component should be used.
- Defining approved Markdown usage patterns.
- Defining expected Renderer behavior without prescribing HTML, CSS, or JavaScript.
- Preventing agents from inventing random Component types.

The Component Library is not responsible for:

- HTML implementation.
- CSS.
- JavaScript.
- Visual styling.
- Theme rules.
- Renderer internals.

## Core Model

```text
Documentation Author
        |
        v
Markdown
        |
        v
Official Component Usage
        |
        v
Renderer
        |
        v
Human-readable Output
```

Markdown remains the source of truth. Official Component usage is authored in Markdown and interpreted by Renderers according to framework contracts.

Generated output is derivative. A Renderer may choose the most appropriate presentation for each Component, but it must preserve the Component's semantic meaning.

## Component Specification Format

Every Component should be documented with:

- **Name:** The official Component name.
- **Category:** The Component category that owns the Component.
- **Support Level:** Whether the Component is Core or Extended.
- **Purpose:** The meaning or authoring intent represented by the Component.
- **When to Use:** The situations where the Component is appropriate.
- **Markdown Usage:** The mandatory approved Markdown pattern expected from authors or AI agents.
- **Expected Rendering:** The semantic behavior a Renderer should preserve.
- **Notes:** Additional constraints, cautions, or relationship details.
- **Examples:** Representative authoring examples.

## Component Support Levels

### Core Components

Core Components are required for any Renderer claiming basic framework compatibility.

A Renderer that supports only Core Components must still preserve readable documentation, structural hierarchy, and semantic intent for the required set.

### Extended Components

Extended Components are optional but recommended for richer documentation.

A Renderer may support Core only, Core plus selected Extended Components, or the full Component Library. Unsupported Extended Components should degrade gracefully to readable Markdown or a simple Content Block while preserving the authored meaning as much as possible.

## Component Categories

### 1. Basic Components

Basic Components represent standard Markdown content structures and common authored content units.

- Heading.
- Paragraph.
- List.
- Ordered List.
- Checklist.
- Table.
- Quote.
- Code Block.
- Inline Code.
- Horizontal Rule.
- Link.
- Image.

### 2. Information Components

Information Components highlight explanatory, advisory, cautionary, or example-based content.

- Note.
- Info.
- Tip.
- Warning.
- Important.
- Success.
- Example.
- Best Practice.

### 3. Technical Components

Technical Components describe software, APIs, configuration, runtime concepts, and engineering reference material.

- API.
- Method.
- Property.
- Parameter.
- Return Value.
- Event.
- Enumeration.
- Interface.
- Class.
- Namespace.
- Configuration.

### 4. Architecture Components

Architecture Components describe structural, behavioral, or temporal relationships in systems and documentation.

- Flow.
- Process.
- Timeline.
- Sequence.
- Pipeline.
- State.
- Lifecycle.
- Decision Tree.

### 5. Reference Components

Reference Components connect authored content to related documentation, external resources, assets, or glossary entries.

- Glossary Reference.
- Cross Reference.
- Related Documents.
- External Link.
- Asset Reference.
- Download.

### 6. Media Components

Media Components represent authored use of visual, audiovisual, or compact visual-reference content.

- Figure.
- Gallery.
- Screenshot.
- Video.
- Icon.
- Badge.

### 7. Governance Components

Governance Components preserve project reasoning and reduce repeated discussions by recording decisions, alternatives, assumptions, risks, and unresolved questions.

- Requirement.
- Objective.
- Decision.
- Alternative.
- Trade-off.
- Constraint.
- Assumption.
- Dependency.
- Risk.
- Open Question.

### 8. Navigation Components

Navigation Components support user movement through documentation but do not replace the Navigation System.

- See Also.
- Previous.
- Next.
- Back to Top.

The Navigation System defines navigation concepts and relationships. Navigation Components provide authored semantic markers that a Renderer may use when presenting movement options.

## Core Component Set

The initial required Core Component set is:

- Heading.
- Paragraph.
- List.
- Table.
- Image.
- Code Block.
- Quote.
- Note.
- Info.
- Tip.
- Warning.
- Important.
- Example.
- See Also.
- Related Documents.

## Extended Component Set

The initial Extended Component set is:

- Timeline.
- Flow.
- Pipeline.
- API.
- Method.
- Parameter.
- Property.
- Configuration.
- Gallery.
- Badge.
- Requirement.
- Decision.
- Trade-off.
- Alternative.
- Risk.
- Assumption.
- Open Question.

## Markdown Usage Conventions

The Component Library defines three official authoring patterns:

1. Standard Markdown.
2. Callout Syntax.
3. Structured Block Syntax.

These conventions must remain readable in raw Markdown and must not require authors to write raw HTML.

### 1. Standard Markdown

Basic Components must use Standard Markdown whenever possible.

Use Standard Markdown for:

- Heading.
- Paragraph.
- List.
- Ordered List.
- Checklist.
- Table.
- Quote.
- Code Block.
- Inline Code.
- Horizontal Rule.
- Link.
- Image.

Example:

````md
# Document Title

## Chapter

### Section

Regular paragraph.

- Item
- Item

| Field  | Value    |
|--------|----------|
| Status | Approved |

```csharp
faceController.PlayAnimation("blink");
```
````

Standard Markdown must be preferred whenever it can express the content clearly.

### 2. Callout Syntax

Information Components must use blockquote-style callouts.

Syntax:

```md
> [!TYPE]
> Content goes here.
```

Optional title syntax:

```md
> [!TYPE] Optional Title
> Content goes here.
```

Supported callout types:

- `NOTE`
- `INFO`
- `TIP`
- `WARNING`
- `IMPORTANT`
- `SUCCESS`
- `EXAMPLE`
- `BEST_PRACTICE`

Examples:

```md
> [!WARNING]
> Changing this ID may break existing animation references.
```

```md
> [!TIP] Workflow Recommendation
> Create a reusable template state before authoring shared animations.
```

Callouts must remain readable as raw Markdown. Renderers may style callouts visually. Authors must not use raw HTML to force callout appearance.

### 3. Structured Block Syntax

Extended or structured Components must use fenced semantic blocks.

Syntax:

```md
:::component-name
Content goes here.
:::
```

Component names must use `lowercase-kebab-case`.

Examples:

```md
:::decision
**Decision:** Use Markdown as the source of truth.

**Reason:** Markdown is easy to edit, review, version, and render.

**Status:** Approved
:::
```

```md
:::risk
**Risk:** Documentation may become inconsistent if terminology changes.

**Impact:** Medium

**Mitigation:** Update Terminology.md before introducing new concepts.
:::
```

```md
:::open-question
**Question:** Should the renderer support PDF export in v1?

**Status:** Open
:::
```

Use Structured Block Syntax for Components such as:

- API.
- Method.
- Property.
- Parameter.
- Timeline.
- Flow.
- Process.
- Pipeline.
- Decision.
- Alternative.
- Trade-off.
- Constraint.
- Assumption.
- Dependency.
- Risk.
- Open Question.
- Requirement.
- Objective.

Structured Blocks are used when a Component needs fields, Metadata, or multi-part content. Renderers may transform Structured Blocks into richer visual layouts. Unsupported Structured Blocks must degrade gracefully into readable content.

Agents must not invent new Structured Block names unless explicitly proposing a new Component.

## Component Naming Rules

Callout types must use uppercase snake case inside `[!TYPE]`.

Structured Block names must use lowercase kebab case.

Component names in prose should use Title Case.

Aliases must not be created unless they are officially documented.

Contributors and AI agents must not invent synonyms for existing Components.

Correct:

```md
> [!BEST_PRACTICE]
```

```md
:::open-question
:::
```

Incorrect:

```md
> [!BestPractice]
```

```md
:::openQuestion
:::
```

```md
:::question-block
:::
```

## Links and References

Use standard Markdown links for internal and external references.

Do not introduce wiki-style links such as `[[Term]]` in v1.

Glossary references should also use standard Markdown links.

Cross-document references should remain readable in raw Markdown.

Examples:

```md
See [Content System](ContentSystem.md).
```

```md
See [FaceState](Glossary.md#facestate).
```

## Renderer Expectations

Renderers must understand Standard Markdown.

Renderers must support all Core Components.

Renderers should support official Callout Syntax.

Renderers may progressively support Extended Components.

Renderers should support Structured Block Syntax when implementing Extended Components.

If a Renderer does not support an Extended Component, it should gracefully degrade to readable content or a simple Content Block.

Renderers should preserve the semantic meaning of each Component.

Renderers should not require authors to write raw HTML, CSS, JavaScript, or renderer-specific markup.

## Design Decisions

### Components Are Semantic

**Decision:** Components are defined by meaning and authoring intent before visual treatment.

**Rationale:** Semantic Components can be authored consistently, validated, rendered accessibly, and translated across output formats.

**Consequence:** Visual presentation belongs to Renderers and Themes, not to the Component Library.

### The Library Is Renderer-Independent

**Decision:** The Component Library defines Components independently from HTML, CSS, JavaScript, and other output technologies.

**Rationale:** Documentation authored for the framework must remain portable across Renderers.

**Consequence:** A Component's contract must remain meaningful even when a Renderer cannot reproduce the same visual treatment as another Renderer.

### Core and Extended Support Levels Exist

**Decision:** Components are grouped into Core and Extended support levels.

**Rationale:** Basic compatibility must be achievable by simple Renderers, while richer documentation still needs a path for more expressive Components.

**Consequence:** Renderers can declare compatible support levels without forcing every Renderer to implement the full library immediately.

### Governance Components Are Included

**Decision:** Governance Components are part of the official Component Library.

**Rationale:** Documentation often needs to preserve decisions, alternatives, trade-offs, assumptions, risks, dependencies, and open questions.

**Consequence:** Project reasoning can be captured in structured documentation instead of being repeated, lost, or scattered across informal discussions.

### Markdown Syntax Is Centralized Here

**Decision:** The Component Library defines the official Markdown usage conventions for Components.

**Rationale:** Component authoring needs one predictable source of truth so human authors and AI agents do not invent competing notation.

**Consequence:** Standard Markdown, Callout Syntax, Structured Block Syntax, naming rules, and link conventions are centralized in this specification while Renderer implementation remains outside its scope.

## Out of Scope

The Component Library does not define:

- HTML.
- CSS.
- JavaScript.
- Bootstrap.
- Theme styling.
- Renderer implementation.
- Parser implementation.
- Visual layout.

## Future Extensions

The Component Library may later support:

- Custom project-specific Components.
- Component aliases.
- Component validation.
- Component templates.
- Renderer compatibility tables.
- Component examples library.
- Game Design Document-specific Component presets.
- Engineering-specific Component presets.

Future extensions must preserve semantic meaning, renderer independence, and Markdown as the source of truth.

# Related Documents

- [DocumentationFramework.md](DocumentationFramework.md) — Defines the framework vision, principles, and intended documentation experience.
- [FrameworkArchitecture.md](FrameworkArchitecture.md) — Defines the root architecture and subsystem relationships.
- [DocumentationStandards.md](DocumentationStandards.md) — Defines the authoring and maintenance standards applied to this specification.
- [Terminology.md](Terminology.md) — Defines the official vocabulary used by this specification.
- [ContentSystem.md](ContentSystem.md) — Defines the editorial hierarchy where Components participate in authored content.
- [NavigationSystem.md](NavigationSystem.md) — Defines navigation concepts and relationships that may be supported by Navigation Components.
- [AssetSystem.md](AssetSystem.md) — Defines where asset files live and how asset-related Components reference them.
- [RenderingSystem.md](RenderingSystem.md) — Defines Renderer contracts, output lifecycle, and Component rendering expectations.
- [ThemeSystem.md](ThemeSystem.md) — Defines semantic Theme Tokens, visual direction, and Component presentation policies.

# Revision History

| Version | Date       | Author          | Description                              |
|---------|------------|-----------------|------------------------------------------|
| 0.2.2   | 2026-07-02 | Immersive Games | Updated Related Documents to reflect current Rendering and Theme System specifications. |
| 0.2.1   | 2026-06-30 | Immersive Games | Added Asset System reference. |
| 0.2.0   | 2026-06-26 | Immersive Games | Added official Markdown component authoring conventions. |
| 0.1.0   | 2026-06-26 | Immersive Games | Initial Component Library specification. |
