<a id="projectconf-pio-build-cache-dir"></a>

# `build_cache_dir` {#build-cache-dir}

Type: `DirPath` | Multiple: `No` | Default: None (Disabled)

[PlatformIO Core (CLI)](../../../get-started/platformio-core.md) uses this folder to store derived files from a build system (objects, firmwares, ELFs). These files are shared between all build environments. To speed up a build process, you can use the same cache folder between different projects if they depend on the same development platform and framework.

This option can also be configured by the global environment variable [`PLATFORMIO_BUILD_CACHE_DIR`](../../environment-variables.md#envvar-PLATFORMIO_BUILD_CACHE_DIR).

The example of ["platformio.ini" (Project Configuration File)](../index.md) below instructs PlatformIO Build System to check [build_cache_dir](#projectconf-pio-build-cache-dir) for already compiled objects for [STM32Cube](/hardware/frameworks/stm32cube) and project source files. The cached object will not be used if the original source file was modified or build environment has a different configuration (new build flags, etc):

```ini
[platformio]
; Set a path to a cache folder
build_cache_dir =

; Examples:
; (Unix) build_cache_dir = /path/to/cache/folder
; (Windows) build_cache_dir = C:/path/to/cache/folder

[env:bluepill_f103c6]
platform = ststm32
framework = stm32cube
board = bluepill_f103c6

[env:nucleo_f411re]
platform = ststm32
framework = stm32cube
board = nucleo_f411re
```
