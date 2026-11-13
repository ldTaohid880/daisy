---
name: daisy-property-group
description: Add a Properties panel group or control through the properties registry, reading and writing real CSS declarations.
---

# Property group

Spec: PLAN.md 6 (architecture 6.1, adapting 6.2, the group in 6.4), UI_DESIGN_PLAN.md 5 and the group's board.

1. Registry entry in `packages/model/src/registry/properties/<group>.ts`: CSS longhands it owns, when it shows, summary text.
2. Control in `packages/editor/src/panels/properties/<group>/`: an adapter class (`<Group>Adapter`) reading and writing declarations, plus a thin React view; unknown or
   `var()` values show as "custom" and are never rewritten (PLAN R5).
3. Advanced options open as the anchored popover (328 wide, Pin and Close) — reuse `ui/Popover`.
4. Colours: blue accent for focus/selection only; no rainbow labels.
5. Tests: adapter round-trips (parse → control value → declarations) in unit tests; one e2e editing the value and
   checking the export.
