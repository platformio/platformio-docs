---
description: Environment variables that configure PlatformIO Core and override platformio.ini options and settings.
---

# Environment variables

PlatformIO Core reads the environment variables listed on this page. Use them
to configure PlatformIO in CI, containers and scripts without editing
`platformio.ini` or the settings.

To set a variable for the current terminal session:

```bash
# macOS and Linux (Bash, Zsh)
export PLATFORMIO_BUILD_FLAGS="-DDEBUG=1"

# fish
set -x PLATFORMIO_BUILD_FLAGS "-DDEBUG=1"

# Windows (Command Prompt)
set PLATFORMIO_BUILD_FLAGS=-DDEBUG=1

# Windows (PowerShell)
$env:PLATFORMIO_BUILD_FLAGS = "-DDEBUG=1"
```

Boolean variables are enabled only by the value `true`.

## General {#general}

### `CI` {#envvar-CI}

Most CI services set `CI=true`. PlatformIO uses it to recognize CI runs, for
example to report the CI service in [telemetry](./cli/pio-settings.md#setting-enable-telemetry).
In CI, also consider setting
[`PLATFORMIO_DISABLE_PROGRESSBAR`](#envvar-PLATFORMIO_DISABLE_PROGRESSBAR).

### `PLATFORMIO_AUTH_TOKEN` {#envvar-PLATFORMIO_AUTH_TOKEN}

A personal authentication token that signs you in to your
[PlatformIO Account](../get-started/platformio-account.md) without
[`pio account login`](./cli/pio-account/login.md). Use it in
[CI](../guides/ci/index.md) and for
[remote development](../guides/remote-development.md). Get a token with
[`pio account token`](./cli/pio-account/token.md).

### `PLATFORMIO_NO_ANSI` {#envvar-PLATFORMIO_NO_ANSI}

Set to `true` to not print ANSI control characters, such as colors. The same
as [`pio --no-ansi`](./cli/index.md#cmdoption-pio-no-ansi).
`PLATFORMIO_DISABLE_COLOR` is a deprecated alias.

### `PLATFORMIO_FORCE_ANSI` {#envvar-PLATFORMIO_FORCE_ANSI}

Set to `true` to print ANSI control characters even when the output is not a
terminal, for example when it is piped. `PLATFORMIO_FORCE_COLOR` is a
deprecated alias.

### `PLATFORMIO_DISABLE_PROGRESSBAR` {#envvar-PLATFORMIO_DISABLE_PROGRESSBAR}

Set to `true` to hide the progress bars of downloads and uploads. Useful when
the output is logged or piped.

### `PLATFORMIO_DISABLE_UPGRADE_CHECK` {#envvar-PLATFORMIO_DISABLE_UPGRADE_CHECK}

Set to `true` to not check for new versions of PlatformIO Core.

### `PLATFORMIO_SYSTEM_TYPE` {#envvar-PLATFORMIO_SYSTEM_TYPE}

Override the detected host system type, which selects the packages built for
your host. Examples: `windows_amd64`, `windows_arm64`, `linux_x86_64`,
`linux_armv7l`, `darwin_arm64`. Run [`pio system info`](./cli/pio-system/info.md)
to see the detected value.

### `PLATFORMIO_RUN_JOBS` {#envvar-PLATFORMIO_RUN_JOBS}

The default number of parallel build jobs, as
[`pio run --jobs`](./cli/pio-run.md#cmdoption-pio-run-j). Default: the number of
CPUs.

### `PLATFORMIO_CI_SRC` {#envvar-PLATFORMIO_CI_SRC}

The source paths for [`pio ci`](./cli/pio-ci.md) when you do not pass them as
arguments. Separate several paths with the operating system's path separator:
`:` on macOS and Linux, `;` on Windows.

### `PLATFORMIO_CALLER` {#envvar-PLATFORMIO_CALLER}

The ID of the application that runs PlatformIO Core, as
[`pio --caller`](./cli/index.md#cmdoption-pio-caller).

### `PLATFORMIO_REMOTE_AGENT_DIR` {#envvar-PLATFORMIO_REMOTE_AGENT_DIR}

The working directory of a remote agent, as
[`pio remote agent start --working-dir`](./cli/pio-remote/agent.md#cmdoption-pio-remote-agent-start-d).

## Project options {#building}

These variables set [`platformio.ini`](./platformio-ini/index.md) options for
every project and environment. For options that accept multiple values, the
variable adds to the values in `platformio.ini`; for the others, it replaces
the value.

<a id="uploading"></a>

### `PLATFORMIO_BUILD_FLAGS` {#envvar-PLATFORMIO_BUILD_FLAGS}

Sets the [`build_flags`](./platformio-ini/env/build-flags.md) option of every project. Its value is added to the values in `platformio.ini`.

### `PLATFORMIO_BUILD_SRC_FILTER` {#envvar-PLATFORMIO_BUILD_SRC_FILTER}

Sets the [`build_src_filter`](./platformio-ini/env/build-src-filter.md) option of every project. Its value is added to the values in `platformio.ini`.

### `PLATFORMIO_BUILD_SRC_FLAGS` {#envvar-PLATFORMIO_BUILD_SRC_FLAGS}

Sets the [`build_src_flags`](./platformio-ini/env/build-src-flags.md) option of every project. Its value is added to the values in `platformio.ini`.

### `PLATFORMIO_BUILD_UNFLAGS` {#envvar-PLATFORMIO_BUILD_UNFLAGS}

Sets the [`build_unflags`](./platformio-ini/env/build-unflags.md) option of every project. Its value is added to the values in `platformio.ini`.

### `PLATFORMIO_DEFAULT_ENVS` {#envvar-PLATFORMIO_DEFAULT_ENVS}

Sets the [`default_envs`](./platformio-ini/platformio/default-envs.md) option of every project. Its value is added to the values in `platformio.ini`.

### `PLATFORMIO_EXTRA_SCRIPTS` {#envvar-PLATFORMIO_EXTRA_SCRIPTS}

Sets the [`extra_scripts`](./platformio-ini/env/extra-scripts.md) option of every project. Its value is added to the values in `platformio.ini`.

### `PLATFORMIO_LIB_EXTRA_DIRS` {#envvar-PLATFORMIO_LIB_EXTRA_DIRS}

Sets the [`lib_extra_dirs`](./platformio-ini/env/lib-extra-dirs.md) option of every project. Its value is added to the values in `platformio.ini`.

### `PLATFORMIO_UPLOAD_FLAGS` {#envvar-PLATFORMIO_UPLOAD_FLAGS}

Sets the [`upload_flags`](./platformio-ini/env/upload-flags.md) option of every project. Its value is added to the values in `platformio.ini`.

### `PLATFORMIO_UPLOAD_PORT` {#envvar-PLATFORMIO_UPLOAD_PORT}

Sets the [`upload_port`](./platformio-ini/env/upload-port.md) option of every project. It overrides the value in `platformio.ini`.

:::warning

If build flags contain characters that your shell interprets, such as `$`,
`&` or `~`, use [interpolation](../guides/projects/interpolation.md) in
`platformio.ini` instead of `PLATFORMIO_BUILD_FLAGS`.

:::

## Directories {#directories}

These variables set the [directory options](./platformio-ini/platformio/directory-options.md)
of the `[platformio]` section.

### `PLATFORMIO_BOARDS_DIR` {#envvar-PLATFORMIO_BOARDS_DIR}

Sets the [`boards_dir`](./platformio-ini/platformio/boards-dir.md) option of every project. It overrides the value in `platformio.ini`.

### `PLATFORMIO_BUILD_CACHE_DIR` {#envvar-PLATFORMIO_BUILD_CACHE_DIR}

Sets the [`build_cache_dir`](./platformio-ini/platformio/build-cache-dir.md) option of every project. It overrides the value in `platformio.ini`.

### `PLATFORMIO_BUILD_DIR` {#envvar-PLATFORMIO_BUILD_DIR}

Sets the [`build_dir`](./platformio-ini/platformio/build-dir.md) option of every project. It overrides the value in `platformio.ini`.

### `PLATFORMIO_CACHE_DIR` {#envvar-PLATFORMIO_CACHE_DIR}

Sets the [`cache_dir`](./platformio-ini/platformio/cache-dir.md) option of every project. It overrides the value in `platformio.ini`.

### `PLATFORMIO_CORE_DIR` {#envvar-PLATFORMIO_CORE_DIR}

Sets the [`core_dir`](./platformio-ini/platformio/core-dir.md) option of every project. It overrides the value in `platformio.ini`.

### `PLATFORMIO_DATA_DIR` {#envvar-PLATFORMIO_DATA_DIR}

Sets the [`data_dir`](./platformio-ini/platformio/data-dir.md) option of every project. It overrides the value in `platformio.ini`.

### `PLATFORMIO_GLOBALLIB_DIR` {#envvar-PLATFORMIO_GLOBALLIB_DIR}

Sets the [`globallib_dir`](./platformio-ini/platformio/globallib-dir.md) option of every project. It overrides the value in `platformio.ini`.

### `PLATFORMIO_INCLUDE_DIR` {#envvar-PLATFORMIO_INCLUDE_DIR}

Sets the [`include_dir`](./platformio-ini/platformio/include-dir.md) option of every project. It overrides the value in `platformio.ini`.

### `PLATFORMIO_LIBDEPS_DIR` {#envvar-PLATFORMIO_LIBDEPS_DIR}

Sets the [`libdeps_dir`](./platformio-ini/platformio/libdeps-dir.md) option of every project. It overrides the value in `platformio.ini`.

### `PLATFORMIO_LIB_DIR` {#envvar-PLATFORMIO_LIB_DIR}

Sets the [`lib_dir`](./platformio-ini/platformio/lib-dir.md) option of every project. It overrides the value in `platformio.ini`.

### `PLATFORMIO_MONITOR_DIR` {#envvar-PLATFORMIO_MONITOR_DIR}

Sets the [`monitor_dir`](./platformio-ini/platformio/monitor-dir.md) option of every project. It overrides the value in `platformio.ini`.

### `PLATFORMIO_PACKAGES_DIR` {#envvar-PLATFORMIO_PACKAGES_DIR}

Sets the [`packages_dir`](./platformio-ini/platformio/packages-dir.md) option of every project. It overrides the value in `platformio.ini`.

### `PLATFORMIO_PLATFORMS_DIR` {#envvar-PLATFORMIO_PLATFORMS_DIR}

Sets the [`platforms_dir`](./platformio-ini/platformio/platforms-dir.md) option of every project. It overrides the value in `platformio.ini`.

### `PLATFORMIO_SHARED_DIR` {#envvar-PLATFORMIO_SHARED_DIR}

Sets the [`shared_dir`](./platformio-ini/platformio/shared-dir.md) option of every project. It overrides the value in `platformio.ini`.

### `PLATFORMIO_SRC_DIR` {#envvar-PLATFORMIO_SRC_DIR}

Sets the [`src_dir`](./platformio-ini/platformio/src-dir.md) option of every project. It overrides the value in `platformio.ini`.

### `PLATFORMIO_TEST_DIR` {#envvar-PLATFORMIO_TEST_DIR}

Sets the [`test_dir`](./platformio-ini/platformio/test-dir.md) option of every project. It overrides the value in `platformio.ini`.

### `PLATFORMIO_WORKSPACE_DIR` {#envvar-PLATFORMIO_WORKSPACE_DIR}

Sets the [`workspace_dir`](./platformio-ini/platformio/workspace-dir.md) option of every project. It overrides the value in `platformio.ini`.

## Settings {#settings}

Every [setting](./cli/pio-settings.md#settings) can be overridden with
`PLATFORMIO_SETTING_<NAME>`, where `<NAME>` is the setting name in upper case.
For example, `PLATFORMIO_SETTING_ENABLE_TELEMETRY=no`.

### `PLATFORMIO_SETTING_CHECK_PLATFORMIO_INTERVAL` {#envvar-PLATFORMIO_SETTING_CHECK_PLATFORMIO_INTERVAL}

Overrides the [`check_platformio_interval`](./cli/pio-settings.md#setting-check-platformio-interval) setting.

### `PLATFORMIO_SETTING_CHECK_PRUNE_SYSTEM_THRESHOLD` {#envvar-PLATFORMIO_SETTING_CHECK_PRUNE_SYSTEM_THRESHOLD}

Overrides the [`check_prune_system_threshold`](./cli/pio-settings.md#setting-check-prune-system-threshold) setting.

### `PLATFORMIO_SETTING_ENABLE_CACHE` {#envvar-PLATFORMIO_SETTING_ENABLE_CACHE}

Overrides the [`enable_cache`](./cli/pio-settings.md#setting-enable-cache) setting.

### `PLATFORMIO_SETTING_ENABLE_TELEMETRY` {#envvar-PLATFORMIO_SETTING_ENABLE_TELEMETRY}

Overrides the [`enable_telemetry`](./cli/pio-settings.md#setting-enable-telemetry) setting.

### `PLATFORMIO_SETTING_FORCE_VERBOSE` {#envvar-PLATFORMIO_SETTING_FORCE_VERBOSE}

Overrides the [`force_verbose`](./cli/pio-settings.md#setting-force-verbose) setting.

### `PLATFORMIO_SETTING_PROJECTS_DIR` {#envvar-PLATFORMIO_SETTING_PROJECTS_DIR}

Overrides the [`projects_dir`](./cli/pio-settings.md#setting-projects-dir) setting.

### `PLATFORMIO_SETTING_ENABLE_PROXY_STRICT_SSL` {#envvar-PLATFORMIO_SETTING_ENABLE_PROXY_STRICT_SSL}

Overrides the [`enable_proxy_strict_ssl`](./cli/pio-settings.md#setting-enable-proxy-strict-ssl) setting.

### `PLATFORMIO_SETTING_DISABLE_UDEV_RULES_CHECK` {#envvar-PLATFORMIO_SETTING_DISABLE_UDEV_RULES_CHECK}

Overrides the [`disable_udev_rules_check`](./cli/pio-settings.md#setting-disable-udev-rules-check) setting.
