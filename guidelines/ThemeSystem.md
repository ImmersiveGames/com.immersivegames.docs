# Theme System

**Project:** `com.immersivegames.docs`  
**Document Type:** Subsystem Specification  
**Status:** Draft  
**Version:** 0.1.6

---

## Purpose

The Theme System defines the visual identity of rendered documentation.

It controls visual presentation such as colors, typography, spacing, borders, shadows, visual hierarchy, responsive visual behavior, and Component appearance.

It does not define content, Markdown authoring, navigation logic, rendering structure, or HTML generation.

## Core Philosophy

The Theme System styles the semantic structure emitted by the Rendering System.

The Rendering System owns structure and semantic classes.

The Theme System owns visual appearance.

The Theme System must support consistent documentation across different projects while keeping the visual style calm, readable, technical, and professional.

## Responsibilities

The Theme System is responsible for:

- Visual Direction.
- Theme Modes.
- Color palette.
- Typography.
- Spacing.
- Borders.
- Shadows.
- Component styling.
- Layout visual treatment.
- Responsive visual behavior.
- Accessibility-oriented visual rules.

The Theme System is not responsible for:

- Markdown content.
- Documentation hierarchy.
- Navigation concepts.
- HTML structure generation.
- JavaScript behavior.
- Search behavior.
- Glossary data.

## Visual Direction

### General Direction

The default visual identity should be inspired by the Face System HTML documentation and modern dark documentation interfaces.

The style should feel:

- Modern.
- Technical.
- Calm.
- Readable.
- Professional.
- Suitable for game, system, tool, asset, and Game Design Document documentation.

The design should avoid excessive decoration, saturated colors, visual noise, or heavy effects that reduce readability.

### Theme Modes

The Theme System must support at least two Theme Modes:

- Dark Theme.
- Light Theme.

Dark Theme is the primary visual reference for the initial implementation.

Light Theme must be supported as part of the Theme System direction, even if implementation may come later.

### Dark Theme Direction

The Dark Theme direction is:

- Main background should be black or near-black.
- Panels, cards, sidebars, and content containers should use dark charcoal tones.
- Borders should use subtle dark gray tones slightly lighter than the panel background.
- Main text should use soft off-white, not pure white, to avoid eye strain.
- Secondary text should use muted light gray.
- Muted text should use medium gray.
- Accent colors should be restrained and used mainly for active navigation, links, highlights, and Component emphasis.
- The Dark Theme should feel close to contemporary developer tools and modern chat or documentation interfaces.

### Light Theme Direction

The Light Theme direction is:

- Main background should use off-white or very light gray.
- Panels and content containers should use white or near-white.
- Borders should use subtle light gray.
- Main text should use near-black, not pure black when possible.
- Secondary text should use medium gray.
- Accent colors should remain consistent with the Dark Theme.
- The Light Theme should feel clean, readable, and professional without becoming visually flat.

### Typography Direction

System fonts are the default typography strategy.

Local and system fonts preserve offline support.

Recommended primary font stack:

```text
system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif
```

Recommended code font stack:

```text
"Cascadia Code", "Consolas", "Courier New", monospace
```

System fonts are preferred because they work offline.

No external font service should be required.

Typography should prioritize readability over branding.

Code typography must be clear for technical documentation.

### Readability Direction

Readability rules include:

- Avoid pure white text on pure black backgrounds for long reading.
- Use sufficient line height.
- Use clear heading hierarchy.
- Use comfortable paragraph width.
- Use visible but subtle separators.
- Use callouts and Structured Blocks to improve scanning.
- Avoid relying only on color to communicate meaning.

## Theme Tokens

Theme Tokens define the reusable visual values used by the documentation Theme.

Future CSS implementations should use Theme Tokens to keep visual styling consistent across Theme Modes and Documentation Projects.

Theme Tokens should control:

- Colors.
- Text colors.
- Accent colors.
- Semantic status colors.
- Spacing.
- Radius.
- Borders.
- Shadows.
- Typography.
- Layout dimensions.
- Responsive breakpoints.
- Z-index layers.

Components must use Theme Tokens instead of hardcoded visual values.

### Token Naming Convention

The official token naming pattern is:

```text
--docs-[category]-[role]
```

