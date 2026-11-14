# M00 · Project setup and toolchain

- **Goal:** A green `pnpm check`, CI and a packaged unsigned app on all three OSes before any feature work.
- **Source:** new (not in PLAN.md)
- **Spec:** —
- **Designs:** all repo
- **Packages:** docs/adr/0001–0010
- **Code style:** ADR 0011 — where PLAN.md names functions (`createEmptyDocument`, `generateCss`, `insertNode`…), build them as classes and methods with injected dependencies.

## Acceptance criteria

- `pnpm install && pnpm check` passes on Windows, macOS and Linux.
- CI is green on a PR; `main` is protected.
- `pnpm package` produces an installer that opens the placeholder window and shows its version.
- A tag on a test branch produces a draft GitHub Release with all artifacts.

**Done when:** Any agent can clone, run `pnpm check`, pick M01-T01 and open a PR that CI verifies.

## Tasks

### M00-T01 Install and verify toolchain versions

- **Status:** done
- **Needs:** —
- **Done when:** Run `pnpm install`; fix any range that does not resolve (electron-vite ↔ Vite 8, @vitejs/plugin-react, typescript-eslint ↔ TS 6); commit `pnpm-lock.yaml`; record pins in ADR 0008.
- **Notes:** Two ranges fixed (electron-vite ^6, @modelcontextprotocol/node ^2.1.2); pins in ADR 0008. `pnpm-lock.yaml` is generated; committed in the first commit (e882f63).

### M00-T02 Make `pnpm check` green on all three OSes

- **Status:** done
- **Needs:** M00-T01
- **Done when:** Format, lint, check:deps, typecheck and unit tests pass locally on Windows (owner PC) and in CI on macOS/Linux.
- **Notes:** Green on Windows locally; `pnpm check` passed on Windows, macOS and Linux runners in the release dry run, and the CI check job (Linux) is required on `main`.

### M00-T03 Run the app and the first e2e test

- **Status:** done
- **Needs:** M00-T01
- **Done when:** `pnpm dev` opens the window; `pnpm build && pnpm test:e2e` passes `launch.spec.ts`.
- **Notes:** Verified on Windows: window opens and shows "Version 0.1.0"; `launch.spec.ts` passes. Fixed the preload being externalised by electron-vite 6 and the e2e launch path. The native addon is required (ADR 0015).

### M00-T04 Create the GitHub repository and protect main

- **Status:** done
- **Needs:** M00-T02
- **Done when:** Public repo `daisy`; replace OWNER_PLACEHOLDER in electron-builder.yml and CODEOWNERS; branch protection: PR required, CI required, squash only; enable private vulnerability reporting, Dependabot, CodeQL.
- **Notes:** Public repo https://github.com/ldTaohid880/daisy. Owner set in electron-builder.yml and CODEOWNERS. `main` protected: PR required (0 approvals, solo maintainer), all CI jobs + PR title required, strict up-to-date, linear history, conversation resolution, no force push or delete, enforced for admins. Squash merge only (title = PR title), branches deleted on merge. Private vulnerability reporting, Dependabot alerts and security fixes on; Dependabot version updates and CodeQL run from `.github/`.

### M00-T05 First CI run and release dry run

- **Status:** done
- **Needs:** M00-T04
- **Done when:** CI green on a PR; push tag `v0.1.0-alpha.0` from a branch → draft release with Windows, macOS and Linux artifacts; delete it afterwards.
- **Notes:** CI green on PR #6. Tag `v0.1.0-alpha.0` from a branch (version set to 0.1.0-alpha.0) produced a draft release with Windows NSIS x64/arm64, macOS dmg+zip arm64/x64, Linux AppImage+deb and `latest*.yml`; deleted afterwards. Fixes: release fails when the tag does not match the app version; empty signing secrets are unset (macOS read an empty `CSC_LINK` as a path).

### M00-T06 App icon and product identity

- **Status:** todo
- **Needs:** —
- **Done when:** Icons in apps/desktop/build (ico, icns, png) from the Daisy mark on the design canvas; appId confirmed.

### M00-T07 Signing accounts (can run in parallel with M01+)

- **Status:** todo
- **Needs:** M00-T05
- **Done when:** Decide Windows signing (certificate or Azure Trusted Signing) and Apple Developer ID; store secrets; enable notarisation. Not blocking alpha.

### M00-T08 Electron Fuses and packaging hardening

- **Status:** done
- **Needs:** M00-T03
- **Done when:** Add @electron/fuses in an afterPack hook (docs/architecture/SECURITY.md list); verify the packaged app still starts.
- **Notes:** Used electron-builder's built-in `electronFuses` instead of an `@electron/fuses` afterPack hook (same library, no new dependency, correct order with signing). Verified on a Windows x64 package: fuses read back as set; the app starts, shows its version and loads the native addon. Playwright cannot attach to a fused build (inspect is off), so the check uses Chromium's remote-debugging port.

### M00-T09 Add PLAN.md pointers to superseding ADRs

- **Status:** done
- **Needs:** —
- **Done when:** PLAN.md 12.2, 15, 16 and 19.1 carry a one-line note pointing to ADRs 0001–0005 and 0010.
