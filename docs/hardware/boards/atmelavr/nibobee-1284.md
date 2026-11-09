---
title: "nicai-systems NIBObee robot with Tuning Kit"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-atmelavr-nibobee-1284"></a>

# nicai-systems NIBObee robot with Tuning Kit

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | ATMEGA1284P |
| **Frequency** | 20MHz |
| **Flash** | 128KB |
| **RAM** | 16KB |
| **Vendor** | [nicai-systems](http://www.nicai-systems.com/en/nibobee?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `nibobee_1284` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:nibobee_1284]
platform = atmelavr
board = nibobee_1284
```

You can override default nicai-systems NIBObee robot with Tuning Kit settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [nibobee_1284.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/nibobee_1284.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:nibobee_1284]
platform = atmelavr
board = nibobee_1284

; change microcontroller
board_build.mcu = atmega1284p

; change MCU frequency
board_build.f_cpu = 20000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

nicai-systems NIBObee robot with Tuning Kit does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

| Compatible Tools | On-board | Default |
|---|---|---|
| [simavr](../../debug-probes/simavr.md) |  | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
