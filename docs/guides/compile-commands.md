# Compilation database `compile_commands.json`

A [compilation database](https://clang.llvm.org/docs/JSONCompilationDatabase.html) is a [JSON-formatted](https://www.json.org/) file named `compile_commands.json` that contains structured data about every compilation unit in your project.

Editors and tools such as clangd, ccls and Clang-Tidy use it for code completion and analysis. Generate it with the `compiledb` [project target](../reference/cli/pio-run.md#cmdoption-pio-run-t):

```bash
pio run -t compiledb
```

By default, the file is saved in the project directory.

To customize it, set these build variables in an [extra script](./scripting/index.md):

| Variable | Description |
|---|---|
| `COMPILATIONDB_PATH` | Where to save the file. Default: `$PROJECT_DIR/compile_commands.json` |
| `COMPILATIONDB_INCLUDE_TOOLCHAIN` | Also include the toolchain's include paths. Default: `False` (only the project's include paths) |

## Example {#example}

Include the toolchain paths and save a separate database per environment in its [build folder](../reference/platformio-ini/platformio/build-dir.md):

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

Generate the database:

```bash
pio run -t compiledb
```
