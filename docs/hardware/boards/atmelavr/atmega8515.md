---
title: "ATmega8515"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-atmelavr-atmega8515"></a>

# ATmega8515

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | ATMEGA8515 |
| **Frequency** | 16MHz |
| **Flash** | 8KB |
| **RAM** | 512B |
| **Vendor** | [Microchip](https://www.microchip.com/wwwproducts/en/ATmega8515?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `ATmega8515` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:ATmega8515]
platform = atmelavr
board = ATmega8515
```

You can override default ATmega8515 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [ATmega8515.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/ATmega8515.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:ATmega8515]
platform = atmelavr
board = ATmega8515

; change microcontroller
board_build.mcu = atmega8515

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support ATmega8515 board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
