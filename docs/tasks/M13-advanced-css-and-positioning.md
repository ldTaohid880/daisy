# M13 · Advanced CSS and positioning

- **Goal:** Professional-level control: transforms, gradients on canvas, remaining placement modes, element-level custom CSS and code inspection.
- **Source:** PLAN.md §16 Milestone 13
- **Spec:** PLAN.md 7.4, 9.10
- **Designs:** D-16, D-19
- **Packages:** css, renderer, editor
- **Code style:** ADR 0011 — where PLAN.md names functions (`createEmptyDocument`, `generateCss`, `insertNode`…), build them as classes and methods with injected dependencies.

**Implementation notes:** Matrix-based oriented overlay boxes. Gradient parsing and on-canvas stop editing. Fixed rendering in the first-screen box (9.9). `ExtraRule` editing and generation. Read-only code view generated from the same generators. CodeMirror lazy-loaded.

## Acceptance criteria

- Rotating an element 30° writes only `transform`; neighbours do not move; the selection box is drawn rotated and handles still work.
- Typing `padding-top: 20px` in Custom CSS updates the Spacing diagram, and dragging the padding band updates the Custom CSS text.
- A sticky header sticks in Preview and in the exported page; a fixed element is shown in the first-screen box on the canvas and fixed in Preview.
- A `::before` rule with `content` renders on the canvas and exports as `.name::before { … }`.

**Done when:** A professional can express essentially any single-element CSS in Daisy, by handle where one exists and by value where not, and inspect the code as they work.

## Tasks

### M13-T01 Implement the Transform group and the Transform tool (rotate, scale, origin, skew) with oriented selection boxes and the untransformed ghost.

- **Status:** todo

### M13-T02 Make hit testing, handles and snapping correct for transformed elements and transformed ancestors.

- **Status:** todo

### M13-T03 Implement the Gradient tool with on-canvas line and stops for linear, radial and conic gradients.

- **Status:** todo

### M13-T04 Implement Nudged, Fixed and Sticky placement with their canvas affordances and warnings.

- **Status:** todo

### M13-T05 Implement the "position uses a formula" lock and "Replace with fixed value".

- **Status:** todo

### M13-T06 Implement the Custom CSS group: declarations editor with autocomplete and validation, merged into the element's stored declarations.

- **Status:** todo

### M13-T07 Implement extra selectors (`ExtraRule`): create, edit, generate, including `::before` / `::after`.

- **Status:** todo

### M13-T08 Build the Code drawer with the Element tab: live HTML and CSS of the selection.

- **Status:** todo

### M13-T09 Implement rulers and draggable guides with snapping; persist guides.

- **Status:** todo

### M13-T10 Add multi-column text, `clip-path` presets and mask controls to their groups' Advanced areas.

- **Status:** todo

### M13-T11 Add "Also styled by Page CSS" detection hook (used fully in Milestone 15).

- **Status:** todo
