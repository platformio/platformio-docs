---
title: "Ebyte E77 Dev Board"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-ststm32-ebyte-e77-dev"></a>

# Ebyte E77 Dev Board

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32WLE5CC |
| **Frequency** | 48MHz |
| **Flash** | 256KB |
| **RAM** | 64KB |
| **Vendor** | [Ebyte](https://www.cdebyte.com/products/E77-400MBL-01?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `ebyte_e77_dev` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:ebyte_e77_dev]
platform = ststm32
board = ebyte_e77_dev
```

You can override default Ebyte E77 Dev Board settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [ebyte_e77_dev.json](https://github.com/platformio/platform-ststm32/blob/master/boards/ebyte_e77_dev.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:ebyte_e77_dev]
platform = ststm32
board = ebyte_e77_dev

; change microcontroller
board_build.mcu = stm32wle5cc

; change MCU frequency
board_build.f_cpu = 48000000L
```

## Uploading

Ebyte E77 Dev Board supports the following uploading protocols:

- `jlink`
- `stlink`

Default protocol is `stlink`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:ebyte_e77_dev]
platform = ststm32
board = ebyte_e77_dev

upload_protocol = stlink
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

Ebyte E77 Dev Board does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

| Compatible Tools | On-board | Default |
|---|---|---|
| [J-LINK](../../debug-probes/jlink.md) |  | Yes |
| [ST-LINK](../../debug-probes/stlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
