---
title: "Generic ATtiny84"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Generic ATtiny84 (ATTINY84, 8MHz, 8KB flash, 512B RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-atmelavr-attiny84"></a>

# Generic ATtiny84

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | ATTINY84 |
| **Frequency** | 8MHz |
| **Flash** | 8KB |
| **RAM** | 512B |
| **Vendor** | [Atmel](http://www.atmel.com/devices/ATTINY84.aspx?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `attiny84` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:attiny84]
platform = atmelavr
board = attiny84
```

To override a setting of the board manifest [attiny84.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/attiny84.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:attiny84]
platform = atmelavr
board = attiny84

; change microcontroller
board_build.mcu = attiny84

; change MCU frequency
board_build.f_cpu = 8000000L
```

## Debugging

The Generic ATtiny84 has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

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
