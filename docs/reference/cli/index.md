---
description: Reference of the pio command-line interface - global options and all commands.
---

<a id="piocore-userguide"></a>

# CLI reference {#cli-guide}

The `pio` command (also available as `platformio`) is the command-line
interface of [PlatformIO Core](../../get-started/platformio-core.md).

## Usage {#usage}

```bash
pio [OPTIONS] COMMAND [ARGS]...
```

## Options {#options}

These options go before the command, for example `pio --no-ansi run`.

### `--version` {#cmdoption-pio-version}

Show the PlatformIO Core version and exit.

### `-c, --caller` {#cmdoption-pio-caller}

The ID of the application that runs PlatformIO Core, for example an IDE
extension. Integrations use it to identify themselves.

### `--no-ansi` {#cmdoption-pio-no-ansi}

Do not print ANSI control characters, such as colors. See also the
[`PLATFORMIO_NO_ANSI`](../environment-variables.md#envvar-PLATFORMIO_NO_ANSI)
and [`PLATFORMIO_FORCE_ANSI`](../environment-variables.md#envvar-PLATFORMIO_FORCE_ANSI)
environment variables.

<a id="cmdoption-pio-h"></a>

### `-h, --help` {#cmdoption-pio-help}

Show the available options and commands. It works for every command:

```bash
pio --help
pio COMMAND --help
```

## Commands {#commands}

| Command | Description |
| --- | --- |
| [`pio run`](./pio-run.md) | Build, upload and run other project targets |
| [`pio test`](./pio-test.md) | Run unit tests |
| [`pio check`](./pio-check.md) | Run static code analysis |
| [`pio debug`](./pio-debug.md) | Start a debug session |
| [`pio device`](./pio-device/index.md) | List devices and open a serial monitor |
| [`pio project`](./pio-project/index.md) | Create projects and inspect their configuration |
| [`pio pkg`](./pio-pkg/index.md) | Manage platforms, tools and libraries |
| [`pio boards`](./pio-boards.md) | List supported boards |
| [`pio ci`](./pio-ci.md) | Build code in continuous integration |
| [`pio home`](./pio-home.md) | Start PlatformIO Home |
| [`pio remote`](./pio-remote/index.md) | Work with devices on remote computers |
| [`pio account`](./pio-account/index.md) | Manage your PlatformIO Account |
| [`pio org`](./pio-org/index.md) | Manage organizations |
| [`pio team`](./pio-team/index.md) | Manage teams |
| [`pio access`](./pio-access/index.md) | Manage access to registry packages |
| [`pio settings`](./pio-settings.md) | View and change settings |
| [`pio system`](./pio-system/index.md) | System information, cleanup and shell completion |
| [`pio upgrade`](./pio-upgrade.md) | Upgrade PlatformIO Core |
