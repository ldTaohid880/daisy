# M05 · Layers and document hierarchy

- **Goal:** See and control the real structure of the page.
- **Source:** PLAN.md §16 Milestone 5
- **Spec:** PLAN.md 8.3, 4.5
- **Designs:** D-24, D-25
- **Packages:** editor
- **Code style:** ADR 0011 — where PLAN.md names functions (`createEmptyDocument`, `generateCss`, `insertNode`…), build them as classes and methods with injected dependencies.

**Implementation notes:** Virtualised tree over the node map. Drag and drop in the tree using `moveNode` and `canContain`. `locked` flag honoured by hit testing. Hide writes `display: none` to the base. Group and ungroup as composite commands. Class name generation from names (11.3).

## Acceptance criteria

- The tree always equals the DOM structure of the edit frame (automated comparison after random operations).
- Renaming "Box 3" to "Price card" makes the exported class `price-card`.
- A locked element cannot be selected by clicking the canvas but can be from Layers.
- Grouping three siblings creates one `<div>` containing them in the same order; ungrouping restores the previous structure exactly.

**Done when:** A user can organise a page of fifty nested elements: name them, find them, restructure them and protect finished parts from accidental edits.

## Tasks

### M05-T01 Build the virtualised Layers tree with expand/collapse, icons and default names.

- **Status:** todo

### M05-T02 Two-way selection sync, including auto-expand and scroll into view.

- **Status:** todo

### M05-T03 Hovering a row highlights the element on the canvas, and the reverse.

- **Status:** todo

### M05-T04 Inline rename with class name regeneration and uniqueness.

- **Status:** todo

### M05-T05 Drag to reorder and nest within the tree, with between/inside indicators and validation.

- **Status:** todo

### M05-T06 Lock: flag, icon, canvas hit-test skip, `Ctrl+Shift+L`.

- **Status:** todo

### M05-T07 Hide: `display: none`, eye icon, hidden notice in Properties, `Ctrl+Shift+H`.

- **Status:** todo

### M05-T08 Group (`Ctrl+G`) and Ungroup (`Ctrl+Shift+G`) with the style-loss warning.

- **Status:** todo

### M05-T09 Layer context menu; "Select layer" submenu on the canvas context menu.

- **Status:** todo

### M05-T10 Name/tag filter field.

- **Status:** todo

### M05-T11 `Ctrl+[` / `Ctrl+]` reorder shortcuts and `Tab` / `Shift+Tab` sibling navigation.

- **Status:** todo
