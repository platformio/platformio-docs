---
title: "Digispark Pro (32 byte buffer)"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-atmelavr-digispark-pro32"></a>

# Digispark Pro (32 byte buffer)

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | ATTINY167 |
| **Frequency** | 16MHz |
| **Flash** | 14.50KB |
| **RAM** | 512B |
| **Vendor** | [Digistump](http://digistump.com/products/109?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `digispark-pro32` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:digispark-pro32]
platform = atmelavr
board = digispark-pro32
```

You can override default Digispark Pro (32 byte buffer) settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [digispark-pro32.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/digispark-pro32.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:digispark-pro32]
platform = atmelavr
board = digispark-pro32

; change microcontroller
board_build.mcu = attiny167

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support Digispark Pro (32 byte buffer) board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
