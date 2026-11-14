# M21 · MCP server for AI apps

- **Goal:** AI apps such as Claude Code and Cursor can read and edit the open project through Daisy's MCP server, with access levels and approvals.
- **Source:** new (not in PLAN.md)
- **Spec:** UI_DESIGN_PLAN.md Phase I; ADR 0006
- **Designs:** D-59, D-59b, D-59c
- **Packages:** mcp-server, ipc, editor, desktop
- **Code style:** ADR 0011 — where PLAN.md names functions (`createEmptyDocument`, `generateCss`, `insertNode`…), build them as classes and methods with injected dependencies.

## Acceptance criteria

- Turning the server on in Preferences (D-59) starts it on 127.0.0.1; copied settings work in Claude Code, Cursor and VS Code.
- Read only apps are refused writes and the user is told once (D-59c).
- "Ask before changes" shows the request popover; allowed changes are one undo step named after the app (D-59b).
- An app that stops mid-task leaves each change whole or not started (D-59c).
- History lists app steps and reads.

**Done when:** From Claude Code a user can ask "make the Home hero warmer", approve the three changes in Daisy, and undo them with one Ctrl Z.

## Tasks

### M21-T01 MCP tool and resource design

- **Status:** todo
- **Needs:** M06
- **Done when:** Write docs/architecture/MCP.md: resources (project, pages, selection, design system), read tools (get_page, find_elements, get_styles), write tools (set_text, set_styles, insert_element, move, delete, apply_token), all mapped to model commands.

### M21-T02 Server on 127.0.0.1 with token and origin checks

- **Status:** todo
- **Needs:** M21-T01
- **Done when:** Streamable HTTP via MCP SDK v2; per-install token; Host/Origin validation; start/stop from main.

### M21-T03 Change requests through the renderer

- **Status:** todo
- **Needs:** M21-T02
- **Done when:** IPC mcp.request → renderer validates, applies in one transaction or none; results back.

### M21-T04 Access policy and grants

- **Status:** todo
- **Needs:** M21-T03
- **Done when:** Read only / Ask before changes / Change freely; reach; first-connection request (D-59c).

### M21-T05 Preferences › AI tools and MCP

- **Status:** todo
- **Needs:** M20
- **Done when:** D-59: switch, address, quick setup copy for Claude Code / Cursor / VS Code / JSON, connected apps list.

### M21-T06 Live activity and approvals

- **Status:** todo
- **Needs:** M21-T04
- **Done when:** D-59b: top-bar chip with Pause/Stop, canvas outline and Was/Now card, request popover.

### M21-T07 History and interrupted tasks

- **Status:** todo
- **Needs:** M21-T06
- **Done when:** D-59c: app steps in History, reads listed, stop mid-task handling.

### M21-T08 stdio bridge

- **Status:** todo
- **Needs:** M21-T02
- **Done when:** `mcp-stdio` entry forwards stdio to the running app; included in the package; quick-setup "Local app (stdio)".
- **Constraint:** the packaged app has the `RunAsNode` fuse off (M00-T08), so the bridge cannot run as `Daisy --` with `ELECTRON_RUN_AS_NODE`. Pick another launch (e.g. a Daisy command-line switch handled by the main process, or a utility process) and record it in an ADR.

### M21-T09 MCP end-to-end tests

- **Status:** todo
- **Needs:** M21-T07
- **Done when:** Playwright drives Daisy while an MCP client script calls tools; asserts approvals, undo grouping, refusal.
