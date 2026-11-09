---
title: "Pontech NoFire"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-microchippic32-nofire"></a>

# Pontech NoFire

## Hardware

Platform [Microchip PIC32](../../platforms/microchippic32.md): Microchip's 32-bit portfolio with the MIPS microAptiv or M4K core offer high performance microcontrollers, and all the tools needed to develop your embedded projects. PIC32 MCUs gives your application the processing power, memory and peripherals your design needs!

| Specification | Value |
|---|---|
| **Microcontroller** | 32MZ2048EFG100 |
| **Frequency** | 200MHz |
| **Flash** | 1.98MB |
| **RAM** | 512KB |
| **Vendor** | [Pontech](http://www.pontech.com/products?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `nofire` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:nofire]
platform = microchippic32
board = nofire
```

You can override default Pontech NoFire settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [nofire.json](https://github.com/platformio/platform-microchippic32/blob/master/boards/nofire.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:nofire]
platform = microchippic32
board = nofire

; change microcontroller
board_build.mcu = 32MZ2048EFG100

; change MCU frequency
board_build.f_cpu = 200000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support Pontech NoFire board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
