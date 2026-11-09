---
title: "Digilent chipKIT uC32"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-microchippic32-chipkit-uc32"></a>

# Digilent chipKIT uC32

## Hardware

Platform [Microchip PIC32](../../platforms/microchippic32.md): Microchip's 32-bit portfolio with the MIPS microAptiv or M4K core offer high performance microcontrollers, and all the tools needed to develop your embedded projects. PIC32 MCUs gives your application the processing power, memory and peripherals your design needs!

| Specification | Value |
|---|---|
| **Microcontroller** | 32MX340F512H |
| **Frequency** | 80MHz |
| **Flash** | 508KB |
| **RAM** | 32KB |
| **Vendor** | [Digilent](http://store.digilentinc.com/chipkit-uc32-basic-microcontroller-board-with-uno-r3-headers/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `chipkit_uc32` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:chipkit_uc32]
platform = microchippic32
board = chipkit_uc32
```

You can override default Digilent chipKIT uC32 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [chipkit_uc32.json](https://github.com/platformio/platform-microchippic32/blob/master/boards/chipkit_uc32.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:chipkit_uc32]
platform = microchippic32
board = chipkit_uc32

; change microcontroller
board_build.mcu = 32MX340F512H

; change MCU frequency
board_build.f_cpu = 80000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support Digilent chipKIT uC32 board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
