# @daisy/mcp-server

Daisy's MCP server so AI apps (Claude Code, Cursor…) can read and edit the open project.

**Owns:** Tool and resource definitions, permission policy (Read only / Ask before changes / Change freely), HTTP transport on 127.0.0.1, stdio bridge, change grouping.

**Specification:** UI_DESIGN_PLAN.md Phase I (D-59, D-59b, D-59c); docs/adr/0006-daisy-is-an-mcp-server-changes-go-through-renderer-commands.md

**May import:** @daisy/di, @daisy/model, @daisy/ipc · @modelcontextprotocol/server, @modelcontextprotocol/node, zod. The full graph is in `docs/architecture/dependencies.json` and is checked by `pnpm check:deps`.

**Rules:** Never apply a change directly: every write goes to the renderer as a command and waits for approval per policy. Bind to 127.0.0.1 only.

**Tests:** `pnpm --filter @daisy/mcp-server test`. Test files sit next to the code as `*.test.ts`.
