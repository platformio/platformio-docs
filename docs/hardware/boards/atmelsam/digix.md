---
title: "Digistump DigiX"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Digistump DigiX (AT91SAM3X8E, 84MHz, 512KB flash, 96KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-atmelsam-digix"></a>

# Digistump DigiX

## Hardware

Platform [Atmel SAM](../../platforms/atmelsam.md): Atmel | SMART offers Flash- based ARM products based on the ARM Cortex-M0+, Cortex-M3 and Cortex-M4 architectures, ranging from 8KB to 2MB of Flash including a rich peripheral and feature mix.

| Specification | Value |
|---|---|
| **Microcontroller** | AT91SAM3X8E |
| **Frequency** | 84MHz |
| **Flash** | 512KB |
| **RAM** | 96KB |
| **Vendor** | [Digistump](http://digistump.com/products/50?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `digix` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:digix]
platform = atmelsam
board = digix
```

To override a setting of the board manifest [digix.json](https://github.com/platformio/platform-atmelsam/blob/master/boards/digix.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:digix]
platform = atmelsam
board = digix

; change microcontroller
board_build.mcu = at91sam3x8e

; change MCU frequency
board_build.f_cpu = 84000000L
```

## Uploading

Digistump DigiX supports these upload protocols:

- `atmel-ice`
- `blackmagic`
- `jlink`
- `sam-ba`
- `stlink`

The default is `sam-ba`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:digix]
platform = atmelsam
board = digix

upload_protocol = sam-ba
```

## Debugging

The Digistump DigiX has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [Atmel-ICE](../../debug-probes/atmel-ice.md) |  | Yes |
| [Black magic probe](../../debug-probes/blackmagic.md) |  |  |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [ST-LINK](../../debug-probes/stlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
