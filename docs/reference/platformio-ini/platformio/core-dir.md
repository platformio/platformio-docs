---
description: "PlatformIO Core location where it keeps installed development platforms, packages, global libraries, and other internal information (platformio.ini option core_dir)."
---

# `core_dir`

- **Type:** Path
- **Multiple values:** No
- **Environment variable:** [`PLATFORMIO_CORE_DIR`](../../environment-variables.md#envvar-PLATFORMIO_CORE_DIR), overrides the value in `platformio.ini`
- **Deprecated name:** `home_dir` (still accepted, with a warning)

The core_dir variable points out the directory used for all development platform packages (toolchains, frameworks, SDKs, upload and debug tools), global libraries for [Library Dependency Finder (LDF)](../../../guides/libraries/ldf.md), and other PlatformIO Core service data. The size of this folder will depend on the number of installed development platforms.

The default value is the user's home directory:

- Unix `~/.platformio`
- Windows `%HOMEPATH%\.platformio`

## Example

```ini
[platformio]
core_dir = /path/to/custom/pio-core/storage
```
