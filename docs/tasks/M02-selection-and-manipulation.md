# M02 · Selection and manipulation

- **Goal:** Direct manipulation on the canvas: move, resize, reorder, multi-select, duplicate, zoom and pan.
- **Source:** PLAN.md §16 Milestone 2
- **Spec:** PLAN.md 9.4–9.8
- **Designs:** D-05–D-11, D-19
- **Packages:** renderer, editor
- **Code style:** ADR 0011 — where PLAN.md names functions (`createEmptyDocument`, `generateCss`, `insertNode`…), build them as classes and methods with injected dependencies.

**Implementation notes:** Measurement pass (9.5). Resize calculation and flow drag insertion finder (9.6) for Stack parents. `moveNode` command. World transform for zoom/pan with pointer-anchored zoom. Scope rule for selection. Clipboard as serialised subtrees.

## Acceptance criteria

- Dragging a box above another reorders the DOM and the model identically; one undo restores it.
- A whole drag or resize is a single history entry; `Esc` mid-drag leaves the document unchanged.
- Outlines and handles stay aligned with elements at every zoom from 10% to 800%, and stay the same screen size.
- Resizing an element taller pushes following elements down live.
- Pasting produces elements with class names not used elsewhere.

**Done when:** A user can lay out a simple stacked page by drawing boxes and text, dragging them into order and into each other, resizing by hand, and navigating with zoom and pan.

## Tasks

### M02-T01 Implement the measurement scheduler (rAF pass, `ResizeObserver` on body and selection, frame auto-height).

- **Status:** todo

### M02-T02 Draw 8 resize handles; implement resize for flow elements writing `width` / `height` in px inside a transaction.

- **Status:** todo

### M02-T03 Show the live size label; implement `Shift` proportional resize.

- **Status:** todo

### M02-T04 Implement `moveNode` and flow drag: container detection, insertion index, insertion line, drop target outline, ghost.

- **Status:** todo

### M02-T05 Implement nesting by dropping into a box, including the 400 ms hover-to-open rule.

- **Status:** todo

### M02-T06 Implement the selection scope rule, double-click to enter, `Esc` to parent, `Ctrl+click` deep select.

- **Status:** todo

### M02-T07 Implement multi-selection: `Shift+click`, marquee, bounding box, group move.

- **Status:** todo

### M02-T08 Implement duplicate (`Ctrl+D`, `Alt+drag`), copy, cut, paste, paste inside, delete, with new ids and unique class names.

- **Status:** todo

### M02-T09 Implement zoom (wheel, shortcuts, fit, 100%) and pan (wheel, `Space+drag`, middle drag), Hand and Zoom tools.

- **Status:** todo

### M02-T10 Implement the status bar breadcrumb with click and hover behaviour.

- **Status:** todo

### M02-T11 Implement the element context menu with the actions available so far.

- **Status:** todo

### M02-T12 Implement alignment guides and size-match snapping during resize.

- **Status:** todo
