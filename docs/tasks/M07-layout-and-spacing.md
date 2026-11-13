# M07 · Layout and spacing

- **Goal:** Visual control of arrangement: rows, columns, grids, gaps, padding and margin on the canvas.
- **Source:** PLAN.md §16 Milestone 7
- **Spec:** PLAN.md 7
- **Designs:** D-14, D-15, Layout-Advanced
- **Packages:** model, css, editor, renderer
- **Code style:** ADR 0011 — where PLAN.md names functions (`createEmptyDocument`, `generateCss`, `insertNode`…), build them as classes and methods with injected dependencies.

**Implementation notes:** `readLayout` / `writeLayout` and the track-list parser (7.2). Insertion finder extended to rows, wrapped rows and grids. Gap, band and track overlays using computed styles. Child controls for rows and grids in Size. Alignment and distribution actions.

## Acceptance criteria

- Choosing Row then dragging a gap bar writes `display: flex` and `gap` and nothing else.
- Setting Grid with 3 columns then dragging the first line produces a three-track template whose pixel result matches the pointer within 1 px.
- A grid template using `subgrid` or named lines is displayed but not draggable, and is never rewritten.
- Switching Row → Grid → Row restores the original row settings.
- Dragging the top padding band of a section 64 px writes `padding-top: 64px`.

**Done when:** A user can build a navigation bar, a two-column block and a three-card grid from empty boxes using only the Layout and Spacing tools.

## Tasks

### M07-T01 Implement `readLayout`, `writeLayout`, and the `TrackList` parser with the `editable` flag.

- **Status:** todo

### M07-T02 Implement the Layout group: Stack / Row / Grid, direction, alignment grid, spread, wrap, gap; Advanced raw properties; inactive-property tags and "Clean up".

- **Status:** todo

### M07-T03 Extend flow drag and creation insertion to row, wrapped row and grid parents.

- **Status:** todo

### M07-T04 Implement the Stack → Column conversion when aligning, with the status message.

- **Status:** todo

### M07-T05 Implement child controls: Grow to fill, shrink, basis, align self, order; grid column/row start and span.

- **Status:** todo

### M07-T06 Implement the Layout tool for rows: gap bars (drag), direction arrow, per-child grow toggle, options bar.

- **Status:** todo

### M07-T07 Implement the Layout tool for grids: track lines and badges, drag to resize tracks, add/remove tracks, drag child to cell, drag edge to span.

- **Status:** todo

### M07-T08 Implement the Spacing tool: padding and margin bands, edge drag, `Alt`/`Shift` modifiers, gap drag between siblings, double-click to type, zero-size grab strips.

- **Status:** todo

### M07-T09 Draw bands and gaps when hovering or focusing the matching fields in the panel.

- **Status:** todo

### M07-T10 Implement alignment and distribution buttons for single flow children, multi-selections and free elements.

- **Status:** todo

### M07-T11 Implement `Alt`-hover distance readouts and the Measure tool.

- **Status:** todo

### M07-T12 Show the margin-collapse tag in the Spacing tool.

- **Status:** todo
