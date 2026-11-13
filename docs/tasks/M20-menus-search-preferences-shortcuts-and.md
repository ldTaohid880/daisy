# M20 · Menus, search, preferences, shortcuts and themes

- **Goal:** Every menu, search, preference and theme from the designs.
- **Source:** new (not in PLAN.md)
- **Spec:** UI_DESIGN_PLAN.md 3.3, 7.5, 9.2
- **Designs:** D-38, D-40, D-48, D-49, D-50, D-51, D-33, D-33b–d, D-34
- **Packages:** editor, ui, desktop
- **Code style:** ADR 0011 — where PLAN.md names functions (`createEmptyDocument`, `generateCss`, `insertNode`…), build them as classes and methods with injected dependencies.

## Acceptance criteria

- File, Edit, Element, View and Help menus match D-38; every action is also in a menu (PLAN R16).
- Right-click menus per D-48.
- Search (D-40), Find and replace (D-51), Preferences (D-49), Keyboard shortcuts with conflict check (D-50).
- Light theme (D-33, D-33b–d) and compact layout (D-34) pass the contrast checks in UI_DESIGN_PLAN.md 9.2.

**Done when:** The editor is fully navigable from menus and keyboard, in both themes.

## Tasks

### M20-T01 Command registry and menu bar

- **Status:** todo
- **Needs:** M06
- **Done when:** One registry of commands with ids, labels, shortcuts, enabled state; D-38 menus render from it.

### M20-T02 Right-click menus

- **Status:** todo
- **Needs:** M20-T01
- **Done when:** D-48 for canvas, layers, pages, assets.

### M20-T03 Search

- **Status:** todo
- **Needs:** M20-T01
- **Done when:** D-40: commands, layers, pages, assets, settings; Ctrl P.

### M20-T04 Preferences

- **Status:** todo
- **Needs:** M03
- **Done when:** D-49 sections stored in app data; the AI tools and MCP tab is added in M21.

### M20-T05 Keyboard shortcuts editor

- **Status:** todo
- **Needs:** M20-T01
- **Done when:** D-50 with conflict check and reserved-combination warnings.

### M20-T06 Find and replace

- **Status:** todo
- **Needs:** M20-T03
- **Done when:** D-51 across pages with scope, kinds, regex.

### M20-T07 Light theme

- **Status:** todo
- **Needs:** M01
- **Done when:** Complete light tokens (9.2); D-33, D-33b–d screens match.

### M20-T08 Compact layout for 1440 × 900

- **Status:** todo
- **Needs:** M20-T07
- **Done when:** D-34 rules.
