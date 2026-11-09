---
title: "ATmega3209"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-atmelmegaavr-atmega3209"></a>

# ATmega3209

## Hardware

Platform [Atmel megaAVR](../../platforms/atmelmegaavr.mdx): 8-bit MCUs Built for Real-time Control with Core Independent Peripherals combining intelligent hardware peripherals along with the low-power capability of an AVR core, megaAVR microcontrollers (MCUs) broaden the effectiveness of your real-time control systems.

| Specification | Value |
|---|---|
| **Microcontroller** | ATMEGA3209 |
| **Frequency** | 16MHz |
| **Flash** | 32KB |
| **RAM** | 4KB |
| **Vendor** | [Microchip](https://www.microchip.com/wwwproducts/en/ATMEGA3209?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `ATmega3209` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:ATmega3209]
platform = atmelmegaavr
board = ATmega3209
```

You can override default ATmega3209 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [ATmega3209.json](https://github.com/platformio/platform-atmelmegaavr/blob/master/boards/ATmega3209.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:ATmega3209]
platform = atmelmegaavr
board = ATmega3209

; change microcontroller
board_build.mcu = atmega3209

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support ATmega3209 board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
