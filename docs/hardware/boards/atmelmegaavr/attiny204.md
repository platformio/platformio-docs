---
title: "ATtiny204"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "ATtiny204 (ATTINY204, 16MHz, 2KB flash, 128B RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# ATtiny204

## Hardware

Platform [Atmel megaAVR](../../platforms/atmelmegaavr.mdx): 8-bit MCUs Built for Real-time Control with Core Independent Peripherals combining intelligent hardware peripherals along with the low-power capability of an AVR core, megaAVR microcontrollers (MCUs) broaden the effectiveness of your real-time control systems.

| Specification | Value |
|---|---|
| **Microcontroller** | ATTINY204 |
| **Frequency** | 16MHz |
| **Flash** | 2KB |
| **RAM** | 128B |
| **Vendor** | [Microchip](https://www.microchip.com/wwwproducts/en/ATTINY204?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `ATtiny204` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:ATtiny204]
platform = atmelmegaavr
board = ATtiny204
```

To override a setting of the board manifest [ATtiny204.json](https://github.com/platformio/platform-atmelmegaavr/blob/master/boards/ATtiny204.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:ATtiny204]
platform = atmelmegaavr
board = ATtiny204

; change microcontroller
board_build.mcu = attiny204

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the ATtiny204 yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
