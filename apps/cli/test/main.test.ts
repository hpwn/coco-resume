import { describe, expect, it } from 'vitest';

import { main } from '../src/index.js';

describe('main', () => {
  it('returns a greeting for the provided name', () => {
    expect(main(['node', 'cli', 'Ada'])).toBe('Hello, Ada!');
  });

  it('defaults to world when no name is provided', () => {
    expect(main(['node', 'cli'])).toBe('Hello, world!');
  });
});
