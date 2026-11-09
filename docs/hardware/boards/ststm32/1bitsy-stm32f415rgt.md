---
title: "1Bitsy"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "1Bitsy (STM32F415RGT, 168MHz, 1MB flash, 128KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# 1Bitsy

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32F415RGT |
| **Frequency** | 168MHz |
| **Flash** | 1MB |
| **RAM** | 128KB |
| **Vendor** | [1BitSquared](http://1bitsy.org?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `1bitsy_stm32f415rgt` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:1bitsy_stm32f415rgt]
platform = ststm32
board = 1bitsy_stm32f415rgt
```

To override a setting of the board manifest [1bitsy_stm32f415rgt.json](https://github.com/platformio/platform-ststm32/blob/master/boards/1bitsy_stm32f415rgt.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:1bitsy_stm32f415rgt]
platform = ststm32
board = 1bitsy_stm32f415rgt

; change microcontroller
board_build.mcu = stm32f415rgt

; change MCU frequency
board_build.f_cpu = 168000000L
```

## Uploading

1Bitsy supports these upload protocols:

- `blackmagic`
- `cmsis-dap`
- `jlink`
- `stlink`

The default is `blackmagic`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:1bitsy_stm32f415rgt]
platform = ststm32
board = 1bitsy_stm32f415rgt

upload_protocol = blackmagic
```

## Debugging

The 1Bitsy has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [Black magic probe](../../debug-probes/blackmagic.md) |  | Yes |
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) |  |  |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [ST-LINK](../../debug-probes/stlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [CMSIS](../../frameworks/cmsis.md) | Vendor-independent hardware abstraction layer for the Cortex-M processor series |
| [LibOpenCM3](../../frameworks/libopencm3.md) | The libopencm3 project aims to create an open-source firmware library for various ARM Cortex-M microcontrollers. |
| [Standard Peripheral Library](../../frameworks/spl.mdx) | Standard Peripheral Library for ST STM32 microcontrollers |
| [STM32Cube](../../frameworks/stm32cube.mdx) | STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency |
