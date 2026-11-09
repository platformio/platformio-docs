---
title: "NXP LPC"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
---

<a id="platform-nxplpc"></a>

# NXP LPC

**Registry:** [https://registry.platformio.org/platforms/platformio/nxplpc](https://registry.platformio.org/platforms/platformio/nxplpc)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/nxplpc`

The NXP LPC is a family of 32-bit microcontroller integrated circuits by NXP Semiconductors. The LPC chips are grouped into related series that are based around the same 32-bit ARM processor core, such as the Cortex-M4F, Cortex-M3, Cortex-M0+, or Cortex-M0. Internally, each microcontroller consists of the processor core, static RAM memory, flash memory, debugging interface, and various peripherals.

For more detailed information please visit [vendor site](http://www.nxp.com/products/microcontrollers/?utm_source=platformio.org&utm_medium=docs).

## Examples

Examples are listed from [NXP LPC development platform repository](https://github.com/platformio/platform-nxplpc/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [zephyr-blink](https://github.com/platformio/platform-nxplpc/tree/master/examples/zephyr-blink?utm_source=platformio.org&utm_medium=docs)
- [mbed-rtos-blockdevice](https://github.com/platformio/platform-nxplpc/tree/master/examples/mbed-rtos-blockdevice?utm_source=platformio.org&utm_medium=docs)
- [mbed-rtos-blink-baremetal](https://github.com/platformio/platform-nxplpc/tree/master/examples/mbed-rtos-blink-baremetal?utm_source=platformio.org&utm_medium=docs)
- [mbed-rtos-thread-statistics](https://github.com/platformio/platform-nxplpc/tree/master/examples/mbed-rtos-thread-statistics?utm_source=platformio.org&utm_medium=docs)
- [zephyr-custom-board](https://github.com/platformio/platform-nxplpc/tree/master/examples/zephyr-custom-board?utm_source=platformio.org&utm_medium=docs)
- [zephyr-synchronization](https://github.com/platformio/platform-nxplpc/tree/master/examples/zephyr-synchronization?utm_source=platformio.org&utm_medium=docs)

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
| [LPCXpresso11U68](../boards/nxplpc/lpc11u68.md) | LPC11U68 | 50MHz | 256KB | 36KB |
| [NXP LPCXpresso54114](../boards/nxplpc/lpc54114.md) | LPC54114J256BD64 | 100MHz | 256KB | 192KB |
| [NXP LPCXpresso54608](../boards/nxplpc/lpc546xx.md) | LPC54608ET512 | 180MHz | 512KB | 200KB |
| [NXP LPCXpresso55S16](../boards/nxplpc/lpcxpresso55s16.md) | LPC55S16 | 150MHz | 256KB | 96KB |
| [NXP mbed LPC1768](../boards/nxplpc/lpc1768.md) | LPC1768 | 96MHz | 512KB | 64KB |
| [Seeed Arch Pro](../boards/nxplpc/seeedarchpro.md) | LPC1768 | 96MHz | 512KB | 64KB |

## Stable and upstream versions

You can switch between [stable releases](https://github.com/platformio/platform-nxplpc/releases) of NXP LPC development platform and the latest upstream version using [platform](../../reference/platformio-ini/env/platform.md) option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md) as described below.

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