Examples:

- `--docs-color-bg`
- `--docs-color-surface`
- `--docs-color-border`
- `--docs-color-text`
- `--docs-color-text-muted`
- `--docs-color-accent`
- `--docs-spacing-md`
- `--docs-radius-md`

Token naming rules:

- Token names must describe purpose, not fixed color names.
- Names such as `--blue`, `--gray-1`, or `--card-color` should be avoided.
- Semantic roles should be used, such as `background`, `surface`, `text`, `accent`, `warning`, `success`, `danger`, and `border`.
- Token names must remain stable across Dark Theme and Light Theme.
- Only token values should change between Theme Modes.

### Shared Tokens

Shared Tokens are values that are usually the same across Theme Modes.

Examples include:

- Spacing.
- Radius.
- Typography scale.
- Font families.
- Layout dimensions.
- Breakpoints.
- Z-index layers.

Example token categories:

- `--docs-spacing-*`
- `--docs-radius-*`
- `--docs-font-*`
- `--docs-layout-*`
- `--docs-breakpoint-*`
- `--docs-z-*`

### Theme Mode Tokens

Dark Theme and Light Theme must use the same token names.

Only the values assigned to those token names should differ between Theme Modes.

Conceptual structure:

```css
:root {
  --docs-spacing-md: 1rem;
  --docs-radius-md: 8px;
}

[data-theme="dark"] {
  --docs-color-bg: ...;
  --docs-color-surface: ...;
}

[data-theme="light"] {
  --docs-color-bg: ...;
  --docs-color-surface: ...;
}
```

This example describes token organization only. It does not implement CSS for the framework.

## Typography

### Typography Strategy

Documentation should use local and system fonts to preserve offline-first behavior.

External font services must not be required.

Typography must prioritize readability, technical clarity, and long-form documentation comfort over decorative branding.

### Primary Font Stack

Recommended primary font stack:

```text
system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif
```

This stack works well across operating systems and does not require bundled fonts or internet access.

### Code Font Stack

Recommended code font stack:

```text
"Cascadia Code", "Consolas", "Courier New", monospace
```

Code typography must support technical documentation, C#, JSON, YAML, Markdown, and command examples.

### Base Text

Base text direction:

- Base font size should start around `16px`.
- Line height should be comfortable for long reading, around `1.6`.
- Paragraphs should have a comfortable reading width.
- Main content should avoid overly wide text lines.
- Text should remain readable in both Dark Theme and Light Theme.

### Heading Scale

Headings should create a clear visual hierarchy that matches the editorial hierarchy defined by the Content System.

Heading direction:

- H1 represents the Document title.
- H2 represents Chapters.
- H3 represents Sections.
- H4 represents Subsections.
- H5 and H6 represent deeper details only when necessary.

Headings must work well with Sidebar and Table of Contents generation.

This specification does not define exact final CSS values for heading sizes, weights, margins, or spacing. Those values may be defined by Theme Tokens in a future revision.

### Text Colors and Emphasis

Main text should use high-readability colors.

Dark Theme should use soft off-white instead of pure white.

Light Theme should use near-black instead of pure black when possible.

Secondary text should be muted but readable.

Muted text should be used for Metadata, labels, dates, and low-priority information.

Emphasis should be clear but not visually noisy.

### Links

Links should use the Theme accent color.

Links must be visually distinguishable from normal text.

Hover and focus states should be clear.

Links should not rely only on color when possible.

### Code Typography

Code Blocks use the code font stack.

Code Blocks may use slightly smaller text than body text.

Code Blocks must remain readable.

Code Blocks must support horizontal overflow when needed.

Inline Code must be visually distinct but not distracting.

### Table Typography

Tables should prioritize readability.

Header cells should be visually distinct.

Cell spacing should be comfortable.

Table text may be slightly smaller than body text if needed.

Tables must remain usable on smaller screens.

### Captions and Metadata

Captions, labels, dates, version information, and helper text should use smaller typography.

They should use secondary or muted text colors.

They should not compete visually with primary content.

### Accessibility Notes

Typography must maintain readable contrast.

Text must remain legible at common browser zoom levels.

Focus states for links must be visible.

Typography must not rely on font weight alone to communicate important meaning.

