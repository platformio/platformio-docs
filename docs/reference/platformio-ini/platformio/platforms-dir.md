---
description: "A location where PlatformIO Core keeps installed development platforms (platformio.ini option platforms_dir)."
---

<a id="projectconf-pio-platforms-dir"></a>

# `platforms_dir` {#platforms-dir}

- **Type:** Path
- **Multiple values:** No
- **Default:** `${platformio.core_dir}/platforms`
- **Environment variable:** [`PLATFORMIO_PLATFORMS_DIR`](../../environment-variables.md#envvar-PLATFORMIO_PLATFORMS_DIR), overrides the value in `platformio.ini`

Global storage where **PlatformIO Package Manager** installs [Development Platforms](../../../hardware/platforms/index.md).
