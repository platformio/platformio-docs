---
description: "Configure a list of target files or directories for checking (platformio.ini option check_src_filters)."
---

:::info

Added in version 6.1.7.

:::

# `check_src_filters` {#check-src-filters}

- **Type:** String
- **Multiple values:** Yes
- **Deprecated name:** `check_patterns` (still accepted, with a warning)

This option allows one to specify which files should be included or excluded from the check process. The filter supports two templates:

- `+<PATH>` include template
- `-<PATH>` exclude template

`PATH` is relative to [src_dir](../platformio/src-dir.md). All patterns will be applied in their order of definition. [GLOB Patterns](http://en.wikipedia.org/wiki/Glob_%28programming%29) are allowed.

By default, `check_src_filters` is predefined to include ALL files from the [src_dir](../platformio/src-dir.md) and [include_dir](../platformio/include-dir.md) folders.

## Example

```ini
[env:check_src_filters]
platform = ...
board = ...
check_src_filters =
  -<src/*>
  +<src/spi/spi.cpp>
  -<tests/>
  +<tests/test_embedded/*.c*>
```
