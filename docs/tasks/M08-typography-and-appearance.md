# M08 · Typography and appearance

- **Goal:** Full control of how things look: fonts, text styling, fills, gradients, borders, shadows and effects.
- **Source:** PLAN.md §16 Milestone 8
- **Spec:** PLAN.md 6.4
- **Designs:** D-35 Radius, D-39, D-47
- **Packages:** css, editor, ui
- **Code style:** ADR 0011 — where PLAN.md names functions (`createEmptyDocument`, `generateCss`, `insertNode`…), build them as classes and methods with injected dependencies.

**Implementation notes:** Font registry with system stacks; text options in the options bar; range-level typography during text editing. Fill layer model mapped to comma-separated background longhands. Shadow and filter list editors. Tokens as CSS custom properties with `var()` references. Eyedropper via the `EyeDropper` API with a computed-style fallback.

## Acceptance criteria

- Two fill layers (gradient over colour) produce one `background-color` and one `background-image`, and reorder correctly.
- Editing a colour swatch changes every element using it without changing any element's stored declarations.
- Setting text colour on a section changes its children on the canvas, and their Typography group shows the value as coming from the section.
- A shadow list with two shadows round-trips through reload unchanged.

**Done when:** A user can produce a visually finished static page: styled type, colours from a shared palette, gradients, rounded bordered cards with shadows.

## Tasks

### M08-T01 Implement the Typography group simple controls and wire the Text tool's options bar to them.

- **Status:** todo

### M08-T02 Implement Typography advanced controls, including truncation and the fluid size helper.

- **Status:** todo

### M08-T03 Show "from parent" origin for inherited text values with click-through.

- **Status:** todo

### M08-T04 Apply typography to a selected text range (span creation and merging).

- **Status:** todo

### M08-T05 Implement the font picker with system font stacks and previews.

- **Status:** todo

### M08-T06 Implement the Fill layer list: colour and image layers, reorder, toggle; mapping to and from background longhands.

- **Status:** todo

### M08-T07 Implement gradient layers with a stop editor in the panel.

- **Status:** todo

### M08-T08 Complete Border: per-side values, all styles, elliptical radii, outline.

- **Status:** todo

### M08-T09 Implement Effects: opacity, shadow list with inner shadows, blur; Advanced blend mode, filter list, backdrop filter, clip-path, cursor.

- **Status:** todo

### M08-T10 Implement tokens and the Swatches panel: colours, text styles, apply, edit, "Add from selection", detach.

- **Status:** todo

### M08-T11 Extend the colour picker with swatches, rgb / hsl / oklch input and a contrast readout against the background.

- **Status:** todo

### M08-T12 Implement the Eyedropper tool and Copy style / Paste style.

- **Status:** todo

### M08-T13 Implement Page properties (background, base text) when nothing is selected.

- **Status:** todo
