---
title: "ATmega169/P/PA"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "ATmega169/P/PA (ATMEGA169P, 16MHz, 16KB flash, 1KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# ATmega169/P/PA

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | ATMEGA169P |
| **Frequency** | 16MHz |
| **Flash** | 16KB |
| **RAM** | 1KB |
| **Vendor** | [Microchip](https://www.microchip.com/wwwproducts/en/ATmega169P?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `ATmega169P` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:ATmega169P]
platform = atmelavr
board = ATmega169P
```

To override a setting of the board manifest [ATmega169P.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/ATmega169P.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:ATmega169P]
platform = atmelavr
board = ATmega169P

; change microcontroller
board_build.mcu = atmega169p

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the ATmega169/P/PA yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
