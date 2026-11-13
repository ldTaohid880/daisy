# 0001. Desktop app on Electron

- **Status:** Accepted
- **Date:** 2026-11-13
- **Supersedes in PLAN.md / UI_DESIGN_PLAN.md:** PLAN.md 15 "Backend: none / static site" and 19.1 D17 (stack, partly), 19.2 R1 (Safari) becomes low priority.

## Context

Daisy edits project folders on disk, runs a local MCP server and must render the canvas with exactly the engine that will preview the export. PLAN.md 15 planned a static web app.

## Decision

Build Daisy as an Electron app (currently Electron 45, Chromium 156, Node 24). The editor UI stays web technology (React + TypeScript + Vite), so PLAN.md chapters 3–14 apply unchanged.

## Consequences

Same Chromium on Windows, macOS and Linux: canvas fidelity does not vary by OS. Node in the main process gives real files and the MCP server. Larger installers (~100 MB) and the duty to follow Electron's security checklist (docs/architecture/SECURITY.md). Tauri was rejected because it uses the OS web engine (WebKit on macOS).
