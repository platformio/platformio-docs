---
title: "ATtiny1624"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-atmelmegaavr-attiny1624"></a>

# ATtiny1624

## Hardware

Platform [Atmel megaAVR](../../platforms/atmelmegaavr.mdx): 8-bit MCUs Built for Real-time Control with Core Independent Peripherals combining intelligent hardware peripherals along with the low-power capability of an AVR core, megaAVR microcontrollers (MCUs) broaden the effectiveness of your real-time control systems.

| Specification | Value |
|---|---|
| **Microcontroller** | ATTINY1624 |
| **Frequency** | 16MHz |
| **Flash** | 16KB |
| **RAM** | 2KB |
| **Vendor** | [Microchip](https://www.microchip.com/wwwproducts/en/ATTINY1624?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `ATtiny1624` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:ATtiny1624]
platform = atmelmegaavr
board = ATtiny1624
```

You can override default ATtiny1624 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [ATtiny1624.json](https://github.com/platformio/platform-atmelmegaavr/blob/master/boards/ATtiny1624.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:ATtiny1624]
platform = atmelmegaavr
board = ATtiny1624

; change microcontroller
board_build.mcu = attiny1624

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support ATtiny1624 board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
