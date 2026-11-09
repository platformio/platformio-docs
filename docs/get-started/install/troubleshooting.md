# Troubleshooting {#troubleshooting}

:::note

**Linux OS**: Don't forget to install [99-platformio-udev.rules](./udev-rules.md)

**Windows OS**: Please check that you have correctly installed the USB driver from the board manufacturer.

:::

If you find any issues with PlatformIO Core Installer Script, please report to [https://github.com/platformio/platformio-core-installer/issues](https://github.com/platformio/platformio-core-installer/issues)

<a id="multiple-pio-cores-issue"></a>

## Multiple PlatformIO Cores in a system {#multiple-platformio-cores-in-a-system}

Multiple standalone [PlatformIO Core (CLI)](../platformio-core.md) in a system could lead to the different issues. We highly recommend to keep one instance of PlatformIO Core or use built-in PlatformIO Core in [PlatformIO IDE](../platformio-ide.md):

- [PlatformIO IDE for VSCode](../../guides/ide/vscode.md) - [Settings](../../guides/ide/vscode.md#ide-vscode-settings) > Set `platformio-ide.useBuiltinPIOCore` to `true`.

Finally, if you have a standalone [PlatformIO Core (CLI)](../platformio-core.md) in a system, please open system Terminal (not PlatformIO IDE Terminal) and uninstall obsolete PlatformIO Core:

```bash
pip uninstall platformio
python -m pip uninstall platformio

# if you used macOS "brew"
brew uninstall platformio
```

If you need to have [PlatformIO Core (CLI)](../platformio-core.md) globally in a system, please [Install Shell Commands](./shell-commands.md).

## 'platformio' is not recognized as an internal or external command {#platformio-is-not-recognized-as-an-internal-or-external-command}

If you use [PlatformIO IDE](../platformio-ide.md), please check in PlatformIO IDE Settings that "Use built-in PlatformIO Core" is enabled.

If you modify the system environment variable `PATH` in your Bash/Fish/ZSH profile, please do not override global `PATH`. This line `export PATH="/my/custom/path"` is incorrect. Use `export PATH="/my/custom/path":$PATH` instead.

## ImportError: cannot import name \_remove_dead_weakref {#importerror-cannot-import-name-remove-dead-weakref}

Windows users can experience this issue when multiple Python interpreters are installed in a system and conflict with each other. The easy way to fix this problem is uninstalling all Python interpreters using Windows Programs Manager and installing them manually again.

1. "Windows > Start Menu > Settings > System > Apps & Features", select Python interpreters and uninstall them.
2. Install the latest Python interpreter, see [Install Python Interpreter](../../resources/faq/install-python.md) guide
3. Remove `C:\Users\YourUserName\.platformio` and `C:\.platformio` folders if exist (do not forget to replace "YourUserName" with the real user name)
4. Restart [PlatformIO IDE](../platformio-ide.md).
