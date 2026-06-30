# Search System

**Project:** `com.immersivegames.docs`  
**Document Type:** Subsystem Specification  
**Status:** Draft  
**Version:** 0.1.0

---

## Purpose

The Search System defines how users find information inside generated documentation.

The Search System must support offline documentation.

It defines Searchable Content, search behavior, result presentation expectations, navigation targets, Empty State behavior, and integration points.

It does not define visual styling, JavaScript implementation details, rendering structure, content authoring, or search UI Theme.

## Core Philosophy

Search must work offline.

Search must not require a server.

Search must not require remote APIs.

Search must help users quickly find content inside documentation.

The Face System search behavior is the baseline reference for Search v1.

The framework extends that baseline to support multi-document Documentation Projects.

## Responsibilities

The Search System is responsible for defining:

- Offline search requirements.
- Active Document Search.
- Global Search.
- Searchable Content.
- Search Result structure.
- Search Result navigation.
- Empty State behavior.
- Search reset behavior.
- Search accessibility expectations.
- Search integration with Navigation, Rendering, Glossary, and Components.

The Search System is not responsible for:

- Visual styling.
- CSS.
- JavaScript implementation internals.
- HTML layout generation.
- Search ranking algorithms.
- Online search APIs.
- Server-side search.
- Authoring Markdown content.

## Core Model

The conceptual search model is:

```text
Search Input
        |
        v
Active Document Search
        |
        v
Visible Content Filtering
        |
        v
Result Count / Empty State
        |
        v
Optional Global Search
        |
        v
Result List with Document, Path, and Snippet
```

Active Document Search follows the Face System baseline behavior.

Global Search extends the model for complete projects with multiple Documents.

## Face System Baseline

The Face System HTML documentation search is the baseline behavior for Search v1.

Baseline behavior includes:

- Offline search.
- Client-side search.
- No server.
- No external dependency.
- Search input in the documentation interface.
- Search inside the active documentation context.
- Filtering visible content based on the search term.
- Updating visible navigation during search.
- Showing result count.
- Showing an Empty State when no result is found.
- Clearing Search with Escape when supported.
- Resetting Search context when switching major documentation areas.
- Basic accessibility support through labels, roles, and live status where supported.

The framework must preserve this simplicity while supporting larger documentation structures.

## Search Modes

The Search System defines two search modes.

### Active Document Search

Active Document Search is the default mode.

It searches the currently active Document.

Expected behavior:

- Search only the active Document.
- Match Chapters, Sections, Subsections, and visible content.
- Filter visible content when practical.
- Update Sidebar and Local Table of Contents visibility when practical.
- Show the number of matched Sections or results.
- Show an Empty State when nothing matches.
- Allow the user to clear the Search.
- Preserve readable documentation when Search is inactive.

This mode is closest to the Face System search behavior.

### Global Search

Global Search is an extended mode for larger Documentation Projects.

It searches all Documents in the Documentation Project.

Expected behavior:

- Search across all Documents.
- Return results grouped or labeled by Document.
- Show the navigation path for each result.
- Show a short snippet when possible.
- Allow navigation to the matching Document and location.
- Include Glossary terms when available.
- Include relevant Component content.

Global Search may be implemented after Active Document Search but must be supported by the Search System specification.

## Searchable Content

Searchable Content includes:

- Document titles.
- Chapter headings.
- Section headings.
- Subsection headings.
- Paragraph text.
- List content.
- Table text.
- Callout titles.
- Callout content.
- Structured Block field labels.
- Structured Block content.
- Governance Component titles and fields.
- Technical Component names and fields.
- Image captions.
- Figure captions.
- Glossary terms.
- Glossary definitions.
- Related Documents labels.

Code Block content may be searchable, but large Code Blocks should be handled carefully to avoid noisy results.

## Non-Searchable or Low-Priority Content

The following content may be excluded or treated as low priority:

- Decorative labels.
- Repeated navigation text.
- Footer Metadata.
- Generated UI labels.
- Large Code Blocks.
- Raw generated markup.
- Hidden implementation Metadata.

The goal is useful documentation Search, not indexing every repeated UI string.

## Search Result Structure

A Search Result should contain:

- Result title.
- Source Document.
- Navigation path or breadcrumb.
- Matching content type.
- Short snippet when available.
- Target anchor or navigation destination.

Example conceptual result:

```text
FaceController

Engineering > Systems > Face System > API

Found in Method block

"... FaceController manages active FaceState and animation playback..."
```

This specification does not define final HTML layout.

Visual treatment belongs to the Theme System.

## Search Navigation

Search Results must navigate users to the correct documentation location.

Valid search targets include:

- Document.
- Chapter.
- Section.
- Subsection.
- Rendered content unit.
- Glossary term.
- Component location when addressable.

Navigation must follow the Navigation System.

Search must not create a separate navigation model.

## Search and Navigation Integration

Active Document Search may filter visible content and visible navigation entries.

Sidebar and Local Table of Contents may update during Search.

Current location should remain understandable.

Clearing Search should restore the normal navigation state.

Switching Documents should clear or reset Active Document Search unless a Global Search result explicitly navigates there.

Search must not redefine Document Tabs, Sidebar, Breadcrumb, or Local Table of Contents.

## Search and Component Integration

Search must understand content produced by Component Library usage.

Search should include meaningful text from:

- Information Components.
- Technical Components.
- Architecture Components.
- Reference Components.
- Media captions.
- Governance Components.
- Navigation Components when relevant.

Structured Components should expose their meaningful fields to Search.

Examples include:

- Decision.
- Risk.
- Assumption.
- Open Question.
- Method.
- Parameter.
- Configuration.

Search should avoid indexing purely visual Component wrappers.

## Search and Glossary Integration

