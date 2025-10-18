#!/usr/bin/env node
import { fileURLToPath } from 'node:url';

import { createGreeting } from '@coco-resume/core';

export function main(argv: string[] = process.argv): string {
  const [, , name] = argv;
  const target = name ?? 'world';
  const message = createGreeting(target);
  if (isCliEntry(import.meta.url, argv)) {
    // eslint-disable-next-line no-console
    console.log(message);
  }
  return message;
}

function isCliEntry(entryUrl: string, argv: string[]): boolean {
  if (argv.length === 0) {
    return false;
  }
  const executedFile = argv[1];
  return executedFile === fileURLToPath(entryUrl);
}

if (isCliEntry(import.meta.url, process.argv)) {
  main();
}
