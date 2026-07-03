# immersive-documentation-framework

## Purpose

This skill is the official operational entry point for the Immersive Games Documentation Framework.

It guides AI agents in authoring, updating, maintaining, validating, and rendering documentation according to the framework specifications in `guidelines/`.

The skill does not redefine the framework architecture. The guideline documents remain the source of architectural truth. When this skill conflicts with a guideline, the guideline takes precedence according to the resolution order defined below.

## Capabilities

This skill supports:

- creating a Documentation Project;
- updating an existing Documentation Project;
- organizing authored knowledge using the official editorial hierarchy;
- preserving framework terminology and project terminology;
- applying Component Library conventions;
- maintaining Related Documents and Revision History where required;
- validating documentation against framework standards;
- rendering a valid Documentation Project with the default HTML template when requested.

## Operating Modes

### Authoring Mode

Use Authoring Mode when the user asks to create, update, audit, or maintain Markdown documentation.

Possible inputs include:

- source code;
- Unity projects;
- existing Markdown documents;
- architecture documents;
- design documents;
- notes;
- specifications;
- API surfaces;
- project assets;
- existing documentation folders.

The expected output is a Documentation Project or documentation update that follows the current Documentation Framework guidelines.

### Rendering Mode

Use Rendering Mode when the user asks to produce readable HTML documentation from a Documentation Project.

The expected input is a valid Documentation Project.

The expected output is HTML documentation using `templates/html-default/`.

Rendering must preserve the semantics defined by the Content System, Navigation System, Component Library, Theme System, Search System, Glossary System, and Asset System. Rendering must not invent presentation semantics or replace the Markdown source of truth.

## Inputs

Before acting, identify the available input types:

- user request;
- repository files;
- existing guideline documents;
- existing documentation;
- code or project structure;
- assets;
- previous generated output;
- rendering template files, when Rendering Mode is requested.

If required inputs are missing and the task cannot be completed safely, ask for clarification.

## Outputs

Possible outputs include:

- new or updated Markdown documentation;
- updated guideline-consistent metadata;
- updated Related Documents sections;
- updated Revision History entries;
- a rendered HTML documentation package using the default template;
- a validation report;
- a concise summary of changes.

Generated HTML output is derivative. Markdown remains the source of truth.

## Request Interpretation

Before selecting an operating mode or changing documentation, interpret the user's requested outcome.

Determine whether the user is asking for:

- Markdown documentation;
- rendered HTML documentation;
- a new Documentation Project;
- an update to existing documentation;
- a change to one specific Document;
- rendering only;
- review or validation only;
- a combination of authoring and rendering work.

Use the interpretation to select Authoring Mode, Rendering Mode, or both. If the request is ambiguous and the ambiguity could change the output, ask for clarification. If the intended outcome is clear from context, proceed with the smallest safe scope.

## Operational Priorities

When multiple valid actions are possible, follow these priorities:

1. Preserve existing documentation whenever practical.
2. Prefer targeted updates over broad rewrites.
3. Reuse official terminology from `Terminology.md`.
4. Preserve architectural consistency with the guideline documents.
5. Distinguish observed facts from assumptions.
6. Avoid inventing undocumented behavior.
7. Keep authored Markdown renderer-independent.
8. Render HTML only when explicitly requested.
9. Follow the Documentation Framework before applying project-specific conventions.

These priorities guide operational judgment. They do not introduce new framework concepts or implementation requirements.

## Workflow

For each task:

1. Interpret the user's request.
2. Determine whether the task is Authoring Mode, Rendering Mode, review only, or a combination.
3. Identify the requested output.
4. Identify the required project inputs.
5. Load the applicable framework guidelines.
6. Inspect available project artifacts or existing documentation.
7. Extract documentation facts from available sources.
8. Organize information according to the Documentation Framework.
9. Create or update Markdown when documentation changes are requested.
10. Render HTML with `templates/html-default/` only when rendering is explicitly requested.
11. Validate the result.
12. Produce a concise summary.

The workflow describes expected framework behavior, not a required implementation mechanism.

## Guideline Resolution Order

When guideline responsibilities overlap, use this order to resolve architectural interpretation:

1. `DocumentationFramework.md`
2. `DocumentationStandards.md`
3. `FrameworkArchitecture.md`
4. `ContentSystem.md`
5. `NavigationSystem.md`
6. `ComponentLibrary.md`
7. `ThemeSystem.md`
8. `RenderingSystem.md`
9. `SearchSystem.md`
10. `GlossarySystem.md`
11. `AssetSystem.md`
12. `Terminology.md`

