# Security design

Daisy shows untrusted HTML, CSS and scripts (imported pages, `.daisy` files, custom code) and
exposes an MCP server. These are the layers; changing any of them needs an ADR.

## Electron shell

- `contextIsolation: true`, `sandbox: true`, `nodeIntegration: false`, `webSecurity: true` for every window.
- One preload exposing `window.daisy` built from `@daisy/ipc`; no `ipcRenderer` or Node reaches the page.
- CSP on the editor page (`apps/desktop/src/renderer/index.html`): no remote scripts, no `eval`.
- Navigation and `window.open` are blocked; http(s) links open in the system browser.
- All permission requests are denied by default.
- Electron is kept on a supported major (latest three); Dependabot raises updates weekly.
- Electron Fuses are set at packaging time: disable `RunAsNode`, `EnableNodeOptionsEnvironmentVariable`, `EnableNodeCliInspectArguments`; enable `OnlyLoadAppFromAsar` and cookie encryption (task M00-T08).

## Edit frame (PLAN.md 13.3)

Sandboxed iframe without `allow-scripts`, allow-list renderer (only registry elements and safe
attributes), CSP `script-src 'none'`, sanitised HTML blocks (DOMPurify). Tests in PLAN.md 17.2.

## Preview frame (PLAN.md 13.4, ADR 0010)

Runs the exported page in its own session partition (`persist:false`, no preload, no Node),
served from a custom `daisy-preview://` protocol rooted at a temporary export, with
`allow-scripts` but an opaque origin. It cannot reach `window.daisy`, the project folder, or the
editor's storage. Messages to the editor go through a validated bridge only.

## Files

The main process only reads and writes inside the open project folder, folders the user picked in
a native dialog, and Daisy's own app-data folder. Every path from the renderer is resolved and
checked against those roots.

## MCP server (UI_DESIGN_PLAN.md Phase I, ADR 0006)

Off by default. Listens on `127.0.0.1` only, with a per-install token in the client config and an
`Origin`/`Host` check (DNS-rebinding defence). Access levels Read only / Ask before changes /
Change freely; reads never include files outside the project. Writes are commands applied by the
renderer, grouped as one undo step, and logged in History.

## Updates

electron-updater from GitHub Releases over HTTPS, with signature checks on Windows and macOS once
signing certificates exist (docs/engineering/RELEASING.md).
