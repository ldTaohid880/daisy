---
name: daisy-native-addon
description: Add or change a C++ function in Daisy's Node-API addon (@daisy/native) with its core class, binding, TypeScript service and tests. The addon is required; never add a fallback.
---

# Native addon feature (ADRs 0013, 0015)

Read `packages/native/AGENTS.md` first. For one new capability, e.g. "decode image size":

1. **Core class** in `cpp/include/daisy/<Name>.hpp` + `cpp/src/<Name>.cpp`. Plain C++20, RAII, no Node headers,
   throws `std::runtime_error` with a readable message. Add it to `daisy_core` in `cpp/CMakeLists.txt`.
2. **C++ tests** in `cpp/test/` (register with `TestRunner`); run `pnpm --filter @daisy/native test:cpp`.
3. **Binding**: a static method on `DaisyNativeAddon` in `cpp/binding/DaisyNativeAddon.cpp`, wrapped in
   `NapiBoundary::guard`, arguments via `CallbackArgs` + `Napi::to*`. Anything that can take more than ~1 ms
   (files, images) runs as a job class like `HashFileJob` (napi_async_work + Promise).
4. **Types**: add the function to `src/DaisyNativeAddon.ts` exactly as the binding exposes it.
5. **Service**: an interface (`src/<Service>.ts`) and a native class wrapping the addon. Bind it in
   `NativeModule.register` and add a token in `src/tokens.ts`. **No pure-Node fallback** (AGENTS.md 3c).
6. **Tests**: against known values; a Node API may serve as a test oracle only. Never `skipIf` a missing addon:
   the tests must fail without it.
7. Build and test: `pnpm --filter @daisy/native build && pnpm --filter @daisy/native test`.
8. Consumers (project-fs, main-process handlers) inject the service token; they never import the addon directly.
