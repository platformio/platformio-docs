---
description: "A path to a project workspace directory where PlatformIO keeps by default compiled objects, static libraries, firmwares, and external library dependencies (platformio.ini option workspace_dir)."
---

<a id="projectconf-pio-workspace-dir"></a>

# `workspace_dir` {#workspace-dir}

- **Type:** Path
- **Multiple values:** No
- **Default:** `${PROJECT_DIR}/.pio`
- **Environment variable:** [`PLATFORMIO_WORKSPACE_DIR`](../../environment-variables.md#envvar-PLATFORMIO_WORKSPACE_DIR), overrides the value in `platformio.ini`

The path to a project workspace directory where PlatformIO keeps by default compiled objects, static libraries, firmwares, and external library dependencies. It is used by these options:

- [build_dir](./build-dir.md)
- [libdeps_dir](./libdeps-dir.md).

The default value is `.pio` and means that folder is located in the root of project.
