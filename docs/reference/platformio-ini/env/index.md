---
description: The [env] and [env:NAME] sections of platformio.ini - project environments and the options they accept.
---

# Section `[env]`

A project environment, `[env:NAME]`, describes one way to build the project:
the development platform, board, framework, build flags, libraries, and how to
upload, monitor, test and debug. [`pio run`](../../cli/pio-run.md),
[`pio test`](../../cli/pio-test.md), [`pio check`](../../cli/pio-check.md),
[`pio debug`](../../cli/pio-debug.md) and other commands process environments.

A project can have several environments, for example one per board, or a
`release` and a `debug` variant of the same board.

<a id="projectconf-section-env-named"></a>

## Project environments `[env:NAME]` {#working-env-name}

Each project needs at least one `[env:NAME]` section. Names must be unique and
can contain letters, digits, `_` and `-`, for example `[env:esp32_debug]`.

By default, commands process every environment. To process some of them:

- pass `-e NAME` (or `--environment NAME`) to the command, once per
  environment; or
- list them in the [`default_envs`](../platformio/default-envs.md) option of
  the `[platformio]` section.

## Shared options `[env]` {#common-env}

Options in a plain `[env]` section apply to every `[env:NAME]` environment,
unless the environment sets them itself. Use it when environments share
settings:

```ini
[env]
platform = ststm32
framework = stm32cube
board = nucleo_l152re
lib_deps = Dep1, Dep2

[env:release]
build_flags = -D RELEASE
lib_deps =
    ${env.lib_deps}
    Dep3

[env:debug]
build_type = debug
build_flags = -D DEBUG
lib_deps = DepCustom
```

This is equivalent to:

```ini
[env:release]
platform = ststm32
framework = stm32cube
board = nucleo_l152re
build_flags = -D RELEASE
lib_deps = Dep1, Dep2, Dep3

[env:debug]
platform = ststm32
framework = stm32cube
board = nucleo_l152re
build_type = debug
build_flags = -D DEBUG
lib_deps = DepCustom
```

To reuse options from another section, see [`extends`](./extends.md) and
[interpolation](../../../guides/projects/interpolation.md).

## Options {#options}

| Group | Options |
| --- | --- |
| [Platform options](./platform-options.md) | `platform`, `platform_packages`, `framework`, `board`, `board_build.*`, other [board overrides](./platform-options.md#more-options) |
| [Build options](./build-options.md) | `build_type`, `build_flags`, `build_src_flags`, `build_unflags`, `build_src_filter`, `targets` |
| [Library options](./library-options.md) | `lib_deps`, `lib_ignore`, `lib_extra_dirs`, `lib_ldf_mode`, `lib_compat_mode`, `lib_archive` |
| [Upload options](./upload-options.md) | `upload_port`, `upload_protocol`, `upload_speed`, `upload_flags`, `upload_resetmethod`, `upload_command` |
| [Monitor options](./monitor-options.md) | `monitor_port`, `monitor_speed`, `monitor_parity`, `monitor_filters`, `monitor_rts`, `monitor_dtr`, `monitor_eol`, `monitor_raw`, `monitor_echo`, `monitor_encoding` |
| [Check options](./check-options.md) | `check_tool`, `check_flags`, `check_severity`, `check_skip_packages`, `check_src_filters` |
| [Test options](./test-options.md) | `test_framework`, `test_filter`, `test_ignore`, `test_port`, `test_speed`, `test_build_src`, `test_testing_command` |
| [Debug options](./debug-options.md) | `debug_tool`, `debug_test`, `debug_build_flags`, `debug_init_break`, `debug_init_cmds`, `debug_extra_cmds`, `debug_load_cmds`, `debug_load_mode`, `debug_server`, `debug_port`, `debug_speed`, `debug_svd_path`, `debug_server_ready_pattern` |
| [Advanced options](./advanced-options.md) | `extends`, `extra_scripts` |

You can also add your own options, for example to read them from
[scripts](../../../guides/scripting/examples/platformio-ini-custom-options.md).
