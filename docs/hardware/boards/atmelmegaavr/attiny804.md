---
title: "ATtiny804"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-atmelmegaavr-attiny804"></a>

# ATtiny804

## Hardware

Platform [Atmel megaAVR](../../platforms/atmelmegaavr.mdx): 8-bit MCUs Built for Real-time Control with Core Independent Peripherals combining intelligent hardware peripherals along with the low-power capability of an AVR core, megaAVR microcontrollers (MCUs) broaden the effectiveness of your real-time control systems.

| Specification | Value |
|---|---|
| **Microcontroller** | ATTINY804 |
| **Frequency** | 16MHz |
| **Flash** | 8KB |
| **RAM** | 512B |
| **Vendor** | [Microchip](https://www.microchip.com/wwwproducts/en/ATTINY804?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `ATtiny804` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:ATtiny804]
platform = atmelmegaavr
board = ATtiny804
```

You can override default ATtiny804 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [ATtiny804.json](https://github.com/platformio/platform-atmelmegaavr/blob/master/boards/ATtiny804.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:ATtiny804]
platform = atmelmegaavr
board = ATtiny804

; change microcontroller
board_build.mcu = attiny804

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support ATtiny804 board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
