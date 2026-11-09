# Build Configurations {#build-configurations}

There are 3 types ([build_type](../../reference/platformio-ini/env/build-type.md)) of build configuration in PlatformIO:

<dl>

<dt>

`release`

</dt>

<dd>

**Default configuration**. A "release" configuration of your firmware/program does not contain symbolic debug information and is optimized for the firmware size or speed (depending on [Development Platforms](../../hardware/platforms/index.md))

</dd>

<dt>

`test`

</dt>

<dd>

A "test" configuration extends a build environment with `PIO_UNIT_TESTING` macro and with extra flags provided by the [Unit Testing](../unit-testing/index.md) framework

</dd>

<dt>

`debug`

</dt>

<dd>

A "debug" configuration of your firmware/program is compiled with full symbolic debug information and no optimization. Optimization complicates debugging because the relationship between source code and generated instructions is more complex.

</dd>

</dl>

:::note

If you need to control build flags that are specific for debug configuration please refer to [debug_build_flags](../../reference/platformio-ini/env/debug-build-flags.md).

:::

If you need to build a project in `debug` configuration, please use one of these options:

- In [PlatformIO IDE for VSCode](../ide/vscode.md): Use build option **Pre-Debug** or **Pre-Debug All** in the `Project Tasks` menu.
- Add [build_type](../../reference/platformio-ini/env/build-type.md) with `debug` value to ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md)
- Use [pio debug](../../reference/cli/pio-debug.md) command.

:::note

[Debugging](../debugging/index.md) automatically switches to `debug` configuration when you do project debugging from [PlatformIO IDE](../../get-started/platformio-ide.md) or use the [pio debug](../../reference/cli/pio-debug.md) command.

To avoid having [Debugging](../debugging/index.md) rebuild the project, please create a separate build environment that defines `build_type = debug`. See the example below where the `mydebug` build environment will be used automatically by [Debugging](../debugging/index.md):

```ini
[env]
platform = ...
board = ...
framework = ...
... other common configuration

[env:myrelease]
some_extra_options = ...

[env:mydebug]
build_type = debug
some_extra_options = ...
```

:::

Please note that you can set a default build environment per a project using the [default_envs](../../reference/platformio-ini/platformio/default-envs.md) option in [Section \[platformio\]](../../reference/platformio-ini/platformio/index.md).
