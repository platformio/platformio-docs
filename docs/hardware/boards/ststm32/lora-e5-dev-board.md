---
title: "SeeedStudio LoRa E5 Dev Board"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "SeeedStudio LoRa E5 Dev Board (STM32WLE5JC, 48MHz, 256KB flash, 64KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# SeeedStudio LoRa E5 Dev Board

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32WLE5JC |
| **Frequency** | 48MHz |
| **Flash** | 256KB |
| **RAM** | 64KB |
| **Vendor** | [SeeedStudio](https://www.seeedstudio.com/LoRa-E5-Dev-Kit-p-4868.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `lora_e5_dev_board` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:lora_e5_dev_board]
platform = ststm32
board = lora_e5_dev_board
```

To override a setting of the board manifest [lora_e5_dev_board.json](https://github.com/platformio/platform-ststm32/blob/master/boards/lora_e5_dev_board.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:lora_e5_dev_board]
platform = ststm32
board = lora_e5_dev_board

; change microcontroller
board_build.mcu = stm32wle5jc

; change MCU frequency
board_build.f_cpu = 48000000L
```

## Uploading

SeeedStudio LoRa E5 Dev Board supports these upload protocols:

- `jlink`
- `stlink`

The default is `stlink`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:lora_e5_dev_board]
platform = ststm32
board = lora_e5_dev_board

upload_protocol = stlink
```

## Debugging

The SeeedStudio LoRa E5 Dev Board has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [J-LINK](../../debug-probes/jlink.md) |  | Yes |
| [ST-LINK](../../debug-probes/stlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
