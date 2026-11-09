---
title: "ATmega808"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-atmelmegaavr-atmega808"></a>

# ATmega808

## Hardware

Platform [Atmel megaAVR](../../platforms/atmelmegaavr.mdx): 8-bit MCUs Built for Real-time Control with Core Independent Peripherals combining intelligent hardware peripherals along with the low-power capability of an AVR core, megaAVR microcontrollers (MCUs) broaden the effectiveness of your real-time control systems.

| Specification | Value |
|---|---|
| **Microcontroller** | ATMEGA808 |
| **Frequency** | 16MHz |
| **Flash** | 8KB |
| **RAM** | 1KB |
| **Vendor** | [Microchip](https://www.microchip.com/wwwproducts/en/ATMEGA808?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `ATmega808` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:ATmega808]
platform = atmelmegaavr
board = ATmega808
```

You can override default ATmega808 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [ATmega808.json](https://github.com/platformio/platform-atmelmegaavr/blob/master/boards/ATmega808.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:ATmega808]
platform = atmelmegaavr
board = ATmega808

; change microcontroller
board_build.mcu = atmega808

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support ATmega808 board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
