<a id="cmd-settings"></a>

# pio settings {#pio-settings}

Manage PlatformIO settings

<a id="cmd-settings-get"></a>

## pio settings get {#pio-settings-get}

### Usage {#usage}

```bash
pio settings get [NAME]
```

### Description {#description}

:::note

- The `Yes` value is equal to: `True`, `Y`, `1` and is not case sensitive.
- You can override these settings using [Environment Variables](../environment-variables.md).

:::

Get/List existing settings

### Settings {#settings}

<a id="setting-check-platformio-interval"></a>

#### `check_platformio_interval` {#check-platformio-interval}

<dl>

<dt>

Default

</dt>

<dd>

7

</dd>

<dt>

Values

</dt>

<dd>

Days (Number)

</dd>

</dl>

An interval for checking for the new version of PlatformIO Core.

<a id="setting-check-prune-system-threshold"></a>

#### `check_prune_system_threshold` {#check-prune-system-threshold}

<dl>

<dt>

Default

</dt>

<dd>

1024

</dd>

<dt>

Values

</dt>

<dd>

Megabytes (Number)

</dd>

</dl>

Check for pruning unnecessary data threshold (megabytes). You can list unnecessary PlatformIO system data using [`pio system prune --dry-run`](./pio-system/prune.md#cmdoption-pio-system-prune-dry-run) command. See [pio system prune](./pio-system/prune.md) for the other options.

Do disable checking for unnecessary data, please set threshold to `0` using [pio settings set](#cmd-settings-set) command.

<a id="setting-enable-cache"></a>

#### `enable_cache` {#enable-cache}

<dl>

<dt>

Default

</dt>

<dd>

Yes

</dd>

<dt>

Values

</dt>

<dd>

Yes/No

</dd>

</dl>

Enable caching for Package Manager and for API requests.

<a id="setting-force-verbose"></a>

#### `force_verbose` {#force-verbose}

<dl>

<dt>

Default

</dt>

<dd>

No

</dd>

<dt>

Values

</dt>

<dd>

Yes/No

</dd>

</dl>

Force verbose output when processing environments. This setting overrides

- [`pio run --verbose`](./pio-run.md#cmdoption-pio-run-v)
- [`pio ci --verbose`](./pio-ci.md#cmdoption-pio-ci-v)
- [`pio test --verbose`](./pio-test.md#cmdoption-pio-test-v)

<a id="setting-projects-dir"></a>

#### `projects_dir` {#projects-dir}

<dl>

<dt>

Default

</dt>

<dd>

\~/Documents/PlatformIO/Projects

</dd>

<dt>

Values

</dt>

<dd>

Path to folder

</dd>

</dl>

Default location for PlatformIO projects (PlatformIO Home).

<a id="setting-enable-proxy-strict-ssl"></a>

#### `enable_proxy_strict_ssl` {#enable-proxy-strict-ssl}

<dl>

<dt>

Default

</dt>

<dd>

Yes

</dd>

<dt>

Values

</dt>

<dd>

Yes/No

</dd>

</dl>

Verify the proxy server certificate against the list of supplied CAs. See also PlatformIO Core [Proxy Configuration](../../get-started/install/proxy-configuration.md).

<a id="setting-disable-udev-rules-check"></a>

#### `disable_udev_rules_check` {#disable-udev-rules-check}

<dl>

<dt>

Default

</dt>

<dd>

No

</dd>

<dt>

Values

</dt>

<dd>

Yes/No

</dd>

</dl>

Disable check for udev rules on Linux. See [99-platformio-udev.rules](../../get-started/install/udev-rules.md) for more details about udev rules and how to install them.

<a id="setting-enable-telemetry"></a>

#### `enable_telemetry` {#enable-telemetry}

<dl>

<dt>

Default

</dt>

<dd>

Yes

</dd>

<dt>

Values

</dt>

<dd>

Yes/No

</dd>

</dl>

Share minimal diagnostics and usage information to help us make PlatformIO better.

The source code of telemetry service is [open source](https://github.com/platformio/platformio-core/blob/develop/platformio/telemetry.py). You can make sure that we **DO NOT SHARE PRIVATE** information or source code of your project. All information shares **ANONYMOUSLY**.

Which data do we collect and why?

- **A version of Python Interpreter**. [PlatformIO Core (CLI)](../../get-started/platformio-core.md) is written in [Python language](https://www.python.org/), including development [Development Platforms](../../hardware/platforms/index.md). We need to know which Python version produces such type of exceptions (see below), which is more popular, which version we should drop and focus on a new one
- [PlatformIO Core (CLI)](../../get-started/platformio-core.md) **errors/exceptions**. We report automatically fatal exceptions raised by [PlatformIO Core source code](https://github.com/platformio/platformio-core) but NOT by your project
- **The name of the used platform, board, framework**. We collect this type of information to have a clear picture which software products are the most widely used by our Community and for the which we should provide frequent updates and add new features ( for example, "atmelavr", "arduino", "uno", etc.)
- **The name of CLI command**. It helps us to improve our CLI. For example, "run", "lib list")
- The name of [Cloud & Desktop IDEs](../../guides/ide/index.md). This is very important information for us. We create native extensions based on the popularity of IDEs (for example, [PlatformIO IDE for VSCode](../../guides/ide/vscode.md), [CLion](../../guides/ide/clion.md))

**Thanks a lot that you keep this setting enabled!**

### Examples {#examples}

1. List all settings and theirs current values

```text
> pio settings get

Name                            Value [Default]   Description
------------------------------------------------------------------------------------------
check_platformio_interval       7                 Check for the new PlatformIO Core interval (days)
check_prune_system_threshold    1024              Check for pruning unnecessary data threshold (megabytes)
enable_cache                    Yes               Enable caching for HTTP API requests
enable_telemetry                Yes               Telemetry service <https://bit.ly/pio-telemetry> (Yes/No)
force_verbose                   No                Force verbose output when processing environments
projects_dir                    ~/Documents/PlatformIO/Projects Default location for PlatformIO projects (PlatformIO Home)
```

2. Show specified setting

```bash
> pio settings get check_prune_system_threshold
Name                            Value [Default]   Description
------------------------------------------------------------------------------------------
check_prune_system_threshold    1024              Check for pruning unnecessary data threshold (megabytes)
```

<a id="cmd-settings-set"></a>

## pio settings set {#pio-settings-set}

### Usage

```bash
pio settings set NAME VALUE
```

### Description

Set new value for the setting

### Examples

Change to check for the new PlatformIO Core each day

```bash
> pio settings set check_platformio_interval 1
The new value for the setting has been set!
Name                            Value [Default]   Description
------------------------------------------------------------------------------------------
check_platformio_interval       1 [7]             Check for the new PlatformIO interval (days)
```

<a id="cmd-settings-reset"></a>

## pio settings reset {#pio-settings-reset}

### Usage

```bash
pio settings reset
```

### Description

Reset settings to default

### Examples

```bash
> pio settings reset
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
