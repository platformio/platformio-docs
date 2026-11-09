---
title: "ATtiny814"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "ATtiny814 (ATTINY814, 16MHz, 8KB flash, 512B RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-atmelmegaavr-attiny814"></a>

# ATtiny814

## Hardware

Platform [Atmel megaAVR](../../platforms/atmelmegaavr.mdx): 8-bit MCUs Built for Real-time Control with Core Independent Peripherals combining intelligent hardware peripherals along with the low-power capability of an AVR core, megaAVR microcontrollers (MCUs) broaden the effectiveness of your real-time control systems.

| Specification | Value |
|---|---|
| **Microcontroller** | ATTINY814 |
| **Frequency** | 16MHz |
| **Flash** | 8KB |
| **RAM** | 512B |
| **Vendor** | [Microchip](https://www.microchip.com/wwwproducts/en/ATTINY814?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `ATtiny814` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:ATtiny814]
platform = atmelmegaavr
board = ATtiny814
```

To override a setting of the board manifest [ATtiny814.json](https://github.com/platformio/platform-atmelmegaavr/blob/master/boards/ATtiny814.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:ATtiny814]
platform = atmelmegaavr
board = ATtiny814

; change microcontroller
board_build.mcu = attiny814

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the ATtiny814 yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
