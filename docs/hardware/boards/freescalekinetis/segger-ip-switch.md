---
title: "SEGGER IP Switch Board"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "SEGGER IP Switch Board (MK66FN2M0VMD18, 180MHz, 2MB flash, 256KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# SEGGER IP Switch Board

## Hardware

Platform [Freescale Kinetis](../../platforms/freescalekinetis.md): Freescale Kinetis Microcontrollers is family of multiple hardware- and software-compatible ARM Cortex-M0+, Cortex-M4 and Cortex-M7-based MCU series. Kinetis MCUs offer exceptional low-power performance, scalability and feature integration.

| Specification | Value |
|---|---|
| **Microcontroller** | MK66FN2M0VMD18 |
| **Frequency** | 180MHz |
| **Flash** | 2MB |
| **RAM** | 256KB |
| **Vendor** | [SEGGER](https://www.segger.com/evaluate-our-software/segger/embosip-switch-board/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `segger_ip_switch` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:segger_ip_switch]
platform = freescalekinetis
board = segger_ip_switch
```

To override a setting of the board manifest [segger_ip_switch.json](https://github.com/platformio/platform-freescalekinetis/blob/master/boards/segger_ip_switch.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:segger_ip_switch]
platform = freescalekinetis
board = segger_ip_switch

; change microcontroller
board_build.mcu = mk66fn2m0vmd18

; change MCU frequency
board_build.f_cpu = 180000000L
```

## Uploading

SEGGER IP Switch Board supports these upload protocols:

- `jlink`
- `mbed`

The default is `jlink`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:segger_ip_switch]
platform = freescalekinetis
board = segger_ip_switch

upload_protocol = jlink
```

## Debugging

The SEGGER IP Switch Board has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

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
