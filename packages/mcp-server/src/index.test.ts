import { describe, expect, it } from 'vitest';
import { Container } from '@daisy/di';
import { McpModule, McpTokens, type ClientGrant } from './index.js';

const grant = (access: ClientGrant['access']): ClientGrant => ({
  clientId: 'c',
  name: 'Cursor',
  access,
  reach: 'open-project',
});
const policy = new Container().load(new McpModule()).resolve(McpTokens.AccessPolicy);

describe('AccessPolicy (D-59c)', () => {
  it('always allows reads', () => {
    expect(policy.decide(grant('read'), 'read')).toBe('allow');
  });
  it('refuses writes from read-only apps', () => {
    expect(policy.decide(grant('read'), 'write')).toBe('refuse');
  });
  it('asks before changes by default', () => {
    expect(policy.decide(grant('ask'), 'write')).toBe('ask');
  });
  it('allows writes when the app may change freely', () => {
    expect(policy.decide(grant('free'), 'write')).toBe('allow');
  });
});

describe('McpEndpoint', () => {
  it('listens on loopback only', () => {
    expect(new Container().load(new McpModule()).resolve(McpTokens.Endpoint).url).toBe(
      'http://127.0.0.1:7341/mcp',
    );
  });
});
