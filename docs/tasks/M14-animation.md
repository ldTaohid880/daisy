# M14 · Animation

- **Goal:** Keyframe animation with a timeline.
- **Source:** PLAN.md §16 Milestone 14
- **Spec:** PLAN.md 6.4 (animation)
- **Designs:** D-28, D-28b
- **Packages:** model, css, editor
- **Code style:** ADR 0011 — where PLAN.md names functions (`createEmptyDocument`, `generateCss`, `insertNode`…), build them as classes and methods with injected dependencies.

**Implementation notes:** `KeyframesDef` in the model; `@keyframes` generation; `animation-*` longhands. Timeline scrubbing by setting a negative `animation-delay` with a paused play state on the edited element (exempted from the editor's animation-off rule). `motion.js` and `data-animate` output. Reduced-motion wrapping.

## Acceptance criteria

- A fade-in exports one `@keyframes` block and animation longhands (collapsed to `animation`), and plays on load in Preview.
- Scrubbing the timeline shows intermediate states on the canvas without altering the document.
- With "scrolled into view", the exported page includes `js/motion.js` and the element animates only when scrolled to; with scripts disabled the element is still visible.
- With the operating system set to reduce motion, the exported page shows no animation.

**Done when:** A user can make elements fade, slide and scale in on load or on scroll, fine-tune keyframes on a timeline, and export it as standard CSS.

## Tasks

### M14-T01 Implement keyframes commands and `@keyframes` generation with unique names.

- **Status:** todo

### M14-T02 Implement the Animation group simple controls and the starting choices (Fade in, Move in, Scale in, Spin, Custom).

- **Status:** todo

### M14-T03 Build the Timeline: tracks per animated property, keyframe add/move/delete, per-keyframe easing, duration and delay handles.

- **Status:** todo

### M14-T04 Implement scrub, play and pause on the canvas.

- **Status:** todo

### M14-T05 Record mode: while a keyframe is selected, canvas and panel edits write into that keyframe.

- **Status:** todo

### M14-T06 Implement advanced controls: iteration, direction, fill mode, multiple animations.

- **Status:** todo

### M14-T07 Implement "When scrolled into view": `MotionTrigger`, `data-animate`, paused-until-class CSS, `motion.js` export.

- **Status:** todo

### M14-T08 Implement scroll-driven timelines as an Advanced option with a support note.

- **Status:** todo

### M14-T09 Implement reduced-motion handling (on by default).

- **Status:** todo

### M14-T10 Add Layers badges and Preview replay button.

- **Status:** todo
