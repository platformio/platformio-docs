---
title: "Arduino Nicla Vision (M4 core)"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Arduino Nicla Vision (M4 core) (STM32H747XIH6, 480MHz, 1MB flash, 287.35KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-ststm32-nicla-vision-m4"></a>

# Arduino Nicla Vision (M4 core)

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32H747XIH6 |
| **Frequency** | 480MHz |
| **Flash** | 1MB |
| **RAM** | 287.35KB |
| **Vendor** | [Arduino](https://store.arduino.cc/products/nicla-vision?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `nicla_vision_m4` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:nicla_vision_m4]
platform = ststm32
board = nicla_vision_m4
```

To override a setting of the board manifest [nicla_vision_m4.json](https://github.com/platformio/platform-ststm32/blob/master/boards/nicla_vision_m4.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:nicla_vision_m4]
platform = ststm32
board = nicla_vision_m4

; change microcontroller
board_build.mcu = stm32h747xih6

; change MCU frequency
board_build.f_cpu = 480000000L
```

## Uploading

Arduino Nicla Vision (M4 core) supports these upload protocols:

- `cmsis-dap`
- `dfu`
- `jlink`
- `mbed`
- `stlink`

The default is `dfu`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:nicla_vision_m4]
platform = ststm32
board = nicla_vision_m4

upload_protocol = dfu
```

## Debugging

The Arduino Nicla Vision (M4 core) has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) |  | Yes |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [ST-LINK](../../debug-probes/stlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
