---
title: "Element14 chipKIT Pi"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
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

Please use `chipkit_pi` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:chipkit_pi]
platform = microchippic32
board = chipkit_pi
```

You can override default Element14 chipKIT Pi settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [chipkit_pi.json](https://github.com/platformio/platform-microchippic32/blob/master/boards/chipkit_pi.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

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

[Debugging](../../../guides/debugging/index.md) currently does not support Element14 chipKIT Pi board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
