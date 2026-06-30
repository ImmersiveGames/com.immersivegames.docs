# Asset System

**Project:** `com.immersivegames.docs`  
**Document Type:** Subsystem Specification  
**Status:** Draft  
**Version:** 0.1.0

---

## Purpose

The Asset System defines how documentation assets are organized, named, referenced, validated, and packaged.

Assets include images, screenshots, diagrams, icons, videos, downloads, and reference files.

The Asset System ensures generated documentation remains offline-friendly and does not break due to missing or inconsistent asset paths.

The Asset System does not define visual styling, rendering implementation, content authoring, or Component meaning.

## Core Philosophy

Documentation assets must be local whenever they are required for reading the documentation.

Asset references must remain portable.

Relative paths should be used.

Assets should be organized predictably.

Asset naming should be consistent.

The Renderer should preserve or copy assets into the offline output.

Broken asset references should be reported clearly.

## Responsibilities

The Asset System is responsible for defining:

- Standard asset folder structure.
- Asset naming conventions.
- Asset reference rules.
- Supported asset categories.
- Shared assets.
- Document-specific assets.
- Downloadable files.
- Reference files.
- Offline asset requirements.
- Asset validation expectations.
- Renderer integration.
- Component integration.

The Asset System is not responsible for:

- Creating assets.
- Editing images.
- Compressing media.
- Visual styling.
- HTML implementation.
- JavaScript behavior.
- Markdown component syntax.
- Project-specific art direction.

## Core Model

The conceptual asset model is:

```text
Documentation Project
        |
        v
Asset Folder Structure
        |
        v
Markdown Asset References
        |
        v
Renderer Asset Handling
        |
        v
Offline Output Package
```

Authors and agents reference assets from Markdown, while the Renderer ensures those references remain valid in the generated output.

## Standard Asset Folder Structure

The preferred structure is:

