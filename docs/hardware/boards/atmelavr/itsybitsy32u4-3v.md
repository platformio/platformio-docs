---
title: "Adafruit ItsyBitsy 3V/8MHz"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-atmelavr-itsybitsy32u4-3v"></a>

# Adafruit ItsyBitsy 3V/8MHz

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | ATMEGA32U4 |
| **Frequency** | 8MHz |
| **Flash** | 28KB |
| **RAM** | 2.50KB |
| **Vendor** | [Adafruit](https://www.adafruit.com/product/3675?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `itsybitsy32u4_3V` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:itsybitsy32u4_3V]
platform = atmelavr
board = itsybitsy32u4_3V
```

You can override default Adafruit ItsyBitsy 3V/8MHz settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [itsybitsy32u4_3V.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/itsybitsy32u4_3V.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:itsybitsy32u4_3V]
platform = atmelavr
board = itsybitsy32u4_3V

; change microcontroller
board_build.mcu = atmega32u4

; change MCU frequency
board_build.f_cpu = 8000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

Adafruit ItsyBitsy 3V/8MHz does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

| Compatible Tools | On-board | Default |
|---|---|---|
| [simavr](../../debug-probes/simavr.md) |  | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
