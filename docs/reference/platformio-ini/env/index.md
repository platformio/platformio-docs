<a id="projectconf-section-env"></a>

# Section `[env]` {#section-env}

Each project may have multiple *configuration environments* defining the available project tasks for building, programming, debugging, unit testing, device monitoring, library dependencies, etc. The configuration environments are declared using `[env]` sections in ["platformio.ini" (Project Configuration File)](../index.md).

The allowed options are listed under [Options](#options).

## Common `[env]` {#common-env}

An optional configuration environment with common options that will be shared between all `[env:NAME]` environments in the platformio.ini file. It is very useful if the configuration file has a lot of environments `[env:NAME]` and they share common settings.

For example:

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

In this example we have two configuration environments `release` and `debug`. This is equivalent to duplicating all options as shown below:

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

<a id="projectconf-section-env-named"></a>

## Working `[env:NAME]` {#working-env-name}

A working environment in PlatformIO is defined using the `[env:NAME]` syntax. This environment is used by various PlatformIO commands such as [pio run](../../cli/pio-run.md), [pio test](../../cli/pio-test.md), [pio check](../../cli/pio-check.md), [pio debug](../../cli/pio-debug.md), and others. Every project must define at least one working environment.

You can define multiple working environments in your project by using different names for the `[env:NAME]` section. It's important to note that each environment must have a unique name. The name should only include lowercase letters `a-z`, numbers `0-9`, and special characters `_` (underscore) and `-` (hyphen). For example, `[env:hello_world]` is a valid name.

If you have defined multiple working environments and you only want to process a subset of them, you can use the `-e` or `--environment` option with the PlatformIO commands mentioned above. You can specify the name of the environment you want to process using this option.

In addition to using the `-e` option, you can define a default set of working environments for the PlatformIO commands to process by using the `[platformio]` [default_envs](../platformio/default-envs.md) option. This can be useful if you frequently work with a specific set of environments and don't want to specify them every time you run a command.

## Options {#options}

- [Platform options](./platform-options.md)

  - [`platform`](./platform.md)
  - [`platform_packages`](./platform-packages.md)
  - [`framework`](./framework.md)
  - [`board`](./board.md)
  - [`board_build.mcu`](./board-build-mcu.md)
  - [`board_build.f_cpu`](./board-build-f-cpu.md)
  - [`board_build.ldscript`](./board-build-ldscript.md)
  - [More options](./platform-options.md#more-options)

- [Build options](./build-options.md)

  - [`build_type`](./build-type.md)
  - [`build_flags`](./build-flags.md)
  - [`build_src_flags`](./build-src-flags.md)
  - [`build_unflags`](./build-unflags.md)
  - [`build_src_filter`](./build-src-filter.md)
  - [`targets`](./targets.md)

- [Library options](./library-options.md)

  - [`lib_deps`](./lib-deps.md)
  - [`lib_ignore`](./lib-ignore.md)
  - [`lib_extra_dirs`](./lib-extra-dirs.md)
  - [`lib_ldf_mode`](./lib-ldf-mode.md)
  - [`lib_compat_mode`](./lib-compat-mode.md)
  - [`lib_archive`](./lib-archive.md)

- [Upload options](./upload-options.md)

  - [`upload_port`](./upload-port.md)
  - [`upload_protocol`](./upload-protocol.md)
  - [`upload_speed`](./upload-speed.md)
  - [Common baud rates](./upload-speed.md#common-baud-rates)
  - [`upload_flags`](./upload-flags.md)
  - [`upload_resetmethod`](./upload-resetmethod.md)
  - [`upload_command`](./upload-command.md)

- [Monitor options](./monitor-options.md)

  - [`monitor_port`](./monitor-port.md)
  - [`monitor_speed`](./monitor-speed.md)
  - [`monitor_parity`](./monitor-parity.md)
  - [`monitor_filters`](./monitor-filters.md)
  - [`monitor_rts`](./monitor-rts.md)
  - [`monitor_dtr`](./monitor-dtr.md)
  - [`monitor_eol`](./monitor-eol.md)
  - [`monitor_raw`](./monitor-raw.md)
  - [`monitor_echo`](./monitor-echo.md)
  - [`monitor_encoding`](./monitor-encoding.md)

- [Check options](./check-options.md)

  - [`check_tool`](./check-tool.md)
  - [`check_flags`](./check-flags.md)
  - [`check_severity`](./check-severity.md)
  - [`check_skip_packages`](./check-skip-packages.md)
  - [`check_src_filters`](./check-src-filters.md)

- [Testing options](./test-options.md)

  - [`test_framework`](./test-framework.md)
  - [`test_filter`](./test-filter.md)
  - [`test_ignore`](./test-ignore.md)
  - [`test_port`](./test-port.md)
  - [`test_speed`](./test-speed.md)
  - [`test_build_src`](./test-build-src.md)
  - [`test_testing_command`](./test-testing-command.md)

- [Debugging options](./debug-options.md)

  - [`debug_tool`](./debug-tool.md)
  - [`debug_build_flags`](./debug-build-flags.md)
  - [`debug_init_break`](./debug-init-break.md)
  - [`debug_init_cmds`](./debug-init-cmds.md)
  - [`debug_extra_cmds`](./debug-extra-cmds.md)
  - [`debug_load_cmds`](./debug-load-cmds.md)
  - [`debug_load_mode`](./debug-load-mode.md)
  - [`debug_server`](./debug-server.md)
  - [`debug_port`](./debug-port.md)
  - [`debug_speed`](./debug-speed.md)
  - [`debug_svd_path`](./debug-svd-path.md)
  - [`debug_server_ready_pattern`](./debug-server-ready-pattern.md)
  - [`debug_test`](./debug-test.md)

- [Advanced options](./advanced-options.md)

  - [`extends`](./extends.md)
  - [`extra_scripts`](./extra-scripts.md)
