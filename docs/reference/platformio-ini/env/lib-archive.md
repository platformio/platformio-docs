---
description: "Create an archive (`*.a`, static library) from the object files and link it into a firmware (program) (platformio.ini option lib_archive)."
---

# `lib_archive`

- **Type:** Boolean: `yes` or `no`
- **Multiple values:** No
- **Default:** `yes`

Create an archive (`*.a`, static library) from the object files and link it into a firmware (program). This is default behavior of PlatformIO Build System (`lib_archive = yes`).

Setting `lib_archive = no` will instruct PlatformIO Build System to link object files directly (in-line). This could be useful if you need to override `weak` symbols defined in framework or other libraries.

You can disable library archiving per a custom library using [libArchive](../../library-json/build/libarchive.md) field in [library.json](../../library-json/index.md) manifest.

## Example

```ini
[env:myenv]
lib_archive = no
```
