# Glossary System

**Project:** `com.immersivegames.docs`  
**Document Type:** Subsystem Specification  
**Status:** Draft  
**Version:** 0.1.0

---

## Purpose

The Glossary System defines how important terms are recorded, explained, referenced, searched, and rendered.

The Glossary System helps keep documentation terminology consistent across Documents, systems, Game Design Documents, APIs, manuals, and project documentation.

It does not define general terminology governance for the framework itself. [Terminology.md](Terminology.md) remains the official vocabulary for the framework architecture.

Project glossaries define vocabulary for specific Documentation Projects.

## Core Philosophy

Terms should be defined once and reused consistently.

Glossaries reduce ambiguity.

Glossaries help humans understand project language.

Glossaries help AI agents avoid inventing synonyms.

Glossaries should remain readable as Markdown.

Glossaries should participate in Search.

Glossaries should be renderable as part of offline HTML documentation.

## Responsibilities

The Glossary System is responsible for defining:

- Glossary document structure.
- Glossary term structure.
- Term definitions.
- Term categories.
- Aliases and synonyms.
- Related terms.
- Term linking rules.
- Search integration.
- Renderer integration.
- Agent maintenance rules.
- Human-readable glossary presentation.

The Glossary System is not responsible for:

- Framework architecture vocabulary.
- Replacing [Terminology.md](Terminology.md).
- Visual styling.
- HTML implementation.
- JavaScript behavior.
- Search implementation internals.
- Project planning.

## Core Model

The conceptual glossary model is:

```text
Glossary Document
        |
        v
Glossary Term
        |
        v
Definition
        |
        v
Aliases / Related Terms / Category
        |
        v
Search + Navigation + Rendering
```

A glossary is authored in Markdown and rendered into the documentation output.

## Glossary Document

A Glossary Document is a Markdown Document that contains official terms for a Documentation Project.

Recommended file name:

```text
glossary.md
```

In a larger project, the glossary may appear alongside other Documents:

```text
documents/
|-- gdd.md
|-- engineering.md
|-- art-bible.md
|-- api-reference.md
`-- glossary.md
```

The glossary may be rendered as a dedicated Document tab.

The glossary may also be integrated into Search.

The glossary should remain readable in raw Markdown.

## Glossary Term Structure

The preferred simple Markdown format is:

```md
## FaceState

**Definition:** Persistent facial state that defines semantic frame mappings for one character expression.

**Category:** Face System

**Aliases:** State, Facial State

