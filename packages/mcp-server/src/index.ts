/**
 * @daisy/mcp-server — Daisy as an MCP server (UI_DESIGN_PLAN.md Phase I, ADR 0006).
 * The server never edits the document: writes become change requests the renderer applies
 * through commands, after the access policy (and the user, when asked) allows them.
 */
export { AccessPolicy, type AccessLevel, type ClientGrant, type Decision } from './AccessPolicy.js';
export { McpEndpoint } from './McpEndpoint.js';
export { McpModule } from './McpModule.js';
export { McpTokens } from './tokens.js';
