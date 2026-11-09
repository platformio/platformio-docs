---
title: "Freescale Kinetis FRDM-K22F"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-freescalekinetis-frdm-k22f"></a>

# Freescale Kinetis FRDM-K22F

## Hardware

Platform [Freescale Kinetis](../../platforms/freescalekinetis.md): Freescale Kinetis Microcontrollers is family of multiple hardware- and software-compatible ARM Cortex-M0+, Cortex-M4 and Cortex-M7-based MCU series. Kinetis MCUs offer exceptional low-power performance, scalability and feature integration.

| Specification | Value |
|---|---|
| **Microcontroller** | MK22FN512VLH12 |
| **Frequency** | 120MHz |
| **Flash** | 512KB |
| **RAM** | 128KB |
| **Vendor** | [Freescale](https://developer.mbed.org/platforms/FRDM-K22F/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `frdm_k22f` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:frdm_k22f]
platform = freescalekinetis
board = frdm_k22f
```

You can override default Freescale Kinetis FRDM-K22F settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [frdm_k22f.json](https://github.com/platformio/platform-freescalekinetis/blob/master/boards/frdm_k22f.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:frdm_k22f]
platform = freescalekinetis
board = frdm_k22f

; change microcontroller
board_build.mcu = mk22fn512vlh12

; change MCU frequency
board_build.f_cpu = 120000000L
```

## Uploading

Freescale Kinetis FRDM-K22F supports the following uploading protocols:

- `cmsis-dap`
- `jlink`
- `mbed`

Default protocol is `mbed`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:frdm_k22f]
platform = freescalekinetis
board = frdm_k22f

upload_protocol = mbed
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

Freescale Kinetis FRDM-K22F has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

| Compatible Tools | On-board | Default |
|---|---|---|
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) | Yes | Yes |
| [J-LINK](../../debug-probes/jlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Mbed](../../frameworks/mbed.mdx) | Arm Mbed OS is a platform operating system designed for the internet of things |
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
