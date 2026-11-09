---
title: "NXP i.MX RT"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "The NXP i.MX RT development platform for PlatformIO: configuration, frameworks, packages, debugging and boards."
---

# NXP i.MX RT

**Registry:** [https://registry.platformio.org/platforms/platformio/nxpimxrt](https://registry.platformio.org/platforms/platformio/nxpimxrt)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/nxpimxrt`

The i.MX RT series of crossover processors features the Arm Cortex-M core, real-time functionality and MCU usability at a cost-effective price.

Vendor website: [www.nxp.com](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i.mx-rt-crossover-mcus:IMX-RT-SERIES?utm_source=platformio.org&utm_medium=docs).

## Examples

Example projects from the [NXP i.MX RT platform repository](https://github.com/platformio/platform-nxpimxrt/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [zephyr-blink](https://github.com/platformio/platform-nxpimxrt/tree/master/examples/zephyr-blink?utm_source=platformio.org&utm_medium=docs)
- [mbed-rtos-blink-baremetal](https://github.com/platformio/platform-nxpimxrt/tree/master/examples/mbed-rtos-blink-baremetal?utm_source=platformio.org&utm_medium=docs)
- [mbed-rtos-cellular](https://github.com/platformio/platform-nxpimxrt/tree/master/examples/mbed-rtos-cellular?utm_source=platformio.org&utm_medium=docs)
- [mbed-rtos-ethernet-tls](https://github.com/platformio/platform-nxpimxrt/tree/master/examples/mbed-rtos-ethernet-tls?utm_source=platformio.org&utm_medium=docs)
- [zephyr-synchronization](https://github.com/platformio/platform-nxpimxrt/tree/master/examples/zephyr-synchronization?utm_source=platformio.org&utm_medium=docs)

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
| [NXP i.MX RT1010 Evaluation Kit](../boards/nxpimxrt/mimxrt1010-evk.md) | MIMXRT1011DAE5A | 500MHz | 64KB | 128KB |
| [NXP i.MX RT1015 Evaluation Kit](../boards/nxpimxrt/mimxrt1015-evk.md) | MIMXRT1015DAF5A | 500MHz | 96KB | 128KB |
| [NXP i.MX RT1020 Evaluation Kit](../boards/nxpimxrt/mimxrt1020-evk.md) | MIMXRT1021DAG5A | 500MHz | 8MB | 32MB |
| [NXP i.MX RT1050 Evaluation Kit](../boards/nxpimxrt/mimxrt1050-evk.md) | MIMXRT1052DVL6B | 600MHz | 8MB | 32MB |
| [NXP i.MX RT1060 Evaluation Kit](../boards/nxpimxrt/mimxrt1060-evk.md) | MIMXRT1062DVL6A | 600MHz | 8MB | 32MB |
| [NXP i.MX RT1064 Evaluation Kit](../boards/nxpimxrt/mimxrt1064-evk.md) | MIMXRT1064DVL6A | 600MHz | 8MB | 32MB |

## Stable and upstream versions

Choose between the [stable releases](https://github.com/platformio/platform-nxpimxrt/releases) of the NXP i.MX RT platform and its latest upstream version with the [platform](../../reference/platformio-ini/env/platform.md) option in [platformio.ini](../../reference/platformio-ini/index.md).

### Stable

```ini
; Latest stable version, NOT recommended
; Pin the version as shown below
[env:latest_stable]
platform = nxpimxrt
board = ...

; Specific version
[env:custom_stable]
platform = nxpimxrt@x.y.z
board = ...
```

### Upstream

```ini
[env:upstream_develop]
platform = https://github.com/platformio/platform-nxpimxrt.git
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
| [NXP i.MX RT1010 Evaluation Kit](../boards/nxpimxrt/mimxrt1010-evk.md) | On-board | MIMXRT1011DAE5A | 500MHz | 64KB | 128KB |
| [NXP i.MX RT1015 Evaluation Kit](../boards/nxpimxrt/mimxrt1015-evk.md) | On-board | MIMXRT1015DAF5A | 500MHz | 96KB | 128KB |
| [NXP i.MX RT1020 Evaluation Kit](../boards/nxpimxrt/mimxrt1020-evk.md) | On-board | MIMXRT1021DAG5A | 500MHz | 8MB | 32MB |
| [NXP i.MX RT1050 Evaluation Kit](../boards/nxpimxrt/mimxrt1050-evk.md) | On-board | MIMXRT1052DVL6B | 600MHz | 8MB | 32MB |
| [NXP i.MX RT1060 Evaluation Kit](../boards/nxpimxrt/mimxrt1060-evk.md) | On-board | MIMXRT1062DVL6A | 600MHz | 8MB | 32MB |
| [NXP i.MX RT1064 Evaluation Kit](../boards/nxpimxrt/mimxrt1064-evk.md) | On-board | MIMXRT1064DVL6A | 600MHz | 8MB | 32MB |
