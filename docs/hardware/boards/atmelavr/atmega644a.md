---
title: "ATmega644/A"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-atmelavr-atmega644a"></a>

# ATmega644/A

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | ATMEGA644A |
| **Frequency** | 16MHz |
| **Flash** | 64KB |
| **RAM** | 4KB |
| **Vendor** | [Microchip](https://www.microchip.com/wwwproducts/en/ATmega644a?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `ATmega644A` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:ATmega644A]
platform = atmelavr
board = ATmega644A
```

You can override default ATmega644/A settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [ATmega644A.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/ATmega644A.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:ATmega644A]
platform = atmelavr
board = ATmega644A

; change microcontroller
board_build.mcu = atmega644a

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support ATmega644/A board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
