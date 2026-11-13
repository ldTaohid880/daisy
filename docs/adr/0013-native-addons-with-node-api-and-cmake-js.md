# 0013. Native addons with Node-API and cmake-js

- **Status:** Accepted; the pure-Node fallback is superseded by [ADR 0015](0015-no-fallbacks-the-native-addon-is-required.md)
- **Date:** 2026-11-13
- **Supersedes in PLAN.md / UI_DESIGN_PLAN.md:** refines ADR 0012 for C++ inside the app.

## Context

The owner wants C++ integrated as Node addons. Addons run in the Electron main process; the renderer is
sandboxed and must never load native code. Electron updates every few months, and addons built against V8 or
Electron internals must be rebuilt for each version.

## Decision

- One package, `@daisy/native`: C++ core in `cpp/src` + `cpp/include` (no Node headers), a binding in
  `cpp/binding` written against **Node-API** (C API, `NAPI_VERSION=9`) through small C++ helper classes, and a
  TypeScript wrapper in `src/`. Node-API is ABI-stable, so a build keeps working across Electron upgrades.
- Built with **CMake via cmake-js** (`scripts/build-native.ts`) into `prebuilds/<platform>-<arch>/daisy_native.node`.
  macOS builds one universal binary; Windows builds x64 and arm64 in release CI.
- Packaged with electron-builder `extraResources` into `resources/native/`; loaded by `NativeAddonLoader`.
- ~~**Every native service has a pure-Node fallback**~~ (superseded by ADR 0015: the addon is required) with the same interface and a parity test, chosen in
  `NativeModule`. A missing or broken addon never stops Daisy from starting.
- First service: `ContentHasher` (SHA-256 of assets, streaming file hashing on a worker thread). It proves the
  whole pipeline; the performance gain over `node:crypto` is small, and that is acceptable for a pilot.
- No third-party C++ dependencies yet; C++ tests use a small in-repo runner with CTest.

## Consequences

~~Contributors without CMake can still build and run Daisy (the build script skips the addon and the fallback is
used); release CI sets `DAISY_NATIVE_REQUIRED=1`.~~ (superseded by ADR 0015) Adding a native feature costs a C++ class, a binding method,
a TS class, a fallback and tests. node-addon-api can be adopted later if the binding grows; the core would not change.
