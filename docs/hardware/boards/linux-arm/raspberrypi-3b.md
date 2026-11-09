---
title: "Raspberry Pi 3 Model B"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Raspberry Pi 3 Model B (BCM2837, 1200MHz, 1GB flash, 1GB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Raspberry Pi 3 Model B

## Hardware

Platform [Linux ARM](../../platforms/linux-arm.md): Linux ARM is a Unix-like and mostly POSIX-compliant computer operating system (OS) assembled under the model of free and open-source software development and distribution. Using host OS (Mac OS X, Linux ARM) you can build native application for Linux ARM platform.

| Specification | Value |
|---|---|
| **Microcontroller** | BCM2837 |
| **Frequency** | 1200MHz |
| **Flash** | 1GB |
| **RAM** | 1GB |
| **Vendor** | [Raspberry Pi](https://www.raspberrypi.org?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `raspberrypi_3b` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:raspberrypi_3b]
platform = linux_arm
board = raspberrypi_3b
```

To override a setting of the board manifest [raspberrypi_3b.json](https://github.com/platformio/platform-linux_arm/blob/master/boards/raspberrypi_3b.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:raspberrypi_3b]
platform = linux_arm
board = raspberrypi_3b

; change microcontroller
board_build.mcu = bcm2837

; change MCU frequency
board_build.f_cpu = 1200000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the Raspberry Pi 3 Model B yet.

## Frameworks

| Name | Description |
|---|---|
| [WiringPi](../../frameworks/wiringpi.md) | WiringPi is a PIN based GPIO access library written in C for the BCM2835, BCM2836 and BCM2837 SoC devices used in all Raspberry Pi |
