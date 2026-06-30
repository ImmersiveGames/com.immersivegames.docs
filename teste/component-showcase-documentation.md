# Face Animation System Manual

**Project:** `com.immersivegames.docs`  
**Document Type:** User Manual  
**Status:** Draft  
**Version:** 0.1.0

---

## Overview

The Face Animation System lets designers author reusable facial states, combine them into animations, and play those animations at runtime through a small API surface.

This manual is a sample Documentation Project document created to exercise the official Component Library in realistic authored content. It uses Markdown as the source of truth and leaves presentation decisions to the Renderer.

> [!INFO] Sample Document
> This file is a test document. It demonstrates how Components may appear inside practical documentation, not a final specification for a production package.

### Key Capabilities

- Create reusable facial states.
- Build animation clips from state transitions.
- Preview expressions before runtime.
- Trigger animations from code.
- Package local screenshots, videos, and reference assets with the documentation.

| Capability | Primary User | Output |
|------------|--------------|--------|
| Face State authoring | Game designer | Reusable expression state |
| Animation sequencing | Technical artist | Timed facial animation |
| Runtime playback | Programmer | API-triggered animation |
| Validation | QA or designer | Checklist of required setup |

> [!TIP] Recommended Reading Path
> Start with the Quick Start chapter, then review the Workflow chapter before using the API Reference.

## Quick Start

This chapter walks through the shortest path from setup to a playable facial animation.

### Requirements

:::requirement
**Requirement:** The project must include a configured character face rig.

**Reason:** Face States reference named rig controls.

**Status:** Required
:::

:::requirement
**Requirement:** Every animation must reference at least one Face State.

**Reason:** Animations are built from state transitions rather than direct rig edits.

**Status:** Required
:::

### Setup Checklist

- [ ] Add the Face Animation System package to the Unity project.
- [ ] Create a `FaceProfile` asset for the character.
- [ ] Register all required rig controls.
- [ ] Create at least one neutral Face State.
- [ ] Create at least one animation clip.
- [ ] Preview the clip in the editor.

> [!WARNING]
> Do not rename rig controls after Face States have been authored. Existing state references may no longer resolve.

### Minimal Playback Example

```csharp
using ImmersiveGames.FaceAnimation;

public sealed class DialogueFaceDriver
{
    private readonly FaceAnimator animator;

    public DialogueFaceDriver(FaceAnimator animator)
    {
        this.animator = animator;
    }

    public void OnDialogueLineStarted(string emotion)
    {
        animator.PlayAnimation(emotion);
    }
}
```

> [!EXAMPLE] Common Animation IDs
> Use IDs such as `neutral`, `blink`, `smile`, `surprised`, and `thinking` when building early prototypes.

## Workflow

The authoring workflow moves from stable rig data to reusable states and finally to playable animations.

:::flow
**Name:** Face Animation Authoring Flow

1. Register character rig controls.
2. Create a neutral Face State.
3. Create expressive Face States.
4. Assemble Face Animations from state transitions.
5. Preview and validate the result.
6. Trigger the animation from runtime code.
:::

### Creating a Face State

A Face State stores a named expression pose. Designers should create states for reusable expressions rather than one-off animation moments.

> [!BEST_PRACTICE]
> Keep Face State names short, stable, and readable. Prefer `smile-soft` over `Smile01_Final_New`.

:::configuration
**Name:** Default Face State

**Type:** Asset Reference

**Default:** `neutral`

**Description:** The state applied when no animation is active.
:::

### Building an Animation

Face Animations are authored as a sequence of transitions between Face States.

:::pipeline
**Name:** Animation Build Pipeline

**Input:** Face States

**Stages:** Select states, define timing, preview transitions, validate references, save animation

**Output:** Playable Face Animation asset
:::

| Step | Action | Validation |
|------|--------|------------|
| 1 | Select a starting state | State exists in the Face Profile |
| 2 | Add one or more target states | All targets resolve |
| 3 | Set transition duration | Duration is greater than `0` |
| 4 | Preview the sequence | No missing rig controls |
| 5 | Save the animation | Asset has a stable ID |

> [!IMPORTANT]
> Animation IDs are part of the runtime contract. Change them only when all calling code has been updated.

### Troubleshooting Workflow

:::decision-tree
**Question:** The animation does not play. Does the animation ID exist?

**Yes:** Check whether the Face Animator component is enabled.

**No:** Create the animation or update the calling code to use an existing ID.

**Question:** The animation plays but looks incorrect. Are all rig controls registered?

**Yes:** Review transition timing.

**No:** Update the Face Profile and revalidate the Face States.
:::

## Architecture Notes

The system separates authored expression data from runtime playback behavior.

:::decision
**Decision:** Face States are reusable assets instead of embedded animation-only data.

**Rationale:** Reusable states reduce duplication and keep expressions consistent across dialogue, cinematics, and gameplay.

**Status:** Approved
:::

:::trade-off
**Trade-off:** Asset-based Face States require more setup than direct keyframe animation.

