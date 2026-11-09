---
description: "Internal storage where Library Manager will install project dependencies declared via `lib_deps` option (platformio.ini option libdeps_dir)."
---

<a id="projectconf-pio-libdeps-dir"></a>

# `libdeps_dir` {#libdeps-dir}

- **Type:** Path
- **Multiple values:** No
- **Default:** `${platformio.workspace_dir}/libdeps`
- **Environment variable:** [`PLATFORMIO_LIBDEPS_DIR`](../../environment-variables.md#envvar-PLATFORMIO_LIBDEPS_DIR), overrides the value in `platformio.ini`

Internal storage where [Library Management](../../../guides/libraries/index.md) will install project dependencies ([lib_deps](../env/lib-deps.md)).
