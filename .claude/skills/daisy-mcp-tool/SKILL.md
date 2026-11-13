---
name: daisy-mcp-tool
description: Add a tool or resource to Daisy's MCP server, mapped to model commands, with access policy and approval behaviour.
---

# MCP tool

Spec: UI_DESIGN_PLAN.md Phase I (D-59, D-59b, D-59c), ADR 0006, docs/architecture/MCP.md (written in M21-T01).

1. Declare in `packages/mcp-server/src/tools/<Name>Tool.ts`, a class implementing `McpTool` with an input schema (Zod),
   `kind: 'read' | 'write'`, and a description written for an AI client (what it does, limits); register it in `McpModule`.
2. Reads use the latest snapshot. Writes produce a ChangeRequest (list of model commands + human summary per change,
   e.g. "Hero heading · text"); never mutate anything in the main process.
3. Policy: the injected `AccessPolicy.decide(grant, kind)`; read-only refusal message; tools that would send data out of Daisy always ask.
4. Tests: policy unit test; e2e with an MCP client script (M21-T09 harness).
