---
description: Solutions to common PlatformIO package manager and build errors.
---

# Troubleshooting

Solutions to common errors. For installation problems, see
[Troubleshoot the installation](../../get-started/install/troubleshooting.md).

## Package manager {#package-manager}

### Windows path length limit (`MAX_PATH`) {#fix-windows-path-length-limitation-max-path}

Windows limits paths to 260 characters by default. Packages with deeply nested
folders, such as ESP-IDF or the ESP32 Arduino core, exceed it, and the
installation fails with `FileNotFoundError` or an extraction error.

Enable long paths in Windows, then restart the computer. Either:

- run this command in PowerShell as administrator:

  ```powershell
  Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1
  ```

- or, in the Registry Editor (<kbd>Win</kbd>+<kbd>R</kbd>, `regedit`), go to
  `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem` and set
  **LongPathsEnabled** to `1`.

:::tip

Without administrator rights, use a shorter PlatformIO folder instead: set the
[`PLATFORMIO_CORE_DIR`](../../reference/environment-variables.md#envvar-PLATFORMIO_CORE_DIR)
environment variable to a short path, such as `C:\pio`.

:::

<a id="faq-package-manager-error-5"></a>

### `[Error 5] Access is denied` {#error-5-access-is-denied}

PlatformIO installs packages into
[`core_dir`](../../reference/platformio-ini/platformio/core-dir.md)`/packages`,
and needs write access to it. It does not need administrator rights or `sudo`.
Try these solutions in order:

<a id="solution-1-remove-folder"></a>

1. **Delete the packages folder.** Delete `core_dir/packages` and build again;
   PlatformIO reinstalls what it needs.

   <a id="solution-2-antivirus"></a>

2. **Check your antivirus.** Some antivirus tools block programs that create
   files in the background, as the package manager does while it downloads
   and unpacks packages. Disable the antivirus temporarily, or add `core_dir`
   to its exclusions.

   <a id="solution-3-run-from-terminal"></a>

3. **Install from a system terminal.** Open Command Prompt (not the PlatformIO
   IDE terminal), go to the project folder and run:

   ```bash
   # Change directory to PlatformIO Project where is located "platformio.ini"
   cd path/to/platformio/project

   # Force PlatformIO to install PlatformIO Home dependencies
   pio home

   # Force PlatformIO to install toolchains
   pio run --target upload
   ```

   If `pio` is not found, use the PlatformIO Core that PlatformIO IDE installed:
   `C:\Users\<user name>\.platformio\penv\Scripts\platformio` on Windows,
   or `~/.platformio/penv/bin/platformio` on macOS and Linux. To make `pio`
   available everywhere, [install the shell commands](../../get-started/install/shell-commands.md).

## Building {#building}

<a id="unicodewarning-unicode-equal-comparison-failed"></a>

### Non-ASCII characters in paths {#unicodedecodeerror-non-ascii-characters-found-in-build-environment}

Toolchains and build tools may fail when the project path, or the path of
[`core_dir`](../../reference/platformio-ini/platformio/core-dir.md), contains
non-ASCII characters, for example a user name with accented letters. Errors
then mention `UnicodeDecodeError` or files that cannot be found.

- Move the project to a folder whose full path contains only ASCII characters.
- Move PlatformIO's data to such a folder too: set the
  [`PLATFORMIO_CORE_DIR`](../../reference/environment-variables.md#envvar-PLATFORMIO_CORE_DIR)
  environment variable, or the [`core_dir`](../../reference/platformio-ini/platformio/core-dir.md)
  option per project. On Windows, PlatformIO also uses `C:\.platformio`
  automatically if that folder exists.

### More build problems {#arm-toolchain-cc1plus-error-while-loading-shared-libraries}

<a id="archlinux-libncurses-so-5-cannot-open-shared-object-file"></a>
<a id="monitoring-a-serial-port-breaks-upload"></a>

- ARM toolchain: `cc1plus: error while loading shared libraries`: see the
  [related issues](https://github.com/platformio/platformio-core/issues?q=error+while+loading+shared+libraries).
- Arch Linux: `libncurses.so.5: cannot open shared object file`: see
  [issue #291](https://github.com/platformio/platformio-core/issues/291).
- An open serial monitor breaks the upload: close the monitor before
  uploading; see [issue #384](https://github.com/platformio/platformio-core/issues/384).

Still stuck? Ask on the [Community forum](https://community.platformio.org/).
