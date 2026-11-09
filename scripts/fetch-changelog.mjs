// Copies PlatformIO Core's HISTORY.md into the docs so the Changelog page can
// import it. Uses the parent Core checkout when the docs are its submodule,
// otherwise downloads it from GitHub. Fails the build if neither works.

import {copyFile, writeFile} from 'node:fs/promises';
import {existsSync} from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const ROOT = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const LOCAL = path.join(ROOT, '..', 'HISTORY.md');
const REMOTE =
  'https://raw.githubusercontent.com/platformio/platformio-core/develop/HISTORY.md';
const TARGET = path.join(ROOT, 'docs', 'resources', '_history.md');

if (existsSync(LOCAL)) {
  await copyFile(LOCAL, TARGET);
  console.log(`[changelog] copied ${LOCAL}`);
} else {
  const response = await fetch(REMOTE);
  if (!response.ok) {
    console.error(`[changelog] cannot fetch ${REMOTE}: HTTP ${response.status}`);
    process.exit(1);
  }
  await writeFile(TARGET, await response.text());
  console.log(`[changelog] downloaded ${REMOTE}`);
}
