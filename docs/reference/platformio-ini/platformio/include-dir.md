<a id="projectconf-pio-include-dir"></a>

# `include_dir` {#include-dir}

Type: `DirPath` | Multiple: `No` | Default: "\<Project>/`include`"

The path to project's default header files. PlatformIO uses it for the [pio run](../../cli/pio-run.md) command. The default value is `include` meaning an `include` directory located under the root directory of the project. This path will be added to `CPPPATH` of the build environment.

If you need to add extra include directories to `CPPPATH` scope, please use [build_flags](../env/build-flags.md) with `-I /path/to/extra/dir` option.

This option can also be configured by the global environment variable [`PLATFORMIO_INCLUDE_DIR`](../../environment-variables.md#envvar-PLATFORMIO_INCLUDE_DIR).
