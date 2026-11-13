# 0004. GitHub Actions for CI/CD; GitHub Releases for distribution

- **Status:** Accepted
- **Date:** 2026-11-13
- **Supersedes in PLAN.md / UI_DESIGN_PLAN.md:** PLAN.md 16 "No CI … appear anywhere in this roadmap".

## Context

The owner chose GitHub. Releases must build on Windows, macOS and Linux. PLAN.md 16 said no CI until there was more than one contributor; with agents there are many.

## Decision

CI on every PR (format, lint, boundaries, types, unit, browser unit, e2e, packaging smoke on three OSes). release-please opens release PRs from Conventional Commits; a tag builds installers with electron-builder and publishes a draft GitHub Release; electron-updater updates installed apps from it.

## Consequences

Free for public repos. Signing certificates (Windows) and Apple notarisation are needed before public 1.0; the pipeline works unsigned until then.
