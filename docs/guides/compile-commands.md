<a id="compilation-db"></a>

# Compilation database `compile_commands.json` {#compilation-database-compile-commands-json}

A [compilation database](https://clang.llvm.org/docs/JSONCompilationDatabase.html) is a [JSON-formatted](https://www.json.org/) file named `compile_commands.json` that contains structured data about every compilation unit in your project.

You can generate a project `compile_commands.json` using the [`pio run --target`](../reference/cli/pio-run.md#cmdoption-pio-run-t) command and `compiledb` target. A default location for `compile_commands.json` is a project directory.

The following build variables can be used for customization using [Advanced Scripting](./scripting/index.md):

| Variable | Description |
|---|---|
| `COMPILATIONDB_PATH` | A path where the `compile_commands.json` file should be saved. A default location is the root of a project |
| `COMPILATIONDB_INCLUDE_TOOLCHAIN` | A boolean flag to control if toolchain paths should be included in the compilation unit. A default value is `False`, only project-dependent includes are exported. |

**Example**

Generate `compile_commands.json` with toolchain includes for each project environment and save database to the "[build_dir](../reference/platformio-ini/platformio/build-dir.md)/envname" folder:

`platformio.ini`:

```ini
[env:myenv]
platform = ...
board = ...
extra_scripts = pre:extra_script.py
```

`extra_script.py`:

```python
import os
Import("env")

# include toolchain paths
env.Replace(COMPILATIONDB_INCLUDE_TOOLCHAIN=True)

# override compilation DB path
env.Replace(COMPILATIONDB_PATH=os.path.join("$BUILD_DIR", "compile_commands.json"))
```

Generate `compile_commands.json`

```text
> pio run -t compiledb
```
