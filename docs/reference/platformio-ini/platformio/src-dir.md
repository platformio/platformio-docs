---
description: "A default location where PlatformIO Build System looks for the project C/C++ source files (platformio.ini option src_dir)."
---

# `src_dir`

- **Type:** Path
- **Multiple values:** No
- **Default:** `${PROJECT_DIR}/src`
- **Environment variable:** [`PLATFORMIO_SRC_DIR`](../../environment-variables.md#envvar-PLATFORMIO_SRC_DIR), overrides the value in `platformio.ini`

The `src_dir` is the path to the directory where the source code of the project is located. It is used by the [pio run](../../cli/pio-run.md) command to compile and upload the code to the device. By default, the `src_dir` is set to `src`, which means the source code is located in a directory named `src` in the root directory of the project.

:::tip

To include or exclude specific source files from the build process, use the [build_src_filter](../env/build-src-filter.md) option in the [`platformio.ini`](../index.md). The [build_src_filter](../env/build-src-filter.md) option can take a list of file patterns in glob syntax. Only the source files that match the specified patterns will be included in the build process.

:::
