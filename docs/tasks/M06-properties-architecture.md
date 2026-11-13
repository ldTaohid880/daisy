# M06 · Properties architecture

- **Goal:** The registry-driven Properties panel with the disclosure pattern and robust value fields.
- **Source:** PLAN.md §16 Milestone 6
- **Spec:** PLAN.md 6
- **Designs:** D-04, D-20
- **Packages:** model, editor, ui
- **Code style:** ADR 0011 — where PLAN.md names functions (`createEmptyDocument`, `generateCss`, `insertNode`…), build them as classes and methods with injected dependencies.

**Implementation notes:** `PropertyGroupDef` and `ControlDef` (6.1). `effectiveDecls` with origin tracking. Shared controls: length field (parsing, units, arithmetic, scrubbing, stepping), colour picker, select, segmented, toggle, box-sides. Style normalisation with shorthand expansion and `CSS.supports` validation (10.3). Free placement conversion (7.4). Mixed values for multi-selection.

## Acceptance criteria

- Typing `50%`, `12rem`, `auto`, `100% - 40px`, `clamp(1rem, 4vw, 3rem)` or `var(--x)` into a length field stores the correct CSS; typing `banana` is rejected.
- Typing `padding: 8px 16px` under Other properties results in four stored longhands and the Spacing diagram showing them.
- Switching an element to Free does not move it by more than 0.5 px, and is one undo step including the parent's `position: relative`.
- Selecting an image does not show Layout or Typography; selecting a paragraph does not show Layout.
- Advanced disclosure state survives selecting other elements and reloading.

**Done when:** A user can precisely control size, placement, spacing, colour and borders of any element, in simple terms or with any CSS value they choose.

## Tasks

### M06-T01 Implement style normalisation: shorthand expansion via the browser, validation, zero handling.

- **Status:** todo

### M06-T02 Implement `effectiveDecls` and its memoisation.

- **Status:** todo

### M06-T03 Build the group container component: collapse, Advanced disclosure with remembered state, set-value dot, "Other properties" rows.

- **Status:** todo

### M06-T04 Build the length field with units, keywords, arithmetic → `calc()`, custom-value fallback, scrub, arrow stepping, validation feedback.

- **Status:** todo

### M06-T05 Implement unit conversion that preserves visual size.

- **Status:** todo

### M06-T06 Build the colour picker (hex, alpha, hue/saturation area, eyedropper button stub).

- **Status:** todo

### M06-T07 Build tooltips showing description, CSS property and current value.

- **Status:** todo

### M06-T08 Implement General (name, kind, tag, class, id).

- **Status:** todo

### M06-T09 Implement Size (modes Fill / Fit content / Fixed, min/max, overflow, aspect ratio) with the "real size differs" note.

- **Status:** todo

### M06-T10 Implement Placement: In flow ↔ Free conversion with anchor handling, pins, offsets, stack order; free drag and nudge on the canvas with snapping.

- **Status:** todo

### M06-T11 Implement Spacing box diagram (numeric only) and "Center horizontally".

- **Status:** todo

### M06-T12 Implement single-colour Fill and simple Border with corner roundness; corner handles on the canvas.

- **Status:** todo

### M06-T13 Implement group adaptation by element type and context (`appliesTo`, `visibleWhen`), and Mixed values.

- **Status:** todo

### M06-T14 Show the selection's X, Y, W, H and placement switch in the Select options bar.

- **Status:** todo
