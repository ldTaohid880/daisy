import { Token } from '@daisy/di';
import type { AccessPolicy } from './AccessPolicy.js';
import type { McpEndpoint } from './McpEndpoint.js';

export const McpTokens = {
  AccessPolicy: new Token<AccessPolicy>('mcp.AccessPolicy'),
  Endpoint: new Token<McpEndpoint>('mcp.Endpoint'),
} as const;
