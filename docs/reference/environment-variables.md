<a id="envvars"></a>

# Environment Variables {#environment-variables}

[Environment variables](http://en.wikipedia.org/wiki/Environment_variable) are a set of dynamic named values that can affect the way running processes will behave on a computer. PlatformIO handles variables which start with `PLATFORMIO_` prefix.

How to set environment variable?

```bash
# Windows
set VARIABLE_NAME=VALUE

# Windows GUI -> https://www.youtube.com/watch?v=bEroNNzqlF4

# Unix (bash, zsh)
export VARIABLE_NAME=VALUE

# Unix (fish)
set -x VARIABLE_NAME VALUE
```

## General {#general}

PlatformIO uses *General* environment variables for the common operations/commands.

### `CI` {#envvar-CI}

PlatformIO handles `CI` variable which is setup by [Continuous Integration](http://en.wikipedia.org/wiki/Continuous_integration) (Travis, Circle and etc.) systems. PlatformIO uses it to disable prompts and progress bars. In other words, `CI=true` automatically setup [`PLATFORMIO_DISABLE_PROGRESSBAR`](#envvar-PLATFORMIO_DISABLE_PROGRESSBAR) to `true`.

### `PLATFORMIO_AUTH_TOKEN` {#envvar-PLATFORMIO_AUTH_TOKEN}

Allows one to specify Personal Authentication Token that could be used for automatic login in to [PlatformIO Account](../get-started/platformio-account.md). It is very useful for [Continuous Integration](../guides/ci/index.md) systems and [Remote Development](../guides/remote-development.md) operations where you are not able manually authorize.

You can get own Personal Authentication Token using [pio account token](./cli/pio-account/token.md) command.

### `PLATFORMIO_FORCE_ANSI` {#envvar-PLATFORMIO_FORCE_ANSI}

Force to output ANSI control character even if the output is a `pipe` (not a `tty`). The possible values are `true` and `false`. Default is `PLATFORMIO_FORCE_ANSI=false`.

### `PLATFORMIO_NO_ANSI` {#envvar-PLATFORMIO_NO_ANSI}

Do not print ANSI control characters. The possible values are `true` and `false`. Default is `PLATFORMIO_NO_ANSI=false`.

You can also use [`pio --no-ansi`](./cli/index.md#cmdoption-pio-no-ansi) flag for [PlatformIO Core (CLI)](../get-started/platformio-core.md).

### `PLATFORMIO_DISABLE_PROGRESSBAR` {#envvar-PLATFORMIO_DISABLE_PROGRESSBAR}

Disable progress bar for package/library downloader and uploader. This is useful when calling PlatformIO from subprocess and output is a `pipe` (not a `tty`). The possible values are `true` and `false`. Default is `PLATFORMIO_DISABLE_PROGRESSBAR=false`.

### `PLATFORMIO_DISABLE_UPGRADE_CHECK` {#envvar-PLATFORMIO_DISABLE_UPGRADE_CHECK}

Disable upgrade availability checks. The possible values are `true` and `false`. Default is `PLATFORMIO_DISABLE_UPGRADE_CHECK=false`.

### `PLATFORMIO_SYSTEM_TYPE` {#envvar-PLATFORMIO_SYSTEM_TYPE}

This environment variable allows you to manually specify the system type, overriding the automatic detection. Examples:

- `windows_amd64`
- `windows_arm64`
- `linux_x86_64`
- `linux_armv7l`
- `darwin_arm64`

### `PLATFORMIO_RUN_JOBS` {#envvar-PLATFORMIO_RUN_JOBS}

Allows one to override [`pio run --jobs`](./cli/pio-run.md#cmdoption-pio-run-j).

## Directories {#directories}

### `PLATFORMIO_CORE_DIR` {#envvar-PLATFORMIO_CORE_DIR}

Allows one to override ["platformio.ini" (Project Configuration File)](./platformio-ini/index.md) option [core_dir](./platformio-ini/platformio/core-dir.md).

It may need to re-install [PlatformIO Core (CLI)](../get-started/platformio-core.md) (remove default core directory) to take effect.

### `PLATFORMIO_GLOBALLIB_DIR` {#envvar-PLATFORMIO_GLOBALLIB_DIR}

Allows one to override ["platformio.ini" (Project Configuration File)](./platformio-ini/index.md) option [globallib_dir](./platformio-ini/platformio/globallib-dir.md).

### `PLATFORMIO_PLATFORMS_DIR` {#envvar-PLATFORMIO_PLATFORMS_DIR}

Allows one to override ["platformio.ini" (Project Configuration File)](./platformio-ini/index.md) option [platforms_dir](./platformio-ini/platformio/platforms-dir.md).

### `PLATFORMIO_PACKAGES_DIR` {#envvar-PLATFORMIO_PACKAGES_DIR}

Allows one to override ["platformio.ini" (Project Configuration File)](./platformio-ini/index.md) option [packages_dir](./platformio-ini/platformio/packages-dir.md).

### `PLATFORMIO_CACHE_DIR` {#envvar-PLATFORMIO_CACHE_DIR}

Allows one to override ["platformio.ini" (Project Configuration File)](./platformio-ini/index.md) option [cache_dir](./platformio-ini/platformio/cache-dir.md).

### `PLATFORMIO_BUILD_CACHE_DIR` {#envvar-PLATFORMIO_BUILD_CACHE_DIR}

Allows one to override ["platformio.ini" (Project Configuration File)](./platformio-ini/index.md) option [build_cache_dir](./platformio-ini/platformio/build-cache-dir.md).

### `PLATFORMIO_WORKSPACE_DIR` {#envvar-PLATFORMIO_WORKSPACE_DIR}

Allows one to override ["platformio.ini" (Project Configuration File)](./platformio-ini/index.md) option [workspace_dir](./platformio-ini/platformio/workspace-dir.md).

### `PLATFORMIO_INCLUDE_DIR` {#envvar-PLATFORMIO_INCLUDE_DIR}

Allows one to override ["platformio.ini" (Project Configuration File)](./platformio-ini/index.md) option [include_dir](./platformio-ini/platformio/include-dir.md).

### `PLATFORMIO_SRC_DIR` {#envvar-PLATFORMIO_SRC_DIR}

Allows one to override ["platformio.ini" (Project Configuration File)](./platformio-ini/index.md) option [src_dir](./platformio-ini/platformio/src-dir.md).

### `PLATFORMIO_LIB_DIR` {#envvar-PLATFORMIO_LIB_DIR}

Allows one to override ["platformio.ini" (Project Configuration File)](./platformio-ini/index.md) option [lib_dir](./platformio-ini/platformio/lib-dir.md).

### `PLATFORMIO_LIBDEPS_DIR` {#envvar-PLATFORMIO_LIBDEPS_DIR}

Allows one to override ["platformio.ini" (Project Configuration File)](./platformio-ini/index.md) option [libdeps_dir](./platformio-ini/platformio/libdeps-dir.md).

### `PLATFORMIO_BUILD_DIR` {#envvar-PLATFORMIO_BUILD_DIR}

Allows one to override ["platformio.ini" (Project Configuration File)](./platformio-ini/index.md) option [build_dir](./platformio-ini/platformio/build-dir.md).

### `PLATFORMIO_DATA_DIR` {#envvar-PLATFORMIO_DATA_DIR}

Allows one to override ["platformio.ini" (Project Configuration File)](./platformio-ini/index.md) option [data_dir](./platformio-ini/platformio/data-dir.md).

### `PLATFORMIO_TEST_DIR` {#envvar-PLATFORMIO_TEST_DIR}

Allows one to override ["platformio.ini" (Project Configuration File)](./platformio-ini/index.md) option [test_dir](./platformio-ini/platformio/test-dir.md).

### `PLATFORMIO_BOARDS_DIR` {#envvar-PLATFORMIO_BOARDS_DIR}

Allows one to override ["platformio.ini" (Project Configuration File)](./platformio-ini/index.md) option [boards_dir](./platformio-ini/platformio/boards-dir.md).

### `PLATFORMIO_MONITOR_DIR` {#envvar-PLATFORMIO_MONITOR_DIR}

Allows one to override ["platformio.ini" (Project Configuration File)](./platformio-ini/index.md) option [monitor_dir](./platformio-ini/platformio/monitor-dir.md).

### `PLATFORMIO_SHARED_DIR` {#envvar-PLATFORMIO_SHARED_DIR}

Allows one to override ["platformio.ini" (Project Configuration File)](./platformio-ini/index.md) option [shared_dir](./platformio-ini/platformio/shared-dir.md).

### `PLATFORMIO_REMOTE_AGENT_DIR` {#envvar-PLATFORMIO_REMOTE_AGENT_DIR}

Allows one to override [`pio remote agent start --working-dir`](./cli/pio-remote/agent.md#cmdoption-pio-remote-agent-start-d).

## Building {#building}

### `PLATFORMIO_BUILD_FLAGS` {#envvar-PLATFORMIO_BUILD_FLAGS}

Allows one to set ["platformio.ini" (Project Configuration File)](./platformio-ini/index.md) option [build_flags](./platformio-ini/env/build-flags.md).

Examples:

```bash
# Unix:
export PLATFORMIO_BUILD_FLAGS=-DFOO
export PLATFORMIO_BUILD_FLAGS=-DFOO -DBAR=1 -Wall

# Windows:
SET PLATFORMIO_BUILD_FLAGS=-DFOO
SET PLATFORMIO_BUILD_FLAGS=-DFOO -DBAR=1 -Wall
```

:::warning

Consider using [Interpolation of Values](../guides/projects/interpolation.md) instead of `PLATFORMIO_BUILD_FLAGS` environment variable if additional build flags contain preprocessor directive with special characters (`$`, `&`, `~`, etc) in its value.

:::

### `PLATFORMIO_BUILD_SRC_FLAGS` {#envvar-PLATFORMIO_BUILD_SRC_FLAGS}

Allows one to set ["platformio.ini" (Project Configuration File)](./platformio-ini/index.md) option [build_src_flags](./platformio-ini/env/build-src-flags.md).

### `PLATFORMIO_BUILD_SRC_FILTER` {#envvar-PLATFORMIO_BUILD_SRC_FILTER}

Allows one to set ["platformio.ini" (Project Configuration File)](./platformio-ini/index.md) option [build_src_filter](./platformio-ini/env/build-src-filter.md).

### `PLATFORMIO_EXTRA_SCRIPTS` {#envvar-PLATFORMIO_EXTRA_SCRIPTS}

Allows one to set ["platformio.ini" (Project Configuration File)](./platformio-ini/index.md) option [extra_scripts](./platformio-ini/env/extra-scripts.md).

### `PLATFORMIO_DEFAULT_ENVS` {#envvar-PLATFORMIO_DEFAULT_ENVS}

Allows one to set ["platformio.ini" (Project Configuration File)](./platformio-ini/index.md) option [default_envs](./platformio-ini/platformio/default-envs.md).

## Uploading {#uploading}

### `PLATFORMIO_UPLOAD_PORT` {#envvar-PLATFORMIO_UPLOAD_PORT}

Allows one to set ["platformio.ini" (Project Configuration File)](./platformio-ini/index.md) option [upload_port](./platformio-ini/env/upload-port.md).

### `PLATFORMIO_UPLOAD_FLAGS` {#envvar-PLATFORMIO_UPLOAD_FLAGS}

Allows one to set ["platformio.ini" (Project Configuration File)](./platformio-ini/index.md) option [upload_flags](./platformio-ini/env/upload-flags.md).

## Settings {#settings}

Allows one to override PlatformIO settings. You can manage them via [pio settings](./cli/pio-settings.md) command.

### `PLATFORMIO_SETTING_CHECK_PLATFORMIO_INTERVAL` {#envvar-PLATFORMIO_SETTING_CHECK_PLATFORMIO_INTERVAL}

Allows one to override setting [check_platformio_interval](./cli/pio-settings.md#setting-check-platformio-interval).

### `PLATFORMIO_SETTING_CHECK_PRUNE_SYSTEM_THRESHOLD` {#envvar-PLATFORMIO_SETTING_CHECK_PRUNE_SYSTEM_THRESHOLD}

Allows one to override setting [check_prune_system_threshold](./cli/pio-settings.md#setting-check-prune-system-threshold).

### `PLATFORMIO_SETTING_ENABLE_CACHE` {#envvar-PLATFORMIO_SETTING_ENABLE_CACHE}

Allows one to override setting [enable_cache](./cli/pio-settings.md#setting-enable-cache).

### `PLATFORMIO_SETTING_ENABLE_TELEMETRY` {#envvar-PLATFORMIO_SETTING_ENABLE_TELEMETRY}

Allows one to override setting [enable_telemetry](./cli/pio-settings.md#setting-enable-telemetry).

### `PLATFORMIO_SETTING_FORCE_VERBOSE` {#envvar-PLATFORMIO_SETTING_FORCE_VERBOSE}

Allows one to override setting [force_verbose](./cli/pio-settings.md#setting-force-verbose).

### `PLATFORMIO_SETTING_PROJECTS_DIR` {#envvar-PLATFORMIO_SETTING_PROJECTS_DIR}

Allows one to override setting [projects_dir](./cli/pio-settings.md#setting-projects-dir).

### `PLATFORMIO_SETTING_ENABLE_PROXY_STRICT_SSL` {#envvar-PLATFORMIO_SETTING_ENABLE_PROXY_STRICT_SSL}

Allows one to override setting [enable_proxy_strict_ssl](./cli/pio-settings.md#setting-enable-proxy-strict-ssl).

### `PLATFORMIO_SETTING_DISABLE_UDEV_RULES_CHECK` {#envvar-PLATFORMIO_SETTING_DISABLE_UDEV_RULES_CHECK}

Allows one to override setting [disable_udev_rules_check](./cli/pio-settings.md#setting-disable-udev-rules-check).
