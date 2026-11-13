---
name: daisy-ui-component
description: Build editor chrome (panels, dialogs, bars, popovers) from a UI_DESIGN_PLAN.md board using @daisy/ui tokens and primitives.
---

# UI component from a design board

1. Find the board (daisy-spec-lookup). Note sizes, labels, states, and which states sheet (`D-xxb/c`) applies.
2. Build from `@daisy/ui` primitives; add a primitive there only if two places need it.
3. Styles: CSS Modules + tokens from `packages/ui/src/tokens.css`. No raw colours or pixel values that are not tokens,
   except layout dimensions stated on the board (e.g. popover at 328 wide).
4. Rules from the owner: one control, one place; advanced options in anchored popovers; violet only for states; blue
   accent only for active/selection; truncate sidebar labels with "…"; don't overdo things.
5. Start the component with `// Design: D-xx <name>`.
6. Keyboard and screen readers: Radix primitives for menus, dialogs, popovers; visible focus ring.
7. Verify: a Playwright visual test at the board's size, and the `ui-fidelity-reviewer` subagent against the board.
