---
title: "SparkFun Fio V3 3.3V/8MHz"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "SparkFun Fio V3 3.3V/8MHz (ATMEGA32U4, 8MHz, 28KB flash, 2.50KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-atmelavr-sparkfun-fiov3"></a>

# SparkFun Fio V3 3.3V/8MHz

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | ATMEGA32U4 |
| **Frequency** | 8MHz |
| **Flash** | 28KB |
| **RAM** | 2.50KB |
| **Vendor** | [SparkFun](https://www.sparkfun.com/products/11520?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `sparkfun_fiov3` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:sparkfun_fiov3]
platform = atmelavr
board = sparkfun_fiov3
```

To override a setting of the board manifest [sparkfun_fiov3.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/sparkfun_fiov3.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:sparkfun_fiov3]
platform = atmelavr
board = sparkfun_fiov3

; change microcontroller
board_build.mcu = atmega32u4

; change MCU frequency
board_build.f_cpu = 8000000L
```

## Debugging

The SparkFun Fio V3 3.3V/8MHz has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

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
