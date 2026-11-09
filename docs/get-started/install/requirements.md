# System Requirements {#system-requirements}

PlatformIO Core is written in [Python](https://www.python.org/downloads/) and works on the most popular operating systems including ARM-based credit-card-sized computers ([Raspberry Pi](http://www.raspberrypi.org), [BeagleBone](http://beagleboard.org), etc.).

<dl>

<dt>

Operating System

</dt>

<dd>

Windows, macOS, Linux, FreeBSD, Linux ARMv6+

</dd>

<dt>

Python Interpreter

</dt>

<dd>

**Python 3.9+ or above**. See detailed instructions on how to [Install Python Interpreter](../../resources/faq/install-python.md).

</dd>

<dt>

Terminal Application

</dt>

<dd>

All CLI commands below should be executed in the [Command-line](http://en.wikipedia.org/wiki/Command-line_interface) application (Terminal). For macOS and Linux OS - *Terminal* application, for Windows OS – `cmd.exe` application.

</dd>

<dt>

Access to Serial Ports (USB/UART)

</dt>

<dd>

**Windows Users:** Please check that you have correctly installed the USB driver from the board manufacturer.

**Linux Users**:

- Please install [99-platformio-udev.rules](./udev-rules.md)
- Raspberry Pi users, please read this article [Enable serial port on Raspberry Pi](https://hallard.me/enable-serial-port-on-raspberry-pi/).

</dd>

</dl>
