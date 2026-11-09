---
title: "4D Systems PICadillo 35T"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-microchippic32-picadillo-35t"></a>

# 4D Systems PICadillo 35T

## Hardware

Platform [Microchip PIC32](../../platforms/microchippic32.md): Microchip's 32-bit portfolio with the MIPS microAptiv or M4K core offer high performance microcontrollers, and all the tools needed to develop your embedded projects. PIC32 MCUs gives your application the processing power, memory and peripherals your design needs!

| Specification | Value |
|---|---|
| **Microcontroller** | 32MX795F512L |
| **Frequency** | 80MHz |
| **Flash** | 508KB |
| **RAM** | 128KB |
| **Vendor** | [4D Systems](http://www.4dsystems.com.au/product/Picadillo_35T/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `picadillo_35t` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:picadillo_35t]
platform = microchippic32
board = picadillo_35t
```

You can override default 4D Systems PICadillo 35T settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [picadillo_35t.json](https://github.com/platformio/platform-microchippic32/blob/master/boards/picadillo_35t.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:picadillo_35t]
platform = microchippic32
board = picadillo_35t

; change microcontroller
board_build.mcu = 32MX795F512L

; change MCU frequency
board_build.f_cpu = 80000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support 4D Systems PICadillo 35T board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
