---
title: "Element14 chipKIT Pi"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Element14 chipKIT Pi (32MX250F128B, 40MHz, 120KB flash, 32KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-microchippic32-chipkit-pi"></a>

# Element14 chipKIT Pi

## Hardware

Platform [Microchip PIC32](../../platforms/microchippic32.md): Microchip's 32-bit portfolio with the MIPS microAptiv or M4K core offer high performance microcontrollers, and all the tools needed to develop your embedded projects. PIC32 MCUs gives your application the processing power, memory and peripherals your design needs!

| Specification | Value |
|---|---|
| **Microcontroller** | 32MX250F128B |
| **Frequency** | 40MHz |
| **Flash** | 120KB |
| **RAM** | 32KB |
| **Vendor** | [element14](http://www.element14.com/community/community/knode/dev_platforms_kits/element14_dev_kits/microchip-chipkit/chipkit_pi?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `chipkit_pi` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:chipkit_pi]
platform = microchippic32
board = chipkit_pi
```

To override a setting of the board manifest [chipkit_pi.json](https://github.com/platformio/platform-microchippic32/blob/master/boards/chipkit_pi.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:chipkit_pi]
platform = microchippic32
board = chipkit_pi

; change microcontroller
board_build.mcu = 32MX250F128B

; change MCU frequency
board_build.f_cpu = 40000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the Element14 chipKIT Pi yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