**Related Terms:** FaceAnimation, FaceSpriteLibrary, Semantic Frame
```

Each term should use a heading.

The heading becomes the term anchor.

Definition is required.

Category is recommended.

Aliases are optional.

Related Terms are optional.

Custom syntax for Glossary Terms is not required in v1.

## Required Term Fields

Required fields:

- Term.
- Definition.

A term must have a clear definition.

The term heading acts as the official term name.

## Optional Term Fields

Optional fields:

- Category.
- Aliases.
- Related Terms.
- Source Document.
- Status.
- Notes.
- Examples.

Category should be used to group project-specific terms by domain or subject.

Aliases should be used when readers may know a concept by another name.

Related Terms should be used when concepts are connected and readers may need to move between them.

Source Document should be used when a term is primarily defined or owned by a specific Document.

Status should be used when a term is proposed, active, deprecated, or otherwise lifecycle-dependent.

Notes should be used for clarifying usage guidance.

Examples should be used when a definition benefits from concrete usage.

## Term Categories

Categories help group terms.

Examples include:

- Face System.
- Runtime.
- Authoring.
- Gameplay.
- Engineering.
- API.
- Art.
- Narrative.
- Production.
- Marketing.

Categories should remain project-specific.

## Aliases and Synonyms

Aliases are alternative names users may search for.

Aliases should not replace the official term.

Agents must prefer the official term in documentation.

Aliases are useful for Search and onboarding.

Contributors should avoid creating multiple competing terms for the same concept.

Example:

```md
**Aliases:** State, Facial State
```

## Related Terms

Related Terms connect concepts.

Related Terms should use official term names.

Related Terms may become links when rendered.

Related Terms help readers move between concepts.

Example:

```md
**Related Terms:** FaceAnimation, FaceSpriteLibrary, Semantic Frame
```

## Term Linking

Use standard Markdown links for glossary references.

Do not introduce wiki-style links in v1.

Link to glossary anchors when referring to terms.

Links should remain readable in raw Markdown.

Examples:

```md
See [FaceState](glossary.md#facestate).
```

```md
See [Content System](ContentSystem.md).
```

Link formatting must follow Component Library conventions.

## Agent Maintenance Rules

AI agents should add or update glossary terms when introducing:

- New system concepts.
- Project-specific terms.
- Game mechanics.
- Gameplay resources.
- Technical concepts.
- API concepts.
- Acronyms.
- Abbreviations.
- Repeated domain terms.
- Terms that may be ambiguous to readers.

Agents should consult the glossary before introducing new terms.

Agents should not invent synonyms when an official term exists.

Agents should recommend glossary updates when they detect missing or inconsistent terminology.

## Search Integration

Glossary content must participate in Search.

Searchable glossary content includes:

- Term name.
- Definition.
- Aliases.
- Category.
- Related Terms.
- Examples.
- Notes.

Glossary results should be identifiable as glossary results.

Search behavior belongs to the Search System.

The Glossary System defines what glossary data should be searchable.

## Rendering Integration

The Rendering System may render the glossary as:

- A dedicated Document tab.
- A dedicated glossary section.
- A searchable glossary panel.
- An integrated glossary view.

For v1, the recommended default is:

```text
Glossary as a dedicated Document tab
```

The Theme System defines visual styling.

The Glossary System defines content structure and behavior expectations.

## Navigation Integration

Glossary terms should have stable anchors.

Glossary terms should be reachable through normal navigation.

Glossary references should navigate using standard Markdown links.

Related Terms may become internal links.

Glossary should not create a separate navigation model.

Navigation behavior must follow the Navigation System.

## Glossary and Terminology.md Boundary

[Terminology.md](Terminology.md) defines the official vocabulary of the Documentation Framework itself.

A project glossary defines the vocabulary of a specific Documentation Project.

Framework terminology examples:

- Document.
- Chapter.
- Component.
- Renderer.
- Theme System.

Project glossary terminology examples:

- FaceState.
- FaceAnimation.
- Core Loop.
- Player State.
- Enemy Type.

The Glossary System does not replace [Terminology.md](Terminology.md).

## Design Decisions

### Glossary Uses Markdown Headings

**Decision:** Glossary Terms use Markdown headings.

**Rationale:** Headings keep glossary terms readable, navigable, searchable, and easy to link.

**Consequence:** A Glossary Term heading can become a stable anchor in rendered output.

### Glossary Is a Documentation Document

**Decision:** The glossary should behave like a normal Document in the framework.

**Rationale:** Treating the glossary as a Document makes it renderable, searchable, and navigable through existing framework contracts.

**Consequence:** Glossary content can participate in Document Tabs, Search, and Navigation without a separate document model.

### Terminology.md Remains Framework Vocabulary

**Decision:** Project glossaries do not replace the framework's own terminology.

**Rationale:** Framework vocabulary and project vocabulary have different scopes and authorities.

**Consequence:** [Terminology.md](Terminology.md) remains the source of truth for architecture terms, while project glossaries define project-specific terms.

### Standard Markdown Links Preserve Simplicity

**Decision:** Glossary references use standard Markdown links in v1.

**Rationale:** Standard Markdown links remain readable, portable, and compatible with existing Markdown workflows.

**Consequence:** The framework avoids wiki-style links in v1.

### Aliases Support Search, Not Terminology Drift

**Decision:** Aliases help users find terms but do not replace official names.

**Rationale:** Search and onboarding benefit from alternate names, but documentation consistency depends on a preferred official term.

**Consequence:** Agents and contributors should use the official term in authored content and reserve aliases for discovery.

## Out of Scope

The Glossary System does not define:

- Visual styling.
- HTML implementation.
- JavaScript behavior.
- Search ranking.
- Automatic term extraction.
- AI-generated glossary inference without review.
- Wiki-style link syntax.
- Replacing [Terminology.md](Terminology.md).
- Project management vocabulary unrelated to documentation.

## Future Extensions

The Glossary System may later support:

- Automatic glossary validation.
- Missing-term detection.
- Alias conflict detection.
- Glossary import/export.
- Tooltip previews.
- Glossary popovers.
- Term usage reports.
- Glossary-only search mode.
- Localized glossary terms.
- Deprecated terms.
- Term status indicators.
- Term ownership metadata.

# Related Documents

- [DocumentationFramework.md](DocumentationFramework.md) - Defines the framework vision, principles, and intended documentation experience.
- [FrameworkArchitecture.md](FrameworkArchitecture.md) - Defines the root architecture and subsystem relationships.
- [DocumentationStandards.md](DocumentationStandards.md) - Defines the documentation standards used by this specification.
- [Terminology.md](Terminology.md) - Defines the official framework vocabulary and the boundary between framework terminology and project glossaries.
- [ContentSystem.md](ContentSystem.md) - Defines Documents and authored content structures that may include Glossary Documents.
- [NavigationSystem.md](NavigationSystem.md) - Defines navigation concepts used to reach Glossary Terms.
- [ComponentLibrary.md](ComponentLibrary.md) - Defines Markdown link conventions and related reference Components.
- [RenderingSystem.md](RenderingSystem.md) - Defines output hooks and rendering expectations for glossary content.
- [ThemeSystem.md](ThemeSystem.md) - Defines visual treatment for glossary presentation.
- [SearchSystem.md](SearchSystem.md) - Defines how Glossary Terms participate in Search.

# Revision History

| Version | Date       | Author          | Description                            |
|---------|------------|-----------------|----------------------------------------|
| 0.1.0   | 2026-06-30 | Immersive Games | Initial Glossary System specification. |
