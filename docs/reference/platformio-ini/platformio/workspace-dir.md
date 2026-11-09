<a id="projectconf-pio-workspace-dir"></a>

# `workspace_dir` {#workspace-dir}

Type: `DirPath` | Multiple: `No` | Default: "\<Project>/`.pio`"

The path to a project workspace directory where PlatformIO keeps by default compiled objects, static libraries, firmwares, and external library dependencies. It is used by these options:

- [build_dir](./build-dir.md)
- [libdeps_dir](./libdeps-dir.md).

The default value is `.pio` and means that folder is located in the root of project.

This option can also be configured by the global environment variable [`PLATFORMIO_WORKSPACE_DIR`](../../environment-variables.md#envvar-PLATFORMIO_WORKSPACE_DIR).
