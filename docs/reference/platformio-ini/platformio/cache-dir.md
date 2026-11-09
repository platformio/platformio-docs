<a id="projectconf-pio-cache-dir"></a>

# `cache_dir` {#cache-dir}

Type: `DirPath` | Multiple: `No` | Default: "[core_dir](./core-dir.md)/cache"

[PlatformIO Core (CLI)](../../../get-started/platformio-core.md) uses this folder to store caching information (requests to PlatformIO Registry, downloaded packages and other service information).

To reset a cache, please run [`pio system prune --cache`](../../cli/pio-system/prune.md#cmdoption-pio-system-prune-cache) command.

This option can also be configured by the global environment variable [`PLATFORMIO_CACHE_DIR`](../../environment-variables.md#envvar-PLATFORMIO_CACHE_DIR).
