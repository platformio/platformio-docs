---
description: "Run remotely tests from PlatformIO based project."
---

# pio remote test

Helper command for remote [Unit Testing](../../../guides/unit-testing/index.md).

## Usage {#usage}

```bash
pio remote test [OPTIONS]

# run tests on specified PlatformIO Remote Agent
pio remote --agent NAME test [OPTIONS]
```

## Description {#description}

Run remotely tests from PlatformIO based project. More details about PlatformIO [Unit Testing](../../../guides/unit-testing/index.md).

This command allows you to apply the tests for the environments specified in [`platformio.ini`](../../platformio-ini/index.md).

## Options {#options}

<a id="cmdoption-pio-remote-test-environment"></a>

### `-e, --environment` {#cmdoption-pio-remote-test-e}

Process specified environments. More details [`pio run --environment`](../pio-run.md#cmdoption-pio-run-e)

<a id="cmdoption-pio-remote-test-filter"></a>

### `-f, --filter` {#cmdoption-pio-remote-test-f}

Process only the tests where the name matches specified patterns. More than one pattern is allowed. If you need to filter some tests for a specific environment, please take a look at [test_filter](../../platformio-ini/env/test-filter.md) option from [`platformio.ini`](../../platformio-ini/index.md).

| Pattern | Meaning |
|---|---|
| `*` | matches everything |
| `?` | matches any single character |
| `[seq]` | matches any character in seq |
| `[!seq]` | matches any character not in seq |

For example, `pio test --filter "mytest*" -i "test[13]"`

<a id="cmdoption-pio-remote-test-ignore"></a>

### `-i, --ignore` {#cmdoption-pio-remote-test-i}

Ignore tests where the name matches specified patterns. More than one pattern is allowed. If you need to ignore some tests for the specific environment, please take a look at [test_ignore](../../platformio-ini/env/test-ignore.md) option from [`platformio.ini`](../../platformio-ini/index.md).

| Pattern | Meaning |
|---|---|
| `*` | matches everything |
| `?` | matches any single character |
| `[seq]` | matches any character in seq |
| `[!seq]` | matches any character not in seq |

For example, `pio remote test --ignore "mytest*" -i "test[13]"`

### `--upload-port` {#cmdoption-pio-remote-test-upload-port}

A port that is intended for firmware uploading. To list available ports please use [pio device list](../pio-device/list.md) command.

If upload port is not specified, PlatformIO will try to detect it automatically.

### `--test-port` {#cmdoption-pio-remote-test-test-port}

A Serial/UART port that PlatformIO uses as communication interface between PlatformIO Unit Test Engine and target device. To list available ports please use [pio device list](../pio-device/list.md) command.

If test port is not specified, PlatformIO will try to detect it automatically.

<a id="cmdoption-pio-remote-test-project-dir"></a>

### `-d, --project-dir` {#cmdoption-pio-remote-test-d}

The project directory. Default: the current working directory.

<a id="cmdoption-pio-remote-test-force-remote"></a>

### `-r, --force-remote` {#cmdoption-pio-remote-test-r}

By default, [Remote Development](../../../guides/remote-development.md) processes project on a host machine and deploy final testing firmware (program) to remote device (embedded board).

If you need to process project on remote machine, please use [`pio remote test --force-remote`](#cmdoption-pio-remote-test-r) option. In this case, [Remote Development](../../../guides/remote-development.md) will automatically synchronize your project with remote machine, install required toolchains, frameworks, SDKs, etc., and process project.

### `--without-building` {#cmdoption-pio-remote-test-without-building}

Skip building stage.

### `--without-uploading` {#cmdoption-pio-remote-test-without-uploading}

Skip uploading stage

<a id="cmdoption-pio-remote-test-verbose"></a>

### `-v, --verbose` {#cmdoption-pio-remote-test-v}

Print detailed information while processing environments.

This option can also be set globally using [force_verbose](../pio-settings.md#setting-force-verbose) setting or by environment variable [`PLATFORMIO_SETTING_FORCE_VERBOSE`](../../environment-variables.md#envvar-PLATFORMIO_SETTING_FORCE_VERBOSE).

## Examples {#examples}

For the examples see [Unit Testing](../../../guides/unit-testing/index.md) page.
