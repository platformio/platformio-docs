---
title: "AVR-IoT WG Development Board"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-atmelmegaavr-avr-iot-wg"></a>

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

Please use `avr_iot_wg` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:avr_iot_wg]
platform = atmelmegaavr
board = avr_iot_wg
```

You can override default AVR-IoT WG Development Board settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [avr_iot_wg.json](https://github.com/platformio/platform-atmelmegaavr/blob/master/boards/avr_iot_wg.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

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

[Debugging](../../../guides/debugging/index.md) currently does not support AVR-IoT WG Development Board board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
