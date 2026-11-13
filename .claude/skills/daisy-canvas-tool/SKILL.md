---
name: daisy-canvas-tool
description: Implement a canvas tool (Select, Box, Text, Layout, Spacing…) with the Tool interface, gestures, overlay and tests.
---

# Canvas tool

Spec: PLAN.md 5.2–5.3 (tool rules and the tool's own spec), 9.4 (pointer interaction), 9.6 (drag maths); its D-board.

1. File: `packages/editor/src/tools/<Name>Tool.ts`, a class implementing `Tool` (`onPointerDown/Move/Up`, `onKey`,
   `cursor`, `overlay`) with its collaborators (doc store, hit tester, snapping) injected; register it in the tool registry module.
2. Gestures run inside one transaction: `store.begin()` on down, preview with `store.update`, `commit` on up, `rollback` on Esc.
   One gesture = one history entry.
3. Geometry maths goes in `packages/renderer` as small classes with no side effects (`Snapper`, `InsertionFinder`) and unit tests.
4. Options bar content: only tool behaviour (UI_DESIGN_PLAN.md 4.3 "one control, one place").
5. Tests: unit for maths; e2e in `apps/desktop/e2e/tools/<tool>.spec.ts` that performs the gesture and asserts the model
   AND the exported CSS (exact declarations), plus Esc-cancels and single-undo.
