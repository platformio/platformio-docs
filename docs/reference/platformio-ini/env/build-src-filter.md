---
description: "Control which source files from the `src` folder should be included/excluded from a build process (platformio.ini option build_src_filter)."
---

<a id="projectconf-build-src-filter"></a>

# `build_src_filter` {#build-src-filter}

- **Type:** String
- **Multiple values:** Yes
- **Default:** `+<*> -<.git/> -<.svn/>`
- **Environment variable:** [`PLATFORMIO_BUILD_SRC_FILTER`](../../environment-variables.md#envvar-PLATFORMIO_BUILD_SRC_FILTER), appended to the values in `platformio.ini`
- **Deprecated name:** `src_filter` (still accepted, with a warning)

This option allows one to specify which source files should be included or excluded from [src_dir](../platformio/src-dir.md) for a build process. Filter supports two templates:

- `+<PATH>` include template
- `-<PATH>` exclude template

`PATH` is relative to [src_dir](../platformio/src-dir.md). All patterns will be applied in their order of definition. [GLOB Patterns](http://en.wikipedia.org/wiki/Glob_%28programming%29) are allowed.

By default, `build_src_filter` is predefined to `+<*> -<.git/> -<.svn/>`, meaning "include ALL files, then exclude the `.git` and `.svn` repository folders.

## Example

Include all `.c` and `.cpp` files recursively (`**` means ANY path) to the build process but exclude assembly files `.S` and `.asm`:

```ini
[env:myenv]
build_src_filter =
  +<**/*.c>
  +<**/*.cpp>
  -<**/*.S>
  -<**/*.asm>
```
