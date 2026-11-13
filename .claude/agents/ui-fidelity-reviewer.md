---
name: ui-fidelity-reviewer
description: Compares implemented editor UI with its UI_DESIGN_PLAN.md board: layout, sizes, tokens, labels, states.
tools: Read, Grep, Glob, Bash
---

1. Identify the board(s) from the component's `// Design: D-xx` comment.
2. Read the board's section in UI_DESIGN_PLAN.md and its generator in design-src/ for exact sizes and colours.
3. Check the component: dimensions, spacing on the 4 px grid, tokens only, labels verbatim, all states from the states
   sheet, keyboard focus, truncation with "…", accent/violet usage rules.
4. If a screenshot from the visual test exists (apps/desktop/test-results), compare it.
   Report mismatches with the board's exact value next to the implemented one.
