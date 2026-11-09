---
description: Install or upgrade PlatformIO Core in an isolated Python environment with the official installer script.
---

# Install with the installer script

The [installer script](https://github.com/platformio/platformio-core-installer)
installs PlatformIO Core into its own Python virtual environment, isolated from
the rest of your system. This is the recommended method for workstations.

The virtual environment is created in
[`core_dir`](../../reference/platformio-ini/platformio/core-dir.md)`/penv`,
which is `~/.platformio/penv` by default. Run the same script again to upgrade.

:::warning

Do not use `sudo` or an administrator account. PlatformIO does not need
elevated privileges, and installing with them causes permission errors later.

:::

## Before you begin {#before-you-begin}

You need Python 3.9 or later. See [System requirements](./requirements.md).

## macOS and Linux {#super-quick-macos-linux}

Run in a terminal:

```bash
curl -fsSL -o get-platformio.py https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py
python3 get-platformio.py
```

If you do not have `curl`, download the script with `wget`:

```bash
wget -O get-platformio.py https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py
python3 get-platformio.py
```

## Windows {#local-download-macos-linux-windows}

1. Download
   [get-platformio.py](https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py)
   (right-click the link and select **Save link as**).
2. Open Command Prompt or PowerShell in the folder where you saved it, and run:

   ```bash
   python get-platformio.py
   ```

The same steps also work on macOS and Linux if you prefer to download the
script manually.

## Next steps {#next-steps}

The installer does not add `pio` to your `PATH`. To run `pio` from any
terminal, [install the shell commands](./shell-commands.md).

:::tip

If PlatformIO Core stops working, delete the `penv` folder and run the
installer script again.

:::
