---
title: "96Boards Neonkey"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "96Boards Neonkey (STM32F427VIT6, 168MHz, 1.99MB flash, 256KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# 96Boards Neonkey

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32F427VIT6 |
| **Frequency** | 168MHz |
| **Flash** | 1.99MB |
| **RAM** | 256KB |
| **Vendor** | [96Boards](https://www.96boards.org/product/aerocore2/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `b96b_aerocore2` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:b96b_aerocore2]
platform = ststm32
board = b96b_aerocore2
```

To override a setting of the board manifest [b96b_aerocore2.json](https://github.com/platformio/platform-ststm32/blob/master/boards/b96b_aerocore2.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:b96b_aerocore2]
platform = ststm32
board = b96b_aerocore2

; change microcontroller
board_build.mcu = stm32f427vit6

; change MCU frequency
board_build.f_cpu = 168000000L
```

## Uploading

96Boards Neonkey supports these upload protocols:

- `blackmagic`
- `dfu`
- `jlink`
- `serial`
- `stlink`

The default is `dfu`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:b96b_aerocore2]
platform = ststm32
board = b96b_aerocore2

upload_protocol = dfu
```

## Debugging

The 96Boards Neonkey has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [Black magic probe](../../debug-probes/blackmagic.md) |  | Yes |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [ST-LINK](../../debug-probes/stlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [CMSIS](../../frameworks/cmsis.md) | Vendor-independent hardware abstraction layer for the Cortex-M processor series |
| [LibOpenCM3](../../frameworks/libopencm3.md) | The libopencm3 project aims to create an open-source firmware library for various ARM Cortex-M microcontrollers. |
| [STM32Cube](../../frameworks/stm32cube.mdx) | STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency |
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
