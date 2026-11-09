---
description: "A location where PlatformIO Core stores caching information (requests to PlatformIO Registry, downloaded packages and other service information) (platformio.ini option cache_dir)."
---

<a id="projectconf-pio-cache-dir"></a>

# `cache_dir` {#cache-dir}

- **Type:** Path
- **Multiple values:** No
- **Default:** `${platformio.core_dir}/.cache`
- **Environment variable:** [`PLATFORMIO_CACHE_DIR`](../../environment-variables.md#envvar-PLATFORMIO_CACHE_DIR), overrides the value in `platformio.ini`

[PlatformIO Core (CLI)](../../../get-started/platformio-core.md) uses this folder to store caching information (requests to PlatformIO Registry, downloaded packages and other service information).

To reset a cache, please run [`pio system prune --cache`](../../cli/pio-system/prune.md#cmdoption-pio-system-prune-cache) command.
