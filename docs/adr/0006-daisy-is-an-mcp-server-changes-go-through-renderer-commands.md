# 0006. Daisy is an MCP server; changes go through renderer commands

- **Status:** Accepted
- **Date:** 2026-11-13
- **Supersedes in PLAN.md / UI_DESIGN_PLAN.md:** —

## Context

UI_DESIGN_PLAN.md Phase I: AI apps (Claude Code, Cursor) read and edit the open project with access levels and approvals.

## Decision

`@daisy/mcp-server` runs in the main process on 127.0.0.1 (Streamable HTTP, MCP TypeScript SDK v2) with a stdio bridge. Reads come from the latest snapshot; writes become change requests the renderer applies via `store.run`, after the policy and, when needed, the user's approval (D-59b). One request = one undo step.

## Consequences

The document keeps one writer (the renderer), so undo, autosave and the canvas stay correct. MCP client support and backend services are deferred.
