<a id="scripting"></a>

# Advanced Scripting {#advanced-scripting}

:::warning

Advanced Scripting is recommended for Advanced Users and requires knowledge of the Python language.

:::

The PlatformIO Build System allows the user to extend the build process with custom scripts using the Python interpreter and the [SCons](http://www.scons.org) construction tool. Build flags, upload flags, targets, toolchains data and other information are available for modification as [SCons Construction Environments](http://www.scons.org/doc/production/HTML/scons-user.html#chap-environments). Custom scripts are included with [extra_scripts](../../reference/platformio-ini/env/extra-scripts.md).

:::warning

Please note that you can not run or debug these scripts independently with Python interpreter. They will be loaded automatically when the [pio run](../../reference/cli/pio-run.md) command processes the project environment.

:::

- [Launch Types](../../reference/scripting-api/launch-types.md)

- [Construction Environments](../../reference/scripting-api/construction-environments.md)

- [Pre & Post Actions](../../reference/scripting-api/actions.md)

- [Build Middlewares](../../reference/scripting-api/middlewares.md)

- [Custom Targets](./custom-targets.md)

  - [Build System API](./custom-targets.md#build-system-api)
  - [Examples](./custom-targets.md#examples)

- [Examples](./examples/index.md)

  - [Custom options in `platformio.ini`](./examples/platformio-ini-custom-options.md)
  - [Split C/C++ build flags](./examples/split-build-flags.md)
  - [Extra linker flags without `-Wl,` prefix](./examples/extra-linker-flags.md)
  - [Upload to Cloud (OTA)](./examples/upload-to-cloud.md)
  - [Custom firmware/program name](./examples/custom-program-name.md)
  - [Asking for input (prompts)](./examples/asking-for-input.md)
  - [Override package files](./examples/override-package-files.md)
  - [Override board configuration](./examples/override-board-configuration.md)
  - [Extra Python packages](./examples/extra-python-packages.md)
  - [Build external sources](./examples/external-sources.md)
