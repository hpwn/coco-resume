import { describe, expect, it } from 'vitest';

import { createGreeting } from '../src/index.js';

describe('createGreeting', () => {
  it('creates a friendly greeting', () => {
    expect(createGreeting('Developer')).toBe('Hello, Developer!');
  });
});
