/** Where the server listens. Loopback only (docs/architecture/SECURITY.md). */
export class McpEndpoint {
  static readonly host = '127.0.0.1';
  static readonly defaultPort = 7341;

  readonly port: number;

  constructor(port: number = McpEndpoint.defaultPort) {
    this.port = port;
  }

  get url(): string {
    return `http://${McpEndpoint.host}:${String(this.port)}/mcp`;
  }
}
