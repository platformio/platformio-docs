---
description: View, change and reset PlatformIO Core settings, and the reference of every setting.
---

<a id="cmd-settings"></a>

# pio settings {#pio-settings}

View, change and reset PlatformIO Core settings. Settings apply to all
projects of the current user.

You can also override any setting for a single run with the environment
variable `PLATFORMIO_SETTING_<NAME>`, for example
`PLATFORMIO_SETTING_ENABLE_TELEMETRY=no`. See
[Environment variables](../environment-variables.md).

## Commands {#commands}

<a id="cmd-settings-get"></a>

### pio settings get {#pio-settings-get}

Show all settings, or one setting, with the current and default values.

```bash
pio settings get [NAME]
```

Show all settings:

```bash
pio settings get
```

```text
Name                            Value [Default]   Description
------------------------------------------------------------------------------------------
check_platformio_interval       7                 Check for the new PlatformIO Core interval (days)
check_prune_system_threshold    1024              Check for pruning unnecessary data threshold (megabytes)
enable_cache                    Yes               Enable caching for HTTP API requests
enable_telemetry                Yes               Telemetry service <https://bit.ly/pio-telemetry> (Yes/No)
force_verbose                   No                Force verbose output when processing environments
projects_dir                    ~/Documents/PlatformIO/Projects Default location for PlatformIO projects (PlatformIO Home)
```

Show one setting:

```bash
pio settings get check_prune_system_threshold
```

```text
Name                            Value [Default]   Description
------------------------------------------------------------------------------------------
check_prune_system_threshold    1024              Check for pruning unnecessary data threshold (megabytes)
```

<a id="cmd-settings-set"></a>

### pio settings set {#pio-settings-set}

Change a setting.

```bash
pio settings set NAME VALUE
```

For Yes/No settings, `yes`, `y`, `true` and `1` (case-insensitive) mean Yes;
any other value means No.

Check for a new PlatformIO Core version every day:

```bash
pio settings set check_platformio_interval 1
```

```text
The new value for the setting has been set!
Name                            Value [Default]   Description
------------------------------------------------------------------------------------------
check_platformio_interval       1 [7]             Check for the new PlatformIO interval (days)
```

<a id="cmd-settings-reset"></a>

### pio settings reset {#pio-settings-reset}

Reset all settings to their defaults.

```bash
pio settings reset
```

```text
The settings have been reset!
Name                            Value [Default]   Description
------------------------------------------------------------------------------------------
check_platformio_interval       7                 Check for the new PlatformIO Core interval (days)
check_prune_system_threshold    1024              Check for pruning unnecessary data threshold (megabytes)
enable_cache                    Yes               Enable caching for HTTP API requests
enable_telemetry                Yes               Telemetry service <https://bit.ly/pio-telemetry> (Yes/No)
force_verbose                   No                Force verbose output when processing environments
projects_dir                    ~/Documents/PlatformIO/Projects Default location for PlatformIO projects (PlatformIO Home)
```

<a id="usage"></a>
<a id="description"></a>

## Settings {#settings}

<a id="setting-check-platformio-interval"></a>

### `check_platformio_interval` {#check-platformio-interval}

How often, in days, to check for a new version of PlatformIO Core.

- Type: number (days)
- Default: `7`

<a id="setting-check-prune-system-threshold"></a>

### `check_prune_system_threshold` {#check-prune-system-threshold}

When unused PlatformIO data (cached and unused packages) exceeds this size, in
megabytes, PlatformIO suggests running [`pio system prune`](./pio-system/prune.md).
Set it to `0` to turn the check off. To see what would be removed, run
[`pio system prune --dry-run`](./pio-system/prune.md#cmdoption-pio-system-prune-dry-run).

- Type: number (megabytes)
- Default: `1024`

<a id="setting-enable-cache"></a>

### `enable_cache` {#enable-cache}

Cache the responses of the package manager and of API requests.

- Type: Yes/No
- Default: Yes

<a id="setting-force-verbose"></a>

### `force_verbose` {#force-verbose}

Always print verbose output when processing environments, as if you passed
`--verbose` to [`pio run`](./pio-run.md#cmdoption-pio-run-v),
[`pio ci`](./pio-ci.md#cmdoption-pio-ci-v) or
[`pio test`](./pio-test.md#cmdoption-pio-test-v).

- Type: Yes/No
- Default: No

<a id="setting-projects-dir"></a>

### `projects_dir` {#projects-dir}

The default folder for new projects created in
[PlatformIO Home](../../get-started/platformio-home.md). The folder must exist.

- Type: path
- Default: `~/Documents/PlatformIO/Projects`

<a id="setting-enable-proxy-strict-ssl"></a>

### `enable_proxy_strict_ssl` {#enable-proxy-strict-ssl}

Verify the proxy server's certificate against the trusted certificate
authorities. Turn it off if your proxy uses its own certificate. See
[Configure a proxy](../../get-started/install/proxy-configuration.md).

- Type: Yes/No
- Default: Yes

<a id="setting-disable-udev-rules-check"></a>

### `disable_udev_rules_check` {#disable-udev-rules-check}

Linux only. Do not check whether the
[udev rules](../../get-started/install/udev-rules.md) are installed.

- Type: Yes/No
- Default: No

<a id="setting-enable-telemetry"></a>

### `enable_telemetry` {#enable-telemetry}

Send anonymous usage and diagnostic data that helps us improve PlatformIO.
The [telemetry code](https://github.com/platformio/platformio-core/blob/develop/platformio/telemetry.py)
is open source. It never sends your source code.

- Type: Yes/No
- Default: Yes

When enabled, PlatformIO Core sends:

| Data | Why |
| --- | --- |
| A client ID (a one-way hash of the computer's network hardware address, or of the `GITHUB_USER` or `GITPOD_GIT_USER_NAME` value when set), the date PlatformIO was first run, and the host system type (operating system and architecture) | To count active installations and know which hosts to support |
| The command you run, for example `run` or `pkg install`, and, in CI, the CI service name | To learn which commands to improve |
| For builds and debug sessions: the `platform`, `framework`, `board`, `upload_protocol`, `check_tool`, `debug_tool` and `test_framework` options, the platform version, the project targets, and a one-way hash of the project path | To prioritize platforms, boards and tools |
| Internal errors of PlatformIO Core: the error type and message, the traceback (with file paths shortened to PlatformIO's own modules), and the command-line arguments; for debugging errors, the message with paths shortened | To find and fix bugs |

Errors caused by your project, such as compiler errors, are not sent.
