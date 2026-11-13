---
name: daisy-spec-lookup
description: Find the exact PLAN.md / UI_DESIGN_PLAN.md sections, ADRs and design boards for a Daisy task before writing code.
---

# Spec lookup

1. Read the task entry and its milestone header in `docs/tasks/Mxx-*.md` (Spec, Designs).
2. Open each listed section. Headings are numbered: `grep -n "^### 9.6" PLAN.md`, `grep -n "D-31" UI_DESIGN_PLAN.md`.
3. Check `docs/adr/` for anything that supersedes those sections (each ADR lists what it supersedes).
4. Designs: every board is described in UI_DESIGN_PLAN.md under its code (D-xx) with exact sizes, labels and states. The
   canvas map in UI_DESIGN_PLAN.md 11 tells you the row. The generator scripts in `design-src/` contain the exact markup
   and token values of each board (`design-src/d31.py` for D-31) — read them when a measurement is unclear.
5. Vocabulary: UI_DESIGN_PLAN.md 6.4 for labels shown to users.
6. Write a short "Spec" section in your PR description quoting section numbers (not long passages).

If the spec is silent or contradictory: stop and ask, or propose the change to the document in the same PR.
