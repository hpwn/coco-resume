import { describe, expect, it } from 'vitest';

import { AiClient } from '../src/index.js';

describe('AiClient', () => {
  it('describes the configured model', () => {
    const client = new AiClient({ model: 'test-model' });
    expect(client.describe()).toContain('test-model');
  });
});