Use `Terminology.md` as the vocabulary source of truth for all framework terms. The resolution order defines architectural interpretation; it does not permit inventing terminology or bypassing the terminology governance rules.

## Documentation Rules

When creating documentation:

- preserve existing project terminology;
- use official framework terminology;
- avoid inventing architecture;
- document observed behavior;
- mark assumptions clearly when facts cannot be verified;
- preserve Markdown as the source of truth;
- follow the editorial hierarchy defined by the Content System;
- use Component Library conventions for semantic components;
- follow Navigation System expectations for navigable structure;
- keep renderer-specific details out of authored content unless the document is explicitly about rendering;
- prefer references over duplicated content;
- keep each document focused on a single responsibility.

The official editorial hierarchy is:

```text
Documentation Project → Document → Chapter → Section → Subsection → Content Block
```

Markdown heading usage must reflect this hierarchy.

## Documentation Update Rules

When updating existing documentation:

- preserve unaffected documents whenever possible;
- update only the requested scope unless consistency requires a related correction;
- check whether the information already exists before adding new content;
- update cross-references when document relationships change;
- update Glossary content when project terms change;
- update Asset references when assets are added, moved, or removed;
- update Revision History when required by the Documentation Standards;
- avoid broad rewrites when a targeted correction is sufficient.

Examples of valid incremental requests include:

- update Engineering documentation;
- update Glossary terms;
- update Architecture documentation;
- update an API reference;
- update only one Document;
- add a new section to an existing Document;
- revise Related Documents after a new specification is added.

## Rendering Rules

When rendering is requested:

- use the default HTML template in `templates/html-default/`;
- preserve authored Markdown semantics;
- preserve document identity and ordering;
- preserve navigation destinations;
- preserve Component meaning;
- preserve Theme System compatibility;
- preserve Search compatibility;
- preserve Glossary compatibility;
- preserve local Asset references;
- keep the rendered output offline-first;
- do not make generated HTML the source of truth.

Rendering may adapt presentation for the output format, but it must not redefine framework concepts.

## Documentation Standards Rules

Guideline and specification documents must follow `DocumentationStandards.md`.

In particular:

- guideline documents must be Markdown;
- guideline documents must be written in English;
- each document must have one clear responsibility;
- architectural documents must clearly separate Purpose, Responsibilities, Out of Scope, Design Decisions, Related Documents, and Revision History;
- every document inside `guidelines/` must end with `# Related Documents` followed by `# Revision History`;
- Revision History tables must use ISO dates.

## Validation Checklist

Before completing a task, verify the applicable items:

- requested scope was followed;
- requested output was produced;
- correct Documentation Project was identified;
- correct Document was selected or created;
- terminology is consistent with `Terminology.md`;
- architectural responsibilities remain consistent with the guideline documents;
- observed facts and assumptions are clearly separated;
- existing documentation was preserved when updates were requested;
- documentation completeness is appropriate for the requested scope;
- Markdown formatting is valid;
- Markdown heading hierarchy is valid;
- Content System hierarchy is preserved;
- Navigation System expectations are preserved;
- Component Library conventions are followed;
- Theme System assumptions remain renderer-independent;
- Search and Glossary expectations remain consistent;
- Asset references are local and valid;
- Related Documents are accurate;
- Revision History is updated when required;
- renderer-specific assumptions did not leak into authored content;
- rendered output, when requested, remains derivative and offline-first;
- no unrelated documents were rewritten unnecessarily.

## Limitations

This skill does not:

- redesign the Documentation Framework;
- create new guideline documents unless the user explicitly requests it;
- define new framework concepts without updating `Terminology.md`;
- implement a Markdown renderer by default;
- create build tooling by default;
- replace the guideline documents as the architectural source of truth;
- treat HTML output as the source of truth.

## Success Criteria

A task succeeds when the result:

- follows the Immersive Games Documentation Framework;
- preserves Markdown as the source of truth;
- is understandable by humans;
- is predictable for AI agents;
- is consistent with the current guidelines;
- can be rendered without changing authored semantics;
- keeps implementation concerns separate from framework architecture.

## Revision History

| Version | Date       | Author          | Description |
|---------|------------|-----------------|-------------|
| 1.0.1   | 2026-07-02 | Immersive Games | Refined operating mode terminology, request interpretation, workflow, and validation guidance. |
| 1.0.0   | 2026-07-02 | Immersive Games | Refactored as the official Documentation Framework operational skill. |
| 0.1.0   | 2026-06-26 | Immersive Games | Initial documentation authoring skill. |