## Layout Styling

Layout Styling defines the visual treatment of the main documentation shell.

It covers:

- Header.
- Document Tabs.
- Sidebar.
- Main Content.
- Local Table of Contents.
- Footer.
- Back to Top.
- Visual separation between layout regions.

Layout Styling must use Theme Tokens and must not introduce hardcoded visual values.

The Rendering System defines structural regions and semantic classes. The Theme System defines the visual treatment of those regions.

### Header

The Header should be semi-fixed on desktop.

It should keep project context and search accessible while reading.

It should visually anchor the documentation.

It should contain project title, documentation Metadata, and search entry point.

It should avoid becoming visually heavy.

It should use subtle borders or background separation instead of heavy shadows.

The exact sticky behavior belongs to implementation, but the visual direction expects persistent context.

### Document Tabs

Document Tabs should appear directly below the Header.

They represent primary navigation between Documents.

They should be horizontal on desktop.

The active Document must be clearly visible.

Tabs should use the accent token for active state or highlight.

In constrained layouts, tabs may become scrollable, compact, or menu-based.

Document Tabs should not contain local content actions such as Back to Top.

### Sidebar

The Sidebar displays only the active Document hierarchy.

It should visually support Chapters, Sections, and Subsections.

It should preserve the editorial order.

It should have its own scroll behavior only when the navigation list exceeds available height.

It should feel stable and anchored on desktop.

It should use subtle indentation, active states, and muted labels.

It should avoid visual noise and excessive nesting decoration.

### Main Content

Main Content should be the primary reading area.

Recommended maximum content width is around `960px`.

Main Content should avoid overly wide text lines.

It should provide comfortable spacing between Sections.

It should make headings, paragraphs, Code Blocks, Tables, images, and Structured Components easy to scan.

It may use a clean content surface or panel treatment depending on the Theme Mode.

It must remain visually calmer than callouts and special Components.

### Local Table of Contents

The Local Table of Contents should appear on the right side on desktop when space allows.

It represents the current rendered content, not the full Document hierarchy.

It should be visually lighter than the Sidebar.

It should support quick scanning of the current content.

It should highlight the current local Section when supported.

On tablet, it may become collapsible or optional.

On mobile, it may be collapsed, hidden, or available through a compact control.

### Footer

The Footer should be simple and low-emphasis.

It should include project name, documentation version, last updated date when available, and generator attribution.

It should use muted typography.

It should not compete with Main Content.

It may include copyright, license, or repository links when available.

### Back to Top

On desktop, Back to Top should preferably appear inside the Local Table of Contents area.

It should be shown as a discreet local navigation action, such as `↑ Back to Top`.

It should remain accessible before the user reaches the end of the Document.

On tablet and mobile, it may appear as a discreet floating action after the user scrolls a meaningful distance.

A fallback link may appear at the end of the content.

Back to Top should not be placed in the Document Tabs, because Document Tabs are reserved for primary Document navigation.

The Navigation System defines the capability, the Rendering System provides the structural hook, and the Theme System defines the visual treatment.

### Visual Separation

Layout regions should be separated with subtle borders, background contrast, spacing, or lightweight surfaces.

The default Dark Theme should use a near-black page background and dark charcoal panels.

Sidebar, Header, Local Table of Contents, and content containers should feel related but visually distinct.

Borders should be subtle.

Shadows should be minimal, especially in the Dark Theme.

The interface should avoid heavy decoration and excessive contrast.

### Desktop Layout Direction

Desktop visual direction includes:

- Semi-fixed Header.
- Document Tabs below Header.
- Left Sidebar for active Document hierarchy.
- Central Main Content with recommended maximum width around `960px`.
- Right Local Table of Contents.
- Footer after content.
- Back to Top inside Local Table of Contents when possible.

### Tablet Layout Direction

Tablet visual direction includes:

- Header remains accessible but may become more compact.
- Document Tabs may become scrollable or compact.
- Sidebar may become collapsible.
- Local Table of Contents may be optional or collapsible.
- Main Content should remain comfortable and readable.

### Mobile Layout Direction

Mobile visual direction includes:

