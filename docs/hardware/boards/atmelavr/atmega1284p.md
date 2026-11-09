---
title: "ATmega1284P"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "ATmega1284P (ATMEGA1284P, 16MHz, 128KB flash, 16KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# ATmega1284P

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | ATMEGA1284P |
| **Frequency** | 16MHz |
| **Flash** | 128KB |
| **RAM** | 16KB |
| **Vendor** | [Microchip](https://www.microchip.com/wwwproducts/en/ATmega1284p?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `ATmega1284P` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:ATmega1284P]
platform = atmelavr
board = ATmega1284P
```

To override a setting of the board manifest [ATmega1284P.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/ATmega1284P.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:ATmega1284P]
platform = atmelavr
board = ATmega1284P

; change microcontroller
board_build.mcu = atmega1284p

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

The ATmega1284P has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

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
