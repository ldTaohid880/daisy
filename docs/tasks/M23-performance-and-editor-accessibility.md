# M23 · Performance and editor accessibility

- **Goal:** Daisy stays fast on large pages and is usable by keyboard and assistive technology.
- **Source:** PLAN.md §16 Milestone 18
- **Spec:** PLAN.md 9.11
- **Designs:** —
- **Packages:** all
- **Code style:** ADR 0011 — where PLAN.md names functions (`createEmptyDocument`, `generateCss`, `insertNode`…), build them as classes and methods with injected dependencies.

**Implementation notes:** Profiling against the budgets in 9.11 with generated large fixtures. Measurement batching review, memoisation, virtualisation. Lazy loading of heavy modules. ARIA roles for tree, toolbar, tabs; focus management; keyboard equivalents for canvas operations.

## Acceptance criteria

- All budgets in 9.11 are met in the automated performance tests.
- A complete simple page can be created, styled, saved and exported without a mouse.
- A screen reader announces tool changes, the selected element's name and type, and property labels with values.
- Initial load transfers under the bundle budget; the code editor is not loaded until the drawer opens.

**Done when:** A user can work comfortably on a long, complex page, and a keyboard-only user can use every feature that does not inherently require pointing.

## Tasks

### M23-T01 Create fixture generators for 500, 2,000 and 5,000-element documents and automated timing tests.

- **Status:** todo

### M23-T02 Profile and fix open time, drag frame rate, property edit latency, and memory over long undo sequences.

- **Status:** todo

### M23-T03 Ensure only overlay-relevant elements are measured; remove any full-tree walks from hot paths.

- **Status:** todo

### M23-T04 Lazy-load CodeMirror, Timeline, export, zip and sanitiser code; set a bundle size budget.

- **Status:** todo

### M23-T05 Downscale thumbnails for large images in Assets and Home.

- **Status:** todo

### M23-T06 Make every panel operable by keyboard with visible focus; implement roving focus in the tool strip and tree semantics in Layers.

- **Status:** todo

### M23-T07 Provide keyboard equivalents for canvas actions: move in order, resize by keys in a "resize mode", change placement, enter and leave containers.

- **Status:** todo

### M23-T08 Add accessible names to all controls; announce selection changes and operation results through a live region.

- **Status:** todo

### M23-T09 Check editor colour contrast in both themes; respect the operating system's reduced-motion setting in editor animations.

- **Status:** todo

### M23-T10 Build the keyboard shortcuts reference dialog.

- **Status:** todo
