# M12 · States and transitions

- **Goal:** Interactive styling: hover, pressed, focus and smooth changes between them.
- **Source:** PLAN.md §16 Milestone 12
- **Spec:** PLAN.md 6.5
- **Designs:** D-21
- **Packages:** model, css, editor
- **Code style:** ADR 0011 — where PLAN.md names functions (`createEmptyDocument`, `generateCss`, `insertNode`…), build them as classes and methods with injected dependencies.

**Implementation notes:** State keys in `ResponsiveStyles` are already modelled. Forced-state selectors and `data-d-state` in the edit target. State-ordered rule output. Transition controls and a canvas play-through using a temporary class swap in the edit frame.

## Acceptance criteria

- A button with a hover fill exports `.name:hover { background-color: … }` after the normal rule; hovering in Preview changes the colour.
- With Mouse over selected, the canvas shows the hover appearance without the pointer being over the element.
- Enabling "Animate changes" adds transition longhands to the normal rule only.
- Focus styles are visible when tabbing in Preview.

**Done when:** A user can make buttons, links and fields respond to mouse over, press and keyboard focus with smooth transitions.

## Tasks

### M12-T01 Implement the State selector with element-appropriate states and custom suffix entry.

- **Status:** todo

### M12-T02 Route writes to the active state; show the chip; reset to Normal on selection change.

- **Status:** todo

### M12-T03 Generate state rules in the fixed order; add forced-state selectors for the edit target.

- **Status:** todo

### M12-T04 Show Normal values as muted placeholders while editing a state.

- **Status:** todo

### M12-T05 Implement the Transition group simple controls and the inline suggestion on first hover style.

- **Status:** todo

### M12-T06 Implement per-property transitions and the cubic-bezier editor.

- **Status:** todo

### M12-T07 Implement the canvas transition preview button.

- **Status:** todo

### M12-T08 Add Layers badges for state styles; add "Add mouse-over style" to the Button options.

- **Status:** todo

### M12-T09 Support states combined with screen sizes.

- **Status:** todo

### M12-T10 Implement `::placeholder` editing for fields.

- **Status:** todo
