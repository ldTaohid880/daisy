# Releasing

## Versions

One app version (`apps/desktop/package.json`), semver. release-please reads Conventional Commit
titles on `main` and keeps a release PR open with the next version and CHANGELOG. Merging it
creates the tag `vX.Y.Z`.

## Pipeline (.github/workflows)

- `ci.yml` — every PR and push to `main`: install (frozen lockfile), format, lint, boundaries,
  typecheck, unit, browser unit, build, e2e (Linux, xvfb), packaging smoke (Windows, macOS, Linux).
- `release-please.yml` — on `main`: maintains the release PR; on release, triggers `release.yml`.
- `release.yml` — on tag `v*`: builds installers on Windows (NSIS x64/arm64), macOS (dmg+zip
  arm64/x64), Linux (AppImage, deb); uploads them and `latest*.yml` update metadata to a **draft**
  GitHub Release. A maintainer checks and publishes it; installed apps then auto-update.
- `nightly.yml` — e2e on all three OSes and performance budgets.
- `codeql.yml` — code scanning; `dependency-review.yml` — licence and vulnerability check on PRs.

## Channels

`latest` (stable) and `beta` (pre-release tags `vX.Y.Z-beta.N`). The app follows the channel the
user chose in Preferences › Privacy and updates.

## Signing (needed before public 1.0 — tasks M00-T06/T07, M24)

- Windows: code-signing certificate (or Azure Trusted Signing) → secrets `CSC_LINK`, `CSC_KEY_PASSWORD`.
- macOS: Apple Developer ID + notarisation → `CSC_LINK` (p12), `APPLE_ID`,
  `APPLE_APP_SPECIFIC_PASSWORD`, `APPLE_TEAM_ID`; then set `notarize: true` in electron-builder.yml.
- Linux: AppImage is unsigned; deb is published as-is.
  Unsigned builds work for testing; Windows SmartScreen and macOS Gatekeeper will warn.

## Manual checklist for a release

1. Release PR merged, tag created, `release.yml` green on three OSes.
2. Install each artifact on a clean machine; open the Halden sample; export; check auto-update from the previous version.
3. Publish the draft release.