- Header should become compact.
- Document Tabs may become scrollable, stacked, or menu-based.
- Sidebar should become a drawer, menu, or collapsible navigation area.
- Local Table of Contents should be collapsed, hidden, or available through a compact control.
- Main Content should use full available width with comfortable padding.
- Back to Top may become a discreet floating control.

## Component Styling

Component Styling defines the visual treatment of official documentation Components.

Component Styling must use Theme Tokens.

It must not use hardcoded values.

It must not define Component syntax.

It must not redefine Component meaning.

The Component Library defines Component meaning and Markdown Usage. The Rendering System emits semantic structure and classes. The Theme System defines how those Components should look visually.

### General Component Styling Principles

Components should improve readability and scanning.

Components should make semantic meaning visually clear.

Components should not create visual noise.

Components should use consistent spacing, borders, radius, typography, and color tokens.

Components should remain readable in both Dark Theme and Light Theme.

Components should not rely only on color to communicate meaning.

Components should degrade visually in a readable way when advanced styling is unavailable.

### Basic Components

Basic Components include:

- Headings.
- Paragraphs.
- Lists.
- Tables.
- Quotes.
- Code Blocks.
- Inline Code.
- Links.
- Images.

Basic Components should be clean and unobtrusive.

Headings should create clear hierarchy.

Paragraphs should prioritize long-form reading.

Lists should have comfortable spacing.

Tables should be legible, with clear headers and subtle borders.

Quotes should be visually distinct but calm.

Code Blocks should use a dedicated surface, monospace font, padding, and overflow handling.

Inline Code should be distinct without being distracting.

Images should be constrained to content width and support captions when available.

### Information Components

Information Components include:

- Note.
- Info.
- Tip.
- Warning.
- Important.
- Success.
- Example.
- Best Practice.

Information Components should appear as callout blocks.

Callouts should use consistent layout and spacing.

Each callout type should use semantic status tokens.

Warning and Important should feel stronger than Note or Info.

Tip and Best Practice should feel helpful and positive.

Success should communicate completion or correct outcome.

Example should feel instructional.

Callouts should include clear titles when available.

Callouts should remain readable without icons.

This specification does not define exact colors or icons.

### Technical Components

Technical Components include:

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

Technical Components should feel precise, structured, and compact.

API and Method blocks should clearly separate name, description, parameters, return values, examples, and notes.

Parameter and Property tables should be highly readable.

Configuration blocks should make required and optional fields easy to identify.

Technical Components should use code typography where appropriate.

Technical Components should avoid excessive decoration.

### Architecture Components

Architecture Components include:

- Flow.
- Process.
- Timeline.
- Sequence.
- Pipeline.
- State.
- Lifecycle.
- Decision Tree.

Architecture Components should communicate structure, order, or relationships.

Flow, Process, Sequence, and Pipeline should visually suggest direction.

Timeline should suggest chronological progression.

State and Lifecycle should emphasize phases or transitions.

Decision Tree should emphasize branching choices.

Renderers may choose different visual representations, but the Theme System should support clear grouping, spacing, labels, and connectors.

This specification does not define exact diagram implementation.

### Reference Components

Reference Components include:

- Glossary Reference.
- Cross Reference.
- Related Documents.
- External Link.
- Asset Reference.
- Download.

Reference Components should make connected information easy to find.

Related Documents and See Also style blocks should be visually grouped.

External links should be distinguishable from internal links when possible.

Download and Asset Reference Components should make the target type clear.

Reference Components should use subtle surfaces and clear link styling.

### Media Components

Media Components include:

- Figure.
- Gallery.
- Screenshot.
- Video.
- Icon.
- Badge.

Media Components should remain aligned with the content width.

Figures and screenshots should support captions.

Galleries should use consistent spacing and avoid overwhelming the page.

Badges should be compact and readable.

Icons should support meaning but not be required to understand content.

Media elements should not break layout on smaller screens.

### Governance Components

Governance Components include:

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

Governance Components should preserve project reasoning.

They should look like formal records, not casual notes.

Decision blocks should clearly show the chosen decision, reason, alternatives, status, and date when available.

Alternative blocks should make rejected or considered options clear.

Trade-off blocks should visually separate pros, cons, and rationale.

Constraint and Assumption blocks should be easy to scan.

Risk blocks should emphasize risk, impact, and mitigation.

