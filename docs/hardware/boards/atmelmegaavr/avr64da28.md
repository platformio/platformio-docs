---
title: "AVR64DA28"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-atmelmegaavr-avr64da28"></a>

# AVR64DA28

## Hardware

Platform [Atmel megaAVR](../../platforms/atmelmegaavr.mdx): 8-bit MCUs Built for Real-time Control with Core Independent Peripherals combining intelligent hardware peripherals along with the low-power capability of an AVR core, megaAVR microcontrollers (MCUs) broaden the effectiveness of your real-time control systems.

| Specification | Value |
|---|---|
| **Microcontroller** | AVR64DA28 |
| **Frequency** | 24MHz |
| **Flash** | 64KB |
| **RAM** | 8KB |
| **Vendor** | [Microchip](https://www.microchip.com/wwwproducts/en/AVR64DA28?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `AVR64DA28` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:AVR64DA28]
platform = atmelmegaavr
board = AVR64DA28
```

You can override default AVR64DA28 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [AVR64DA28.json](https://github.com/platformio/platform-atmelmegaavr/blob/master/boards/AVR64DA28.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:AVR64DA28]
platform = atmelmegaavr
board = AVR64DA28

; change microcontroller
board_build.mcu = avr64da28

; change MCU frequency
board_build.f_cpu = 24000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support AVR64DA28 board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
