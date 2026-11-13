# 0010. Preview in an isolated Electron session

- **Status:** Accepted
- **Date:** 2026-11-13
- **Supersedes in PLAN.md / UI_DESIGN_PLAN.md:** PLAN.md 13.4 (mechanism), 19.2 R6/R7.

## Context

PLAN.md 13.4 isolates Preview with an opaque-origin sandboxed iframe in a browser. Electron allows stronger isolation.

## Decision

Preview renders the exported page from a temporary folder through a `daisy-preview://` protocol in a separate session partition with no preload and scripts allowed only after consent for imported code (13.6). The bridge to the editor is a validated postMessage channel.

## Consequences

Scripts in Preview cannot reach the project, the editor or `window.daisy`. Preview matches a hosted page more closely than `data:` assets did (PLAN R7 reduced).
