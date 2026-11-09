---
title: "ATmega1608"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-atmelmegaavr-atmega1608"></a>

# ATmega1608

## Hardware

Platform [Atmel megaAVR](../../platforms/atmelmegaavr.mdx): 8-bit MCUs Built for Real-time Control with Core Independent Peripherals combining intelligent hardware peripherals along with the low-power capability of an AVR core, megaAVR microcontrollers (MCUs) broaden the effectiveness of your real-time control systems.

| Specification | Value |
|---|---|
| **Microcontroller** | ATMEGA1608 |
| **Frequency** | 16MHz |
| **Flash** | 16KB |
| **RAM** | 2KB |
| **Vendor** | [Microchip](https://www.microchip.com/wwwproducts/en/ATMEGA1608?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `ATmega1608` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:ATmega1608]
platform = atmelmegaavr
board = ATmega1608
```

You can override default ATmega1608 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [ATmega1608.json](https://github.com/platformio/platform-atmelmegaavr/blob/master/boards/ATmega1608.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:ATmega1608]
platform = atmelmegaavr
board = ATmega1608

; change microcontroller
board_build.mcu = atmega1608

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support ATmega1608 board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
