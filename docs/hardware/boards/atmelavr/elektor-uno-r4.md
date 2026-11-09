---
title: "Elektor Uno R4"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Elektor Uno R4 (ATMEGA328PB, 16MHz, 31.50KB flash, 2KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Elektor Uno R4

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | ATMEGA328PB |
| **Frequency** | 16MHz |
| **Flash** | 31.50KB |
| **RAM** | 2KB |
| **Vendor** | [Elektor](https://www.elektor.com/elektor-uno-r4?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `elektor_uno_r4` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:elektor_uno_r4]
platform = atmelavr
board = elektor_uno_r4
```

To override a setting of the board manifest [elektor_uno_r4.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/elektor_uno_r4.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:elektor_uno_r4]
platform = atmelavr
board = elektor_uno_r4

; change microcontroller
board_build.mcu = atmega328pb

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the Elektor Uno R4 yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
