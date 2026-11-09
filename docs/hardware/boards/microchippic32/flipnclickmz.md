---
title: "MikroElektronika Flip N Click MZ"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-microchippic32-flipnclickmz"></a>

# MikroElektronika Flip N Click MZ

## Hardware

Platform [Microchip PIC32](../../platforms/microchippic32.md): Microchip's 32-bit portfolio with the MIPS microAptiv or M4K core offer high performance microcontrollers, and all the tools needed to develop your embedded projects. PIC32 MCUs gives your application the processing power, memory and peripherals your design needs!

| Specification | Value |
|---|---|
| **Microcontroller** | 32MZ2048EFH100 |
| **Frequency** | 252MHz |
| **Flash** | 1.98MB |
| **RAM** | 512KB |
| **Vendor** | [MikroElektronika](https://shop.mikroe.com/flipclick-pic32mz?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `flipnclickmz` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:flipnclickmz]
platform = microchippic32
board = flipnclickmz
```

You can override default MikroElektronika Flip N Click MZ settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [flipnclickmz.json](https://github.com/platformio/platform-microchippic32/blob/master/boards/flipnclickmz.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:flipnclickmz]
platform = microchippic32
board = flipnclickmz

; change microcontroller
board_build.mcu = 32MZ2048EFH100

; change MCU frequency
board_build.f_cpu = 252000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support MikroElektronika Flip N Click MZ board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
