---
title: "Digilent chipKIT WF32"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Digilent chipKIT WF32 (32MX695F512L, 80MHz, 508KB flash, 128KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Digilent chipKIT WF32

## Hardware

Platform [Microchip PIC32](../../platforms/microchippic32.md): Microchip's 32-bit portfolio with the MIPS microAptiv or M4K core offer high performance microcontrollers, and all the tools needed to develop your embedded projects. PIC32 MCUs gives your application the processing power, memory and peripherals your design needs!

| Specification | Value |
|---|---|
| **Microcontroller** | 32MX695F512L |
| **Frequency** | 80MHz |
| **Flash** | 508KB |
| **RAM** | 128KB |
| **Vendor** | [Digilent](http://store.digilentinc.com/chipkit-wf32-wifi-enabled-microntroller-board-with-uno-r3-headers/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `chipkit_wf32` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:chipkit_wf32]
platform = microchippic32
board = chipkit_wf32
```

To override a setting of the board manifest [chipkit_wf32.json](https://github.com/platformio/platform-microchippic32/blob/master/boards/chipkit_wf32.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:chipkit_wf32]
platform = microchippic32
board = chipkit_wf32

; change microcontroller
board_build.mcu = 32MX695F512L

; change MCU frequency
board_build.f_cpu = 80000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the Digilent chipKIT WF32 yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
