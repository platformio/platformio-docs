---
title: "ATtiny13A"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "ATtiny13A (ATTINY13A, 9MHz, 1KB flash, 64B RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# ATtiny13A

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | ATTINY13A |
| **Frequency** | 9MHz |
| **Flash** | 1KB |
| **RAM** | 64B |
| **Vendor** | [Microchip](https://www.microchip.com/wwwproducts/en/ATtiny13A?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `attiny13a` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:attiny13a]
platform = atmelavr
board = attiny13a
```

To override a setting of the board manifest [attiny13a.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/attiny13a.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:attiny13a]
platform = atmelavr
board = attiny13a

; change microcontroller
board_build.mcu = attiny13a

; change MCU frequency
board_build.f_cpu = 9600000L
```

## Debugging

The ATtiny13A has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

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
