---
title: "Silicon Labs EFM32"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "The Silicon Labs EFM32 development platform for PlatformIO: configuration, frameworks, packages, debugging and boards."
---

# Silicon Labs EFM32

**Registry:** [https://registry.platformio.org/platforms/platformio/siliconlabsefm32](https://registry.platformio.org/platforms/platformio/siliconlabsefm32)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/siliconlabsefm32`

Silicon Labs EFM32 Gecko 32-bit microcontroller (MCU) family includes devices that offer flash memory configurations up to 256 kB, 32 kB of RAM and CPU speeds up to 48 MHz. Based on the powerful ARM Cortex-M core, the Gecko family features innovative low energy techniques, short wake-up time from energy saving modes and a wide selection of peripherals, making it ideal for battery operated applications and other systems requiring high performance and low-energy consumption.

Vendor website: [www.silabs.com](http://www.silabs.com/products/mcu/32-bit/efm32-gecko/Pages/efm32-gecko.aspx?utm_source=platformio.org&utm_medium=docs).

## Examples

Example projects from the [Silicon Labs EFM32 platform repository](https://github.com/platformio/platform-siliconlabsefm32/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [zephyr-subsys-console-getline](https://github.com/platformio/platform-siliconlabsefm32/tree/master/examples/zephyr-subsys-console-getline?utm_source=platformio.org&utm_medium=docs)
- [zephyr-blink](https://github.com/platformio/platform-siliconlabsefm32/tree/master/examples/zephyr-blink?utm_source=platformio.org&utm_medium=docs)
- [mbed-rtos-blink-baremetal](https://github.com/platformio/platform-siliconlabsefm32/tree/master/examples/mbed-rtos-blink-baremetal?utm_source=platformio.org&utm_medium=docs)
- [mbed-rtos-usb-cdc](https://github.com/platformio/platform-siliconlabsefm32/tree/master/examples/mbed-rtos-usb-cdc?utm_source=platformio.org&utm_medium=docs)
- [mbed-rtos-semaphore](https://github.com/platformio/platform-siliconlabsefm32/tree/master/examples/mbed-rtos-semaphore?utm_source=platformio.org&utm_medium=docs)

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
| [EFM32GG-STK3700 Giant Gecko](../boards/siliconlabsefm32/efm32gg-stk3700.md) | EFM32GG990F1024 | 48MHz | 1MB | 128KB |
| [EFM32WG-STK3800 Wonder Gecko](../boards/siliconlabsefm32/efm32wg-stk3800.md) | EFM32WG990F256 | 48MHz | 256KB | 32KB |
| [SLSTK3400A USB-enabled Happy Gecko](../boards/siliconlabsefm32/efm32hg-stk3400.md) | EFM32HG322F64 | 25MHz | 64KB | 8KB |
| [SLSTK3701A Giant Gecko S1](../boards/siliconlabsefm32/efm32gg11-stk3701.md) | EFM32GG11B820F2048GL192 | 48MHz | 2MB | 512KB |
| [Thunderboard Sense 2 Sensor-to-Cloud Advanced IoT](../boards/siliconlabsefm32/tb-sense-12.md) | EFR32MG12P432F1024 | 40MHz | 1MB | 256KB |

## Stable and upstream versions

Choose between the [stable releases](https://github.com/platformio/platform-siliconlabsefm32/releases) of the Silicon Labs EFM32 platform and its latest upstream version with the [platform](../../reference/platformio-ini/env/platform.md) option in [platformio.ini](../../reference/platformio-ini/index.md).

### Stable

```ini
; Latest stable version, NOT recommended
; Pin the version as shown below
[env:latest_stable]
platform = siliconlabsefm32
board = ...

; Specific version
[env:custom_stable]
platform = siliconlabsefm32@x.y.z
board = ...
```

### Upstream

```ini
[env:upstream_develop]
platform = https://github.com/platformio/platform-siliconlabsefm32.git
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

### Silicon Labs

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [EFM32GG-STK3700 Giant Gecko](../boards/siliconlabsefm32/efm32gg-stk3700.md) | On-board | EFM32GG990F1024 | 48MHz | 1MB | 128KB |
| [EFM32WG-STK3800 Wonder Gecko](../boards/siliconlabsefm32/efm32wg-stk3800.md) | On-board | EFM32WG990F256 | 48MHz | 256KB | 32KB |
| [SLSTK3400A USB-enabled Happy Gecko](../boards/siliconlabsefm32/efm32hg-stk3400.md) | On-board | EFM32HG322F64 | 25MHz | 64KB | 8KB |
| [SLSTK3701A Giant Gecko S1](../boards/siliconlabsefm32/efm32gg11-stk3701.md) | On-board | EFM32GG11B820F2048GL192 | 48MHz | 2MB | 512KB |
| [Thunderboard Sense 2 Sensor-to-Cloud Advanced IoT](../boards/siliconlabsefm32/tb-sense-12.md) | On-board | EFR32MG12P432F1024 | 40MHz | 1MB | 256KB |
