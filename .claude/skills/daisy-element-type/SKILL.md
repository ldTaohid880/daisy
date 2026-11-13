---
name: daisy-element-type
description: Add an HTML element type to the element registry with nesting rules, defaults, HTML output and accessibility checks.
---

# Element type

Spec: PLAN.md 8.1–8.4, 14.2.

1. Definition in `packages/model/src/registry/elements/<category>.ts`: tag, label, icon, default styles (real CSS,
   visible starting size — PLAN D12), `canContain`, attributes allowed.
2. HTML output rule in `packages/html` if it differs from the default.
3. Accessibility checks in `packages/model/src/a11y` if the element needs any.
4. Tests: canContain table row; html-validate on export; the element appears in Elements panel search.
