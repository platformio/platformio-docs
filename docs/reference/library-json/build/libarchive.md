---
description: "Create an archive (*.a, static library) from the object files and link it into a firmware (program)."
---

# `libArchive`

- **Required:** No
- **Type:** Boolean

Create an archive (`*.a`, static library) from the object files and link it into a firmware (program). This is default behavior of PlatformIO Build System (`"libArchive": true`).

Setting `"libArchive": false` will instruct PlatformIO Build System to link object files directly (in-line). This could be useful if you need to override `weak` symbols defined in framework or other libraries.

You can disable library archiving globally using [lib_archive](../../platformio-ini/env/lib-archive.md) option in [`platformio.ini`](../../platformio-ini/index.md).