Open Question blocks should clearly indicate unresolved status.

Governance Components should reduce repeated discussions by making context visible.

### Navigation Components

Navigation Components include:

- See Also.
- Previous.
- Next.
- Back to Top.

Navigation Components should be clear but not visually dominant.

See Also should group related links.

Previous and Next should support reading flow.

Back to Top should be discreet and easy to access.

Navigation Components must remain visually consistent with the Navigation System and Rendering System.

### Component Density

Components should have enough spacing to be readable.

Technical and Governance Components may be denser than callouts.

Dense Components must remain scannable.

Large Components should avoid excessive vertical clutter.

Mobile layouts may simplify or stack Component content.

### Component Status and Severity

Some Components express status or severity.

Warning, Important, Risk, Success, Open Question, and deprecated-like statuses should be visually distinguishable.

Status should use semantic tokens.

Status should not rely only on color.

Labels, titles, icons, or text indicators may be used by Renderers.

## Responsive Visual Behavior

Responsive Visual Behavior defines how the documentation Theme adapts to different viewport sizes while preserving readability, navigation clarity, and offline usability.

The Theme must support:

- Desktop.
- Tablet.
- Mobile.

Responsive behavior must use Theme Tokens, especially layout tokens and breakpoint tokens.

This specification does not define final CSS media queries.

### Responsive Principles

Reading comfort is more important than showing every navigation panel at once.

Main Content must remain readable on all screen sizes.

Navigation must remain accessible even when sidebars collapse.

The interface should progressively simplify as space becomes limited.

Responsive behavior must not change the documentation structure.

Responsive behavior must not require different Markdown content.

Components should stack or simplify when necessary.

### Desktop Behavior

The preferred desktop layout includes:

- Semi-fixed Header.
- Document Tabs below Header.
- Left Sidebar visible for the active Document hierarchy.
- Central Main Content.
- Right Local Table of Contents visible when space allows.
- Footer after content.
- Back to Top inside the Local Table of Contents when possible.
- Sidebar and Local Table of Contents may have independent scrolling when needed.
- Main Content should use the recommended readable width, around `960px`.

Desktop is the primary reference layout for the full documentation experience.

### Tablet Behavior

The preferred tablet layout includes:

- Header remains accessible but may become more compact.
- Document Tabs may become horizontally scrollable or compact.
- Sidebar may become collapsible.
- Local Table of Contents may become optional, collapsible, or hidden behind a control.
- Main Content receives more available width.
- Back to Top may remain in local navigation if visible, or become a discreet floating control.
- Components may reduce horizontal complexity.

Tablet layout should preserve navigation access without forcing three-column density.

### Mobile Behavior

The preferred mobile layout includes:

- Header becomes compact.
- Search remains accessible, but may be collapsed behind an icon or compact control.
- Document Tabs may become scrollable, stacked, or menu-based.
- Sidebar becomes a drawer, menu, or collapsible navigation area.
- Local Table of Contents is collapsed, hidden, or available through a compact control.
- Main Content uses full available width with comfortable padding.
- Back to Top may appear as a discreet floating control after meaningful scrolling.
- Tables, Code Blocks, timelines, galleries, and Structured Blocks must remain usable through stacking, wrapping, or horizontal overflow when appropriate.

Mobile should prioritize reading and simple navigation over full layout visibility.

### Component Responsiveness

Callouts should keep their semantic emphasis but reduce excessive padding on small screens.

Tables may scroll horizontally when necessary.

Code Blocks may scroll horizontally.

Galleries should stack or reduce columns.

Timeline, Flow, Pipeline, and Process Components may become vertical.

Technical and Governance Components should stack fields vertically on narrow screens.

Badges and labels should wrap cleanly.

Images and figures should fit within available width.

### Navigation Responsiveness

Document navigation must remain accessible at all sizes.

Sidebar navigation must be reachable even when collapsed.

Local Table of Contents may be hidden on smaller layouts, but should remain available when practical.

Current location should remain clear.

Back to Top should remain available when users scroll long content.

Responsive navigation must follow the Navigation System and must not redefine navigation relationships.

### Breakpoint Guidance

Exact breakpoint values belong to implementation, but the Theme System should define semantic breakpoint categories:

