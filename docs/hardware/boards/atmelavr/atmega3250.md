---
title: "ATmega3250/A"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-atmelavr-atmega3250"></a>

# ATmega3250/A

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | ATMEGA3250 |
| **Frequency** | 16MHz |
| **Flash** | 32KB |
| **RAM** | 2KB |
| **Vendor** | [Microchip](https://www.microchip.com/wwwproducts/en/ATmega3250?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `ATmega3250` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:ATmega3250]
platform = atmelavr
board = ATmega3250
```

You can override default ATmega3250/A settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [ATmega3250.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/ATmega3250.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:ATmega3250]
platform = atmelavr
board = ATmega3250

; change microcontroller
board_build.mcu = atmega3250

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support ATmega3250/A board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
