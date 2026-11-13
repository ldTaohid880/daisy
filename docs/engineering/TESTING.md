# Testing

From PLAN.md 17, adapted to the monorepo.

| Layer                                            | Where                                    | Command                                                                 | When                                    |
| ------------------------------------------------ | ---------------------------------------- | ----------------------------------------------------------------------- | --------------------------------------- |
| Unit                                             | `packages/*/src/**/*.test.ts`            | `pnpm test`                                                             | every change (CI on every PR)           |
| Browser unit (real Chromium CSS engine)          | `*.browser.test.ts` in `css`, `renderer` | `pnpm test:browser`                                                     | every PR                                |
| End-to-end (Electron + Playwright)               | `apps/desktop/e2e`                       | `pnpm build && pnpm test:e2e`                                           | every PR on Linux; nightly on all OSes  |
| C++ core (CTest)                                 | `packages/native/cpp/test`               | `pnpm --filter @daisy/native test:cpp`                                  | every PR touching `packages/native/cpp` |
| Native ↔ Node parity                             | `packages/native/src/*.test.ts`          | `pnpm --filter @daisy/native build && pnpm --filter @daisy/native test` | every PR on three OSes                  |
| Golden export files                              | `packages/export/src/__golden__`         | part of unit                                                            | every PR                                |
| Fidelity harness (canvas = export within 0.5 px) | `apps/desktop/e2e/fidelity`              | part of e2e                                                             | from M10 on, every PR                   |
| Visual (screenshots vs design boards)            | `apps/desktop/e2e/visual`                | `pnpm test:e2e --grep @visual`                                          | UI tasks                                |
| Performance budgets (PLAN.md 9.11)               | `apps/desktop/e2e/perf`                  | nightly                                                                 | from M18 on                             |

Rules

- **A visual edit is tested by its exported code**: gestures assert on the model and on the generated HTML/CSS.
- Every command: result test + inverse test. Property-based sequence test for invariants (fast-check) from M02.
- Every schema version: a fixture saved in the previous version and a migration test.
- Every bug fix starts with a failing test.
- Acceptance tests A1–A12 (PLAN.md 17.3) live in `apps/desktop/e2e/acceptance` and must all pass before 1.0.
- Use the Halden sample project from `@daisy/test-utils` for realistic fixtures.
