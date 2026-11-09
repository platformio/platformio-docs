---
title: "AVR64DD14"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "AVR64DD14 (AVR64DD14, 24MHz, 64KB flash, 8KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# AVR64DD14

## Hardware

Platform [Atmel megaAVR](../../platforms/atmelmegaavr.mdx): 8-bit MCUs Built for Real-time Control with Core Independent Peripherals combining intelligent hardware peripherals along with the low-power capability of an AVR core, megaAVR microcontrollers (MCUs) broaden the effectiveness of your real-time control systems.

| Specification | Value |
|---|---|
| **Microcontroller** | AVR64DD14 |
| **Frequency** | 24MHz |
| **Flash** | 64KB |
| **RAM** | 8KB |
| **Vendor** | [Microchip](https://www.microchip.com/wwwproducts/en/AVR64DD14?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `AVR64DD14` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:AVR64DD14]
platform = atmelmegaavr
board = AVR64DD14
```

To override a setting of the board manifest [AVR64DD14.json](https://github.com/platformio/platform-atmelmegaavr/blob/master/boards/AVR64DD14.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:AVR64DD14]
platform = atmelmegaavr
board = AVR64DD14

; change microcontroller
board_build.mcu = avr64dd14

; change MCU frequency
board_build.f_cpu = 24000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the AVR64DD14 yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
