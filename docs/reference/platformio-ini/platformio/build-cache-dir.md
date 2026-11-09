---
description: "A location where PlatformIO Core keeps derived files from a build system (objects, firmwares, ELFs) and caches them between build environments (platformio.ini option build_cache_dir)."
---

# `build_cache_dir`

- **Type:** Path
- **Multiple values:** No
- **Environment variable:** [`PLATFORMIO_BUILD_CACHE_DIR`](../../environment-variables.md#envvar-PLATFORMIO_BUILD_CACHE_DIR), overrides the value in `platformio.ini`

[PlatformIO Core (CLI)](../../../get-started/platformio-core.md) uses this folder to store derived files from a build system (objects, firmwares, ELFs). These files are shared between all build environments. To speed up a build process, you can use the same cache folder between different projects if they depend on the same development platform and framework.

The example of [`platformio.ini`](../index.md) below instructs PlatformIO Build System to check build_cache_dir for already compiled objects for [STM32Cube](/hardware/frameworks/stm32cube) and project source files. The cached object will not be used if the original source file was modified or build environment has a different configuration (new build flags, etc):

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
