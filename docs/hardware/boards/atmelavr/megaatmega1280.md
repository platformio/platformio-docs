---
title: "Arduino Mega or Mega 2560 ATmega1280"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Arduino Mega or Mega 2560 ATmega1280 (ATMEGA1280, 16MHz, 124KB flash, 8KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Arduino Mega or Mega 2560 ATmega1280

## Hardware

Platform [Atmel AVR](../../platforms/atmelavr.mdx): Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

| Specification | Value |
|---|---|
| **Microcontroller** | ATMEGA1280 |
| **Frequency** | 16MHz |
| **Flash** | 124KB |
| **RAM** | 8KB |
| **Vendor** | [Arduino](https://www.arduino.cc/en/Main/ArduinoBoardMega2560?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `megaatmega1280` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:megaatmega1280]
platform = atmelavr
board = megaatmega1280
```

To override a setting of the board manifest [megaatmega1280.json](https://github.com/platformio/platform-atmelavr/blob/master/boards/megaatmega1280.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:megaatmega1280]
platform = atmelavr
board = megaatmega1280

; change microcontroller
board_build.mcu = atmega1280

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

The Arduino Mega or Mega 2560 ATmega1280 has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

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
