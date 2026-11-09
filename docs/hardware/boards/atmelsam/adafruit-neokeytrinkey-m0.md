---
title: "Adafruit NeoKey Trinkey"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Adafruit NeoKey Trinkey (SAMD21E18A, 48MHz, 256KB flash, 32KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-atmelsam-adafruit-neokeytrinkey-m0"></a>

# Adafruit NeoKey Trinkey

## Hardware

Platform [Atmel SAM](../../platforms/atmelsam.md): Atmel | SMART offers Flash- based ARM products based on the ARM Cortex-M0+, Cortex-M3 and Cortex-M4 architectures, ranging from 8KB to 2MB of Flash including a rich peripheral and feature mix.

| Specification | Value |
|---|---|
| **Microcontroller** | SAMD21E18A |
| **Frequency** | 48MHz |
| **Flash** | 256KB |
| **RAM** | 32KB |
| **Vendor** | [Adafruit](https://www.adafruit.com/product/5020?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `adafruit_neokeytrinkey_m0` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:adafruit_neokeytrinkey_m0]
platform = atmelsam
board = adafruit_neokeytrinkey_m0
```

To override a setting of the board manifest [adafruit_neokeytrinkey_m0.json](https://github.com/platformio/platform-atmelsam/blob/master/boards/adafruit_neokeytrinkey_m0.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:adafruit_neokeytrinkey_m0]
platform = atmelsam
board = adafruit_neokeytrinkey_m0

; change microcontroller
board_build.mcu = samd21e18a

; change MCU frequency
board_build.f_cpu = 48000000L
```

## Uploading

Adafruit NeoKey Trinkey supports these upload protocols:

- `atmel-ice`
- `blackmagic`
- `jlink`
- `sam-ba`

The default is `sam-ba`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:adafruit_neokeytrinkey_m0]
platform = atmelsam
board = adafruit_neokeytrinkey_m0

upload_protocol = sam-ba
```

## Debugging

The Adafruit NeoKey Trinkey has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [Atmel-ICE](../../debug-probes/atmel-ice.md) |  | Yes |
| [Black magic probe](../../debug-probes/blackmagic.md) |  |  |
| [J-LINK](../../debug-probes/jlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