- Small.
- Medium.
- Large.
- Extra Large.

Reference Theme Token categories:

- `--docs-breakpoint-sm`
- `--docs-breakpoint-md`
- `--docs-breakpoint-lg`
- `--docs-breakpoint-xl`

This specification does not define exact pixel values yet.

### Accessibility in Responsive Layouts

Collapsed navigation must remain discoverable.

Touch targets should be comfortable on mobile.

Focus states must remain visible.

Text must remain readable under zoom.

Responsive layouts must not hide critical documentation content.

Navigation controls must not rely only on hover behavior.

## Accessibility

Accessibility in the Theme System defines visual and interaction-related expectations that help users read, navigate, and understand documentation comfortably.

Accessibility must apply to:

- Dark Theme.
- Light Theme.
- Desktop layout.
- Tablet layout.
- Mobile layout.
- Navigation regions.
- Documentation Components.
- Code Blocks.
- Tables.
- Links.
- Callouts.
- Structured Blocks.

This section defines accessibility expectations for the Theme System. It does not define ARIA implementation, JavaScript behavior, or final CSS.

### Contrast

Text must have sufficient contrast against its background.

Main text must remain readable in both Dark Theme and Light Theme.

Muted text must still be readable.

Borders and separators should be subtle but still perceivable.

Callouts and status Components must remain distinguishable from normal content.

Dark Theme should avoid harsh pure white text on pure black backgrounds for long reading.

Light Theme should avoid overly weak gray text.

This revision does not define exact contrast ratios. Future implementation should validate contrast.

### Text Readability

Body text must remain comfortable for long reading.

Line height must support readability.

Paragraph width must avoid overly long lines.

Text must remain legible at common browser zoom levels.

Headings must create a clear hierarchy.

Small text should be reserved for Metadata, labels, captions, and low-emphasis information.

Documentation must remain readable without relying on decorative typography.

### Focus and Active States

Interactive elements must have visible focus states.

Active navigation items must be clearly distinguishable.

Hover states should not be the only indicator of interactivity.

Keyboard users must be able to understand where focus is.

Focus styling should use Theme Tokens and remain visible in both Dark Theme and Light Theme.

This specification does not define implementation-specific focus behavior.

### Links

Links must be visually distinguishable from normal text.

Links should use the accent token.

Links should have clear hover and focus states.

External links may be visually differentiated when supported.

Links should not rely only on color when possible.

Inline links must remain readable in dense technical documentation.

### Non-Color-Only Communication

Semantic meaning must not rely only on color.

Warning, Important, Risk, Success, Open Question, and similar Components should also use labels, titles, icons, borders, or text indicators when supported.

Callouts must remain understandable even if color perception is limited.

Status badges should include readable text, not only color.

### Navigation Accessibility

Current location must be visually clear.

Sidebar hierarchy must be easy to scan.

Document Tabs must clearly show the active Document.

Local Table of Contents must not compete visually with the Sidebar.

Collapsed navigation must remain discoverable.

Back to Top must be easy to find when long content is being read.

Responsive layouts must preserve access to navigation.

### Component Accessibility

Components must remain readable in both Theme Modes.

Callouts must have clear titles or labels when available.

Structured Blocks must visually separate fields and content.

Technical Components must keep names, parameters, return values, and examples easy to distinguish.

Governance Components must make decision status, risks, assumptions, and open questions clear.

Components should not become visually overwhelming.

### Code and Table Accessibility

Code Blocks must remain readable and scrollable when needed.

Code font must be legible.

Syntax highlighting, if added later, must not reduce contrast.

Tables must have readable headers.

Tables must remain usable on smaller screens.

Dense tables should preserve spacing and alignment.

Horizontal overflow is acceptable when it preserves readability.

### Touch and Mobile Accessibility

Mobile navigation controls should have comfortable touch targets.

Collapsible controls should be visually clear.

Floating actions such as Back to Top should not cover important content.

Main Content should keep comfortable padding.

Components should stack or simplify without losing meaning.

Mobile layouts should prioritize reading over visual density.

### Motion and Visual Effects

Motion should be minimal.

Animations should not be required to understand the interface.

Transitions, if used, should be subtle.

