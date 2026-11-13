# Coding standards

- **Classes first (ADR 0011).** All logic is in classes; no module-level functions in `.ts` files (ESLint). Use
  `#private` fields, `readonly` where possible, constructor injection via `static readonly inject`, tokens in
  `tokens.ts`, registrations in an `XModule` class. Static methods for stateless helpers. Only React components
  and hooks are functions.
- One class per file, file named after the class (`AccessPolicy.ts`).
- TypeScript strict, `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`. No `any`, no non-null `!` outside tests.
- ES modules everywhere; imports use `.js` extensions for local files and `import type` for types.
- Pure packages hold side-effect-free classes. Side effects live at the edges (stores, renderer, main process).
- C++ (only in `packages/native`) follows `.clang-format`, C++20, classes and RAII; Python tooling in `py/` uses ruff. Classes first in both (ADR 0014).
- Names follow the vocabulary in UI_DESIGN_PLAN.md 6.4 and PLAN.md 3.7 in UI text; code uses CSS names (`padding`, not "space inside").
- One component per file in `editor`/`ui`; each screen-level component starts with a comment naming its design board (`// Design: D-31 Page settings`).
- Styling: CSS Modules + tokens from `packages/ui/src/tokens.css`. No inline colours, no utility CSS.
- Errors: throw `DaisyError` subclasses with a user-facing message key; never show stack traces in UI.
- Comments explain why, not what. Link spec sections (`// PLAN.md 9.6`).
- Every command class in `model` has an inverse test that applies and undoes it.
- No new dependency without a line in the PR explaining why the platform or existing deps are not enough; licences must be MIT-compatible.
