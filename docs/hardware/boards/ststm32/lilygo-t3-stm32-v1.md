---
title: "LilyGo T3-STM32"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "LilyGo T3-STM32 (STM32WLE5CCU7, 48MHz, 256KB flash, 64KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# LilyGo T3-STM32

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32WLE5CCU7 |
| **Frequency** | 48MHz |
| **Flash** | 256KB |
| **RAM** | 64KB |
| **Vendor** | [LilyGo](https://github.com/Xinyuan-LilyGO/T3-STM32?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `lilygo_t3_stm32_v1` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:lilygo_t3_stm32_v1]
platform = ststm32
board = lilygo_t3_stm32_v1
```

To override a setting of the board manifest [lilygo_t3_stm32_v1.json](https://github.com/platformio/platform-ststm32/blob/master/boards/lilygo_t3_stm32_v1.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:lilygo_t3_stm32_v1]
platform = ststm32
board = lilygo_t3_stm32_v1

; change microcontroller
board_build.mcu = stm32wle5ccu7

; change MCU frequency
board_build.f_cpu = 48000000L
```

## Uploading

LilyGo T3-STM32 supports these upload protocols:

- `jlink`
- `serial`
- `stlink`

The default is `serial`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:lilygo_t3_stm32_v1]
platform = ststm32
board = lilygo_t3_stm32_v1

upload_protocol = serial
```

## Debugging

The LilyGo T3-STM32 has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

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