**Benefit:** Designers can reuse and validate expressions across many animations.

**Cost:** Early prototypes need an initial Face Profile and neutral state before playback.
:::

:::risk
**Risk:** Missing rig controls may produce incomplete expressions.

**Impact:** Medium

**Mitigation:** Validate every Face State against the active Face Profile before packaging.

**Status:** Open
:::

:::assumption
**Assumption:** Each character uses one active Face Profile at runtime.

**Confidence:** Medium

**Validation:** Test multi-character dialogue scenes before release.
:::

### Runtime Lifecycle

:::timeline
**Name:** Runtime Animation Lifecycle

| Order | Event | Result |
|-------|-------|--------|
| 1 | Animator initializes | Default Face State is applied |
| 2 | Playback request arrives | Animation ID is resolved |
| 3 | Animation starts | Transition sequence begins |
| 4 | Animation completes | Final state is retained or reset |
| 5 | Animator resets | Default Face State is restored |
:::

## API Reference

This chapter demonstrates how Technical Components can appear inside a practical API reference.

:::api
**Name:** Face Animator API

**Namespace:** `ImmersiveGames.FaceAnimation`

**Purpose:** Provides runtime access to facial animation playback.
:::

### FaceAnimator Class

:::class
**Name:** `FaceAnimator`

**Purpose:** Plays authored Face Animations on a character face rig.

**Namespace:** `ImmersiveGames.FaceAnimation`
:::

:::property
**Name:** `DefaultStateId`

**Type:** `string`

**Access:** Read/write

**Description:** Identifies the Face State restored when playback resets.
:::

:::method
**Name:** `PlayAnimation`

**Signature:** `bool PlayAnimation(string animationId)`

**Purpose:** Starts playback for a Face Animation by ID.
:::

:::parameter
**Name:** `animationId`

**Type:** `string`

**Required:** Yes

**Description:** Stable ID of the animation to play.
:::

:::return-value
**Type:** `bool`

**Description:** Returns `true` when the animation exists and playback starts.
:::

:::event
**Name:** `AnimationCompleted`

**Payload:** `string animationId`

**Description:** Raised when a Face Animation finishes playback.
:::

:::enumeration
**Name:** `FacePlaybackMode`

| Value | Meaning |
|-------|---------|
| `Once` | Play the animation one time. |
| `Loop` | Repeat until stopped. |
| `HoldFinalState` | Keep the final Face State after playback. |
:::

> [!NOTE]
> Unsupported Structured Blocks should still remain readable as Markdown, even when a Renderer does not provide specialized API formatting.

## Media Reference

Media Components describe visual and audiovisual documentation assets without defining how they must be styled.

![Face Animation editor overview](assets/face-animation-editor-overview.png)

Figure: The editor view used to assemble Face Animations from reusable Face States.

:::gallery
**Name:** Expression State Examples

- ![Neutral expression](assets/expression-neutral.png)
- ![Smile expression](assets/expression-smile.png)
- ![Surprised expression](assets/expression-surprised.png)
:::

:::screenshot
**Title:** Face Profile Validation Panel

**Image:** `assets/face-profile-validation.png`

**Alt:** Screenshot of validation results for a Face Profile.
:::

:::video
**Title:** Face Animation Authoring Walkthrough

**Source:** `media/face-animation-authoring.mp4`

**Description:** Shows the process of creating a Face State and adding it to an animation.
:::

:::badge
**Label:** Draft

**Meaning:** This sample manual is intended for Component rendering tests.
:::

## Release Notes

This chapter demonstrates compact governance and navigation content in a normal document ending.

:::objective
**Objective:** Provide a readable sample that exercises Core and Extended Components.

**Measure:** The document can be rendered without structural changes.

**Status:** Active
:::

:::alternative
**Alternative:** Build one isolated example for every Component.

**Outcome:** Not used in this file.

**Reason:** A realistic document makes component interactions easier to evaluate.
:::

:::open-question
**Question:** Should future test documents include intentionally unsupported Components to verify fallback behavior?

**Status:** Open
:::

### See Also

- [Component Usage Reference](component-usage-reference.md)
- [Component Library](../guidelines/ComponentLibrary.md)
- [Content System](../guidelines/ContentSystem.md)

:::previous
**Label:** Workflow

**Target:** `#workflow`
:::

:::next
**Label:** API Reference

**Target:** `#api-reference`
:::

[Back to Top](#face-animation-system-manual)

# Related Documents

- [Component Usage Reference](component-usage-reference.md) - Provides a catalog-style summary of every official Component.
- [ComponentLibrary.md](../guidelines/ComponentLibrary.md) - Defines official Component categories, support levels, and Markdown Usage patterns.
- [ContentSystem.md](../guidelines/ContentSystem.md) - Defines the editorial hierarchy used by this document.
- [DocumentationFramework.md](../guidelines/DocumentationFramework.md) - Defines the authoring-first framework vision.

# Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 0.1.0 | 2026-06-26 | Codex | Initial realistic Component showcase document. |
