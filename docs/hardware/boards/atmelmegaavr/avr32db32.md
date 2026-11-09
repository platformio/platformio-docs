---
title: "AVR32DB32"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "AVR32DB32 (AVR32DB32, 24MHz, 32KB flash, 4KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-atmelmegaavr-avr32db32"></a>

# AVR32DB32

## Hardware

Platform [Atmel megaAVR](../../platforms/atmelmegaavr.mdx): 8-bit MCUs Built for Real-time Control with Core Independent Peripherals combining intelligent hardware peripherals along with the low-power capability of an AVR core, megaAVR microcontrollers (MCUs) broaden the effectiveness of your real-time control systems.

| Specification | Value |
|---|---|
| **Microcontroller** | AVR32DB32 |
| **Frequency** | 24MHz |
| **Flash** | 32KB |
| **RAM** | 4KB |
| **Vendor** | [Microchip](https://www.microchip.com/wwwproducts/en/AVR32DB32?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `AVR32DB32` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:AVR32DB32]
platform = atmelmegaavr
board = AVR32DB32
```

To override a setting of the board manifest [AVR32DB32.json](https://github.com/platformio/platform-atmelmegaavr/blob/master/boards/AVR32DB32.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:AVR32DB32]
platform = atmelmegaavr
board = AVR32DB32

; change microcontroller
board_build.mcu = avr32db32

; change MCU frequency
board_build.f_cpu = 24000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the AVR32DB32 yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
