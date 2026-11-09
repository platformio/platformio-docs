---
title: "DataStation Mini"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-microchippic32-dsmini"></a>

# DataStation Mini

## Hardware

Platform [Microchip PIC32](../../platforms/microchippic32.md): Microchip's 32-bit portfolio with the MIPS microAptiv or M4K core offer high performance microcontrollers, and all the tools needed to develop your embedded projects. PIC32 MCUs gives your application the processing power, memory and peripherals your design needs!

| Specification | Value |
|---|---|
| **Microcontroller** | 32MX150F128C |
| **Frequency** | 40MHz |
| **Flash** | 120KB |
| **RAM** | 32KB |
| **Vendor** | [Makerology](http://www.makerologist.com/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `dsmini` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:dsmini]
platform = microchippic32
board = dsmini
```

You can override default DataStation Mini settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [dsmini.json](https://github.com/platformio/platform-microchippic32/blob/master/boards/dsmini.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:dsmini]
platform = microchippic32
board = dsmini

; change microcontroller
board_build.mcu = 32MX150F128C

; change MCU frequency
board_build.f_cpu = 40000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support DataStation Mini board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
