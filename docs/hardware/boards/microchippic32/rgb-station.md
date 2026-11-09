---
title: "RGB Station"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-microchippic32-rgb-station"></a>

# RGB Station

## Hardware

Platform [Microchip PIC32](../../platforms/microchippic32.md): Microchip's 32-bit portfolio with the MIPS microAptiv or M4K core offer high performance microcontrollers, and all the tools needed to develop your embedded projects. PIC32 MCUs gives your application the processing power, memory and peripherals your design needs!

| Specification | Value |
|---|---|
| **Microcontroller** | 32MX270F256D |
| **Frequency** | 48MHz |
| **Flash** | 240KB |
| **RAM** | 62KB |
| **Vendor** | [ChipKIT](https://github.com/chipKIT32/RGB_Station?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `rgb_station` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:rgb_station]
platform = microchippic32
board = rgb_station
```

You can override default RGB Station settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [rgb_station.json](https://github.com/platformio/platform-microchippic32/blob/master/boards/rgb_station.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:rgb_station]
platform = microchippic32
board = rgb_station

; change microcontroller
board_build.mcu = 32MX270F256D

; change MCU frequency
board_build.f_cpu = 48000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support RGB Station board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
