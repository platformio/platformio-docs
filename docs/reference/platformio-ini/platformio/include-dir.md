---
description: "A default location for project header files. PlatformIO Build System automatically adds this path to CPPPATH scope (platformio.ini option include_dir)."
---

# `include_dir`

- **Type:** Path
- **Multiple values:** No
- **Default:** `${PROJECT_DIR}/include`
- **Environment variable:** [`PLATFORMIO_INCLUDE_DIR`](../../environment-variables.md#envvar-PLATFORMIO_INCLUDE_DIR), overrides the value in `platformio.ini`

The path to project's default header files. PlatformIO uses it for the [pio run](../../cli/pio-run.md) command. The default value is `include` meaning an `include` directory located under the root directory of the project. This path will be added to `CPPPATH` of the build environment.

If you need to add extra include directories to `CPPPATH` scope, please use [build_flags](../env/build-flags.md) with `-I /path/to/extra/dir` option.
