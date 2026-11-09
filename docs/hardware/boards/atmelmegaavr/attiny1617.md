---
title: "ATtiny1617"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "ATtiny1617 (ATTINY1617, 16MHz, 16KB flash, 2KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# ATtiny1617

## Hardware

Platform [Atmel megaAVR](../../platforms/atmelmegaavr.mdx): 8-bit MCUs Built for Real-time Control with Core Independent Peripherals combining intelligent hardware peripherals along with the low-power capability of an AVR core, megaAVR microcontrollers (MCUs) broaden the effectiveness of your real-time control systems.

| Specification | Value |
|---|---|
| **Microcontroller** | ATTINY1617 |
| **Frequency** | 16MHz |
| **Flash** | 16KB |
| **RAM** | 2KB |
| **Vendor** | [Microchip](https://www.microchip.com/wwwproducts/en/ATTINY1617?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `ATtiny1617` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:ATtiny1617]
platform = atmelmegaavr
board = ATtiny1617
```

To override a setting of the board manifest [ATtiny1617.json](https://github.com/platformio/platform-atmelmegaavr/blob/master/boards/ATtiny1617.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:ATtiny1617]
platform = atmelmegaavr
board = ATtiny1617

; change microcontroller
board_build.mcu = attiny1617

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the ATtiny1617 yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
