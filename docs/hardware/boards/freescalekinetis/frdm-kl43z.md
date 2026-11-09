---
title: "Freescale Kinetis FRDM-KL43Z"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Freescale Kinetis FRDM-KL43Z (MKL43Z256VLH4, 48MHz, 256KB flash, 32KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-freescalekinetis-frdm-kl43z"></a>

# Freescale Kinetis FRDM-KL43Z

## Hardware

Platform [Freescale Kinetis](../../platforms/freescalekinetis.md): Freescale Kinetis Microcontrollers is family of multiple hardware- and software-compatible ARM Cortex-M0+, Cortex-M4 and Cortex-M7-based MCU series. Kinetis MCUs offer exceptional low-power performance, scalability and feature integration.

| Specification | Value |
|---|---|
| **Microcontroller** | MKL43Z256VLH4 |
| **Frequency** | 48MHz |
| **Flash** | 256KB |
| **RAM** | 32KB |
| **Vendor** | [Freescale](https://os.mbed.com/platforms/FRDM-KL43Z/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `frdm_kl43z` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:frdm_kl43z]
platform = freescalekinetis
board = frdm_kl43z
```

To override a setting of the board manifest [frdm_kl43z.json](https://github.com/platformio/platform-freescalekinetis/blob/master/boards/frdm_kl43z.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:frdm_kl43z]
platform = freescalekinetis
board = frdm_kl43z

; change microcontroller
board_build.mcu = mkl43z256vlh4

; change MCU frequency
board_build.f_cpu = 48000000L
```

## Uploading

Freescale Kinetis FRDM-KL43Z supports these upload protocols:

- `cmsis-dap`
- `jlink`
- `mbed`

The default is `mbed`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:frdm_kl43z]
platform = freescalekinetis
board = frdm_kl43z

upload_protocol = mbed
```

## Debugging

The Freescale Kinetis FRDM-KL43Z has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

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
