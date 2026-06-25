# ADR-0001 - Authoring First

**Status:** Accepted  
**Date:** 2026-06-25  
**Project:** com.immersivegames.docs

## Context

Documentation frameworks are often defined by their first output technology. This can cause authoring concepts, content organization, and maintenance practices to become coupled to templates, browser behavior, or generated files.

The Immersive Games Documentation Framework must support multiple documentation types, human authors, AI agents, and future output formats. Its architecture therefore requires a stable authoring model that exists independently from any Renderer.

## Decision

The framework prioritizes how documentation is authored, organized, and maintained before any rendering technology.

The following principles apply:

- The framework is not primarily an HTML template.
- The framework guides humans and AI agents in producing structured documentation.
- The Content System defines the authoring model.
- Rendering consumes authored documentation and must not define its editorial structure.
- HTML is only the first output format.
- Future Renderers must preserve the meaning and hierarchy of authored documentation.

## Consequences

- Authoring guidelines and subsystem specifications must exist before implementation begins.
- Renderer-specific concepts must remain outside the authoritative authoring model.
- HTML implementation choices cannot redefine framework architecture.
- Humans and AI agents can author documentation without knowledge of a target Renderer.
- New output formats can be added without redesigning the Content System.
- Additional architecture work is required to define clear contracts between Authoring, Rendering, Navigation, and Presentation.

## Related Documents

- [DocumentationFramework.md](../guidelines/DocumentationFramework.md) — Defines the framework vision and authoring-first philosophy.
- [FrameworkArchitecture.md](../guidelines/FrameworkArchitecture.md) — Defines the root architecture and dependency direction.
- [ContentSystem.md](../guidelines/ContentSystem.md) — Defines the editorial authoring model.

## Revision History

| Version | Date       | Author          | Description                |
|---------|------------|-----------------|----------------------------|
| 0.1.0   | 2026-06-25 | Immersive Games | Initial accepted decision. |
