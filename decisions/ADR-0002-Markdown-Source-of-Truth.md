# ADR-0002 - Markdown Source of Truth

**Status:** Accepted  
**Date:** 2026-06-25  
**Project:** com.immersivegames.docs

## Context

The framework requires an authoring format that is portable, human-readable, compatible with version control, suitable for technical writing, and practical for both human authors and AI agents.

Generated HTML and other output formats are optimized for consumption rather than authoritative maintenance. Treating generated output as source content would couple documentation to a Renderer and make reproducible multi-format output difficult.

## Decision

Markdown is the official source-of-truth authoring format for documentation content.

The following principles apply:

- Human authors and AI agents author Markdown.
- The Content System interprets Markdown as an editorial hierarchy and a set of Content Blocks.
- Renderers consume Markdown structure and semantics.
- HTML must not become the source of truth.
- Generated output must not be edited as the authoritative content source.
- Implementation output should be reproducible from Markdown and its associated project configuration and assets.

## Consequences

- Documentation changes must be made in Markdown and rendered again.
- Generated outputs are derivative artifacts.
- Renderer implementations must preserve Markdown meaning and hierarchy.
- Validation can operate against a stable, readable source format.
- Version-control history remains focused on authored documentation rather than generated files.
- Renderer-specific capabilities require documented fallback behavior when they cannot be represented consistently across outputs.

## Related Documents

- [ContentSystem.md](../guidelines/ContentSystem.md) — Defines the Markdown authoring model and editorial hierarchy.
- `guidelines/RenderingSystem.md` — Planned specification for Renderer contracts and reproducible output.
- [DocumentationStandards.md](../guidelines/DocumentationStandards.md) — Defines Markdown authoring and governance standards.

## Revision History

| Version | Date       | Author          | Description                |
|---------|------------|-----------------|----------------------------|
| 0.1.0   | 2026-06-25 | Immersive Games | Initial accepted decision. |
