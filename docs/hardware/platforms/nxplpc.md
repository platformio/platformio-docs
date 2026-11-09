---
title: "NXP LPC"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "The NXP LPC development platform for PlatformIO: configuration, frameworks, packages, debugging and boards."
---

<a id="platform-nxplpc"></a>

# NXP LPC

**Registry:** [https://registry.platformio.org/platforms/platformio/nxplpc](https://registry.platformio.org/platforms/platformio/nxplpc)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/nxplpc`

The NXP LPC is a family of 32-bit microcontroller integrated circuits by NXP Semiconductors. The LPC chips are grouped into related series that are based around the same 32-bit ARM processor core, such as the Cortex-M4F, Cortex-M3, Cortex-M0+, or Cortex-M0. Internally, each microcontroller consists of the processor core, static RAM memory, flash memory, debugging interface, and various peripherals.

Vendor website: [www.nxp.com](http://www.nxp.com/products/microcontrollers/?utm_source=platformio.org&utm_medium=docs).

## Examples

Example projects from the [NXP LPC platform repository](https://github.com/platformio/platform-nxplpc/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [zephyr-blink](https://github.com/platformio/platform-nxplpc/tree/master/examples/zephyr-blink?utm_source=platformio.org&utm_medium=docs)
- [mbed-rtos-blockdevice](https://github.com/platformio/platform-nxplpc/tree/master/examples/mbed-rtos-blockdevice?utm_source=platformio.org&utm_medium=docs)
- [mbed-rtos-blink-baremetal](https://github.com/platformio/platform-nxplpc/tree/master/examples/mbed-rtos-blink-baremetal?utm_source=platformio.org&utm_medium=docs)
- [mbed-rtos-thread-statistics](https://github.com/platformio/platform-nxplpc/tree/master/examples/mbed-rtos-thread-statistics?utm_source=platformio.org&utm_medium=docs)
- [zephyr-custom-board](https://github.com/platformio/platform-nxplpc/tree/master/examples/zephyr-custom-board?utm_source=platformio.org&utm_medium=docs)
- [zephyr-synchronization](https://github.com/platformio/platform-nxplpc/tree/master/examples/zephyr-synchronization?utm_source=platformio.org&utm_medium=docs)

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
| [LPCXpresso11U68](../boards/nxplpc/lpc11u68.md) | LPC11U68 | 50MHz | 256KB | 36KB |
| [NXP LPCXpresso54114](../boards/nxplpc/lpc54114.md) | LPC54114J256BD64 | 100MHz | 256KB | 192KB |
| [NXP LPCXpresso54608](../boards/nxplpc/lpc546xx.md) | LPC54608ET512 | 180MHz | 512KB | 200KB |
| [NXP LPCXpresso55S16](../boards/nxplpc/lpcxpresso55s16.md) | LPC55S16 | 150MHz | 256KB | 96KB |
| [NXP mbed LPC1768](../boards/nxplpc/lpc1768.md) | LPC1768 | 96MHz | 512KB | 64KB |
| [Seeed Arch Pro](../boards/nxplpc/seeedarchpro.md) | LPC1768 | 96MHz | 512KB | 64KB |

## Stable and upstream versions

Choose between the [stable releases](https://github.com/platformio/platform-nxplpc/releases) of the NXP LPC platform and its latest upstream version with the [platform](../../reference/platformio-ini/env/platform.md) option in [platformio.ini](../../reference/platformio-ini/index.md).

### Stable

```ini
; Latest stable version, NOT recommended
; Pin the version as shown below
[env:latest_stable]
platform = nxplpc
board = ...

; Specific version
[env:custom_stable]
platform = nxplpc@x.y.z
board = ...
```

### Upstream

```ini
[env:upstream_develop]
platform = https://github.com/platformio/platform-nxplpc.git
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
| [tool-openocd](https://registry.platformio.org/tools/platformio/tool-openocd) | Open On-Chip Debugger. Free and Open On-Chip Debugging, In-System Programming and Boundary-Scan Testing |
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

### NXP

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [LPCXpresso11U68](../boards/nxplpc/lpc11u68.md) | On-board | LPC11U68 | 50MHz | 256KB | 36KB |
| [NXP LPCXpresso54114](../boards/nxplpc/lpc54114.md) | On-board | LPC54114J256BD64 | 100MHz | 256KB | 192KB |
| [NXP LPCXpresso54608](../boards/nxplpc/lpc546xx.md) | On-board | LPC54608ET512 | 180MHz | 512KB | 200KB |
| [NXP LPCXpresso55S16](../boards/nxplpc/lpcxpresso55s16.md) | On-board | LPC55S16 | 150MHz | 256KB | 96KB |
| [NXP mbed LPC1768](../boards/nxplpc/lpc1768.md) | On-board | LPC1768 | 96MHz | 512KB | 64KB |

### SeeedStudio

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Seeed Arch Pro](../boards/nxplpc/seeedarchpro.md) | On-board | LPC1768 | 96MHz | 512KB | 64KB |
