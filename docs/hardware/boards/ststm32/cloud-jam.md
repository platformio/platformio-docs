---
title: "RushUp Cloud-JAM"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "RushUp Cloud-JAM (STM32F401RET6, 84MHz, 512KB flash, 96KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# RushUp Cloud-JAM

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32F401RET6 |
| **Frequency** | 84MHz |
| **Flash** | 512KB |
| **RAM** | 96KB |
| **Vendor** | [RushUp](https://developer.mbed.org/platforms/ST-Nucleo-F401RE/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `cloud_jam` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:cloud_jam]
platform = ststm32
board = cloud_jam
```

To override a setting of the board manifest [cloud_jam.json](https://github.com/platformio/platform-ststm32/blob/master/boards/cloud_jam.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:cloud_jam]
platform = ststm32
board = cloud_jam

; change microcontroller
board_build.mcu = stm32f401ret6

; change MCU frequency
board_build.f_cpu = 84000000L
```

## Uploading

RushUp Cloud-JAM supports these upload protocols:

- `blackmagic`
- `cmsis-dap`
- `jlink`
- `mbed`
- `stlink`

The default is `stlink`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:cloud_jam]
platform = ststm32
board = cloud_jam

upload_protocol = stlink
```

## Debugging

The RushUp Cloud-JAM has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [Black magic probe](../../debug-probes/blackmagic.md) |  |  |
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) |  |  |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [ST-LINK](../../debug-probes/stlink.md) | Yes | Yes |

## Frameworks

| Name | Description |
|---|---|
| [CMSIS](../../frameworks/cmsis.md) | Vendor-independent hardware abstraction layer for the Cortex-M processor series |
| [LibOpenCM3](../../frameworks/libopencm3.md) | The libopencm3 project aims to create an open-source firmware library for various ARM Cortex-M microcontrollers. |
| [Mbed](../../frameworks/mbed.mdx) | Arm Mbed OS is a platform operating system designed for the internet of things |
| [Standard Peripheral Library](../../frameworks/spl.mdx) | Standard Peripheral Library for ST STM32 microcontrollers |
| [STM32Cube](../../frameworks/stm32cube.mdx) | STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency |
