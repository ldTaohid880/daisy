# M18 · Design system

- **Goal:** Each project can have a design system (colours, type, spacing, radii, shadows) used by properties and exported as CSS variables.
- **Source:** new (not in PLAN.md)
- **Spec:** UI_DESIGN_PLAN.md D-36 sections
- **Designs:** D-36, D-36b, D-36c, D-02b step 3
- **Packages:** model, css, editor
- **Code style:** ADR 0011 — where PLAN.md names functions (`createEmptyDocument`, `generateCss`, `insertNode`…), build them as classes and methods with injected dependencies.

## Acceptance criteria

- New project steps can create a design system or skip it; it can be added later (D-36b).
- Editing a token updates every use on the canvas and in export.
- Properties show linked tokens and allow unlinking (D-47 pattern).
- D-36c states all reproducible.

**Done when:** Halden uses its design system end to end and exports clean `:root` variables.

## Tasks

### M18-T01 Design-system model and file

- **Status:** todo
- **Needs:** M06
- **Done when:** `design-system.json` schema: token groups, modes (light/dark), references; migrations.

### M18-T02 CSS variables generation

- **Status:** todo
- **Needs:** M18-T01
- **Done when:** css emits `:root` and mode blocks; values referenced as `var(--…)` in rules.

### M18-T03 Design system editor

- **Status:** todo
- **Needs:** M18-T01
- **Done when:** D-36 screen: groups, edit token, usage count, rename with reference update.

### M18-T04 Opt in later and setup flow

- **Status:** todo
- **Needs:** M18-T03
- **Done when:** D-36b; wizard step in D-02b becomes real.

### M18-T05 Token pickers in properties

- **Status:** todo
- **Needs:** M18-T02
- **Done when:** Colour, type, spacing, radius, shadow controls show tokens first; link/unlink.

### M18-T06 States sheet behaviours

- **Status:** todo
- **Needs:** M18-T03
- **Done when:** D-36c: empty, conflicts, deleting a used token, import from CSS.
