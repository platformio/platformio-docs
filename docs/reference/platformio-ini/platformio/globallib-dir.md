---
description: "A library folder/storage where PlatformIO Library Dependency Finder (LDF) looks for global libraries (platformio.ini option globallib_dir)."
---

# `globallib_dir`

- **Type:** Path
- **Multiple values:** No
- **Default:** `${platformio.core_dir}/lib`
- **Environment variable:** [`PLATFORMIO_GLOBALLIB_DIR`](../../environment-variables.md#envvar-PLATFORMIO_GLOBALLIB_DIR), overrides the value in `platformio.ini`

:::warning

This option is **DEPRECATED**. We do not recommend using global libraries for new projects. Use a declarative approach for the safety-critical embedded development and declare project dependencies using the [lib_deps](../env/lib-deps.md) option.

:::

Global library storage for PlatfrmIO projects and [Library Management](../../../guides/libraries/index.md) where [Library Dependency Finder (LDF)](../../../guides/libraries/ldf.md) looks for dependencies.
