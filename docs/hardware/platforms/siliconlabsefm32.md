---
title: "Silicon Labs EFM32"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
---

<a id="platform-siliconlabsefm32"></a>

# Silicon Labs EFM32

**Registry:** [https://registry.platformio.org/platforms/platformio/siliconlabsefm32](https://registry.platformio.org/platforms/platformio/siliconlabsefm32)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/siliconlabsefm32`

Silicon Labs EFM32 Gecko 32-bit microcontroller (MCU) family includes devices that offer flash memory configurations up to 256 kB, 32 kB of RAM and CPU speeds up to 48 MHz. Based on the powerful ARM Cortex-M core, the Gecko family features innovative low energy techniques, short wake-up time from energy saving modes and a wide selection of peripherals, making it ideal for battery operated applications and other systems requiring high performance and low-energy consumption.

For more detailed information please visit [vendor site](http://www.silabs.com/products/mcu/32-bit/efm32-gecko/Pages/efm32-gecko.aspx?utm_source=platformio.org&utm_medium=docs).

## Examples

Examples are listed from [Silicon Labs EFM32 development platform repository](https://github.com/platformio/platform-siliconlabsefm32/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [zephyr-subsys-console-getline](https://github.com/platformio/platform-siliconlabsefm32/tree/master/examples/zephyr-subsys-console-getline?utm_source=platformio.org&utm_medium=docs)
- [zephyr-blink](https://github.com/platformio/platform-siliconlabsefm32/tree/master/examples/zephyr-blink?utm_source=platformio.org&utm_medium=docs)
- [mbed-rtos-blink-baremetal](https://github.com/platformio/platform-siliconlabsefm32/tree/master/examples/mbed-rtos-blink-baremetal?utm_source=platformio.org&utm_medium=docs)
- [mbed-rtos-usb-cdc](https://github.com/platformio/platform-siliconlabsefm32/tree/master/examples/mbed-rtos-usb-cdc?utm_source=platformio.org&utm_medium=docs)
- [mbed-rtos-semaphore](https://github.com/platformio/platform-siliconlabsefm32/tree/master/examples/mbed-rtos-semaphore?utm_source=platformio.org&utm_medium=docs)

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
| [EFM32GG-STK3700 Giant Gecko](../boards/siliconlabsefm32/efm32gg-stk3700.md) | EFM32GG990F1024 | 48MHz | 1MB | 128KB |
| [EFM32WG-STK3800 Wonder Gecko](../boards/siliconlabsefm32/efm32wg-stk3800.md) | EFM32WG990F256 | 48MHz | 256KB | 32KB |
| [SLSTK3400A USB-enabled Happy Gecko](../boards/siliconlabsefm32/efm32hg-stk3400.md) | EFM32HG322F64 | 25MHz | 64KB | 8KB |
| [SLSTK3701A Giant Gecko S1](../boards/siliconlabsefm32/efm32gg11-stk3701.md) | EFM32GG11B820F2048GL192 | 48MHz | 2MB | 512KB |
| [Thunderboard Sense 2 Sensor-to-Cloud Advanced IoT](../boards/siliconlabsefm32/tb-sense-12.md) | EFR32MG12P432F1024 | 40MHz | 1MB | 256KB |

## Stable and upstream versions

You can switch between [stable releases](https://github.com/platformio/platform-siliconlabsefm32/releases) of Silicon Labs EFM32 development platform and the latest upstream version using [platform](../../reference/platformio-ini/env/platform.md) option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md) as described below.

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

### Silicon Labs

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [EFM32GG-STK3700 Giant Gecko](../boards/siliconlabsefm32/efm32gg-stk3700.md) | On-board | EFM32GG990F1024 | 48MHz | 1MB | 128KB |
| [EFM32WG-STK3800 Wonder Gecko](../boards/siliconlabsefm32/efm32wg-stk3800.md) | On-board | EFM32WG990F256 | 48MHz | 256KB | 32KB |
| [SLSTK3400A USB-enabled Happy Gecko](../boards/siliconlabsefm32/efm32hg-stk3400.md) | On-board | EFM32HG322F64 | 25MHz | 64KB | 8KB |
| [SLSTK3701A Giant Gecko S1](../boards/siliconlabsefm32/efm32gg11-stk3701.md) | On-board | EFM32GG11B820F2048GL192 | 48MHz | 2MB | 512KB |
| [Thunderboard Sense 2 Sensor-to-Cloud Advanced IoT](../boards/siliconlabsefm32/tb-sense-12.md) | On-board | EFR32MG12P432F1024 | 40MHz | 1MB | 256KB |
