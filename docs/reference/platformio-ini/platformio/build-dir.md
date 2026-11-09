---
description: "PlatformIO Build System uses this folder for project environments to store compiled object files, static libraries, firmwares, and other cached information (platformio.ini option build_dir)."
---

<a id="projectconf-pio-build-dir"></a>

# `build_dir` {#build-dir}

:::warning

**PLEASE DO NOT EDIT FILES IN THIS FOLDER**. PlatformIO will overwrite your changes on the next build. **THIS IS A CACHE DIRECTORY**.

:::

- **Type:** Path
- **Multiple values:** No
- **Default:** `${platformio.workspace_dir}/build`
- **Environment variable:** [`PLATFORMIO_BUILD_DIR`](../../environment-variables.md#envvar-PLATFORMIO_BUILD_DIR), overrides the value in `platformio.ini`

*PlatformIO Build System* uses this folder for project environments to store compiled object files, static libraries, firmwares and other cached information. It allows PlatformIO to build source code extremely fast!

*You can delete this folder without any risk!* If you modify [`platformio.ini`](../index.md), then PlatformIO will remove this folder automatically. It will be created on the next build operation.

:::note

If you have any problems with building your project environments which are defined in [`platformio.ini`](../index.md), then **TRY TO DELETE** this folder. In this situation you will remove all cached files without any risk. Also, you can use "clean" target for [`pio run --target`](../../cli/pio-run.md#cmdoption-pio-run-t) command.

:::
