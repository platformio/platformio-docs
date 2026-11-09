---
title: "Arduino Nano ATmega328 (New Bootloader)"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-atmelavr-nanoatmega328new"></a>

# Arduino Nano ATmega328 (New Bootloader)

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | ATMEGA328P |
| **Frequency** | 16MHz |
| **Flash** | 30KB |
| **RAM** | 2KB |
| **Vendor** | [Arduino](https://www.arduino.cc/en/Main/ArduinoBoardNano?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `nanoatmega328new` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:nanoatmega328new]
platform = atmelavr
board = nanoatmega328new
```

You can override default Arduino Nano ATmega328 (New Bootloader) settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [nanoatmega328new.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/nanoatmega328new.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:nanoatmega328new]
platform = atmelavr
board = nanoatmega328new

; change microcontroller
board_build.mcu = atmega328p

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

Arduino Nano ATmega328 (New Bootloader) does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

| Compatible Tools | On-board | Default |
|---|---|---|
| [avr-stub](../../debug-probes/avr-stub.md) |  | Yes |
| [simavr](../../debug-probes/simavr.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
