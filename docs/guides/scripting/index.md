---
description: Extend the PlatformIO build with Python and SCons scripts - change flags, add actions and custom targets.
---

# Extending the build

The PlatformIO build system runs on [SCons](https://scons.org/). With extra
scripts, written in Python, you can change almost anything about a build:
compiler and linker flags, upload settings, which files are built, and actions
before and after each step. You can also add your own targets.

Add a script to a project environment with the
[`extra_scripts`](../../reference/platformio-ini/env/extra-scripts.md) option:

```ini
[env:myenv]
platform = ...
board = ...
extra_scripts = pre:extra_script.py
```

```python
Import("env")

env.Append(CPPDEFINES=["MY_MACRO"])
```

:::note

Extra scripts run inside the build system: [`pio run`](../../reference/cli/pio-run.md)
loads them while it processes the environment. You cannot run or debug them on
their own with a Python interpreter. Scripting requires Python knowledge.

:::

## Concepts {#concepts}

| Topic | What it covers |
| --- | --- |
| [Launch types](../../reference/scripting-api/launch-types.md) | `pre:` and `post:` scripts: when a script runs |
| [Construction environments](../../reference/scripting-api/construction-environments.md) | `env`, `projenv` and `DefaultEnvironment()`: what a script can change |
| [Pre and post actions](../../reference/scripting-api/actions.md) | Running code before or after build and upload steps |
| [Build middlewares](../../reference/scripting-api/middlewares.md) | Changing or skipping individual source files |
| [Custom targets](./custom-targets.md) | Adding your own targets to `pio run -t` |

## Examples {#examples}

| Example | |
| --- | --- |
| [Custom options in `platformio.ini`](./examples/platformio-ini-custom-options.md) | Read your own options from `platformio.ini` |
| [Split C/C++ build flags](./examples/split-build-flags.md) | Different flags for C and C++ files |
| [Extra linker flags without `-Wl,`](./examples/extra-linker-flags.md) | Pass flags to the linker directly |
| [Upload to a cloud service (OTA)](./examples/upload-to-cloud.md) | Replace the upload step |
| [Custom firmware name](./examples/custom-program-name.md) | Change the name of the built program |
| [Asking for input](./examples/asking-for-input.md) | Prompt the user during the build |
| [Override package files](./examples/override-package-files.md) | Patch files of a framework or toolchain |
| [Override board configuration](./examples/override-board-configuration.md) | Change board settings from a script |
| [Extra Python packages](./examples/extra-python-packages.md) | Install Python packages a script needs |
| [Build external sources](./examples/external-sources.md) | Build sources from outside the project |
