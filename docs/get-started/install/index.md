---
description: Install PlatformIO Core, the pio command-line tool, on Windows, macOS or Linux.
---

# Install PlatformIO Core

This page helps you install [PlatformIO Core](../platformio-core.md), the `pio`
command-line tool.

:::note

[PlatformIO IDE](../platformio-ide.md) already includes PlatformIO Core. If you
use it, you do not need to install anything: open the
[PlatformIO Core CLI](../../guides/ide/vscode.md#platformio-core-cli) terminal
in the IDE. To use the IDE's PlatformIO Core from other terminals,
[install the shell commands](./shell-commands.md).

:::

<a id="installation-methods"></a>

## Choose an installation method {#choose-an-installation-method}

Check the [system requirements](./requirements.md) first, then install with
**one** of these methods:

| Method | Use it when |
| --- | --- |
| [Installer script](./installer-script.md) (recommended) | You install PlatformIO for yourself on a workstation. PlatformIO goes into its own isolated Python environment and is easy to upgrade or remove. |
| [pip](./pip.md) | You build in CI or in containers, or you manage Python environments yourself. |
| [Homebrew](./homebrew.md) | You use macOS and manage your tools with Homebrew. |

Installing PlatformIO Core more than once (for example, with both the
installer script and pip) causes conflicts. See
[Multiple PlatformIO Core installations](./troubleshooting.md#multiple-platformio-cores-in-a-system).

## Verify the installation {#verify-the-installation}

Open a new terminal and run:

```bash
pio --version
```

If the command is not found, see
[Install shell commands](./shell-commands.md) and
[Troubleshooting](./troubleshooting.md#platformio-is-not-recognized-as-an-internal-or-external-command).

## After installing {#after-installing}

- **Linux:** [install the udev rules](./udev-rules.md) so that you can upload
  to boards without root privileges.
- **Behind a proxy:** [configure the proxy](./proxy-configuration.md).
- **Next:** follow the [Quick start](../quick-start.md).

## More topics {#more-topics}

- [Development version](./development-version.md): try unreleased changes.
- [Integration with your application](./integration.md): install PlatformIO
  Core automatically from an IDE extension or plugin.
- [Uninstall PlatformIO Core](./uninstall.md).
