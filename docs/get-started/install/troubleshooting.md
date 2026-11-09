---
sidebar_label: "Troubleshooting"
description: Fix common problems when installing and running PlatformIO Core.
---

# Troubleshoot the installation {#troubleshooting}

Solutions to common installation problems. For board connection problems,
first check the basics:

- **Linux:** install the [udev rules](./udev-rules.md).
- **Windows:** install the USB driver from the board manufacturer.

If the installer script fails, report it on
[GitHub](https://github.com/platformio/platformio-core-installer/issues).

<a id="multiple-pio-cores-issue"></a>

## More than one PlatformIO Core is installed {#multiple-platformio-cores-in-a-system}

Several installations of PlatformIO Core on one computer (for example, one
from pip and one from PlatformIO IDE) cause unpredictable errors. Keep one.

If you use PlatformIO IDE, use its built-in PlatformIO Core:

1. In VS Code, set
   [`platformio-ide.useBuiltinPIOCore`](../../guides/ide/vscode.md#platformio-ide-usebuiltinpiocore)
   to `true`.
2. In a system terminal (not the IDE terminal), remove the other
   installations:

   ```bash
   python -m pip uninstall platformio

   # if you installed it with Homebrew
   brew uninstall platformio
   ```

3. To use the IDE's PlatformIO Core from other terminals,
   [install the shell commands](./shell-commands.md).

## `pio` is not recognized as a command {#platformio-is-not-recognized-as-an-internal-or-external-command}

The terminal cannot find PlatformIO Core in your `PATH`.

- In PlatformIO IDE, check that
  [`platformio-ide.useBuiltinPIOCore`](../../guides/ide/vscode.md#platformio-ide-usebuiltinpiocore)
  is `true`.
- Outside the IDE, [install the shell commands](./shell-commands.md).
- If you set `PATH` in your shell profile, append to it instead of replacing
  it. `export PATH="/my/custom/path"` hides every other folder; use
  `export PATH="/my/custom/path:$PATH"`.

## `ImportError: cannot import name _remove_dead_weakref` {#importerror-cannot-import-name-remove-dead-weakref}

On Windows, this error means several Python installations conflict with each
other. Reinstall Python:

1. Open **Settings > Apps > Installed apps** and uninstall every Python
   version.
2. [Install the latest Python](../../resources/faq/install-python.md).
3. Delete the `C:\Users\<your user name>\.platformio` and `C:\.platformio`
   folders, if they exist.
4. Restart PlatformIO IDE, or run the [installer script](./installer-script.md)
   again.
