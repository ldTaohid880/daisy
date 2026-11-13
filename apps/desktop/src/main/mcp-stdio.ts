/**
 * Entry AI apps start for MCP over stdio ("Local app (stdio)" in D-59). It forwards to the running
 * Daisy app on 127.0.0.1 so every request passes the same policy and approvals. Task M21-T08.
 */
class McpStdioBridge {
  run(): never {
    console.error(
      'Daisy MCP stdio bridge: not implemented yet (docs/tasks/M21-mcp-server-for-ai-apps.md, M21-T08).',
    );
    process.exit(1);
  }
}

new McpStdioBridge().run();