Heavy effects, flashing, or distracting animations should be avoided.

The documentation should remain usable if animations are disabled.

### Accessibility Validation

Future implementation should validate:

- Text contrast.
- Focus visibility.
- Link visibility.
- Readability under zoom.
- Mobile navigation usability.
- Component readability.
- Keyboard navigation expectations where supported.

This section defines expectations, not tooling implementation.

## Design Decisions

### Theme Is Separate from Rendering

**Decision:** The Rendering System emits semantic structure and classes, while the Theme System defines how those structures look.

**Rationale:** Separating structure from appearance allows Renderers and Themes to evolve independently.

**Consequence:** The Theme System can define visual identity without owning HTML generation, JavaScript behavior, or authored content.

### Dark Theme as Primary Reference

**Decision:** The initial visual direction is based on a dark documentation interface inspired by Face System, while the Theme System must support both Dark Theme and Light Theme.

**Rationale:** Dark technical interfaces are a strong fit for the initial documentation experience, but documentation should remain usable across different reading preferences and accessibility needs.

**Consequence:** Dark Theme guides the first visual implementation, but Theme contracts must not prevent Light Theme support.

### System Fonts Preserve Offline Support

**Decision:** The default typography strategy uses local system fonts.

**Rationale:** Documentation must work offline and should not depend on remote font providers. System fonts preserve offline functionality, reduce distribution requirements, and remain familiar across platforms.

**Consequence:** The Theme System prioritizes readability and portability over external font-based branding.

### Theme Tokens Are Semantic

**Decision:** Theme Tokens use stable semantic names instead of fixed color or component-specific names.

**Rationale:** Semantic names allow Dark Theme and Light Theme to share the same token contract while changing only token values.

**Consequence:** Components depend on reusable visual roles instead of hardcoded values or Theme Mode-specific names.

### Semi-Fixed Header Preserves Context

**Decision:** The Header should keep project identity and search available without dominating the reading experience.

**Rationale:** Documentation users benefit from persistent project context and search access while reading long-form content.

**Consequence:** The Header should be visually stable and accessible, but restrained enough to avoid competing with Main Content.

### Sidebar Is Scoped to the Active Document

**Decision:** The visual layout reinforces the Navigation System rule that the Sidebar only shows the active Document hierarchy.

**Rationale:** Showing only the active Document hierarchy keeps navigation focused and avoids unnecessary visual noise.

**Consequence:** Primary Document navigation belongs to Document Tabs, while Document-internal navigation belongs to the Sidebar.

### Back to Top Belongs to Local Navigation

**Decision:** Back to Top is a local reading and navigation action and should not be placed in Document Tabs.

**Rationale:** Document Tabs are reserved for primary navigation between Documents. Back to Top belongs to the current reading context.

**Consequence:** Back to Top should appear in the Local Table of Contents area, as a discreet floating action, or as a fallback content link.

### Main Content Width Supports Long Reading

**Decision:** Main Content should use a comfortable reading width, with a recommended maximum around `960px`.

**Rationale:** Overly wide text lines reduce readability and make long-form technical documentation harder to scan.

**Consequence:** Layout styling should prioritize reading comfort over filling all available horizontal space.

### Components Represent Meaning Before Appearance

**Decision:** Component styling must preserve semantic meaning instead of creating arbitrary visual decoration.

**Rationale:** Components are defined by the Component Library according to purpose and authoring intent.

**Consequence:** Visual styling must clarify Component meaning without redefining it.

### Governance Components Preserve Project Reasoning

**Decision:** Governance Components are visually distinguished because they record decisions, alternatives, risks, assumptions, and unresolved questions.

**Rationale:** Project reasoning needs to remain visible and easy to revisit during future maintenance.

**Consequence:** Governance Components should look like formal records and should reduce repeated discussions by preserving context.

### Component Styling Uses Theme Tokens

**Decision:** All Component styling must use Theme Tokens.

**Rationale:** Theme Tokens prevent visual fragmentation and allow Components to remain consistent across Dark Theme and Light Theme.

**Consequence:** Component styling must not rely on hardcoded visual values.

### Responsive Layout Prioritizes Reading

**Decision:** As screen space decreases, the Theme should prioritize Main Content readability over showing all navigation panels simultaneously.

