---
title: "Raspberry Pi Zero"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-linux-arm-raspberrypi-zero"></a>

# Raspberry Pi Zero

## Hardware

Platform [Linux ARM](../../platforms/linux-arm.md): Linux ARM is a Unix-like and mostly POSIX-compliant computer operating system (OS) assembled under the model of free and open-source software development and distribution. Using host OS (Mac OS X, Linux ARM) you can build native application for Linux ARM platform.

| Specification | Value |
|---|---|
| **Microcontroller** | BCM2835 |
| **Frequency** | 1000MHz |
| **Flash** | 512MB |
| **RAM** | 512MB |
| **Vendor** | [Raspberry Pi](https://www.raspberrypi.org?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `raspberrypi_zero` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:raspberrypi_zero]
platform = linux_arm
board = raspberrypi_zero
```

You can override default Raspberry Pi Zero settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [raspberrypi_zero.json](https://github.com/platformio/platform-linux_arm/blob/master/boards/raspberrypi_zero.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:raspberrypi_zero]
platform = linux_arm
board = raspberrypi_zero

; change microcontroller
board_build.mcu = bcm2835

; change MCU frequency
board_build.f_cpu = 1000000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support Raspberry Pi Zero board.

## Frameworks

| Name | Description |
|---|---|
| [WiringPi](../../frameworks/wiringpi.md) | WiringPi is a PIN based GPIO access library written in C for the BCM2835, BCM2836 and BCM2837 SoC devices used in all Raspberry Pi |
