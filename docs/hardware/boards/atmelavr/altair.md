---
title: "Altair"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Altair (ATMEGA256RFR2, 16MHz, 248KB flash, 32KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Altair

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | ATMEGA256RFR2 |
| **Frequency** | 16MHz |
| **Flash** | 248KB |
| **RAM** | 32KB |
| **Vendor** | [makerlab.mx](http://www.aquila.io/en?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `altair` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:altair]
platform = atmelavr
board = altair
```

To override a setting of the board manifest [altair.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/altair.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:altair]
platform = atmelavr
board = altair

; change microcontroller
board_build.mcu = atmega256rfr2

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the Altair yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
