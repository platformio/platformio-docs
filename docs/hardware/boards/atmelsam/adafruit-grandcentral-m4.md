---
title: "Adafruit Grand Central M4"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Adafruit Grand Central M4 (SAMD51P20A, 120MHz, 1MB flash, 256KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-atmelsam-adafruit-grandcentral-m4"></a>

# Adafruit Grand Central M4

## Hardware

Platform [Atmel SAM](../../platforms/atmelsam.md): Atmel | SMART offers Flash- based ARM products based on the ARM Cortex-M0+, Cortex-M3 and Cortex-M4 architectures, ranging from 8KB to 2MB of Flash including a rich peripheral and feature mix.

| Specification | Value |
|---|---|
| **Microcontroller** | SAMD51P20A |
| **Frequency** | 120MHz |
| **Flash** | 1MB |
| **RAM** | 256KB |
| **Vendor** | [Adafruit](https://www.adafruit.com/product/4064?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `adafruit_grandcentral_m4` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:adafruit_grandcentral_m4]
platform = atmelsam
board = adafruit_grandcentral_m4
```

To override a setting of the board manifest [adafruit_grandcentral_m4.json](https://github.com/platformio/platform-atmelsam/blob/master/boards/adafruit_grandcentral_m4.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:adafruit_grandcentral_m4]
platform = atmelsam
board = adafruit_grandcentral_m4

; change microcontroller
board_build.mcu = samd51p20a

; change MCU frequency
board_build.f_cpu = 120000000L
```

## Uploading

Adafruit Grand Central M4 supports these upload protocols:

- `atmel-ice`
- `jlink`
- `sam-ba`

The default is `sam-ba`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:adafruit_grandcentral_m4]
platform = atmelsam
board = adafruit_grandcentral_m4

upload_protocol = sam-ba
```

## Debugging

The Adafruit Grand Central M4 has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [Atmel-ICE](../../debug-probes/atmel-ice.md) |  | Yes |
| [J-LINK](../../debug-probes/jlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
