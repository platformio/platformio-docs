---
title: "Generic ATtiny828"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Generic ATtiny828 (ATTINY828, 8MHz, 8KB flash, 512B RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-atmelavr-attiny828"></a>

# Generic ATtiny828

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | ATTINY828 |
| **Frequency** | 8MHz |
| **Flash** | 8KB |
| **RAM** | 512B |
| **Vendor** | [Atmel](http://www.atmel.com/devices/ATTINY828.aspx?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `attiny828` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:attiny828]
platform = atmelavr
board = attiny828
```

To override a setting of the board manifest [attiny828.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/attiny828.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:attiny828]
platform = atmelavr
board = attiny828

; change microcontroller
board_build.mcu = attiny828

; change MCU frequency
board_build.f_cpu = 8000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the Generic ATtiny828 yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
