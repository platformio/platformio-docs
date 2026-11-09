---
title: "ATmega324A"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "ATmega324A (ATMEGA324A, 16MHz, 32KB flash, 2KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# ATmega324A

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | ATMEGA324A |
| **Frequency** | 16MHz |
| **Flash** | 32KB |
| **RAM** | 2KB |
| **Vendor** | [Microchip](https://www.microchip.com/wwwproducts/en/ATmega324a?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `ATmega324A` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:ATmega324A]
platform = atmelavr
board = ATmega324A
```

To override a setting of the board manifest [ATmega324A.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/ATmega324A.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:ATmega324A]
platform = atmelavr
board = ATmega324A

; change microcontroller
board_build.mcu = atmega324a

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

The ATmega324A has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

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
