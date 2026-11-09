---
description: Install the development version of PlatformIO Core from the develop branch, and switch back to stable.
---

<a id="installation-develop"></a>

# Install the development version {#development-version}

The development version is built from the `develop` branch of
[PlatformIO Core](https://github.com/platformio/platformio-core). Use it to try
fixes and features before they are released.

## In PlatformIO IDE {#in-platformio-ide}

In VS Code, set
[`platformio-ide.useDevelopmentPIOCore`](../../guides/ide/vscode.md#platformio-ide-usedevelopmentpiocore)
to `true` in the [settings](../../guides/ide/vscode.md#settings), then restart
VS Code.

## From the command line {#from-the-command-line}

Switch an existing installation to the development version:

```bash
pio upgrade --dev
```

Or install it with pip:

```bash
python -m pip install -U https://github.com/platformio/platformio-core/archive/develop.zip
```

The development version does not update itself with every commit. To get the
latest [changes](https://github.com/platformio/platformio-core/commits/develop),
run one of the commands above again.

## Return to the stable version {#return-to-the-stable-version}

```bash
python -m pip uninstall platformio
python -m pip install -U platformio
```
