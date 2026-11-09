---
title: "ATtiny3227"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-atmelmegaavr-attiny3227"></a>

# ATtiny3227

## Hardware

Platform [Atmel megaAVR](../../platforms/atmelmegaavr.mdx): 8-bit MCUs Built for Real-time Control with Core Independent Peripherals combining intelligent hardware peripherals along with the low-power capability of an AVR core, megaAVR microcontrollers (MCUs) broaden the effectiveness of your real-time control systems.

| Specification | Value |
|---|---|
| **Microcontroller** | ATTINY3227 |
| **Frequency** | 16MHz |
| **Flash** | 32KB |
| **RAM** | 3KB |
| **Vendor** | [Microchip](https://www.microchip.com/wwwproducts/en/ATTINY3227?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `ATtiny3227` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:ATtiny3227]
platform = atmelmegaavr
board = ATtiny3227
```

You can override default ATtiny3227 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [ATtiny3227.json](https://github.com/platformio/platform-atmelmegaavr/blob/master/boards/ATtiny3227.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:ATtiny3227]
platform = atmelmegaavr
board = ATtiny3227

; change microcontroller
board_build.mcu = attiny3227

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support ATtiny3227 board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
