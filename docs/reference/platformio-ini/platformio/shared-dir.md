---
description: "A location which PlatformIO Remote Development service uses to synchronize extra files between remote machines (platformio.ini option shared_dir)."
---

<a id="projectconf-pio-shared-dir"></a>

# `shared_dir` {#shared-dir}

- **Type:** Path
- **Multiple values:** No
- **Default:** `${PROJECT_DIR}/shared`
- **Environment variable:** [`PLATFORMIO_SHARED_DIR`](../../environment-variables.md#envvar-PLATFORMIO_SHARED_DIR), overrides the value in `platformio.ini`

[Remote Development](../../../guides/remote-development.md) uses this folder to synchronize extra files between remote machine. For example, you can share [extra_scripts](../env/extra-scripts.md).

Note that these folders are automatically shared between remote machine with [`pio remote run --force-remote`](../../cli/pio-remote/run.md#cmdoption-pio-remote-run-r) or [`pio remote test --force-remote`](../../cli/pio-remote/test.md#cmdoption-pio-remote-test-r) commands:

- [lib_dir](./lib-dir.md)
- [include_dir](./include-dir.md)
- [src_dir](./src-dir.md)
- [boards_dir](./boards-dir.md)
- [data_dir](./data-dir.md)
- [test_dir](./test-dir.md)

The default value is `shared`, meaning a directory named "shared" located in the root of the project.
