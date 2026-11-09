---
title: "ST STM8S105K4T6 Breakout Board"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-ststm8-stm8sblack"></a>

# ST STM8S105K4T6 Breakout Board

## Hardware

Platform [ST STM8](../../platforms/ststm8.md): The STM8 is an 8-bit microcontroller family by STMicroelectronics an extended variant of the ST7 microcontroller architecture. STM8 microcontrollers are particularly low cost for a full-featured 8-bit microcontroller.

| Specification | Value |
|---|---|
| **Microcontroller** | STM8S105K4T6 |
| **Frequency** | 16MHz |
| **Flash** | 16KB |
| **RAM** | 2KB |
| **Vendor** | [ST](https://github.com/TG9541/stm8ef/wiki/Breakout-Boards?utm_source=platformio.org&utm_medium=docs#stm8s105k4t6-breakout-board) |

## Configuration

Please use `stm8sblack` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:stm8sblack]
platform = ststm8
board = stm8sblack
```

You can override default ST STM8S105K4T6 Breakout Board settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [stm8sblack.json](https://github.com/platformio/platform-ststm8/blob/master/boards/stm8sblack.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:stm8sblack]
platform = ststm8
board = stm8sblack

; change microcontroller
board_build.mcu = stm8s105k4t6

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Uploading

ST STM8S105K4T6 Breakout Board supports the following uploading protocols:

- `serial`
- `stlinkv2`

Default protocol is `serial`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:stm8sblack]
platform = ststm8
board = stm8sblack

upload_protocol = serial
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

ST STM8S105K4T6 Breakout Board does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

| Compatible Tools | On-board | Default |
|---|---|---|
| [ST-LINK](../../debug-probes/stlink.md) |  | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [Standard Peripheral Library](../../frameworks/spl.mdx) | Standard Peripheral Library for ST STM32 microcontrollers |
