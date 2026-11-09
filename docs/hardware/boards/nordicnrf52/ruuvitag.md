---
title: "Ruuvi Tag"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Ruuvi Tag (NRF52832, 64MHz, 512KB flash, 64KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Ruuvi Tag

## Hardware

Platform [Nordic nRF52](../../platforms/nordicnrf52.mdx): The nRF52 Series are built for speed to carry out increasingly complex tasks in the shortest possible time and return to sleep, conserving precious battery power. They have a Cortex-M4F processor which makes them quite capable Bluetooth Smart SoCs.

| Specification | Value |
|---|---|
| **Microcontroller** | NRF52832 |
| **Frequency** | 64MHz |
| **Flash** | 512KB |
| **RAM** | 64KB |
| **Vendor** | [Ruuvi](https://ruuvi.com/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `ruuvitag` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:ruuvitag]
platform = nordicnrf52
board = ruuvitag
```

To override a setting of the board manifest [ruuvitag.json](https://github.com/platformio/platform-nordicnrf52/blob/master/boards/ruuvitag.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:ruuvitag]
platform = nordicnrf52
board = ruuvitag

; change microcontroller
board_build.mcu = nrf52832

; change MCU frequency
board_build.f_cpu = 64000000L
```

## Uploading

Ruuvi Tag supports these upload protocols:

- `blackmagic`
- `cmsis-dap`
- `jlink`
- `mbed`
- `nrfjprog`
- `stlink`

The default is `jlink`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:ruuvitag]
platform = nordicnrf52
board = ruuvitag

upload_protocol = jlink
```

## Debugging

The Ruuvi Tag has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

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
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
