---
title: "AVR64DB28"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "AVR64DB28 (AVR64DB28, 24MHz, 64KB flash, 8KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-atmelmegaavr-avr64db28"></a>

# AVR64DB28

## Hardware

Platform [Atmel megaAVR](../../platforms/atmelmegaavr.mdx): 8-bit MCUs Built for Real-time Control with Core Independent Peripherals combining intelligent hardware peripherals along with the low-power capability of an AVR core, megaAVR microcontrollers (MCUs) broaden the effectiveness of your real-time control systems.

| Specification | Value |
|---|---|
| **Microcontroller** | AVR64DB28 |
| **Frequency** | 24MHz |
| **Flash** | 64KB |
| **RAM** | 8KB |
| **Vendor** | [Microchip](https://www.microchip.com/wwwproducts/en/AVR64DB28?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `AVR64DB28` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:AVR64DB28]
platform = atmelmegaavr
board = AVR64DB28
```

To override a setting of the board manifest [AVR64DB28.json](https://github.com/platformio/platform-atmelmegaavr/blob/master/boards/AVR64DB28.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:AVR64DB28]
platform = atmelmegaavr
board = AVR64DB28

; change microcontroller
board_build.mcu = avr64db28

; change MCU frequency
board_build.f_cpu = 24000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the AVR64DB28 yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
