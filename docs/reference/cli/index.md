<a id="piocore-userguide"></a>

# CLI Guide {#cli-guide}

## Usage {#usage}

```bash
pio [OPTIONS] COMMAND
```

## Options {#options}

### `--no-ansi` {#cmdoption-pio-no-ansi}

Do not print ANSI control characters.

See also [`PLATFORMIO_NO_ANSI`](../environment-variables.md#envvar-PLATFORMIO_NO_ANSI) and [`PLATFORMIO_FORCE_ANSI`](../environment-variables.md#envvar-PLATFORMIO_FORCE_ANSI) environment variables.

### `--version` {#cmdoption-pio-version}

Show the version of PlatformIO

<a id="cmdoption-pio-h"></a>

### `--help, -h` {#cmdoption-pio-help}

Show help for the available options and commands

```bash
$ pio --help
$ pio COMMAND --help
```

## Commands {#commands}

- [pio access](./pio-access/index.md)

  - [pio access grant](./pio-access/grant.md)
  - [pio access list](./pio-access/list.md)
  - [pio access private](./pio-access/private.md)
  - [pio access public](./pio-access/public.md)
  - [pio access revoke](./pio-access/revoke.md)

- [pio account](./pio-account/index.md)

  - [pio account destroy](./pio-account/destroy.md)
  - [pio account forgot](./pio-account/forgot.md)
  - [pio account login](./pio-account/login.md)
  - [pio account logout](./pio-account/logout.md)
  - [pio account password](./pio-account/password.md)
  - [pio account register](./pio-account/register.md)
  - [pio account show](./pio-account/show.md)
  - [pio account token](./pio-account/token.md)
  - [pio account update](./pio-account/update.md)

- [pio boards](./pio-boards.md)

  - [Usage](./pio-boards.md#usage)
  - [Description](./pio-boards.md#description)
  - [Examples](./pio-boards.md#examples)

- [pio check](./pio-check.md)

  - [Usage](./pio-check.md#usage)
  - [Description](./pio-check.md#description)
  - [Options](./pio-check.md#options)
  - [Examples](./pio-check.md#examples)

- [pio ci](./pio-ci.md)

  - [Usage](./pio-ci.md#usage)
  - [Description](./pio-ci.md#description)
  - [Options](./pio-ci.md#options)
  - [Examples](./pio-ci.md#examples)

- [pio debug](./pio-debug.md)

  - [Usage](./pio-debug.md#usage)
  - [Description](./pio-debug.md#description)
  - [Options](./pio-debug.md#options)
  - [Examples](./pio-debug.md#examples)

- [pio device](./pio-device/index.md)

  - [pio device list](./pio-device/list.md)
  - [pio device monitor](./pio-device/monitor.md)

- [pio home](./pio-home.md)

  - [Usage](./pio-home.md#usage)
  - [Description](./pio-home.md#description)
  - [Options](./pio-home.md#options)
  - [Examples](./pio-home.md#examples)

- [pio org](./pio-org/index.md)

  - [pio org add](./pio-org/add.md)
  - [pio org create](./pio-org/create.md)
  - [pio org destroy](./pio-org/destroy.md)
  - [pio org list](./pio-org/list.md)
  - [pio org remove](./pio-org/remove.md)
  - [pio org update](./pio-org/update.md)

- [pio pkg](./pio-pkg/index.md)

  - [pio pkg exec](./pio-pkg/exec.md)
  - [pio pkg install](./pio-pkg/install.md)
  - [pio pkg list](./pio-pkg/list.md)
  - [pio pkg outdated](./pio-pkg/outdated.md)
  - [pio pkg pack](./pio-pkg/pack.md)
  - [pio pkg publish](./pio-pkg/publish.md)
  - [pio pkg search](./pio-pkg/search.md)
  - [pio pkg show](./pio-pkg/show.md)
  - [pio pkg uninstall](./pio-pkg/uninstall.md)
  - [pio pkg unpublish](./pio-pkg/unpublish.md)
  - [pio pkg update](./pio-pkg/update.md)

- [pio project](./pio-project/index.md)

  - [pio project config](./pio-project/config.md)
  - [pio project init](./pio-project/init.md)
  - [pio project metadata](./pio-project/metadata.md)

- [pio remote](./pio-remote/index.md)

  - [PlatformIO Remote Agent](./pio-remote/agent.md)
  - [pio remote device](./pio-remote/device.md)
  - [pio remote run](./pio-remote/run.md)
  - [pio remote test](./pio-remote/test.md)
  - [pio remote update](./pio-remote/update.md)

- [pio run](./pio-run.md)

  - [Usage](./pio-run.md#usage)
  - [Description](./pio-run.md#description)
  - [Options](./pio-run.md#options)
  - [Examples](./pio-run.md#examples)

- [pio settings](./pio-settings.md)

  - [pio settings get](./pio-settings.md#pio-settings-get)
  - [pio settings set](./pio-settings.md#pio-settings-set)
  - [pio settings reset](./pio-settings.md#pio-settings-reset)

- [pio system](./pio-system/index.md)

  - [PlatformIO Shell Completion](./pio-system/completion/index.md)
  - [pio system info](./pio-system/info.md)
  - [pio system prune](./pio-system/prune.md)

- [pio team](./pio-team/index.md)

  - [pio team add](./pio-team/add.md)
  - [pio team create](./pio-team/create.md)
  - [pio team destroy](./pio-team/destroy.md)
  - [pio team list](./pio-team/list.md)
  - [pio team remove](./pio-team/remove.md)
  - [pio team update](./pio-team/update.md)

- [pio test](./pio-test.md)

  - [Usage](./pio-test.md#usage)
  - [Description](./pio-test.md#description)
  - [Options](./pio-test.md#options)
  - [Examples](./pio-test.md#examples)

- [pio upgrade](./pio-upgrade.md)

  - [Usage](./pio-upgrade.md#usage)
  - [Description](./pio-upgrade.md#description)
  - [Options](./pio-upgrade.md#options)
  - [Examples](./pio-upgrade.md#examples)
