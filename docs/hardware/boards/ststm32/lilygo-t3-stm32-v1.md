---
title: "LilyGo T3-STM32"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-ststm32-lilygo-t3-stm32-v1"></a>

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

Please use `lilygo_t3_stm32_v1` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:lilygo_t3_stm32_v1]
platform = ststm32
board = lilygo_t3_stm32_v1
```

You can override default LilyGo T3-STM32 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [lilygo_t3_stm32_v1.json](https://github.com/platformio/platform-ststm32/blob/master/boards/lilygo_t3_stm32_v1.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

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

LilyGo T3-STM32 supports the following uploading protocols:

- `jlink`
- `serial`
- `stlink`

Default protocol is `serial`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:lilygo_t3_stm32_v1]
platform = ststm32
board = lilygo_t3_stm32_v1

upload_protocol = serial
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

LilyGo T3-STM32 does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

| Compatible Tools | On-board | Default |
|---|---|---|
| [J-LINK](../../debug-probes/jlink.md) |  | Yes |
| [ST-LINK](../../debug-probes/stlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
