---
title: "Linux ARM"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "The Linux ARM development platform for PlatformIO: configuration, frameworks, packages, debugging and boards."
---

# Linux ARM

**Registry:** [https://registry.platformio.org/platforms/platformio/linux_arm](https://registry.platformio.org/platforms/platformio/linux_arm)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/linux_arm`

Linux ARM is a Unix-like and mostly POSIX-compliant computer operating system (OS) assembled under the model of free and open-source software development and distribution. Using host OS (Mac OS X, Linux ARM) you can build native application for Linux ARM platform.

Vendor website: [registry.platformio.org](https://registry.platformio.org/platforms/platformio/linux_arm?utm_source=platformio.org&utm_medium=docs).

## Examples

Example projects from the [Linux ARM platform repository](https://github.com/platformio/platform-linux_arm/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [wiringpi-serial](https://github.com/platformio/platform-linux_arm/tree/master/examples/wiringpi-serial?utm_source=platformio.org&utm_medium=docs)
- [wiringpi-blink](https://github.com/platformio/platform-linux_arm/tree/master/examples/wiringpi-blink?utm_source=platformio.org&utm_medium=docs)

## Stable and upstream versions

Choose between the [stable releases](https://github.com/platformio/platform-linux_arm/releases) of the Linux ARM platform and its latest upstream version with the [platform](../../reference/platformio-ini/env/platform.md) option in [platformio.ini](../../reference/platformio-ini/index.md).

### Stable

```ini
; Latest stable version, NOT recommended
; Pin the version as shown below
[env:latest_stable]
platform = linux_arm

; Specific version
[env:custom_stable]
platform = linux_arm@x.y.z
```

### Upstream

```ini
[env:upstream_develop]
platform = https://github.com/platformio/platform-linux_arm.git
```

## Packages

| Name | Description |
|---|---|
| [framework-wiringpi](https://registry.platformio.org/tools/platformio/framework-wiringpi) | WiringPi is a PIN based GPIO access library written in C for the BCM2835, BCM2836 and BCM2837 SoC devices used in all Raspberry Pi |
| [toolchain-gccarmlinuxgnueabi](https://registry.platformio.org/tools/platformio/toolchain-gccarmlinuxgnueabi) | GCC Toolchain for Linux ARM GNU EABI |

## Frameworks

| Name | Description |
|---|---|
| [WiringPi](../frameworks/wiringpi.md) | WiringPi is a PIN based GPIO access library written in C for the BCM2835, BCM2836 and BCM2837 SoC devices used in all Raspberry Pi |

## Boards

To list the boards from the command line, use [pio boards](../../reference/cli/pio-boards.md).

### Raspberry Pi

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Raspberry Pi 1 Model B](../boards/linux-arm/raspberrypi-1b.md) | No | BCM2835 | 700MHz | 512MB | 512MB |
| [Raspberry Pi 2 Model B](../boards/linux-arm/raspberrypi-2b.md) | No | BCM2836 | 900MHz | 1GB | 1GB |
| [Raspberry Pi 3 Model B](../boards/linux-arm/raspberrypi-3b.md) | No | BCM2837 | 1200MHz | 1GB | 1GB |
| [Raspberry Pi Zero](../boards/linux-arm/raspberrypi-zero.md) | No | BCM2835 | 1000MHz | 512MB | 512MB |
