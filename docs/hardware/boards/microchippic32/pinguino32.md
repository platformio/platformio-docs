---
title: "Olimex PIC32-PINGUINO"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-microchippic32-pinguino32"></a>

# Olimex PIC32-PINGUINO

## Hardware

Platform [Microchip PIC32](../../platforms/microchippic32.md): Microchip's 32-bit portfolio with the MIPS microAptiv or M4K core offer high performance microcontrollers, and all the tools needed to develop your embedded projects. PIC32 MCUs gives your application the processing power, memory and peripherals your design needs!

| Specification | Value |
|---|---|
| **Microcontroller** | 32MX440F256H |
| **Frequency** | 80MHz |
| **Flash** | 252KB |
| **RAM** | 32KB |
| **Vendor** | [Olimex](https://www.olimex.com/Products/Duino/PIC32/PIC32-PINGUINO/open-source-hardware?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `pinguino32` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:pinguino32]
platform = microchippic32
board = pinguino32
```

You can override default Olimex PIC32-PINGUINO settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [pinguino32.json](https://github.com/platformio/platform-microchippic32/blob/master/boards/pinguino32.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:pinguino32]
platform = microchippic32
board = pinguino32

; change microcontroller
board_build.mcu = 32MX440F256H

; change MCU frequency
board_build.f_cpu = 80000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support Olimex PIC32-PINGUINO board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
