---
title: "Freescale Kinetis FRDM-KL25Z"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
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

Please use `frdm_kl25z` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:frdm_kl25z]
platform = freescalekinetis
board = frdm_kl25z
```

You can override default Freescale Kinetis FRDM-KL25Z settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [frdm_kl25z.json](https://github.com/platformio/platform-freescalekinetis/blob/master/boards/frdm_kl25z.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

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

Freescale Kinetis FRDM-KL25Z supports the following uploading protocols:

- `blackmagic`
- `cmsis-dap`
- `jlink`
- `mbed`

Default protocol is `mbed`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:frdm_kl25z]
platform = freescalekinetis
board = frdm_kl25z

upload_protocol = mbed
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

Freescale Kinetis FRDM-KL25Z has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

| Compatible Tools | On-board | Default |
|---|---|---|
| [Black Magic Probe](../../debug-probes/blackmagic.md) |  |  |
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) | Yes | Yes |
| [J-LINK](../../debug-probes/jlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Mbed](../../frameworks/mbed.mdx) | Arm Mbed OS is a platform operating system designed for the internet of things |
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
