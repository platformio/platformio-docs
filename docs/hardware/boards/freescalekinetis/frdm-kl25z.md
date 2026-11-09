---
title: "Freescale Kinetis FRDM-KL25Z"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Freescale Kinetis FRDM-KL25Z (MKL25Z128VLK4, 48MHz, 128KB flash, 16KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-freescalekinetis-frdm-kl25z"></a>

# Freescale Kinetis FRDM-KL25Z

## Hardware

Platform [Freescale Kinetis](../../platforms/freescalekinetis.md): Freescale Kinetis Microcontrollers is family of multiple hardware- and software-compatible ARM Cortex-M0+, Cortex-M4 and Cortex-M7-based MCU series. Kinetis MCUs offer exceptional low-power performance, scalability and feature integration.

| Specification | Value |
|---|---|
| **Microcontroller** | MKL25Z128VLK4 |
| **Frequency** | 48MHz |
| **Flash** | 128KB |
| **RAM** | 16KB |
| **Vendor** | [Freescale](https://developer.mbed.org/platforms/KL25Z/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `frdm_kl25z` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:frdm_kl25z]
platform = freescalekinetis
board = frdm_kl25z
```

To override a setting of the board manifest [frdm_kl25z.json](https://github.com/platformio/platform-freescalekinetis/blob/master/boards/frdm_kl25z.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:frdm_kl25z]
platform = freescalekinetis
board = frdm_kl25z

; change microcontroller
board_build.mcu = mkl25z128vlk4

; change MCU frequency
board_build.f_cpu = 48000000L
```

## Uploading

Freescale Kinetis FRDM-KL25Z supports these upload protocols:

- `blackmagic`
- `cmsis-dap`
- `jlink`
- `mbed`

The default is `mbed`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:frdm_kl25z]
platform = freescalekinetis
board = frdm_kl25z

upload_protocol = mbed
```

## Debugging

The Freescale Kinetis FRDM-KL25Z has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [Black magic probe](../../debug-probes/blackmagic.md) |  |  |
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) | Yes | Yes |
| [J-LINK](../../debug-probes/jlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Mbed](../../frameworks/mbed.mdx) | Arm Mbed OS is a platform operating system designed for the internet of things |
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
