# M01 · Clean document and core editor loop

- **Goal:** Open Daisy, see one empty section, add a box and a text element, change them, and see the real page update.
- **Source:** PLAN.md §16 Milestone 1
- **Spec:** PLAN.md 9.2, 10, 11, 13.3
- **Designs:** D-03, D-04 (shell frame only)
- **Packages:** model, css, renderer, editor, ui
- **Code style:** ADR 0011 — where PLAN.md names functions (`createEmptyDocument`, `generateCss`, `insertNode`…), build them as classes and methods with injected dependencies.

**Implementation notes:** Vite + React + TypeScript project. Types and commands from chapter 10 (nodes, styles for base only, `insertNode`, `removeNode`, `setStyles`). Zustand + Immer store with `run`, `begin`, `commit`, `rollback`, `undo`, `redo`. `generateCss` for base styles and the base stylesheet. `CanvasRenderer` with initial render and patch application. Edit frame with the sandbox settings of 9.2. `CanvasViewport` with hit testing and tool dispatch. SVG overlay for hover and selection outlines.

## Acceptance criteria

- A fresh load shows exactly one empty section on a white 1440 px page; the model contains one section node and one declaration.
- Drawing a box adds a `<div>` to the frame's DOM with a class, and a rule for that class to the frame's stylesheet.
- Changing Width in the panel changes the rule and the canvas within one frame.
- Typing in a text element updates the model's text node.
- Undo and redo step through every action, and the DOM matches the model after each.
- No script can run in the edit frame (test: a node with an `onclick` attribute and a `<script>` child in the model does nothing).

**Done when:** A user can open Daisy, click the section, draw two boxes and a line of text, recolour and resize them from the panel, and undo it all.

## Tasks

### M01-T01 Scaffold the project with strict TypeScript, ESLint, Prettier, Vitest.

- **Status:** done

### M01-T02 Define `DaisyDocument`, `ElementNode`, `TextNode`, `StyleDecls`, `ResponsiveStyles` and a `createEmptyDocument()` that returns one `<section>` with `min-height: 400px`.

- **Status:** todo

### M01-T03 Implement `insertNode`, `removeNode`, `setStyles`, `replaceChildren` with the invariant checker.

- **Status:** todo

### M01-T04 Implement the doc store with patch capture, transactions, undo and redo.

- **Status:** todo

### M01-T05 Implement `generateCss` (base rules only) and the base stylesheet.

- **Status:** todo

### M01-T06 Implement the edit frame and `CanvasRenderer` (initial render; patch → DOM/CSSOM updates; id maps).

- **Status:** todo

### M01-T07 Verify that listeners attached from the editor window fire inside the script-less sandboxed edit frame in Electron's Chromium; record the result in PLAN.md 19.2 R1 (Firefox and Safari are no longer targets, ADR 0001).

- **Status:** todo

### M01-T08 Implement `CanvasViewport`: pointer events, `hitTest`, the `Tool` interface, active-tool dispatch.

- **Status:** todo

### M01-T09 Implement the overlay: hover outline, selection outline with name tag, empty-section hint.

- **Status:** todo

### M01-T10 Implement the Select tool (click to select, `Delete` to remove).

- **Status:** todo

### M01-T11 Implement the Box tool (click and drag to create, in flow, at the end of the section).

- **Status:** todo

### M01-T12 Implement the Text tool (click to create a paragraph; plain-text inline editing with `contenteditable`; commit on `Esc` or blur).

- **Status:** todo

### M01-T13 Build the minimal shell: tool strip with three tools, canvas, and a properties panel with Width, Height, Fill colour, Text colour and Font size wired through `setStyles`.

- **Status:** todo

### M01-T14 Wire `Ctrl+Z` / `Ctrl+Shift+Z`.

- **Status:** todo
