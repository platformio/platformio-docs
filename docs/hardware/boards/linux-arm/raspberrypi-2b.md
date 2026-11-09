---
title: "Raspberry Pi 2 Model B"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Raspberry Pi 2 Model B (BCM2836, 900MHz, 1GB flash, 1GB RAM): PlatformIO board ID, configuration, uploading and debugging."
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

Use the board ID `raspberrypi_2b` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:raspberrypi_2b]
platform = linux_arm
board = raspberrypi_2b
```

To override a setting of the board manifest [raspberrypi_2b.json](https://github.com/platformio/platform-linux_arm/blob/master/boards/raspberrypi_2b.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

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

[Debugging](../../../guides/debugging/index.md) does not support the Raspberry Pi 2 Model B yet.

## Frameworks

| Name | Description |
|---|---|
| [WiringPi](../../frameworks/wiringpi.md) | WiringPi is a PIN based GPIO access library written in C for the BCM2835, BCM2836 and BCM2837 SoC devices used in all Raspberry Pi |
