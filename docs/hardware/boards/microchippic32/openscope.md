---
title: "Digilent OpenScope"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Digilent OpenScope (32MZ2048EFG124, 200MHz, 1.98MB flash, 512KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-microchippic32-openscope"></a>

# Digilent OpenScope

## Hardware

Platform [Microchip PIC32](../../platforms/microchippic32.md): Microchip's 32-bit portfolio with the MIPS microAptiv or M4K core offer high performance microcontrollers, and all the tools needed to develop your embedded projects. PIC32 MCUs gives your application the processing power, memory and peripherals your design needs!

| Specification | Value |
|---|---|
| **Microcontroller** | 32MZ2048EFG124 |
| **Frequency** | 200MHz |
| **Flash** | 1.98MB |
| **RAM** | 512KB |
| **Vendor** | [Digilent](http://store.digilentinc.com/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `openscope` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:openscope]
platform = microchippic32
board = openscope
```

To override a setting of the board manifest [openscope.json](https://github.com/platformio/platform-microchippic32/blob/master/boards/openscope.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:openscope]
platform = microchippic32
board = openscope

; change microcontroller
board_build.mcu = 32MZ2048EFG124

; change MCU frequency
board_build.f_cpu = 200000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the Digilent OpenScope yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
