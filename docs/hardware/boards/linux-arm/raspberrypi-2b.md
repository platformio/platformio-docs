---
title: "Raspberry Pi 2 Model B"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-linux-arm-raspberrypi-2b"></a>

# Raspberry Pi 2 Model B

## Hardware

Platform [Linux ARM](../../platforms/linux-arm.md): Linux ARM is a Unix-like and mostly POSIX-compliant computer operating system (OS) assembled under the model of free and open-source software development and distribution. Using host OS (Mac OS X, Linux ARM) you can build native application for Linux ARM platform.

| Specification | Value |
|---|---|
| **Microcontroller** | BCM2836 |
| **Frequency** | 900MHz |
| **Flash** | 1GB |
| **RAM** | 1GB |
| **Vendor** | [Raspberry Pi](https://www.raspberrypi.org?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `raspberrypi_2b` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:raspberrypi_2b]
platform = linux_arm
board = raspberrypi_2b
```

You can override default Raspberry Pi 2 Model B settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [raspberrypi_2b.json](https://github.com/platformio/platform-linux_arm/blob/master/boards/raspberrypi_2b.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:raspberrypi_2b]
platform = linux_arm
board = raspberrypi_2b

; change microcontroller
board_build.mcu = bcm2836

; change MCU frequency
board_build.f_cpu = 900000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support Raspberry Pi 2 Model B board.

## Frameworks

| Name | Description |
|---|---|
| [WiringPi](../../frameworks/wiringpi.md) | WiringPi is a PIN based GPIO access library written in C for the BCM2835, BCM2836 and BCM2837 SoC devices used in all Raspberry Pi |
