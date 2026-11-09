---
title: "Pontech NoFire"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Pontech NoFire (32MZ2048EFG100, 200MHz, 1.98MB flash, 512KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Pontech NoFire

## Hardware

Platform [Microchip PIC32](../../platforms/microchippic32.md): Microchip's 32-bit portfolio with the MIPS microAptiv or M4K core offer high performance microcontrollers, and all the tools needed to develop your embedded projects. PIC32 MCUs gives your application the processing power, memory and peripherals your design needs!

| Specification | Value |
|---|---|
| **Microcontroller** | 32MZ2048EFG100 |
| **Frequency** | 200MHz |
| **Flash** | 1.98MB |
| **RAM** | 512KB |
| **Vendor** | [Pontech](http://www.pontech.com/products?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `nofire` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:nofire]
platform = microchippic32
board = nofire
```

To override a setting of the board manifest [nofire.json](https://github.com/platformio/platform-microchippic32/blob/master/boards/nofire.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:nofire]
platform = microchippic32
board = nofire

; change microcontroller
board_build.mcu = 32MZ2048EFG100

; change MCU frequency
board_build.f_cpu = 200000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the Pontech NoFire yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
