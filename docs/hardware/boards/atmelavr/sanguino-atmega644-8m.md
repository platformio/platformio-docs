---
title: "Sanguino ATmega644 or ATmega644A (8 MHz)"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Sanguino ATmega644 or ATmega644A (8 MHz) (ATMEGA644, 8MHz, 63KB flash, 4KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-atmelavr-sanguino-atmega644-8m"></a>

# Sanguino ATmega644 or ATmega644A (8 MHz)

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | ATMEGA644 |
| **Frequency** | 8MHz |
| **Flash** | 63KB |
| **RAM** | 4KB |
| **Vendor** | [Sanguino](https://github.com/Lauszus/Sanguino?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `sanguino_atmega644_8m` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:sanguino_atmega644_8m]
platform = atmelavr
board = sanguino_atmega644_8m
```

To override a setting of the board manifest [sanguino_atmega644_8m.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/sanguino_atmega644_8m.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:sanguino_atmega644_8m]
platform = atmelavr
board = sanguino_atmega644_8m

; change microcontroller
board_build.mcu = atmega644

; change MCU frequency
board_build.f_cpu = 8000000L
```

## Debugging

The Sanguino ATmega644 or ATmega644A (8 MHz) has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [simavr](../../debug-probes/simavr.md) |  | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
