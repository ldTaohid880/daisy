import { describe, expect, it } from 'vitest';
import { SchemaInfo } from './index.js';

describe('SchemaInfo', () => {
  it('starts at schema version 1', () => {
    expect(SchemaInfo.current).toBe(1);
  });
});
