# Troubleshooting {#troubleshooting}

## Package Manager {#package-manager}

### Fix Windows Path Length Limitation (MAX_PATH) {#fix-windows-path-length-limitation-max-path}

Windows enforces a default 260-character path limit (`MAX_PATH`). Deeply nested package dependencies—such as ESP-IDF or ESP32-Arduino framework easily exceed this threshold, resulting in `FileNotFoundError` or extraction failures during package installation.

To resolve this issue, enable **Long Paths** in Windows using one of the following methods:

**Method 1: PowerShell (Recommended)**

Run the following command in PowerShell as Administrator, then restart your system:

```powershell
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1
```

**Method 2: Registry Editor**

1. Press <kbd>Win</kbd> + <kbd>R</kbd>, type `regedit`, and press <kbd>Enter</kbd>.
2. Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem`.
3. Double-click **LongPathsEnabled** and change its value to `1`.
4. Restart your computer.

:::tip

If you lack administrative privileges to modify system settings, you can shorten the default PlatformIO storage path instead. Set the [`PLATFORMIO_CORE_DIR`](../../reference/environment-variables.md#envvar-PLATFORMIO_CORE_DIR) environment variable to a shorter location (for example, `C:\pio`).

:::

<a id="faq-package-manager-error-5"></a>

### \[Error 5\] Access is denied {#error-5-access-is-denied}

PlatformIO installs all packages to "[core_dir](../../reference/platformio-ini/platformio/core-dir.md)/packages" directory. You **MUST HAVE** write access to this folder. Please note that **PlatformIO does not require** "sudo"/administrative privileges.

#### Solution 1: Remove folder {#solution-1-remove-folder}

A quick solution is to remove "[core_dir](../../reference/platformio-ini/platformio/core-dir.md)/packages" folder and repeat installation/building/uploading again.

#### Solution 2: Antivirus {#solution-2-antivirus}

Some antivirus tools forbid programs to create files in the background. PlatformIO Package Manager does all work in the background: downloads package, unpacks archive in temporary folder and moves final files to "[core_dir](../../reference/platformio-ini/platformio/core-dir.md)/packages" folder.

Antivirus tool can block PlatformIO, that is why you see "\[Error 5\] Access is denied". Try to **disable it for a while** or add [core_dir](../../reference/platformio-ini/platformio/core-dir.md) directory to exclusion/whitelist.

#### Solution 3: Run from Terminal {#solution-3-run-from-terminal}

As we mentioned in "Solution 2", antivirus tools can block background file system operations. Another solution is to run [PlatformIO Core (CLI)](../../get-started/platformio-core.md) from a system terminal.

1. Open **System Terminal**, on Windows `cmd.exe` (not [PlatformIO IDE](../../get-started/platformio-ide.md) Terminal)

2. Build a project and upload firmware using [PlatformIO Core (CLI)](../../get-started/platformio-core.md) which will download and install all dependent packages:

   ```bash
   # Change directory to PlatformIO Project where is located "platformio.ini"
   cd path/to/platformio/project

   # Force PlatformIO to install PlatformIO Home dependencies
   pio home

   # Force PlatformIO to install toolchains
   pio run --target upload
   ```

If "pio" command is not globally available in your environment and you use [PlatformIO IDE](../../get-started/platformio-ide.md), please use built-in [PlatformIO Core (CLI)](../../get-started/platformio-core.md) which is located in:

- Windows: `C:\Users\{username}\.platformio\penv\Scripts\platformio` Please replace `{username}` with a real user name
- Unix: `~/.platformio/penv/bin/platformio`

:::note

You can add `platformio` and `pio` commands to your system environment. See [Install Shell Commands](../../get-started/install/shell-commands.md).

:::

## Building {#building}

### UnicodeWarning: Unicode equal comparison failed {#unicodewarning-unicode-equal-comparison-failed}

Full warning message is "UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal".

**KNOWN ISSUE**. Please move your project to a folder which full path does not contain non-ASCII chars.

### UnicodeDecodeError: Non-ASCII characters found in build environment {#unicodedecodeerror-non-ascii-characters-found-in-build-environment}

**KNOWN ISSUE**. [PlatformIO Core (CLI)](../../get-started/platformio-core.md) currently does not support projects which contain non-ASCII characters (codes) in a full path or depend on the libraries which use non-ASCII characters in their names.

**TEMPORARY SOLUTION**

1. Use [PlatformIO IDE](../../get-started/platformio-ide.md), it will automatically install [PlatformIO Core (CLI)](../../get-started/platformio-core.md) in a root of system disk (`%DISK%/.platformio`) and avoid an issue when system User contains non-ASCII characters
2. Do not use non-ASCII characters in project folder name or its parent folders.

Also, if you want to place [PlatformIO Core (CLI)](../../get-started/platformio-core.md) in own location, see:

- Set [`PLATFORMIO_CORE_DIR`](../../reference/environment-variables.md#envvar-PLATFORMIO_CORE_DIR) environment variable with own path
- Configure custom location per project using [core_dir](../../reference/platformio-ini/platformio/core-dir.md) option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md).

### ARM toolchain: cc1plus: error while loading shared libraries {#arm-toolchain-cc1plus-error-while-loading-shared-libraries}

See related answers for [error while loading shared libraries](https://github.com/platformio/platformio-core/issues?utf8=✓&q=error+while+loading+shared+libraries).

### Archlinux: libncurses.so.5: cannot open shared object file {#archlinux-libncurses-so-5-cannot-open-shared-object-file}

Answered in [issue #291](https://github.com/platformio/platformio-core/issues/291).

### Monitoring a serial port breaks upload {#monitoring-a-serial-port-breaks-upload}

Answered in [issue #384](https://github.com/platformio/platformio-core/issues/384).
