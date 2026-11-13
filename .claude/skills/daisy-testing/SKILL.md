---
name: daisy-testing
description: Choose and write the right tests for a Daisy change: unit, browser unit, e2e, golden export, fidelity, visual.
---

# Testing

See docs/engineering/TESTING.md for the table. Quick rules:

- Logic in pure packages → Vitest unit next to the file.
- Needs a real CSS engine (computed styles, shorthands) → `*.browser.test.ts` (Chromium via Playwright).
- Gestures, panels, files, preview → Electron e2e in `apps/desktop/e2e`.
- Export output → golden files in `packages/export/src/__golden__` (update with `-u` only when the spec changed).
- Use `@daisy/test-utils` builders and the Halden fixture, not ad-hoc objects.
- Every bug fix: a failing test first.
