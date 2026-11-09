<a id="scripting-envs"></a>

# Construction Environments {#construction-environments}

The PlatformIO Build System uses the following construction environments to process a project:

- `DefaultEnvironment()` - the global construction environment.

  It is used for the [Development Platforms](../../hardware/platforms/index.md) and [Frameworks](../../hardware/frameworks/index.md) build scripts, [Pre & Post Actions](./actions.md), upload tools, [Library Dependency Finder (LDF)](../../guides/libraries/ldf.md), and for other internal operations.

- `Import("projenv")` - the isolated construction environment used for processing the project source code in [src_dir](../platformio-ini/platformio/src-dir.md).

  Please note that any [build_src_flags](../platformio-ini/env/build-src-flags.md) specified in ["platformio.ini" (Project Configuration File)](../platformio-ini/index.md) will be passed to the `projenv` and not to the `DefaultEnvironment()`.

  :::note

  1. The `projenv` is available only for the POST-type scripts (see [Launch Types](./launch-types.md)) and [extraScript](../library-json/build/extrascript.md) (see [library.json](../library-json/index.md)).
  2. Flags passed to the global construction environment using PRE-type scripts will affect the `projenv` too.

  :::

- `Import("env")` - the current working construction environment.

  Imported `env` refers to the `DefaultEnvironment()` for scripts configured using the [extra_scripts](../platformio-ini/env/extra-scripts.md) option in ["platformio.ini" (Project Configuration File)](../platformio-ini/index.md).

  If you use [library.json](../library-json/index.md) and [extraScript](../library-json/build/extrascript.md), the `Import("env")` refers to the library's isolated environment from which a script was called (not to the global environment). Please use `env = DefaultEnvironment()` instead to access the global environment.

---

**Examples**

`my_pre_extra_script.py`:

```python
# Import the current working construction
# environment to the `env` variable.
# alias of `env = DefaultEnvironment()`
Import("env")

# Dump construction environment (for debug purpose)
print(env.Dump())

# append extra flags to global build environment
# which later will be used to build:
# - project source code
# - frameworks
# - dependent libraries
env.Append(CPPDEFINES=[
  "MACRO_1_NAME",
  ("MACRO_2_NAME", "MACRO_2_VALUE")
])
```

`my_post_extra_script.py`:

```python
Import("env", "projenv")

# Dump global construction environment (for debug purpose)
print(env.Dump())

# Dump project construction environment (for debug purpose)
print(projenv.Dump())

# append extra flags to global build environment
# which later will be used to build:
# - frameworks
# - dependent libraries
env.Append(CPPDEFINES=[
  "MACRO_1_NAME",
  ("MACRO_2_NAME", "MACRO_2_VALUE")
])

# append extra flags to only project build environment
projenv.Append(CPPDEFINES=[
  "PROJECT_EXTRA_MACRO_1_NAME",
  ("ROJECT_EXTRA_MACRO_2_NAME", "ROJECT_EXTRA_MACRO_2_VALUE")
])
```
