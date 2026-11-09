---
title: "Arduino LilyPad ATmega168"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-atmelavr-lilypadatmega168"></a>

# Arduino LilyPad ATmega168

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | ATMEGA168 |
| **Frequency** | 8MHz |
| **Flash** | 14KB |
| **RAM** | 1KB |
| **Vendor** | [Arduino](http://arduino.cc/en/Main/ArduinoBoardLilyPad?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `lilypadatmega168` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:lilypadatmega168]
platform = atmelavr
board = lilypadatmega168
```

You can override default Arduino LilyPad ATmega168 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [lilypadatmega168.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/lilypadatmega168.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:lilypadatmega168]
platform = atmelavr
board = lilypadatmega168

; change microcontroller
board_build.mcu = atmega168

; change MCU frequency
board_build.f_cpu = 8000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

Arduino LilyPad ATmega168 does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

| Compatible Tools | On-board | Default |
|---|---|---|
| [simavr](../../debug-probes/simavr.md) |  | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
