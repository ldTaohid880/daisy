# 0014. No Go or standalone C++; C++ only as the Node addon

- **Status:** Accepted
- **Date:** 2026-11-13
- **Supersedes in PLAN.md / UI_DESIGN_PLAN.md:** ADR 0012 (the Go and C++ sidecar parts)

## Context

ADR 0012 allowed Go sidecar tools and standalone C++ programs. ADR 0013 gave C++ a home as a Node-API addon
inside the main process. The owner decided that the addon covers the native needs.

## Decision

- **TypeScript** is the language of the app.
- **C++** is used only inside `packages/native` as the Node-API addon (ADR 0013). No separate executables.
- **Go** is not used. The `go/` and `native/` folders are removed.
- **Python** stays for repository tooling only (`py/`, `design-src/`), never shipped.

## Consequences

One native toolchain (CMake + a C++ compiler) instead of three; fewer CI jobs and nothing extra to sign or ship.
Work that might have been a Go sidecar (image optimisation, a native MCP stdio bridge) becomes either a C++
addon function (no Node fallback, ADR 0015), or plain TypeScript.
