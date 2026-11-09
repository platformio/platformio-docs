---
title: "Curiosity Nano ATmega4809"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-atmelmegaavr-curiosity-nano-4809"></a>

# Curiosity Nano ATmega4809

## Hardware

Platform [Atmel megaAVR](../../platforms/atmelmegaavr.mdx): 8-bit MCUs Built for Real-time Control with Core Independent Peripherals combining intelligent hardware peripherals along with the low-power capability of an AVR core, megaAVR microcontrollers (MCUs) broaden the effectiveness of your real-time control systems.

| Specification | Value |
|---|---|
| **Microcontroller** | ATMEGA4809 |
| **Frequency** | 16MHz |
| **Flash** | 48KB |
| **RAM** | 6KB |
| **Vendor** | [Microchip](https://www.microchip.com/developmenttools/ProductDetails/DM320115?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `curiosity_nano_4809` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:curiosity_nano_4809]
platform = atmelmegaavr
board = curiosity_nano_4809
```

You can override default Curiosity Nano ATmega4809 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [curiosity_nano_4809.json](https://github.com/platformio/platform-atmelmegaavr/blob/master/boards/curiosity_nano_4809.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:curiosity_nano_4809]
platform = atmelmegaavr
board = curiosity_nano_4809

; change microcontroller
board_build.mcu = atmega4809

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support Curiosity Nano ATmega4809 board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
