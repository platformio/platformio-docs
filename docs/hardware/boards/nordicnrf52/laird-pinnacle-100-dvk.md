---
title: "Laird Connectivity Pinnacle 100 DVK"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
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

Please use `laird_pinnacle_100_dvk` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:laird_pinnacle_100_dvk]
platform = nordicnrf52
board = laird_pinnacle_100_dvk
```

You can override default Laird Connectivity Pinnacle 100 DVK settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [laird_pinnacle_100_dvk.json](https://github.com/platformio/platform-nordicnrf52/blob/master/boards/laird_pinnacle_100_dvk.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

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

Laird Connectivity Pinnacle 100 DVK supports the following uploading protocols:

- `blackmagic`
- `cmsis-dap`
- `jlink`
- `mbed`
- `nrfjprog`
- `stlink`

Default protocol is `jlink`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:laird_pinnacle_100_dvk]
platform = nordicnrf52
board = laird_pinnacle_100_dvk

upload_protocol = jlink
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

Laird Connectivity Pinnacle 100 DVK does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

| Compatible Tools | On-board | Default |
|---|---|---|
| [Black Magic Probe](../../debug-probes/blackmagic.md) |  | Yes |
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) |  |  |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [ST-LINK](../../debug-probes/stlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
