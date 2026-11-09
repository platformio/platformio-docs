---
title: "AVR64DB32"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-atmelmegaavr-avr64db32"></a>

# AVR64DB32

## Hardware

Platform [Atmel megaAVR](../../platforms/atmelmegaavr.mdx): 8-bit MCUs Built for Real-time Control with Core Independent Peripherals combining intelligent hardware peripherals along with the low-power capability of an AVR core, megaAVR microcontrollers (MCUs) broaden the effectiveness of your real-time control systems.

| Specification | Value |
|---|---|
| **Microcontroller** | AVR64DB32 |
| **Frequency** | 24MHz |
| **Flash** | 64KB |
| **RAM** | 8KB |
| **Vendor** | [Microchip](https://www.microchip.com/wwwproducts/en/AVR64DB32?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `AVR64DB32` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:AVR64DB32]
platform = atmelmegaavr
board = AVR64DB32
```

You can override default AVR64DB32 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [AVR64DB32.json](https://github.com/platformio/platform-atmelmegaavr/blob/master/boards/AVR64DB32.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:AVR64DB32]
platform = atmelmegaavr
board = AVR64DB32

; change microcontroller
board_build.mcu = avr64db32

; change MCU frequency
board_build.f_cpu = 24000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support AVR64DB32 board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
