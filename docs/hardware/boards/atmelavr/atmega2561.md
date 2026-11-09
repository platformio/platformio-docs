---
title: "ATmega2561"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "ATmega2561 (ATMEGA2561, 16MHz, 256KB flash, 8KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-atmelavr-atmega2561"></a>

# ATmega2561

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | ATMEGA2561 |
| **Frequency** | 16MHz |
| **Flash** | 256KB |
| **RAM** | 8KB |
| **Vendor** | [Microchip](https://www.microchip.com/wwwproducts/ATmega2561?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `ATmega2561` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:ATmega2561]
platform = atmelavr
board = ATmega2561
```

To override a setting of the board manifest [ATmega2561.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/ATmega2561.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:ATmega2561]
platform = atmelavr
board = ATmega2561

; change microcontroller
board_build.mcu = atmega2561

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the ATmega2561 yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
