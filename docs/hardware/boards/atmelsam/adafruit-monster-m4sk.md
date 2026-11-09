---
title: "Adafruit MONSTER M4SK"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Adafruit MONSTER M4SK (SAMD51G19A, 120MHz, 496KB flash, 192KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Adafruit MONSTER M4SK

## Hardware

Platform [Atmel SAM](../../platforms/atmelsam.md): Atmel | SMART offers Flash- based ARM products based on the ARM Cortex-M0+, Cortex-M3 and Cortex-M4 architectures, ranging from 8KB to 2MB of Flash including a rich peripheral and feature mix.

| Specification | Value |
|---|---|
| **Microcontroller** | SAMD51G19A |
| **Frequency** | 120MHz |
| **Flash** | 496KB |
| **RAM** | 192KB |
| **Vendor** | [Adafruit](https://www.adafruit.com/product/4343?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `adafruit_monster_m4sk` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:adafruit_monster_m4sk]
platform = atmelsam
board = adafruit_monster_m4sk
```

To override a setting of the board manifest [adafruit_monster_m4sk.json](https://github.com/platformio/platform-atmelsam/blob/master/boards/adafruit_monster_m4sk.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:adafruit_monster_m4sk]
platform = atmelsam
board = adafruit_monster_m4sk

; change microcontroller
board_build.mcu = samd51g19a

; change MCU frequency
board_build.f_cpu = 120000000L
```

## Uploading

Adafruit MONSTER M4SK supports these upload protocols:

- `atmel-ice`
- `jlink`
- `sam-ba`

The default is `sam-ba`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:adafruit_monster_m4sk]
platform = atmelsam
board = adafruit_monster_m4sk

upload_protocol = sam-ba
```

## Debugging

The Adafruit MONSTER M4SK has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

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
