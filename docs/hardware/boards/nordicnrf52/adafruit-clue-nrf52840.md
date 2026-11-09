---
title: "Adafruit CLUE nRF52840"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Adafruit CLUE nRF52840 (NRF52840, 64MHz, 796KB flash, 243KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Adafruit CLUE nRF52840

## Hardware

Platform [Nordic nRF52](../../platforms/nordicnrf52.mdx): The nRF52 Series are built for speed to carry out increasingly complex tasks in the shortest possible time and return to sleep, conserving precious battery power. They have a Cortex-M4F processor which makes them quite capable Bluetooth Smart SoCs.

| Specification | Value |
|---|---|
| **Microcontroller** | NRF52840 |
| **Frequency** | 64MHz |
| **Flash** | 796KB |
| **RAM** | 243KB |
| **Vendor** | [Adafruit](https://www.adafruit.com/product/4500?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `adafruit_clue_nrf52840` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:adafruit_clue_nrf52840]
platform = nordicnrf52
board = adafruit_clue_nrf52840
```

To override a setting of the board manifest [adafruit_clue_nrf52840.json](https://github.com/platformio/platform-nordicnrf52/blob/master/boards/adafruit_clue_nrf52840.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:adafruit_clue_nrf52840]
platform = nordicnrf52
board = adafruit_clue_nrf52840

; change microcontroller
board_build.mcu = nrf52840

; change MCU frequency
board_build.f_cpu = 64000000L
```

## Uploading

Adafruit CLUE nRF52840 supports these upload protocols:

- `blackmagic`
- `cmsis-dap`
- `jlink`
- `nrfjprog`
- `nrfutil`
- `stlink`

The default is `nrfutil`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:adafruit_clue_nrf52840]
platform = nordicnrf52
board = adafruit_clue_nrf52840

upload_protocol = nrfutil
```

## Debugging

The Adafruit CLUE nRF52840 has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [Black magic probe](../../debug-probes/blackmagic.md) |  | Yes |
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) |  |  |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [ST-LINK](../../debug-probes/stlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
