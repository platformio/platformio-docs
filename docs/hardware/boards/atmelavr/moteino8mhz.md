---
title: "LowPowerLab Moteino (8Mhz)"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-atmelavr-moteino8mhz"></a>

# LowPowerLab Moteino (8Mhz)

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | ATMEGA328P |
| **Frequency** | 8MHz |
| **Flash** | 31.50KB |
| **RAM** | 2KB |
| **Vendor** | [LowPowerLab](https://lowpowerlab.com/shop/product/159?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `moteino8mhz` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:moteino8mhz]
platform = atmelavr
board = moteino8mhz
```

You can override default LowPowerLab Moteino (8Mhz) settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [moteino8mhz.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/moteino8mhz.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:moteino8mhz]
platform = atmelavr
board = moteino8mhz

; change microcontroller
board_build.mcu = atmega328p

; change MCU frequency
board_build.f_cpu = 8000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

LowPowerLab Moteino (8Mhz) does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

| Compatible Tools | On-board | Default |
|---|---|---|
| [avr-stub](../../debug-probes/avr-stub.md) |  | Yes |
| [simavr](../../debug-probes/simavr.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
