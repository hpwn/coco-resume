import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import { defineConfig } from 'vitest/config';

const rootDir = dirname(fileURLToPath(import.meta.url));

const packageAlias = ['core', 'ai', 'export', 'data'].reduce<Record<string, string>>((aliases, name) => {
  aliases[`@coco-resume/${name}`] = resolve(rootDir, `packages/${name}/src/index.ts`);
  return aliases;
}, {});

export default defineConfig({
  resolve: {
    alias: packageAlias,
  },
  test: {
    environment: 'node',
    globals: true,
    coverage: {
      enabled: false,
    },
  },
});
