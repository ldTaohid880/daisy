# M19 · Reusable content: shared parts, components, collections, interactive parts

- **Goal:** Reusable content: shared parts, components with variants, collections with item pages, and interactive parts.
- **Source:** new (not in PLAN.md)
- **Spec:** UI_DESIGN_PLAN.md D-53, D-56–D-58
- **Designs:** D-53, D-56, D-56b, D-57, D-57b, D-58, D-58b
- **Packages:** model, css, html, export, editor
- **Code style:** ADR 0011 — where PLAN.md names functions (`createEmptyDocument`, `generateCss`, `insertNode`…), build them as classes and methods with injected dependencies.

## Acceptance criteria

- Editing a shared part updates every page; page-level overrides are kept (D-53).
- Components with variants and options; swap, detach, delete with keep-as-copies (D-58, D-58b).
- Collections repeat a designed card from data, with filters, sorting and item pages (D-57, D-57b).
- Interactive parts (menu, tabs, accordion, pop-up, slider, show/hide) work in Preview and export with accessible markup (D-56, D-56b).

**Done when:** Halden's header/footer are shared, products are a collection with item pages, product cards are a component, and the mobile menu works.

## Tasks

### M19-T01 Shared parts

- **Status:** todo
- **Needs:** M17
- **Done when:** D-53: make shared, edit once, overrides, detach; stored in `parts/`.

### M19-T02 Components and variants model

- **Status:** todo
- **Needs:** M19-T01
- **Done when:** Component definition, options (exposed props), variants as property overrides.

### M19-T03 Components UI

- **Status:** todo
- **Needs:** M19-T02
- **Done when:** D-58, D-58b: make component, changes on one use, variant editing, swap, delete/detach.

### M19-T04 Collections data and binding

- **Status:** todo
- **Needs:** M19-T02
- **Done when:** D-57: collection files, fields, repeat a card, field mapping, filters and sorting.

### M19-T05 Collection item pages

- **Status:** todo
- **Needs:** M19-T04
- **Done when:** Template page `shop/{slug}.html` with item switcher; export one page per item.

### M19-T06 Collection states

- **Status:** todo
- **Needs:** M19-T04
- **Done when:** D-57b: empty, CSV import, missing fields, large collections.

### M19-T07 Interaction model

- **Status:** todo
- **Needs:** M12
- **Done when:** D-56: when / do / target / start / motion; accessibility rules; minimal generated JS (PLAN.md 14.4).

### M19-T08 Interactive part library

- **Status:** todo
- **Needs:** M19-T07
- **Done when:** Menu for phones, tabs, accordion, pop-up, image slider, show/hide; D-56b states; Preview and export tests.
