---
description: "A location where PlatformIO Core keeps installed packages (platformio.ini option packages_dir)."
---

# `packages_dir`

- **Type:** Path
- **Multiple values:** No
- **Default:** `${platformio.core_dir}/packages`
- **Environment variable:** [`PLATFORMIO_PACKAGES_DIR`](../../environment-variables.md#envvar-PLATFORMIO_PACKAGES_DIR), overrides the value in `platformio.ini`

Global storage where **PlatformIO Package Manager** installs [Development Platforms](../../../hardware/platforms/index.md) dependencies (toolchains, [Frameworks](../../../hardware/frameworks/index.md), SDKs, upload and debug tools).
