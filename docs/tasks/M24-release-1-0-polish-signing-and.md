# M24 · Release 1.0: polish, signing and distribution

- **Goal:** Consistency, clarity and correctness across the whole product.
- **Source:** PLAN.md §16 Milestone 19
- **Spec:** PLAN.md 19; docs/engineering/RELEASING.md
- **Designs:** all boards
- **Packages:** all
- **Code style:** ADR 0011 — where PLAN.md names functions (`createEmptyDocument`, `generateCss`, `insertNode`…), build them as classes and methods with injected dependencies.

**Implementation notes:** Review passes against the vocabulary table (3.7), the disclosure pattern (2.1), and the design standards (4.1). Cross-browser test pass. Error boundaries. Offline support through a simple cache-first service worker for the app shell.

## Acceptance criteria

- No interface string contradicts the vocabulary table.
- Every tool and group passes the progressive-complexity check: usable with defaults; advanced reachable in place; nothing set is invisible.
- The three end-to-end reference pages (17.3) can be rebuilt from an empty document and export identically to their stored expected output.
- Daisy loads and edits offline after the first visit.

**Done when:** A new user can open Daisy for the first time and produce and export a complete, responsive page unaided, and a professional can do the same using advanced CSS, without either encountering an inconsistency or a dead end.

## Tasks

### M24-T01 Audit every label, tooltip and message against the vocabulary table; fix inconsistencies.

- **Status:** todo

### M24-T02 Audit every group and tool for the simple/advanced split and the "advanced value set" dot.

- **Status:** todo

### M24-T03 Complete first-use inline explanations and their dismissal.

- **Status:** todo

### M24-T04 Complete empty states for every panel.

- **Status:** todo

### M24-T05 Add error boundaries around panels and the canvas with "copy details" and non-destructive recovery.

- **Status:** todo

### M24-T06 Finish the light theme; verify visual standards (no stray radii, shadows or decorative colour).

- **Status:** todo

### M24-T07 Full shortcut audit for conflicts with Windows, macOS and Linux and with Electron reserved accelerators.

- **Status:** todo

### M24-T08 Cross-platform pass on Windows, macOS and Linux (fonts, DPI, file dialogs, menus); resolve differences or document them.

- **Status:** todo

### M24-T09 Signed installers, macOS notarisation, and auto-update from the previous release verified on all three OSes (docs/engineering/RELEASING.md).

- **Status:** todo

### M24-T10 Run the full acceptance suite (chapter 17) and the end-to-end "build a real page" scripts.

- **Status:** todo

### M24-T11 Write the in-app keyboard reference and a one-page "How Daisy maps to HTML and CSS" help page.

- **Status:** todo

### M24-T12 Download page

- **Status:** todo
- **Needs:** M24-T09
- **Done when:** A GitHub Pages site (`docs-site/`) with what Daisy is, screenshots and links to the latest release per OS, deployed by a workflow.
