---
title: "Laird Connectivity Pinnacle 100 DVK"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Laird Connectivity Pinnacle 100 DVK (NRF52840, 64MHz, 1MB flash, 256KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-nordicnrf52-laird-pinnacle-100-dvk"></a>

# Laird Connectivity Pinnacle 100 DVK

## Hardware

Platform [Nordic nRF52](../../platforms/nordicnrf52.mdx): The nRF52 Series are built for speed to carry out increasingly complex tasks in the shortest possible time and return to sleep, conserving precious battery power. They have a Cortex-M4F processor which makes them quite capable Bluetooth Smart SoCs.

| Specification | Value |
|---|---|
| **Microcontroller** | NRF52840 |
| **Frequency** | 64MHz |
| **Flash** | 1MB |
| **RAM** | 256KB |
| **Vendor** | [Laird Connectivity](https://www.lairdconnect.com/wireless-modules/cellular-solutions/pinnacle-100-cellular-modem?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `laird_pinnacle_100_dvk` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:laird_pinnacle_100_dvk]
platform = nordicnrf52
board = laird_pinnacle_100_dvk
```

To override a setting of the board manifest [laird_pinnacle_100_dvk.json](https://github.com/platformio/platform-nordicnrf52/blob/master/boards/laird_pinnacle_100_dvk.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:laird_pinnacle_100_dvk]
platform = nordicnrf52
board = laird_pinnacle_100_dvk

; change microcontroller
board_build.mcu = nrf52840

; change MCU frequency
board_build.f_cpu = 64000000L
```

## Uploading

Laird Connectivity Pinnacle 100 DVK supports these upload protocols:

- `blackmagic`
- `cmsis-dap`
- `jlink`
- `mbed`
- `nrfjprog`
- `stlink`

The default is `jlink`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:laird_pinnacle_100_dvk]
platform = nordicnrf52
board = laird_pinnacle_100_dvk

upload_protocol = jlink
```

## Debugging

The Laird Connectivity Pinnacle 100 DVK has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

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
