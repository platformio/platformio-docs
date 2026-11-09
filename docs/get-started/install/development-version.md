<a id="installation-develop"></a>

# Development Version {#development-version}

:::warning

If you use [PlatformIO IDE](../platformio-ide.md), please enable development version and restart IDE:

- [PlatformIO IDE for VSCode](../../guides/ide/vscode.md): Set `platformio-ide.useDevelopmentPIOCore` to `true` in [Settings](../../guides/ide/vscode.md#ide-vscode-settings).

:::

Install the latest PlatformIO from the `develop` branch:

```bash
python -m pip install -U https://github.com/platformio/platformio-core/archive/develop.zip
```

If you want to be up-to-date with the latest `develop` version of PlatformIO, then you need to re-install PlatformIO each time you see a new commit in [PlatformIO GitHub repository (branch: develop)](https://github.com/platformio/platformio-core/commits/develop) like so:

```bash
python -m pip install -U https://github.com/platformio/platformio-core/archive/develop.zip
```

Or:

```bash
pio upgrade --dev
```

To revert to the latest stable version:

```bash
python -m pip uninstall platformio
python -m pip install -U platformio
```
