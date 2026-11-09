---
title: "FYSETC F6 V1.3"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "FYSETC F6 V1.3 (ATMEGA2560, 16MHz, 252KB flash, 8KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# FYSETC F6 V1.3

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | ATMEGA2560 |
| **Frequency** | 16MHz |
| **Flash** | 252KB |
| **RAM** | 8KB |
| **Vendor** | [FYSETC](https://www.fysetc.com/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `fysetc_f6_13` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:fysetc_f6_13]
platform = atmelavr
board = fysetc_f6_13
```

To override a setting of the board manifest [fysetc_f6_13.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/fysetc_f6_13.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:fysetc_f6_13]
platform = atmelavr
board = fysetc_f6_13

; change microcontroller
board_build.mcu = atmega2560

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

The FYSETC F6 V1.3 has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [avr-stub](../../debug-probes/avr-stub.md) |  | Yes |
| [simavr](../../debug-probes/simavr.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
