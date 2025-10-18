import { describe, expect, it } from 'vitest';

import { isFormatSupported, listSupportedFormats } from '../src/index.js';

describe('export package', () => {
  it('lists supported formats', () => {
    expect(listSupportedFormats()).toEqual(['pdf', 'html']);
  });

  it('detects supported formats', () => {
    expect(isFormatSupported('pdf')).toBe(true);
    expect(isFormatSupported('txt')).toBe(false);
  });
});
