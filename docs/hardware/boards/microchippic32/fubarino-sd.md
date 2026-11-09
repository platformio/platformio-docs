---
title: "Fubarino SD (1.5)"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-microchippic32-fubarino-sd"></a>

# Fubarino SD (1.5)

## Hardware

Platform [Microchip PIC32](../../platforms/microchippic32.md): Microchip's 32-bit portfolio with the MIPS microAptiv or M4K core offer high performance microcontrollers, and all the tools needed to develop your embedded projects. PIC32 MCUs gives your application the processing power, memory and peripherals your design needs!

| Specification | Value |
|---|---|
| **Microcontroller** | 32MX795F512H |
| **Frequency** | 80MHz |
| **Flash** | 508KB |
| **RAM** | 128KB |
| **Vendor** | [Fubarino](http://fubarino.org/sd/index.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `fubarino_sd` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:fubarino_sd]
platform = microchippic32
board = fubarino_sd
```

You can override default Fubarino SD (1.5) settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [fubarino_sd.json](https://github.com/platformio/platform-microchippic32/blob/master/boards/fubarino_sd.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:fubarino_sd]
platform = microchippic32
board = fubarino_sd

; change microcontroller
board_build.mcu = 32MX795F512H

; change MCU frequency
board_build.f_cpu = 80000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support Fubarino SD (1.5) board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
