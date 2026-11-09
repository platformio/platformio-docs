---
title: "Freescale Kinetis FRDM-K82F"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Freescale Kinetis FRDM-K82F (MK82FN256VLL15, 150MHz, 256KB flash, 256KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Freescale Kinetis FRDM-K82F

## Hardware

Platform [Freescale Kinetis](../../platforms/freescalekinetis.md): Freescale Kinetis Microcontrollers is family of multiple hardware- and software-compatible ARM Cortex-M0+, Cortex-M4 and Cortex-M7-based MCU series. Kinetis MCUs offer exceptional low-power performance, scalability and feature integration.

| Specification | Value |
|---|---|
| **Microcontroller** | MK82FN256VLL15 |
| **Frequency** | 150MHz |
| **Flash** | 256KB |
| **RAM** | 256KB |
| **Vendor** | [Freescale](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/kinetis-cortex-m-mcus/k-seriesperformancem4/k8x-secure/freedom-development-platform-for-kinetis-k82-k81-and-k80-mcus:FRDM-K82F?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `frdm_k82f` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:frdm_k82f]
platform = freescalekinetis
board = frdm_k82f
```

To override a setting of the board manifest [frdm_k82f.json](https://github.com/platformio/platform-freescalekinetis/blob/master/boards/frdm_k82f.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:frdm_k82f]
platform = freescalekinetis
board = frdm_k82f

; change microcontroller
board_build.mcu = mk82fn256vll15

; change MCU frequency
board_build.f_cpu = 150000000L
```

## Uploading

Freescale Kinetis FRDM-K82F supports these upload protocols:

- `cmsis-dap`
- `jlink`
- `mbed`

The default is `mbed`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:frdm_k82f]
platform = freescalekinetis
board = frdm_k82f

upload_protocol = mbed
```

## Debugging

The Freescale Kinetis FRDM-K82F has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) | Yes | Yes |
| [J-LINK](../../debug-probes/jlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Mbed](../../frameworks/mbed.mdx) | Arm Mbed OS is a platform operating system designed for the internet of things |
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