Search should include Glossary terms and definitions when a Glossary System is available.

Glossary results should be identifiable as glossary results.

Expected glossary result data:

- Term.
- Definition snippet.
- Related Document or context when available.
- Target location.

The Glossary System defines term rules, aliases, and glossary data.

The Search System defines how glossary entries participate in Search Results.

## Search Input Behavior

Expected input behavior:

- Search should respond to typed queries.
- Empty Search should show normal documentation state.
- Search should be clearable.
- Escape may clear the Search when supported.
- Search should ignore accidental leading or trailing spaces.
- Search should handle case-insensitive matching by default.
- Short queries may require minimum length if needed for usability.

This specification does not define implementation details.

## Empty State

When no result is found, the documentation should show a clear Empty State.

The Empty State should:

- Tell the user no results were found.
- Preserve access to normal navigation.
- Allow clearing the Search.
- Avoid hiding the entire documentation shell.
- Avoid presenting an error state.

Example:

```text
No results found.
Try a different term or clear the search.
```

## Result Count and Status

Search should provide a result count or status message when practical.

Examples:

- `3 sections found.`
- `No results found.`
- `12 results across 4 documents.`

Status should be accessible when supported by the Renderer.

## Search Index

A Renderer may generate a local Search Index.

The index must remain local and offline.

The Search System does not require a specific index format.

A Search Index may include:

- Document IDs.
- Heading IDs.
- Anchors.
- Text excerpts.
- Component type.
- Glossary term Metadata.
- Breadcrumb or path data.

This revision does not define a final JSON schema.

## Offline Requirement

Search must work offline.

Requirements:

- No server required.
- No remote search service.
- No external API.
- No CDN dependency.
- Local assets only.
- Search must work when documentation is opened from `index.html`.

## Accessibility

Search input should have a clear label.

Search status should be perceivable.

Empty State should be understandable.

Keyboard users should be able to use Search.

Search Result navigation should be clear.

Search should not rely only on color.

Result focus and active states should be visually clear when supported.

This specification does not define ARIA implementation details.

## Renderer Integration

The Rendering System provides the output hooks required for Search.

The Search System defines behavior and result expectations.

The Theme System defines visual styling for search input, Search Results, status, and Empty States.

The Navigation System defines valid destinations.

The Glossary System defines glossary data.

## Design Decisions

### Face System Search Is the Baseline

**Decision:** The framework uses the proven Face System search behavior as the baseline for Search v1.

**Rationale:** The Face System search behavior is simple, offline, client-side, and already works for generated documentation.

**Consequence:** Search v1 can remain lightweight while establishing a path for larger multi-document projects.

### Active Document Search Comes First

**Decision:** Active Document Search is the default search mode.

**Rationale:** Active Document Search provides fast, focused results and keeps the first implementation simple.

**Consequence:** Documentation can support useful offline search before Global Search is implemented.

### Global Search Supports Large Projects

**Decision:** Global Search extends search across all Documents in a Documentation Project.

**Rationale:** Larger projects need Search across Game Design Documents, Engineering Documentation, Art Bibles, API References, Glossaries, and other Documents.

**Consequence:** Search must define result structures that identify Document, path, snippet, and target location.

### Search Must Remain Offline

**Decision:** Search must work without internet, server, or external search service.

**Rationale:** Documentation must remain portable, distributable, and usable from local offline packages.

**Consequence:** Search behavior, indexes, and assets must remain local.

### Search Integrates With Navigation

**Decision:** Search Results must navigate using the Navigation System instead of creating a separate navigation model.

**Rationale:** Users should move through documentation consistently whether they navigate manually or from Search Results.

**Consequence:** Search targets must align with Documents, Chapters, Sections, Subsections, rendered content units, Glossary terms, and addressable Component locations.

## Out of Scope

The Search System does not define:

- CSS styling.
- HTML layout generation.
- JavaScript implementation details.
- Search ranking algorithms.
- Search backend services.
- Online search.
- Remote APIs.
- Search analytics.
- AI semantic search.
- Full-text database implementation.
- Final search index schema.

## Future Extensions

The Search System may later support:

- Search result highlighting.
- Advanced ranking.
- Filters by Document.
- Filters by Component type.
- Glossary-only search.
- Search history.
- Recently searched terms.
- Fuzzy matching.
- Synonym support.
- Generated search index schema.
- Keyboard shortcut for search.
- Search analytics for local builds.
- Component-specific result badges.

# Related Documents

- [DocumentationFramework.md](DocumentationFramework.md) - Defines the framework vision, principles, and intended documentation experience.
- [FrameworkArchitecture.md](FrameworkArchitecture.md) - Defines the root architecture and subsystem relationships.
- [DocumentationStandards.md](DocumentationStandards.md) - Defines the documentation standards used by this specification.
- [Terminology.md](Terminology.md) - Defines the official vocabulary used by this specification.
- [ContentSystem.md](ContentSystem.md) - Defines the editorial hierarchy and authored content made searchable after rendering.
- [NavigationSystem.md](NavigationSystem.md) - Defines navigation concepts and valid destinations for Search Results.
- [ComponentLibrary.md](ComponentLibrary.md) - Defines Components whose meaningful content participates in Search.
- [RenderingSystem.md](RenderingSystem.md) - Defines output hooks and local package expectations used by Search.
- [ThemeSystem.md](ThemeSystem.md) - Defines visual treatment for search input, Search Results, status, and Empty States.
- [GlossarySystem.md](GlossarySystem.md) - Defines Glossary Terms, definitions, aliases, and glossary data used by Search.

# Revision History

| Version | Date       | Author          | Description                          |
|---------|------------|-----------------|--------------------------------------|
| 0.1.0   | 2026-06-30 | Immersive Games | Initial Search System specification. |
