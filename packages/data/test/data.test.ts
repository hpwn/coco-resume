import { describe, expect, it } from 'vitest';

import { createResumeSection } from '../src/index.js';

describe('createResumeSection', () => {
  it('creates a resume section object', () => {
    const section = createResumeSection('intro', 'Introduction', 'Hello!');
    expect(section).toEqual({ id: 'intro', title: 'Introduction', content: 'Hello!' });
  });
});
