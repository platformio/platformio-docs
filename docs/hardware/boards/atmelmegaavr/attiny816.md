---
title: "ATtiny816"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "ATtiny816 (ATTINY816, 16MHz, 8KB flash, 512B RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-atmelmegaavr-attiny816"></a>

# ATtiny816

## Hardware

Platform [Atmel megaAVR](../../platforms/atmelmegaavr.mdx): 8-bit MCUs Built for Real-time Control with Core Independent Peripherals combining intelligent hardware peripherals along with the low-power capability of an AVR core, megaAVR microcontrollers (MCUs) broaden the effectiveness of your real-time control systems.

| Specification | Value |
|---|---|
| **Microcontroller** | ATTINY816 |
| **Frequency** | 16MHz |
| **Flash** | 8KB |
| **RAM** | 512B |
| **Vendor** | [Microchip](https://www.microchip.com/wwwproducts/en/ATTINY816?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `ATtiny816` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:ATtiny816]
platform = atmelmegaavr
board = ATtiny816
```

To override a setting of the board manifest [ATtiny816.json](https://github.com/platformio/platform-atmelmegaavr/blob/master/boards/ATtiny816.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:ATtiny816]
platform = atmelmegaavr
board = ATtiny816

; change microcontroller
board_build.mcu = attiny816

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the ATtiny816 yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
