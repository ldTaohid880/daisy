# @daisy/native

Daisy's C++ core, exposed to the **Electron main process** as a Node-API addon (`daisy_native.node`),
The addon is **required**: no pure-Node fallback (ADRs 0013, 0015).

```
cpp/include/daisy/   C++ core headers (no Node)        cpp/src/       core implementation
cpp/binding/         Node-API binding (C++ classes)     cpp/test/      C++ tests (CTest)
src/                 TypeScript wrapper, loader, DI module and tokens
scripts/build-native.ts   cmake-js build into prebuilds/<platform>-<arch>/
```

**Rules**

- The core (`cpp/src`, `cpp/include`) never includes Node headers; only `cpp/binding` does.
- Every addon function has: a C++ core class with C++ tests, a binding method, an entry in
  `src/DaisyNativeAddon.ts`, a TypeScript service class, and tests against known values. No fallback class.
- A missing or broken addon throws `NativeAddonError`; never catch it to carry on.
- Long work runs on a worker thread (`napi_async_work`, see `HashFileJob`) and returns a Promise.
- Errors: C++ exceptions are converted at the boundary (`NapiBoundary::guard`); argument errors are `TypeError`.
- Main process only. The renderer (sandboxed) never loads this package.
- Node-API only (`NAPI_VERSION=9`), no V8 or Electron internals, so builds survive Electron upgrades.

**Commands:** `pnpm --filter @daisy/native build` · `pnpm --filter @daisy/native test` (builds the addon first; fails
without it) · `pnpm --filter @daisy/native test:cpp` (C++ tests, needs CMake and a compiler).
