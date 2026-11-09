---
title: "WiringPi"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "The WiringPi framework in PlatformIO: configuration, platforms, debugging and boards."
---

# WiringPi

**Configuration:** [framework](../../reference/platformio-ini/env/framework.md) = `wiringpi`

WiringPi is a PIN based GPIO access library written in C for the BCM2835, BCM2836 and BCM2837 SoC devices used in all Raspberry Pi

## Platforms

| Name | Description |
|---|---|
| [Linux ARM](../platforms/linux-arm.md) | Linux ARM is a Unix-like and mostly POSIX-compliant computer operating system (OS) assembled under the model of free and open-source software development and distribution. Using host OS (Mac OS X, Linux ARM) you can build native application for Linux ARM platform. |

## Examples

- [WiringPi for Linux ARM](https://github.com/platformio/platform-linux_arm/tree/master/examples?utm_source=platformio.org&utm_medium=docs)

## Boards

To list the boards from the command line, use [pio boards](../../reference/cli/pio-boards.md).

### Raspberry Pi

| Name | Platform | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|---|
| [Raspberry Pi 1 Model B](../boards/linux-arm/raspberrypi-1b.md) | [Linux ARM](../platforms/linux-arm.md) | No | BCM2835 | 700MHz | 512MB | 512MB |
| [Raspberry Pi 2 Model B](../boards/linux-arm/raspberrypi-2b.md) | [Linux ARM](../platforms/linux-arm.md) | No | BCM2836 | 900MHz | 1GB | 1GB |
| [Raspberry Pi 3 Model B](../boards/linux-arm/raspberrypi-3b.md) | [Linux ARM](../platforms/linux-arm.md) | No | BCM2837 | 1200MHz | 1GB | 1GB |
| [Raspberry Pi Zero](../boards/linux-arm/raspberrypi-zero.md) | [Linux ARM](../platforms/linux-arm.md) | No | BCM2835 | 1000MHz | 512MB | 512MB |
