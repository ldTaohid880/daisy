import type { Container, Module } from '@daisy/di';
import { AccessPolicy } from './AccessPolicy.js';
import { McpEndpoint } from './McpEndpoint.js';
import { McpTokens } from './tokens.js';

export class McpModule implements Module {
  register(container: Container): void {
    container
      .bindClass(McpTokens.AccessPolicy, AccessPolicy)
      .bindValue(McpTokens.Endpoint, new McpEndpoint());
  }
}
