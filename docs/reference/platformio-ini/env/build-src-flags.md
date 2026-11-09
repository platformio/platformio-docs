---
description: "The same as `build_flags` but configures flags the only for project source files in the `src` folder (platformio.ini option build_src_flags)."
---

<a id="projectconf-build-src-flags"></a>

# `build_src_flags` {#build-src-flags}

- **Type:** String
- **Multiple values:** Yes
- **Environment variable:** [`PLATFORMIO_BUILD_SRC_FLAGS`](../../environment-variables.md#envvar-PLATFORMIO_BUILD_SRC_FLAGS), appended to the values in `platformio.ini`
- **Deprecated name:** `src_build_flags` (still accepted, with a warning)

An option `build_src_flags` has the same behavior as `build_flags` but will be applied only for the project source files in the [src_dir](../platformio/src-dir.md) directory.
