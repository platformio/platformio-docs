---
description: Install a Python interpreter for PlatformIO Core on Linux, macOS and Windows.
---

# Install a Python interpreter

[PlatformIO Core](../../get-started/platformio-core.md) needs Python 3.9 or
later. macOS and most Linux distributions include Python; on Windows, you
usually need to install it. Download the latest version from
[python.org](https://www.python.org/downloads/), and note the following.

## Linux {#linux}

Make sure the Python `venv` module is installed: the
[installer script](../../get-started/install/installer-script.md) needs it. On
Debian, Ubuntu and their derivatives:

```bash
sudo apt install python3-venv
```

See also [platformio-core-installer#85](https://github.com/platformio/platformio-core-installer/issues/85).

## macOS {#macos}

The python.org installer shows "Important Information" about SSL/TLS
certificates. Run **Install Certificates.command** as described there.
Otherwise, PlatformIO cannot download packages, libraries and toolchains.

## Windows {#windows}

In the installer, select **Add Python to PATH**; otherwise, the `python`
command is not available.

![Python installer with the Add Python to PATH option](./img/python-installer-add-path.png)
