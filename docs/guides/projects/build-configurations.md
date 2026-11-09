---
description: The release, debug and test build configurations, and how to build in debug configuration.
---

# Build configurations {#build-configurations}

PlatformIO builds a project in one of three build configurations, set by the
[`build_type`](../../reference/platformio-ini/env/build-type.md) option:

| Configuration | Purpose |
| --- | --- |
| `release` | The default. No debug information; optimized for size or speed, depending on the [development platform](../../hardware/platforms/index.md). |
| `debug` | Full debug information and no optimization, so that the debugger can map instructions to source lines. The flags come from [`debug_build_flags`](../../reference/platformio-ini/env/debug-build-flags.md). |
| `test` | Used for [unit testing](../unit-testing/index.md). Defines the `PIO_UNIT_TESTING` macro and adds the flags of the testing framework. |

## Build in debug configuration {#build-in-debug-configuration}

[Debugging](../debugging/index.md) builds in the `debug` configuration
automatically, both in PlatformIO IDE and with [`pio debug`](../../reference/cli/pio-debug.md).
To build in it without starting a debugger:

- in PlatformIO IDE for VS Code, run **Pre-Debug** in the **Project Tasks**
  panel; or
- set `build_type = debug` in the environment.

## Keep separate release and debug environments {#separate-environments}

Switching one environment between configurations makes PlatformIO rebuild the
project each time. Instead, define one environment per configuration.
Debugging uses the first environment with `build_type = debug`, looking first
in [`default_envs`](../../reference/platformio-ini/platformio/default-envs.md)
and then in all environments:

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