```text
assets/
|-- shared/
|   |-- images/
|   |-- icons/
|   |-- diagrams/
|   `-- videos/
|
|-- documents/
|   |-- gdd/
|   |-- engineering/
|   |-- art-bible/
|   |-- api-reference/
|   `-- glossary/
|
|-- downloads/
`-- references/
```

### `assets/shared/`

Contains assets reused across multiple Documents.

Examples include:

- Project logo.
- Shared icons.
- Global diagrams.
- Shared screenshots.
- Shared visual references.

### `assets/documents/`

Contains assets owned by specific Documents.

Each Document may have its own subfolder.

Examples include:

- `assets/documents/gdd/`
- `assets/documents/engineering/`
- `assets/documents/art-bible/`
- `assets/documents/api-reference/`

Document-specific assets should live close to the Document they support conceptually.

### `assets/downloads/`

Contains files intended for users to download.

Examples include:

- Sample packages.
- PDFs.
- `.unitypackage` files.
- ZIP files.
- Data samples.

### `assets/references/`

Contains supporting reference files.

Examples include:

- JSON samples.
- CSV examples.
- TXT notes.
- PDFs.
- External exported references stored locally.

## Asset Categories

The Asset System supports the following asset categories for v1.

### Images

Examples include:

- `.png`
- `.jpg`
- `.jpeg`
- `.webp`
- `.svg`

Images are used for:

- Screenshots.
- Figures.
- Diagrams.
- Visual references.
- UI captures.

### Icons

Examples include:

- `.svg`
- `.png`

Icons are used for:

- Symbolic UI references.
- Component decoration.
- Project branding.
- Local documentation icons.

Icons must remain local if required for the documentation UI.

### Diagrams

Examples include:

- `.svg`
- `.png`
- `.webp`

Diagrams are used for:

- Architecture diagrams.
- Flow diagrams.
- System diagrams.
- Process visuals.

### Videos

Examples include:

- `.mp4`
- `.webm`

Videos are used for:

- Local demonstrations.
- Feature previews.
- Workflow examples.

Videos should be used carefully to avoid making documentation packages too large.

### Downloads

Examples include:

- `.zip`
- `.pdf`
- `.unitypackage`
- `.json`
- `.csv`
- `.txt`

Downloads are used when users need to download supporting files.

### References

Examples include:

- `.md`
- `.txt`
- `.pdf`
- `.json`
- `.csv`

References are used for supporting material that is not part of the main documentation flow.

## Asset Naming Convention

Asset files and folders should use `lowercase-kebab-case`.

Examples:

```text
face-controller-inspector.png
atlas-layout-example.png
blink-animation-flow.svg
sample-project.zip
gdd-core-loop-diagram.png
```

Avoid:

```text
Imagem Final Nova 2.png
Screenshot (1).png
teste.PNG
My Diagram FINAL.svg
```

Rules:

- Use lowercase letters.
- Use hyphens between words.
- Avoid spaces.
- Avoid special characters.
- Avoid version noise such as `final`, `new`, `copy`, or `(1)`.
- File extensions should be lowercase when possible.
- Names should describe the asset purpose.

## Markdown Asset References

Assets should be referenced with standard Markdown whenever possible.

### Images

Use:

```md
![Face Controller Inspector](assets/documents/engineering/face-controller-inspector.png)
```

Or:

```md
![Atlas Layout Example](assets/shared/diagrams/atlas-layout-example.svg)
```

### Downloads

Use:

```md
[Download sample package](assets/downloads/face-system-sample.zip)
```

### References

Use:

```md
[View sample JSON](assets/references/sample-config.json)
```

Rules:

- Use relative paths.
- Do not use absolute local machine paths.
- Do not use drive-letter paths such as `E:/...`.
- Do not use remote URLs for required local documentation assets.
- Markdown must remain readable in raw form.

## Offline Asset Requirement

Assets required to read or use the documentation must be local.

The generated documentation must not depend on:

- Remote images.
- Remote icons.
- Remote videos.
- External CDN assets.
- External font services.
- Remote scripts.
- Remote stylesheets.

External links may exist as references, but required documentation assets must be packaged locally.

## Shared Assets

Shared assets are used by more than one Document.

Examples include:

- Project logo.
- Global architecture diagram.
- Common icon set.
- Shared system overview image.

Shared assets should live under:

```text
assets/shared/
```

Shared assets should not be duplicated inside multiple Document folders unless there is a strong reason.

## Document-Specific Assets

Document-specific assets support one Document.

Examples include:

- Game Design Document enemy chart.
- Engineering architecture screenshot.
- Art Bible material reference.
- API workflow diagram.

Document-specific assets should live under:

```text
assets/documents/[document-id]/
```

Examples:

```text
assets/documents/gdd/core-loop-diagram.png
assets/documents/engineering/activity-system-flow.svg
assets/documents/art-bible/character-silhouette-reference.png
```

Document-specific assets should use folder names that match or clearly relate to Document IDs.

## Asset References and Components

The Asset System supports asset-related Components defined by the Component Library.

Relevant Components include:

- Image.
- Figure.
- Gallery.
- Screenshot.
- Video.
- Icon.
- Badge.
- Asset Reference.
- Download.

The Asset System defines where assets live and how they are referenced.

The Component Library defines Component meaning and Markdown Usage.

The Rendering System defines how asset references appear in output.

The Theme System defines visual treatment.

## Renderer Integration

The Renderer is responsible for preserving asset references in the offline output.

Renderer expectations:

- Copy required local assets into the output package when needed.
- Preserve relative paths.
- Avoid breaking Markdown image and link references.
- Preserve folder organization when practical.
- Warn about missing referenced assets.
- Avoid silently dropping assets.
- Do not require internet access for required assets.

The Renderer may reorganize assets internally if final references remain valid and the output package remains offline-friendly.

## Asset Validation

Asset Validation should detect:

- Missing files.
- Broken relative paths.
- Unsupported or unexpected file types.
- Duplicate asset names in conflicting contexts.
- Remote assets used as required documentation content.
- Absolute paths.
- Drive-letter paths.
- Incorrect filename casing when relevant.

Validation should report clear warnings.

Validation should not silently guess replacement assets.

## Search Integration

Search may index asset-related Metadata.

Searchable asset Metadata may include:

- Image alt text.
- Figure captions.
- Screenshot captions.
- Gallery captions.
- Download labels.
- Reference labels.
- Asset filenames when useful.
- Nearby heading context.

The Search System defines search behavior.

The Asset System defines what asset Metadata may be meaningful.

## Glossary Integration

Glossary terms may reference assets when useful.

Examples include:

- A term definition may include an image.
- A term may link to a diagram.
- Related terms may reference visual examples.

Glossary asset references must follow the same relative path and offline rules as all other documentation assets.

## Design Decisions

### Assets Are Local by Default

**Decision:** Required documentation assets must be local.

**Rationale:** Local assets preserve offline-first behavior and ensure documentation remains usable without network access.

**Consequence:** Required images, icons, videos, downloads, and reference files must be packaged with the documentation output.

### Relative Paths Preserve Portability

**Decision:** Asset references should use relative paths.

**Rationale:** Relative paths allow generated documentation to move between folders, repositories, and output packages.

**Consequence:** Absolute machine paths and drive-letter paths must be avoided.

### Organized Asset Folders Prevent Documentation Decay

**Decision:** Documentation assets should follow predictable folder organization.

**Rationale:** Predictable folders reduce missing assets, duplicate files, and unclear ownership.

**Consequence:** Shared assets and Document-specific assets have distinct folder locations.

### Standard Markdown References Preserve Simplicity

**Decision:** Images and downloads use standard Markdown references in v1.

**Rationale:** Standard Markdown keeps authoring readable, portable, and compatible with existing tooling.

**Consequence:** Custom asset syntax is not required for v1.

### Broken Assets Must Be Reported

**Decision:** Missing or invalid asset references should produce clear warnings rather than silent failures.

**Rationale:** Broken assets can make documentation misleading or unusable.

**Consequence:** Validation and rendering should report missing files, broken paths, and invalid references clearly.

## Out of Scope

The Asset System does not define:

- Image editing.
- Asset compression.
- Asset generation.
- Video transcoding.
- Icon design.
- Visual styling.
- CSS implementation.
- HTML implementation.
- JavaScript behavior.
- CDN management.
- Remote asset hosting.
- Digital asset management systems.

## Future Extensions

The Asset System may later support:

- Asset manifest.
- Automatic asset validation.
- Asset usage reports.
- Duplicate asset detection.
- Missing asset diagnostics.
- Image optimization.
- Thumbnail generation.
- Gallery generation.
- Asset Metadata files.
- Project-specific asset policies.
- Asset ownership Metadata.
- Asset localization.
- Print-optimized asset variants.

# Related Documents

- [DocumentationFramework.md](DocumentationFramework.md) - Defines the framework vision, principles, and intended documentation experience.
- [FrameworkArchitecture.md](FrameworkArchitecture.md) - Defines the root architecture and subsystem relationships.
- [DocumentationStandards.md](DocumentationStandards.md) - Defines the documentation standards used by this specification.
- [Terminology.md](Terminology.md) - Defines the official vocabulary used by this specification.
- [ContentSystem.md](ContentSystem.md) - Defines Documents and authored content that reference assets.
- [NavigationSystem.md](NavigationSystem.md) - Defines navigation concepts for reaching rendered content that may include assets.
- [ComponentLibrary.md](ComponentLibrary.md) - Defines asset-related Components such as Image, Figure, Gallery, Screenshot, Video, Icon, Badge, Asset Reference, and Download.
- [RenderingSystem.md](RenderingSystem.md) - Defines Renderer responsibilities for preserving local assets in output packages.
- [ThemeSystem.md](ThemeSystem.md) - Defines visual treatment for rendered asset Components.
- [SearchSystem.md](SearchSystem.md) - Defines how asset Metadata may participate in Search.
- [GlossarySystem.md](GlossarySystem.md) - Defines how Glossary Terms may reference assets.

# Revision History

| Version | Date       | Author          | Description                         |
|---------|------------|-----------------|-------------------------------------|
| 0.1.0   | 2026-06-30 | Immersive Games | Initial Asset System specification. |
