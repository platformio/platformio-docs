---
title: "Elektor Uno R4"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-atmelavr-elektor-uno-r4"></a>

# Elektor Uno R4

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | ATMEGA328PB |
| **Frequency** | 16MHz |
| **Flash** | 31.50KB |
| **RAM** | 2KB |
| **Vendor** | [Elektor](https://www.elektor.com/elektor-uno-r4?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `elektor_uno_r4` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:elektor_uno_r4]
platform = atmelavr
board = elektor_uno_r4
```

You can override default Elektor Uno R4 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [elektor_uno_r4.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/elektor_uno_r4.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:elektor_uno_r4]
platform = atmelavr
board = elektor_uno_r4

; change microcontroller
board_build.mcu = atmega328pb

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support Elektor Uno R4 board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
