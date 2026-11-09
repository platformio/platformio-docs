---
title: "SeeedStudio LoRa-E5 mini"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-ststm32-lora-e5-mini"></a>

# SeeedStudio LoRa-E5 mini

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32WLE5JC |
| **Frequency** | 48MHz |
| **Flash** | 256KB |
| **RAM** | 64KB |
| **Vendor** | [SeeedStudio](https://www.seeedstudio.com/LoRa-E5-mini-STM32WLE5JC-p-4869.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `lora_e5_mini` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:lora_e5_mini]
platform = ststm32
board = lora_e5_mini
```

You can override default SeeedStudio LoRa-E5 mini settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [lora_e5_mini.json](https://github.com/platformio/platform-ststm32/blob/master/boards/lora_e5_mini.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:lora_e5_mini]
platform = ststm32
board = lora_e5_mini

; change microcontroller
board_build.mcu = stm32wle5jc

; change MCU frequency
board_build.f_cpu = 48000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

SeeedStudio LoRa-E5 mini does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

| Compatible Tools | On-board | Default |
|---|---|---|
| [ST-LINK](../../debug-probes/stlink.md) |  | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
