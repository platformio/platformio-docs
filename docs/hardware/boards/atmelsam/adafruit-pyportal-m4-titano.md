---
title: "Adafruit PyPortal M4 Titano"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Adafruit PyPortal M4 Titano (SAMD51J20A, 120MHz, 1MB flash, 256KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Adafruit PyPortal M4 Titano

## Hardware

Platform [Atmel SAM](../../platforms/atmelsam.md): Atmel | SMART offers Flash- based ARM products based on the ARM Cortex-M0+, Cortex-M3 and Cortex-M4 architectures, ranging from 8KB to 2MB of Flash including a rich peripheral and feature mix.

| Specification | Value |
|---|---|
| **Microcontroller** | SAMD51J20A |
| **Frequency** | 120MHz |
| **Flash** | 1MB |
| **RAM** | 256KB |
| **Vendor** | [Adafruit](https://www.adafruit.com/product/4444?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `adafruit_pyportal_m4_titano` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:adafruit_pyportal_m4_titano]
platform = atmelsam
board = adafruit_pyportal_m4_titano
```

To override a setting of the board manifest [adafruit_pyportal_m4_titano.json](https://github.com/platformio/platform-atmelsam/blob/master/boards/adafruit_pyportal_m4_titano.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:adafruit_pyportal_m4_titano]
platform = atmelsam
board = adafruit_pyportal_m4_titano

; change microcontroller
board_build.mcu = samd51j20a

; change MCU frequency
board_build.f_cpu = 120000000L
```

## Uploading

Adafruit PyPortal M4 Titano supports these upload protocols:

- `atmel-ice`
- `jlink`
- `sam-ba`

The default is `sam-ba`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:adafruit_pyportal_m4_titano]
platform = atmelsam
board = adafruit_pyportal_m4_titano

upload_protocol = sam-ba
```

## Debugging

The Adafruit PyPortal M4 Titano has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

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
