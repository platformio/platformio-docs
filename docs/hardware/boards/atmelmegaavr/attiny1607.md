---
title: "ATtiny1607"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-atmelmegaavr-attiny1607"></a>

# ATtiny1607

## Hardware

Platform [Atmel megaAVR](../../platforms/atmelmegaavr.mdx): 8-bit MCUs Built for Real-time Control with Core Independent Peripherals combining intelligent hardware peripherals along with the low-power capability of an AVR core, megaAVR microcontrollers (MCUs) broaden the effectiveness of your real-time control systems.

| Specification | Value |
|---|---|
| **Microcontroller** | ATTINY1607 |
| **Frequency** | 16MHz |
| **Flash** | 16KB |
| **RAM** | 1KB |
| **Vendor** | [Microchip](https://www.microchip.com/wwwproducts/en/ATTINY1607?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `ATtiny1607` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:ATtiny1607]
platform = atmelmegaavr
board = ATtiny1607
```

You can override default ATtiny1607 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [ATtiny1607.json](https://github.com/platformio/platform-atmelmegaavr/blob/master/boards/ATtiny1607.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:ATtiny1607]
platform = atmelmegaavr
board = ATtiny1607

; change microcontroller
board_build.mcu = attiny1607

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support ATtiny1607 board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
