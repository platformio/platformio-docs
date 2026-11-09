---
title: "Makerdiary nRF52840-MDK"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Makerdiary nRF52840-MDK (NRF52840, 64MHz, 1MB flash, 256KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-nordicnrf52-nrf52840-mdk"></a>

# Makerdiary nRF52840-MDK

## Hardware

Platform [Nordic nRF52](../../platforms/nordicnrf52.mdx): The nRF52 Series are built for speed to carry out increasingly complex tasks in the shortest possible time and return to sleep, conserving precious battery power. They have a Cortex-M4F processor which makes them quite capable Bluetooth Smart SoCs.

| Specification | Value |
|---|---|
| **Microcontroller** | NRF52840 |
| **Frequency** | 64MHz |
| **Flash** | 1MB |
| **RAM** | 256KB |
| **Vendor** | [Makerdiary](https://wiki.makerdiary.com/nrf52840-mdk?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `nrf52840_mdk` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:nrf52840_mdk]
platform = nordicnrf52
board = nrf52840_mdk
```

To override a setting of the board manifest [nrf52840_mdk.json](https://github.com/platformio/platform-nordicnrf52/blob/master/boards/nrf52840_mdk.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:nrf52840_mdk]
platform = nordicnrf52
board = nrf52840_mdk

; change microcontroller
board_build.mcu = nrf52840

; change MCU frequency
board_build.f_cpu = 64000000L
```

## Uploading

Makerdiary nRF52840-MDK supports these upload protocols:

- `blackmagic`
- `cmsis-dap`
- `jlink`
- `mbed`
- `nrfjprog`
- `stlink`

The default is `cmsis-dap`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:nrf52840_mdk]
platform = nordicnrf52
board = nrf52840_mdk

upload_protocol = cmsis-dap
```

## Debugging

The Makerdiary nRF52840-MDK has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [Black magic probe](../../debug-probes/blackmagic.md) |  |  |
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) | Yes | Yes |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [ST-LINK](../../debug-probes/stlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
