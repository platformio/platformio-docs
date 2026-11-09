---
title: "Digispark Pro (16 MHz) (64 byte buffer)"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Digispark Pro (16 MHz) (64 byte buffer) (ATTINY167, 16MHz, 14.50KB flash, 512B RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Digispark Pro (16 MHz) (64 byte buffer)

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | ATTINY167 |
| **Frequency** | 16MHz |
| **Flash** | 14.50KB |
| **RAM** | 512B |
| **Vendor** | [Digistump](http://digistump.com/products/109?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `digispark-pro64` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:digispark-pro64]
platform = atmelavr
board = digispark-pro64
```

To override a setting of the board manifest [digispark-pro64.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/digispark-pro64.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:digispark-pro64]
platform = atmelavr
board = digispark-pro64

; change microcontroller
board_build.mcu = attiny167

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the Digispark Pro (16 MHz) (64 byte buffer) yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
