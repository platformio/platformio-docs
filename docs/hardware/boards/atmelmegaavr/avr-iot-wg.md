---
title: "AVR-IoT WG Development Board"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "AVR-IoT WG Development Board (ATMEGA4808, 16MHz, 48KB flash, 6KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# AVR-IoT WG Development Board

## Hardware

Platform [Atmel megaAVR](../../platforms/atmelmegaavr.mdx): 8-bit MCUs Built for Real-time Control with Core Independent Peripherals combining intelligent hardware peripherals along with the low-power capability of an AVR core, megaAVR microcontrollers (MCUs) broaden the effectiveness of your real-time control systems.

| Specification | Value |
|---|---|
| **Microcontroller** | ATMEGA4808 |
| **Frequency** | 16MHz |
| **Flash** | 48KB |
| **RAM** | 6KB |
| **Vendor** | [Microchip](https://www.microchip.com/developmenttools/ProductDetails/AC164160?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `avr_iot_wg` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:avr_iot_wg]
platform = atmelmegaavr
board = avr_iot_wg
```

To override a setting of the board manifest [avr_iot_wg.json](https://github.com/platformio/platform-atmelmegaavr/blob/master/boards/avr_iot_wg.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:avr_iot_wg]
platform = atmelmegaavr
board = avr_iot_wg

; change microcontroller
board_build.mcu = atmega4808

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the AVR-IoT WG Development Board yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
