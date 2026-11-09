---
title: "Generic ATtiny2313"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Generic ATtiny2313 (ATTINY2313, 8MHz, 2KB flash, 128B RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Generic ATtiny2313

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | ATTINY2313 |
| **Frequency** | 8MHz |
| **Flash** | 2KB |
| **RAM** | 128B |
| **Vendor** | [Atmel](http://www.microchip.com/wwwproducts/en/ATTINY2313?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `attiny2313` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:attiny2313]
platform = atmelavr
board = attiny2313
```

To override a setting of the board manifest [attiny2313.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/attiny2313.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:attiny2313]
platform = atmelavr
board = attiny2313

; change microcontroller
board_build.mcu = attiny2313

; change MCU frequency
board_build.f_cpu = 8000000L
```

## Debugging

The Generic ATtiny2313 has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

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
