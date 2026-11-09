---
title: "Freescale Kinetis"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
---

<a id="platform-freescalekinetis"></a>

# Freescale Kinetis

**Registry:** [https://registry.platformio.org/platforms/platformio/freescalekinetis](https://registry.platformio.org/platforms/platformio/freescalekinetis)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/freescalekinetis`

Freescale Kinetis Microcontrollers is family of multiple hardware- and software-compatible ARM Cortex-M0+, Cortex-M4 and Cortex-M7-based MCU series. Kinetis MCUs offer exceptional low-power performance, scalability and feature integration.

For more detailed information please visit [vendor site](http://www.freescale.com/webapp/sps/site/homepage.jsp?code=KINETIS&utm_source=platformio.org&utm_medium=docs).

## Examples

Examples are listed from [Freescale Kinetis development platform repository](https://github.com/platformio/platform-freescalekinetis/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [zephyr-blink](https://github.com/platformio/platform-freescalekinetis/tree/master/examples/zephyr-blink?utm_source=platformio.org&utm_medium=docs)
- [zephyr-net-telnet](https://github.com/platformio/platform-freescalekinetis/tree/master/examples/zephyr-net-telnet?utm_source=platformio.org&utm_medium=docs)
- [mbed-rtos-usb-msd](https://github.com/platformio/platform-freescalekinetis/tree/master/examples/mbed-rtos-usb-msd?utm_source=platformio.org&utm_medium=docs)
- [mbed-rtos-blink-baremetal](https://github.com/platformio/platform-freescalekinetis/tree/master/examples/mbed-rtos-blink-baremetal?utm_source=platformio.org&utm_medium=docs)
- [mbed-rtos-ethernet-tls](https://github.com/platformio/platform-freescalekinetis/tree/master/examples/mbed-rtos-ethernet-tls?utm_source=platformio.org&utm_medium=docs)
- [mbed-rtos-psa](https://github.com/platformio/platform-freescalekinetis/tree/master/examples/mbed-rtos-psa?utm_source=platformio.org&utm_medium=docs)
- [mbed-rtos-kvstore](https://github.com/platformio/platform-freescalekinetis/tree/master/examples/mbed-rtos-kvstore?utm_source=platformio.org&utm_medium=docs)

## Debugging

[Debugging](../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

### Tools & Debug Probes

Supported debugging tools are listed in "Debug" column. For more detailed information, please scroll table by horizontal. You can switch between debugging [Tools & Debug Probes](../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md).

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions.

:::

#### On-Board Debug Tools

Boards listed below have on-board debug probe and **ARE READY** for debugging! You do not need to use/buy external debug probe.

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

#### External Debug Tools

Boards listed below are compatible with [Debugging](../../guides/debugging/index.md) but **DEPEND ON** external debug probe. They **ARE NOT READY** for debugging. Please click on board name for the further details.

| Name | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|
| [Freescale Kinetis FRDM-KW24D512](../boards/freescalekinetis/frdm-kw24d.md) | MKW24D512 | 50MHz | 512KB | 64KB |
| [Hexiwear](../boards/freescalekinetis/hexiwear.md) | MK64FN1M0VDC12 | 120MHz | 1MB | 256KB |
| [SEGGER IP Switch Board](../boards/freescalekinetis/segger-ip-switch.md) | MK66FN2M0VMD18 | 180MHz | 2MB | 256KB |

## Stable and upstream versions

You can switch between [stable releases](https://github.com/platformio/platform-freescalekinetis/releases) of Freescale Kinetis development platform and the latest upstream version using [platform](../../reference/platformio-ini/env/platform.md) option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md) as described below.

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

**Linux Users**:

- Install "udev" rules [99-platformio-udev.rules](../../get-started/install/udev-rules.md)
- Raspberry Pi users, please read this article [Enable serial port on Raspberry Pi](https://hallard.me/enable-serial-port-on-raspberry-pi/).

**Windows Users:**

Please check that you have a correctly installed USB driver from board manufacturer

:::

## Frameworks

| Name | Description |
|---|---|
| [Mbed](../frameworks/mbed.mdx) | Arm Mbed OS is a platform operating system designed for the internet of things |
| [Zephyr](../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |

## Boards

:::note

- You can list pre-configured boards by [pio boards](../../reference/cli/pio-boards.md) command
- For more detailed `board` information please scroll the tables below by horizontally.

:::

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
