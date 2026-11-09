---
title: "Pic32 CUI32-Development Stick"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Pic32 CUI32-Development Stick (32MX440F512H, 80MHz, 508KB flash, 32KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Pic32 CUI32-Development Stick

## Hardware

Platform [Microchip PIC32](../../platforms/microchippic32.md): Microchip's 32-bit portfolio with the MIPS microAptiv or M4K core offer high performance microcontrollers, and all the tools needed to develop your embedded projects. PIC32 MCUs gives your application the processing power, memory and peripherals your design needs!

| Specification | Value |
|---|---|
| **Microcontroller** | 32MX440F512H |
| **Frequency** | 80MHz |
| **Flash** | 508KB |
| **RAM** | 32KB |
| **Vendor** | [SparkFun](https://www.sparkfun.com/products/retired/9645?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `cui32` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:cui32]
platform = microchippic32
board = cui32
```

To override a setting of the board manifest [cui32.json](https://github.com/platformio/platform-microchippic32/blob/master/boards/cui32.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:cui32]
platform = microchippic32
board = cui32

; change microcontroller
board_build.mcu = 32MX440F512H

; change MCU frequency
board_build.f_cpu = 80000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the Pic32 CUI32-Development Stick yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
