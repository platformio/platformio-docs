---
title: "Generic ATtiny4313"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-atmelavr-attiny4313"></a>

# Generic ATtiny4313

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | ATTINY4313 |
| **Frequency** | 8MHz |
| **Flash** | 4KB |
| **RAM** | 256B |
| **Vendor** | [Atmel](http://www.microchip.com/wwwproducts/en/ATTINY4313?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `attiny4313` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:attiny4313]
platform = atmelavr
board = attiny4313
```

You can override default Generic ATtiny4313 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [attiny4313.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/attiny4313.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:attiny4313]
platform = atmelavr
board = attiny4313

; change microcontroller
board_build.mcu = attiny4313

; change MCU frequency
board_build.f_cpu = 8000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

Generic ATtiny4313 does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

| Compatible Tools | On-board | Default |
|---|---|---|
| [simavr](../../debug-probes/simavr.md) |  | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
