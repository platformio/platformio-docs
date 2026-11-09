---
title: "ATmega8535"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "ATmega8535 (ATMEGA8535, 16MHz, 8KB flash, 512B RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# ATmega8535

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | ATMEGA8535 |
| **Frequency** | 16MHz |
| **Flash** | 8KB |
| **RAM** | 512B |
| **Vendor** | [Microchip](https://www.microchip.com/wwwproducts/en/ATmega8535?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `ATmega8535` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:ATmega8535]
platform = atmelavr
board = ATmega8535
```

To override a setting of the board manifest [ATmega8535.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/ATmega8535.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:ATmega8535]
platform = atmelavr
board = ATmega8535

; change microcontroller
board_build.mcu = atmega8535

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the ATmega8535 yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
