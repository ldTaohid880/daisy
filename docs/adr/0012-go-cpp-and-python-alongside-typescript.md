# 0012. Go, C++ and Python alongside TypeScript

- **Status:** Superseded in part by ADR 0014 (no Go, no C++ sidecars) and refined by ADR 0013
- **Date:** 2026-11-13
- **Supersedes in PLAN.md / UI_DESIGN_PLAN.md:** —

## Context

The owner welcomes other languages, mainly Go and C++, and Python.

## Decision

TypeScript stays the main language for the app. Go builds standalone sidecar tools (`go/`, stdio JSON lines). C++ builds Node-API addons or sidecars for main-process hot paths (`native/`, cmake-js, Electron ABI). Python is for repository tooling only (`py/`), not shipped. Each component sits behind a TypeScript class bound to a DI token, speaks a versioned schema, has tests in its own language, and runs in CI (`polyglot.yml`); release builds compile Go/C++ per OS and arch. Classes, or types with methods, come first in every language.

## Consequences

The right tool for heavy work (image processing, hashing, large exports) without leaking native code into the renderer. Each language adds a CI job and toolchain setup, so a new component needs a reason in its PR.
