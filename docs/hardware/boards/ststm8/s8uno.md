---
title: "sduino UNO (STM8S105K6)"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-ststm8-s8uno"></a>

# sduino UNO (STM8S105K6)

## Hardware

Platform [ST STM8](../../platforms/ststm8.md): The STM8 is an 8-bit microcontroller family by STMicroelectronics an extended variant of the ST7 microcontroller architecture. STM8 microcontrollers are particularly low cost for a full-featured 8-bit microcontroller.

| Specification | Value |
|---|---|
| **Microcontroller** | STM8S105K6T6 |
| **Frequency** | 16MHz |
| **Flash** | 32KB |
| **RAM** | 2KB |
| **Vendor** | [sduino](https://github.com/roybaer/sduino_uno?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `s8uno` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:s8uno]
platform = ststm8
board = s8uno
```

You can override default sduino UNO (STM8S105K6) settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [s8uno.json](https://github.com/platformio/platform-ststm8/blob/master/boards/s8uno.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:s8uno]
platform = ststm8
board = s8uno

; change microcontroller
board_build.mcu = stm8s105k6t6

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Uploading

sduino UNO (STM8S105K6) supports the following uploading protocols:

- `serial`
- `stlinkv2`

Default protocol is `serial`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:s8uno]
platform = ststm8
board = s8uno

upload_protocol = serial
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

sduino UNO (STM8S105K6) does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

| Compatible Tools | On-board | Default |
|---|---|---|
| [ST-LINK](../../debug-probes/stlink.md) |  | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [Standard Peripheral Library](../../frameworks/spl.mdx) | Standard Peripheral Library for ST STM32 microcontrollers |
