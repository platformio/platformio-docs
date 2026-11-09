---
title: "ATmega640"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-atmelavr-atmega640"></a>

# ATmega640

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | ATMEGA640 |
| **Frequency** | 16MHz |
| **Flash** | 64KB |
| **RAM** | 8KB |
| **Vendor** | [Microchip](https://www.microchip.com/wwwproducts/ATmega640?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `ATmega640` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:ATmega640]
platform = atmelavr
board = ATmega640
```

You can override default ATmega640 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [ATmega640.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/ATmega640.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:ATmega640]
platform = atmelavr
board = ATmega640

; change microcontroller
board_build.mcu = atmega640

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support ATmega640 board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
