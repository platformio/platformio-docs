---
title: "Freescale Kinetis FRDM-KW24D512"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Freescale Kinetis FRDM-KW24D512 (MKW24D512, 50MHz, 512KB flash, 64KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Freescale Kinetis FRDM-KW24D512

## Hardware

Platform [Freescale Kinetis](../../platforms/freescalekinetis.md): Freescale Kinetis Microcontrollers is family of multiple hardware- and software-compatible ARM Cortex-M0+, Cortex-M4 and Cortex-M7-based MCU series. Kinetis MCUs offer exceptional low-power performance, scalability and feature integration.

| Specification | Value |
|---|---|
| **Microcontroller** | MKW24D512 |
| **Frequency** | 50MHz |
| **Flash** | 512KB |
| **RAM** | 64KB |
| **Vendor** | [Freescale](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/kinetis-cortex-m-mcus/w-serieswireless-conn.m0-plus-m4/freedom-development-platform-for-kinetis-kw2x-mcus:FRDM-KW24D512?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `frdm_kw24d` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:frdm_kw24d]
platform = freescalekinetis
board = frdm_kw24d
```

To override a setting of the board manifest [frdm_kw24d.json](https://github.com/platformio/platform-freescalekinetis/blob/master/boards/frdm_kw24d.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:frdm_kw24d]
platform = freescalekinetis
board = frdm_kw24d

; change microcontroller
board_build.mcu = mkw24d512

; change MCU frequency
board_build.f_cpu = 50000000L
```

## Uploading

Freescale Kinetis FRDM-KW24D512 supports these upload protocols:

- `jlink`
- `mbed`

The default is `mbed`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:frdm_kw24d]
platform = freescalekinetis
board = frdm_kw24d

upload_protocol = mbed
```

## Debugging

The Freescale Kinetis FRDM-KW24D512 has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [J-LINK](../../debug-probes/jlink.md) |  | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
