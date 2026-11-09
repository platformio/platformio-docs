---
title: "ATmega164A"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "ATmega164A (ATMEGA164A, 16MHz, 16KB flash, 1KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# ATmega164A

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | ATMEGA164A |
| **Frequency** | 16MHz |
| **Flash** | 16KB |
| **RAM** | 1KB |
| **Vendor** | [Microchip](https://www.microchip.com/wwwproducts/en/ATmega164a?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `ATmega164A` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:ATmega164A]
platform = atmelavr
board = ATmega164A
```

To override a setting of the board manifest [ATmega164A.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/ATmega164A.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:ATmega164A]
platform = atmelavr
board = ATmega164A

; change microcontroller
board_build.mcu = atmega164a

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the ATmega164A yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
