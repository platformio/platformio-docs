<a id="projectconf-pio-core-dir"></a>

# `core_dir` {#core-dir}

Type: `DirPath` | Multiple: `No`

The core_dir variable points out the directory used for all development platform packages (toolchains, frameworks, SDKs, upload and debug tools), global libraries for [Library Dependency Finder (LDF)](../../../guides/libraries/ldf.md), and other PlatformIO Core service data. The size of this folder will depend on the number of installed development platforms.

The default value is the user's home directory:

- Unix `~/.platformio`
- Windows `%HOMEPATH%\.platformio`

This option can also be configured by the global environment variable [`PLATFORMIO_CORE_DIR`](../../environment-variables.md#envvar-PLATFORMIO_CORE_DIR).

Example:

```ini
[platformio]
core_dir = /path/to/custom/pio-core/storage
```
