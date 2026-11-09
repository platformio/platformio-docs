---
title: "ATmega48PB"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-atmelavr-atmega48pb"></a>

# ATmega48PB

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | ATMEGA48PB |
| **Frequency** | 16MHz |
| **Flash** | 4KB |
| **RAM** | 512B |
| **Vendor** | [Microchip](https://www.microchip.com/wwwproducts/en/ATmega48PB?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `ATmega48PB` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:ATmega48PB]
platform = atmelavr
board = ATmega48PB
```

You can override default ATmega48PB settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [ATmega48PB.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/ATmega48PB.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:ATmega48PB]
platform = atmelavr
board = ATmega48PB

; change microcontroller
board_build.mcu = atmega48pb

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support ATmega48PB board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
