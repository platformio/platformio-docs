---
title: "Pinoccio Scout"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-atmelavr-pinoccio"></a>

# Pinoccio Scout

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | ATMEGA256RFR2 |
| **Frequency** | 16MHz |
| **Flash** | 248KB |
| **RAM** | 32KB |
| **Vendor** | [Pinoccio](https://www.crowdsupply.com/pinoccio/mesh-sensor-network?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `pinoccio` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:pinoccio]
platform = atmelavr
board = pinoccio
```

You can override default Pinoccio Scout settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [pinoccio.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/pinoccio.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:pinoccio]
platform = atmelavr
board = pinoccio

; change microcontroller
board_build.mcu = atmega256rfr2

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support Pinoccio Scout board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
