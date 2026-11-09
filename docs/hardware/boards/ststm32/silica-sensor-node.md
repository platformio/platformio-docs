---
title: "ST Sensor Node"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "ST Sensor Node (STM32L476JG, 80MHz, 1MB flash, 128KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# ST Sensor Node

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32L476JG |
| **Frequency** | 80MHz |
| **Flash** | 1MB |
| **RAM** | 128KB |
| **Vendor** | [Avnet Silica](https://www.avnet.com/shop/emea/products/avnet-engineering-services/silicastmsensornodeplus-3074457345633959668/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `silica_sensor_node` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:silica_sensor_node]
platform = ststm32
board = silica_sensor_node
```

To override a setting of the board manifest [silica_sensor_node.json](https://github.com/platformio/platform-ststm32/blob/master/boards/silica_sensor_node.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:silica_sensor_node]
platform = ststm32
board = silica_sensor_node

; change microcontroller
board_build.mcu = stm32l476jg

; change MCU frequency
board_build.f_cpu = 80000000L
```

## Uploading

ST Sensor Node supports these upload protocols:

- `blackmagic`
- `cmsis-dap`
- `jlink`
- `mbed`
- `stlink`

The default is `mbed`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:silica_sensor_node]
platform = ststm32
board = silica_sensor_node

upload_protocol = mbed
```

## Debugging

The ST Sensor Node has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

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
| [STM32Cube](../../frameworks/stm32cube.mdx) | STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency |
