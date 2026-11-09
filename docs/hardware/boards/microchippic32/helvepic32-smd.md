---
title: "HelvePic32"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "HelvePic32 (32MX250F128D, 48MHz, 120KB flash, 32KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# HelvePic32

## Hardware

Platform [Microchip PIC32](../../platforms/microchippic32.md): Microchip's 32-bit portfolio with the MIPS microAptiv or M4K core offer high performance microcontrollers, and all the tools needed to develop your embedded projects. PIC32 MCUs gives your application the processing power, memory and peripherals your design needs!

| Specification | Value |
|---|---|
| **Microcontroller** | 32MX250F128D |
| **Frequency** | 48MHz |
| **Flash** | 120KB |
| **RAM** | 32KB |
| **Vendor** | [BOXTEC](https://www.helvepic32.org/shop-1/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `helvepic32_smd` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:helvepic32_smd]
platform = microchippic32
board = helvepic32_smd
```

To override a setting of the board manifest [helvepic32_smd.json](https://github.com/platformio/platform-microchippic32/blob/master/boards/helvepic32_smd.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:helvepic32_smd]
platform = microchippic32
board = helvepic32_smd

; change microcontroller
board_build.mcu = 32MX250F128D

; change MCU frequency
board_build.f_cpu = 48000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the HelvePic32 yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
