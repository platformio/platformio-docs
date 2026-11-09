---
title: "Freescale Kinetis FRDM-KW24D512"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-freescalekinetis-frdm-kw24d"></a>

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

Please use `frdm_kw24d` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:frdm_kw24d]
platform = freescalekinetis
board = frdm_kw24d
```

You can override default Freescale Kinetis FRDM-KW24D512 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [frdm_kw24d.json](https://github.com/platformio/platform-freescalekinetis/blob/master/boards/frdm_kw24d.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

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

Freescale Kinetis FRDM-KW24D512 supports the following uploading protocols:

- `jlink`
- `mbed`

Default protocol is `mbed`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:frdm_kw24d]
platform = freescalekinetis
board = frdm_kw24d

upload_protocol = mbed
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

Freescale Kinetis FRDM-KW24D512 does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

| Compatible Tools | On-board | Default |
|---|---|---|
| [J-LINK](../../debug-probes/jlink.md) |  | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
