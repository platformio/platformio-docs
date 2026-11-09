---
title: "Freescale Kinetis"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "The Freescale Kinetis development platform for PlatformIO: configuration, frameworks, packages, debugging and boards."
---

# Freescale Kinetis

**Registry:** [https://registry.platformio.org/platforms/platformio/freescalekinetis](https://registry.platformio.org/platforms/platformio/freescalekinetis)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/freescalekinetis`

Freescale Kinetis Microcontrollers is family of multiple hardware- and software-compatible ARM Cortex-M0+, Cortex-M4 and Cortex-M7-based MCU series. Kinetis MCUs offer exceptional low-power performance, scalability and feature integration.

Vendor website: [www.freescale.com](http://www.freescale.com/webapp/sps/site/homepage.jsp?code=KINETIS&utm_source=platformio.org&utm_medium=docs).

## Examples

Example projects from the [Freescale Kinetis platform repository](https://github.com/platformio/platform-freescalekinetis/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [zephyr-blink](https://github.com/platformio/platform-freescalekinetis/tree/master/examples/zephyr-blink?utm_source=platformio.org&utm_medium=docs)
- [zephyr-net-telnet](https://github.com/platformio/platform-freescalekinetis/tree/master/examples/zephyr-net-telnet?utm_source=platformio.org&utm_medium=docs)
- [mbed-rtos-usb-msd](https://github.com/platformio/platform-freescalekinetis/tree/master/examples/mbed-rtos-usb-msd?utm_source=platformio.org&utm_medium=docs)
- [mbed-rtos-blink-baremetal](https://github.com/platformio/platform-freescalekinetis/tree/master/examples/mbed-rtos-blink-baremetal?utm_source=platformio.org&utm_medium=docs)
- [mbed-rtos-ethernet-tls](https://github.com/platformio/platform-freescalekinetis/tree/master/examples/mbed-rtos-ethernet-tls?utm_source=platformio.org&utm_medium=docs)
- [mbed-rtos-psa](https://github.com/platformio/platform-freescalekinetis/tree/master/examples/mbed-rtos-psa?utm_source=platformio.org&utm_medium=docs)
- [mbed-rtos-kvstore](https://github.com/platformio/platform-freescalekinetis/tree/master/examples/mbed-rtos-kvstore?utm_source=platformio.org&utm_medium=docs)

## Debugging

[Debugging](../../guides/debugging/index.md) works with the boards below without extra configuration.

### Debug probes

Select a [debug probe](../../guides/debugging/index.md#debugging-tools) with the [debug_tool](../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../reference/platformio-ini/index.md). Each board's page lists its compatible probes.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

#### Boards with an on-board debug probe

These boards are ready for debugging; no external probe is needed.

| Name | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|
| [Ethernet IoT Starter Kit](../boards/freescalekinetis/ibmethernetkit.md) | MK64FN1M0VLL12 | 120MHz | 1MB | 256KB |
| [Freescale Kinetis FRDM-K22F](../boards/freescalekinetis/frdm-k22f.md) | MK22FN512VLH12 | 120MHz | 512KB | 128KB |
| [Freescale Kinetis FRDM-K64F](../boards/freescalekinetis/frdm-k64f.md) | MK64FN1M0VLL12 | 120MHz | 1MB | 256KB |
| [Freescale Kinetis FRDM-K66F](../boards/freescalekinetis/frdm-k66f.md) | MK66FN2M0VMD18 | 180MHz | 2MB | 256KB |
| [Freescale Kinetis FRDM-K82F](../boards/freescalekinetis/frdm-k82f.md) | MK82FN256VLL15 | 150MHz | 256KB | 256KB |
| [Freescale Kinetis FRDM-KL25Z](../boards/freescalekinetis/frdm-kl25z.md) | MKL25Z128VLK4 | 48MHz | 128KB | 16KB |
| [Freescale Kinetis FRDM-KL43Z](../boards/freescalekinetis/frdm-kl43z.md) | MKL43Z256VLH4 | 48MHz | 256KB | 32KB |
| [Freescale Kinetis FRDM-KL46Z](../boards/freescalekinetis/frdm-kl46z.md) | MKL46Z256VLL4 | 48MHz | 256KB | 32KB |
| [Freescale Kinetis FRDM-KW41Z](../boards/freescalekinetis/frdm-kw41z.md) | MKW41Z512VHT4 | 48MHz | 512KB | 128KB |

#### Boards that need an external debug probe

These boards support [Debugging](../../guides/debugging/index.md) with an external debug probe. See each board's page for the compatible probes.

| Name | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|
| [Freescale Kinetis FRDM-KW24D512](../boards/freescalekinetis/frdm-kw24d.md) | MKW24D512 | 50MHz | 512KB | 64KB |
| [Hexiwear](../boards/freescalekinetis/hexiwear.md) | MK64FN1M0VDC12 | 120MHz | 1MB | 256KB |
| [SEGGER IP Switch Board](../boards/freescalekinetis/segger-ip-switch.md) | MK66FN2M0VMD18 | 180MHz | 2MB | 256KB |

## Stable and upstream versions

Choose between the [stable releases](https://github.com/platformio/platform-freescalekinetis/releases) of the Freescale Kinetis platform and its latest upstream version with the [platform](../../reference/platformio-ini/env/platform.md) option in [platformio.ini](../../reference/platformio-ini/index.md).

### Stable

```ini
; Latest stable version, NOT recommended
; Pin the version as shown below
[env:latest_stable]
platform = freescalekinetis
board = ...

; Specific version
[env:custom_stable]
platform = freescalekinetis@x.y.z
board = ...
```

### Upstream

```ini
[env:upstream_develop]
platform = https://github.com/platformio/platform-freescalekinetis.git
board = ...
```

## Packages

| Name | Description |
|---|---|
| [framework-mbed](https://registry.platformio.org/tools/platformio/framework-mbed) | Arm Mbed OS is a platform operating system designed for the internet of things |
| [framework-zephyr](https://registry.platformio.org/tools/platformio/framework-zephyr) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
| [tool-cmake](https://registry.platformio.org/tools/platformio/tool-cmake) | CMake is an open-source, cross-platform family of tools designed to build, test and package software |
| [tool-dtc](https://registry.platformio.org/tools/platformio/tool-dtc) | Device tree compiler |
| [tool-gperf](https://registry.platformio.org/tools/platformio/tool-gperf) | GNU gperf is a perfect hash function generator |
| [tool-jlink](https://registry.platformio.org/tools/platformio/tool-jlink) | Software and Documentation Pack for SEGGER J-Link debug probes |
| [tool-ninja](https://registry.platformio.org/tools/platformio/tool-ninja) | Ninja is a small build system with a focus on speed |
| [tool-pyocd](https://registry.platformio.org/tools/platformio/tool-pyocd) | Open source python library for programming and debugging ARM Cortex-M microcontrollers using CMSIS-DAP |
| [toolchain-gccarmnoneeabi](https://registry.platformio.org/tools/platformio/toolchain-gccarmnoneeabi) | GNU toolchain for Arm Cortex-M and Cortex-R processors |

:::warning

**Linux:**

- Install the [udev rules](../../get-started/install/udev-rules.md).
- On a Raspberry Pi, [enable the serial port](https://hallard.me/enable-serial-port-on-raspberry-pi/).

**Windows:**

Install the USB driver from the board manufacturer, if needed.

:::

## Frameworks

| Name | Description |
|---|---|
| [Mbed](../frameworks/mbed.mdx) | Arm Mbed OS is a platform operating system designed for the internet of things |
| [Zephyr](../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |

## Boards

To list the boards from the command line, use [pio boards](../../reference/cli/pio-boards.md).

### Freescale

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Ethernet IoT Starter Kit](../boards/freescalekinetis/ibmethernetkit.md) | On-board | MK64FN1M0VLL12 | 120MHz | 1MB | 256KB |
| [Freescale Kinetis FRDM-K22F](../boards/freescalekinetis/frdm-k22f.md) | On-board | MK22FN512VLH12 | 120MHz | 512KB | 128KB |
| [Freescale Kinetis FRDM-K64F](../boards/freescalekinetis/frdm-k64f.md) | On-board | MK64FN1M0VLL12 | 120MHz | 1MB | 256KB |
| [Freescale Kinetis FRDM-K66F](../boards/freescalekinetis/frdm-k66f.md) | On-board | MK66FN2M0VMD18 | 180MHz | 2MB | 256KB |
| [Freescale Kinetis FRDM-K82F](../boards/freescalekinetis/frdm-k82f.md) | On-board | MK82FN256VLL15 | 150MHz | 256KB | 256KB |
| [Freescale Kinetis FRDM-KL25Z](../boards/freescalekinetis/frdm-kl25z.md) | On-board | MKL25Z128VLK4 | 48MHz | 128KB | 16KB |
| [Freescale Kinetis FRDM-KL43Z](../boards/freescalekinetis/frdm-kl43z.md) | On-board | MKL43Z256VLH4 | 48MHz | 256KB | 32KB |
| [Freescale Kinetis FRDM-KL46Z](../boards/freescalekinetis/frdm-kl46z.md) | On-board | MKL46Z256VLL4 | 48MHz | 256KB | 32KB |
| [Freescale Kinetis FRDM-KW24D512](../boards/freescalekinetis/frdm-kw24d.md) | External | MKW24D512 | 50MHz | 512KB | 64KB |
| [Freescale Kinetis FRDM-KW41Z](../boards/freescalekinetis/frdm-kw41z.md) | On-board | MKW41Z512VHT4 | 48MHz | 512KB | 128KB |

### MikroElektronika

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Hexiwear](../boards/freescalekinetis/hexiwear.md) | External | MK64FN1M0VDC12 | 120MHz | 1MB | 256KB |

### SEGGER

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [SEGGER IP Switch Board](../boards/freescalekinetis/segger-ip-switch.md) | External | MK66FN2M0VMD18 | 180MHz | 2MB | 256KB |