**Rationale:** Documentation must remain useful on smaller screens, and reading comfort is the primary user need.

**Consequence:** Navigation panels may simplify, collapse, or move behind compact controls before Main Content becomes difficult to read.

### Navigation Collapses Before Content

**Decision:** Sidebar and Local Table of Contents may collapse or move into compact controls before Main Content readability is compromised.

**Rationale:** Navigation must remain accessible, but it does not need to occupy persistent screen space on every viewport size.

**Consequence:** Responsive layouts preserve content readability while keeping navigation reachable.

### Components Adapt Without Changing Meaning

**Decision:** Responsive behavior may change Component layout, but not Component semantics.

**Rationale:** Components may need to stack, wrap, scroll, or simplify visually on smaller screens.

**Consequence:** The Theme System may adapt presentation while preserving the meaning defined by the Component Library.

### Accessibility Supports Long-Form Reading

**Decision:** Accessibility must prioritize readability, orientation, and reduced fatigue.

**Rationale:** Documentation is often read for long periods and must remain comfortable across Theme Modes, layouts, and content types.

**Consequence:** Typography, contrast, spacing, navigation states, and component presentation must support sustained reading.

### Meaning Must Not Depend Only on Color

**Decision:** Semantic Components must remain understandable through text labels, structure, and visual hierarchy, not color alone.

**Rationale:** Color perception varies, and documentation meaning must remain clear when color cues are unavailable or insufficient.

**Consequence:** Status, severity, and semantic emphasis should use labels, titles, borders, icons, or text indicators when supported.

### Responsive Accessibility Preserves Navigation

**Decision:** Smaller layouts may collapse navigation panels, but must preserve access to Document navigation, current location, and reading controls.

**Rationale:** Responsive simplification should not make documentation harder to navigate.

**Consequence:** Collapsed navigation, Back to Top, and current-location cues must remain discoverable and usable.

## Out of Scope

The Theme System does not define:

- Markdown authoring.
- Component syntax.
- HTML generation.
- JavaScript behavior.
- Search implementation.
- Glossary rules.
- Project-specific branding.
- External font dependencies.
- External CSS frameworks as mandatory dependencies.

## Future Extensions

The Theme System may later support:

- Theme switching.
- Project-specific accent colors.
- Additional Theme presets.
- Print Theme.
- High-contrast Theme.
- Custom branding package.
- Optional Bootstrap-compatible Theme.
- Theme validation checklist.

# Related Documents

- [DocumentationFramework.md](DocumentationFramework.md) - Defines the framework vision, principles, and intended documentation experience.
- [FrameworkArchitecture.md](FrameworkArchitecture.md) - Defines the root architecture and subsystem relationships.
- [DocumentationStandards.md](DocumentationStandards.md) - Defines the documentation standards used by this specification.
- [Terminology.md](Terminology.md) - Defines the official vocabulary used by this specification.
- [ContentSystem.md](ContentSystem.md) - Defines the editorial hierarchy whose rendered output is visually styled by the Theme System.
- [NavigationSystem.md](NavigationSystem.md) - Defines navigation concepts whose rendered structures receive visual treatment.
- [ComponentLibrary.md](ComponentLibrary.md) - Defines the Components whose visual treatment is owned by the Theme System.
- [RenderingSystem.md](RenderingSystem.md) - Defines the semantic structure and hooks styled by the Theme System.

# Revision History

| Version | Date       | Author          | Description                                                   |
|---------|------------|-----------------|---------------------------------------------------------------|
| 0.1.6   | 2026-06-30 | Immersive Games | Defined Accessibility direction. |
| 0.1.5   | 2026-06-30 | Immersive Games | Defined Responsive Visual Behavior direction. |
| 0.1.4   | 2026-06-30 | Immersive Games | Defined Component Styling direction. |
| 0.1.3   | 2026-06-30 | Immersive Games | Defined Layout Styling direction. |
| 0.1.2   | 2026-06-30 | Immersive Games | Defined Theme Tokens model. |
| 0.1.1   | 2026-06-30 | Immersive Games | Defined Typography direction. |
| 0.1.0   | 2026-06-30 | Immersive Games | Initial Theme System specification with Visual Direction. |
