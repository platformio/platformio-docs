---
title: "SEGGER IP Switch Board"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-freescalekinetis-segger-ip-switch"></a>

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

Please use `segger_ip_switch` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:segger_ip_switch]
platform = freescalekinetis
board = segger_ip_switch
```

You can override default SEGGER IP Switch Board settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [segger_ip_switch.json](https://github.com/platformio/platform-freescalekinetis/blob/master/boards/segger_ip_switch.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

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

SEGGER IP Switch Board supports the following uploading protocols:

- `jlink`
- `mbed`

Default protocol is `jlink`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:segger_ip_switch]
platform = freescalekinetis
board = segger_ip_switch

upload_protocol = jlink
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

SEGGER IP Switch Board does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

| Compatible Tools | On-board | Default |
|---|---|---|
| [J-LINK](../../debug-probes/jlink.md) |  | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
