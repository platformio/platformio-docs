---
description: Operating systems, Python version and device access PlatformIO Core needs.
---

# System requirements {#system-requirements}

| Requirement | Details |
| --- | --- |
| Operating system | Windows, macOS, Linux or FreeBSD, including Linux on ARMv6 and later (for example, Raspberry Pi) |
| Python | Python 3.9 or later. See [Install a Python interpreter](../../resources/faq/install-python.md). |
| Terminal | Any terminal: Terminal on macOS and Linux, Command Prompt or PowerShell on Windows |

## Access to serial ports {#access-to-serial-ports}

To upload firmware and use the serial monitor, your user account needs access
to the board's USB or serial port:

- **Windows:** install the USB driver from the board manufacturer, if the
  board needs one.
- **Linux:** install the [udev rules](./udev-rules.md). On a Raspberry Pi,
  also [enable the serial port](https://hallard.me/enable-serial-port-on-raspberry-pi/).
