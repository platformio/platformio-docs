---
description: "There are two execution types for extra scripts."
---

<a id="scripting-launch-types"></a>

# Launch types {#launch-types}

There are two execution types for extra scripts:

- **PRE** - executes before the main script of [Development Platforms](../../hardware/platforms/index.md).

  Useful to pre-generate extra source files or make dynamic changes/patches to the existing, pass flags to the global building environment, add [Build Middlewares](./middlewares.md), etc.

  :::note

  Note that the `projenv` (see [Construction Environments](./construction-environments.md)) is not available at this stage.

  :::

- **POST** - executes after the **PRE** and the main script of [Development Platforms](../../hardware/platforms/index.md).

  The building environment is fully constructed at this stage with all build flags, development platform targets, dependent libraries, and `projenv`. Useful to assign [Pre & Post Actions](./actions.md), modify default build flags set by the development platform, or extend the building workflow.

The extra scripts can be configured using the [extra_scripts](../platformio-ini/env/extra-scripts.md) option in [`platformio.ini`](../platformio-ini/index.md) or using the [extraScript](../library-json/build/extrascript.md) in [library.json](../library-json/index.md) manifest.

The launch type can be specified as a prefix (`pre:` or `post:`) to the script path. If there is no prefix specified, the `post:` will be used automatically.

## Example

```ini
[env:my_env_1]
platform = ...
; Defaults to POST script since no prefix is used
extra_scripts = post_extra_script.py

[env:my_env_2]
platform = ...
extra_scripts =
  pre:pre_extra_script.py
  post:post_extra_script1.py
  post_extra_script2.py
```

:::note

PlatformIO includes a service stage during runtime where it re-executes extra scripts to gather integration information intended for IDE plugins. If you want your scripts to run exclusively for the "build" target, include the following hook at the beginning of your script:

:::

```python
Import("env")

if env.IsIntegrationDump():
   # stop the current script execution
   Return()

# code below runs for the "build" and other targets
env.Append(CPPDEFINES=["MACRO_NAME"])
```
