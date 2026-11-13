# M17 · Pages and project settings

- **Goal:** Projects have many pages with page settings, and project-wide settings.
- **Source:** new (not in PLAN.md)
- **Spec:** UI_DESIGN_PLAN.md phase G/H; ADR 0005
- **Designs:** D-31, D-31b, D-44, D-44b, D-45, D-54
- **Packages:** model, editor, project-fs
- **Code style:** ADR 0011 — where PLAN.md names functions (`createEmptyDocument`, `generateCss`, `insertNode`…), build them as classes and methods with injected dependencies.

## Acceptance criteria

- Pages can be added, duplicated, renamed, reordered and deleted (D-54); each page exports to its own file.
- Page settings (title, description, social image, URL, code) save per page (D-31, D-31b).
- Project settings tabs (D-44, D-44b) change export output exactly as specified.
- Importing an HTML page (D-45) creates an editable page or reports what could not be imported.

**Done when:** A user can build and export a four-page Halden site with correct titles, links and redirects.

## Tasks

### M17-T01 Multi-page model and page tabs

- **Status:** todo
- **Needs:** M03
- **Done when:** Manifest page order; Photoshop-style page tabs (D-04); open/close tabs; links between pages resolve on export.

### M17-T02 Page dialogs: new, duplicate, rename, delete

- **Status:** todo
- **Needs:** M17-T01
- **Done when:** D-54 incl. delete with incoming-link warning.

### M17-T03 Page settings

- **Status:** todo
- **Needs:** M17-T01
- **Done when:** D-31 and D-31b states; output in html (meta, social, canonical).

### M17-T04 Project settings: general and screen sizes

- **Status:** todo
- **Needs:** M17-T01
- **Done when:** D-44, D-44b tabs General and Screen sizes (with CSS direction, PLAN.md 7.3).

### M17-T05 Project settings: redirects, site-wide code, export defaults

- **Status:** todo
- **Needs:** M17-T04
- **Done when:** D-44b remaining tabs; redirects written as the host formats chosen in export.

### M17-T06 Import a page

- **Status:** todo
- **Needs:** M17-T01
- **Done when:** D-45: HTML + CSS import into model with a report of unsupported parts; untrusted-input rules (PLAN.md 12.6).
