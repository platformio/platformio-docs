<a id="installation-installer-script"></a>

# Installer Script (Recommended) {#installer-script-recommended}

:::warning

PlatformIO operates **without the need for administrative or sudo permissions**. It is strongly advised to perform the installation using the default user account and without any additional permissions. This approach ensures a smooth installation process and helps maintain a secure and controlled environment.

:::

:::note

To facilitate the integration of PlatformIO Core with [Continuous Integration](../../../guides/ci/index.md) systems and containers, we highly recommend installing PlatformIO Core directly from the [Python Package Manager](./pypi.md). This method is not only the fastest but also the most straightforward way to ensure a seamless setup.

:::

Install PlatformIO Core into the Virtual Python Environment using the [Installer Script](https://github.com/platformio/platformio-core-installer).

A default location of Python virtual environment is "[core_dir](../../../reference/platformio-ini/platformio/core-dir.md)/penv". If you have any issues with PlatformIO Core, just remove this folder and re-run installer script.

## Super-Quick (macOS / Linux) {#super-quick-macos-linux}

To install or upgrade PlatformIO Core paste that at a *Terminal* prompt:

Using `curl`

```bash
curl -fsSL -o get-platformio.py https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py
python3 get-platformio.py
```

or using `wget`

```bash
wget -O get-platformio.py https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py
python3 get-platformio.py
```

## Local Download (macOS / Linux / Windows) {#local-download-macos-linux-windows}

To install or upgrade PlatformIO Core, download (save as...) [get-platformio.py](https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py) script. Then run the following:

```bash
# change directory to the folder where is located downloaded "get-platformio.py"
cd /path-to-dir/where/get-platformio.py/is-located

# run it
python get-platformio.py
```

On *Windows OS* it may look like this:

```bash
# change directory to the folder where is located downloaded "get-platformio.py"
cd C:/path-to-dir/where/get-platformio.py/is-located

# run it
python.exe get-platformio.py
```

:::note

If you need to have access to `pio` or `pio.exe` commands from other applications or terminals in your OS, please [Install Shell Commands](../shell-commands.md).

:::
