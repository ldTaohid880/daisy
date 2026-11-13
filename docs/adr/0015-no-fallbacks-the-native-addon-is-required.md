# 0015. No fallbacks; the native addon is required

- **Status:** Accepted
- **Date:** 2026-11-13
- **Supersedes in PLAN.md / UI_DESIGN_PLAN.md:** the pure-Node fallback in ADR 0013 and ADR 0014; any
  fallback described in PLAN.md is not approved until the owner confirms it (AGENTS.md 3c).

## Context

ADR 0013 gave every native service a pure-Node fallback, chosen silently when the addon was missing, and let
the addon build skip itself without CMake. The owner's rule is: no fallback unless the owner asks for one by
name. If something does not work, the app breaks, so the failure is seen and fixed instead of hidden.

## Decision

- Daisy's code never degrades silently. Failures throw; there is no skip-and-warn, no alternative
  implementation and no default that hides an error. Recorded as AGENTS.md section 3c.
- `@daisy/native` is required. `NativeAddonLoader` throws `NativeAddonError` when `daisy_native.node` is
  missing or fails to load, so the main process does not start. `NodeCryptoContentHasher` is removed.
- `scripts/build-native.ts` exits 1 without CMake or a compiler; `DAISY_NATIVE_REQUIRED` is gone because
  the addon is always required.
- `app.info` reports `nativeVersion` (the addon's version) instead of `nativeCore: 'native' | 'fallback'`.
- Turbo runs `@daisy/native#build` before `@daisy/native#test`; the tests fail if the addon is missing.
- If `start()` in the main process rejects, the app logs the error and exits with code 1.
- Fallbacks that are features of the **generated website** and are in the approved spec (font fallback
  stacks, WebP with a fallback image) are not affected.

## Consequences

Every contributor and every CI job needs CMake and a C++ compiler (GitHub's Windows, macOS and Ubuntu runners
have them). A platform without a prebuild cannot run Daisy until the addon builds there. Each native feature
costs a C++ class, a binding method, a TS class and tests, with no second implementation. Tests may still use
`node:crypto` as an oracle to check the C++ output; Daisy itself never does.
