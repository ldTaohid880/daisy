# M11 · Responsive editing

- **Goal:** Design for every screen size without overwriting anything by accident.
- **Source:** PLAN.md §16 Milestone 11
- **Spec:** PLAN.md 7.3
- **Designs:** D-22, D-23
- **Packages:** model, css, editor
- **Code style:** ADR 0011 — where PLAN.md names functions (`createEmptyDocument`, `generateCss`, `insertNode`…), build them as classes and methods with injected dependencies.

**Implementation notes:** Breakpoints in the model; `setStyles` already takes a breakpoint id. Media query blocks in the generator in cascade order. Frame width switching. Origin markers from `effectiveDecls`. Reset and promote actions. `vh` rewriting and fold line.

## Acceptance criteria

- Changing font size at Tablet leaves the base declaration byte-for-byte unchanged and adds exactly one declaration under the Tablet key.
- Exported CSS contains the override inside `@media (max-width: 1024px)`, after all base rules.
- An element hidden on Mobile and shown elsewhere keeps its `display: flex` at larger sizes.
- Deleting a screen size never discards values without the user choosing.
- A 3-column grid set to 1 column at Mobile exports and behaves correctly when the browser window is resized.

**Done when:** A user can take a desktop design, switch to tablet and mobile, adjust type, spacing, columns and visibility for each, and export a site that adapts correctly.

## Tasks

### M11-T01 Add default breakpoints (Tablet 1024/768, Mobile 640/390) to new documents and a migration for existing ones.

- **Status:** todo

### M11-T02 Generate `@media` blocks in the correct order for desktop-first, including `min-width` sizes.

- **Status:** todo

### M11-T03 Implement the top bar selector, `Alt+1..3`, and canvas width switching.

- **Status:** todo

### M11-T04 Route all style writes to the active breakpoint; show the `Editing:` chip.

- **Status:** todo

### M11-T05 Implement origin markers and tooltips on every control; Reset and "Set for all sizes".

- **Status:** todo

### M11-T06 Implement the Properties context strip with the list of overrides and "Clear all here".

- **Status:** todo

### M11-T07 Implement the Visibility group with per-size toggles and correct display restoration.

- **Status:** todo

### M11-T08 Implement the structural-edit notice at non-base sizes and base routing for new elements' starting styles.

- **Status:** todo

### M11-T09 Build the Screen sizes dialog: add, edit, delete with discard/merge choice; mobile-first conversion with preview and automatic version.

- **Status:** todo

### M11-T10 Implement the Visual order control with its accessibility note.

- **Status:** todo

### M11-T11 Implement edit-target `vh` rewriting and the fold line.

- **Status:** todo

### M11-T12 Add Layers badges for elements with overrides; drag the page edge to test widths.

- **Status:** todo
