---
title: "Dwenguino"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-atmelavr-dwenguino"></a>

# Dwenguino

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | AT90USB646 |
| **Frequency** | 16MHz |
| **Flash** | 60KB |
| **RAM** | 2KB |
| **Vendor** | [Dwengo](http://www.dwengo.org/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `dwenguino` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:dwenguino]
platform = atmelavr
board = dwenguino
```

You can override default Dwenguino settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [dwenguino.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/dwenguino.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:dwenguino]
platform = atmelavr
board = dwenguino

; change microcontroller
board_build.mcu = at90usb646

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support Dwenguino board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
