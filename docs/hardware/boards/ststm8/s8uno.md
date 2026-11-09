---
title: "sduino UNO (STM8S105K6)"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "sduino UNO (STM8S105K6) (STM8S105K6T6, 16MHz, 32KB flash, 2KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-ststm8-s8uno"></a>

# sduino UNO (STM8S105K6)

## Hardware

Platform [ST STM8](../../platforms/ststm8.md): The STM8 is an 8-bit microcontroller family by STMicroelectronics an extended variant of the ST7 microcontroller architecture. STM8 microcontrollers are particularly low cost for a full-featured 8-bit microcontroller.

| Specification | Value |
|---|---|
| **Microcontroller** | STM8S105K6T6 |
| **Frequency** | 16MHz |
| **Flash** | 32KB |
| **RAM** | 2KB |
| **Vendor** | [sduino](https://github.com/roybaer/sduino_uno?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `s8uno` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:s8uno]
platform = ststm8
board = s8uno
```

To override a setting of the board manifest [s8uno.json](https://github.com/platformio/platform-ststm8/blob/master/boards/s8uno.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:s8uno]
platform = ststm8
board = s8uno

; change microcontroller
board_build.mcu = stm8s105k6t6

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Uploading

sduino UNO (STM8S105K6) supports these upload protocols:

- `serial`
- `stlinkv2`

The default is `serial`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:s8uno]
platform = ststm8
board = s8uno

upload_protocol = serial
```

## Debugging

The sduino UNO (STM8S105K6) has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [ST-LINK](../../debug-probes/stlink.md) |  | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [Standard Peripheral Library](../../frameworks/spl.mdx) | Standard Peripheral Library for ST STM32 microcontrollers |
