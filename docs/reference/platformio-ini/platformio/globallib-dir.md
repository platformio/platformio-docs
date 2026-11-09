<a id="projectconf-pio-globallib-dir"></a>

# `globallib_dir` {#globallib-dir}

Type: `DirPath` | Multiple: `No` | Default: "[core_dir](./core-dir.md)/lib" | **DEPRECATED**

:::warning

This option is **DEPRECATED**. We do not recommend using global libraries for new projects. Please use a declarative approach for the safety-critical embedded development and declare project dependencies using the [lib_deps](../env/lib-deps.md) option.

:::

Global library storage for PlatfrmIO projects and [Library Management](../../../guides/libraries/index.md) where [Library Dependency Finder (LDF)](../../../guides/libraries/ldf.md) looks for dependencies.

This option can also be configured by the global environment variable [`PLATFORMIO_GLOBALLIB_DIR`](../../environment-variables.md#envvar-PLATFORMIO_GLOBALLIB_DIR).
