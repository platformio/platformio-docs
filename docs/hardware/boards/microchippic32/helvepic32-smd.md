---
title: "HelvePic32"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-microchippic32-helvepic32-smd"></a>

# HelvePic32

## Hardware

Platform [Microchip PIC32](../../platforms/microchippic32.md): Microchip's 32-bit portfolio with the MIPS microAptiv or M4K core offer high performance microcontrollers, and all the tools needed to develop your embedded projects. PIC32 MCUs gives your application the processing power, memory and peripherals your design needs!

| Specification | Value |
|---|---|
| **Microcontroller** | 32MX250F128D |
| **Frequency** | 48MHz |
| **Flash** | 120KB |
| **RAM** | 32KB |
| **Vendor** | [BOXTEC](https://www.helvepic32.org/shop-1/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `helvepic32_smd` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:helvepic32_smd]
platform = microchippic32
board = helvepic32_smd
```

You can override default HelvePic32 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [helvepic32_smd.json](https://github.com/platformio/platform-microchippic32/blob/master/boards/helvepic32_smd.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:helvepic32_smd]
platform = microchippic32
board = helvepic32_smd

; change microcontroller
board_build.mcu = 32MX250F128D

; change MCU frequency
board_build.f_cpu = 48000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support HelvePic32 board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
