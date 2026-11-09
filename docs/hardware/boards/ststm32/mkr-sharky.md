---
title: "MKR Sharky"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-ststm32-mkr-sharky"></a>

# MKR Sharky

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32WB55CG |
| **Frequency** | 64MHz |
| **Flash** | 512KB |
| **RAM** | 192KB |
| **Vendor** | [Midatronics](https://midatronics.com/Development_Boards/MKR_Sharky_I?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `mkr_sharky` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:mkr_sharky]
platform = ststm32
board = mkr_sharky
```

You can override default MKR Sharky settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [mkr_sharky.json](https://github.com/platformio/platform-ststm32/blob/master/boards/mkr_sharky.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:mkr_sharky]
platform = ststm32
board = mkr_sharky

; change microcontroller
board_build.mcu = stm32wb55cg

; change MCU frequency
board_build.f_cpu = 64000000L
```

## Uploading

MKR Sharky supports the following uploading protocols:

- `blackmagic`
- `cmsis-dap`
- `dfu`
- `jlink`
- `mbed`
- `serial`

Default protocol is `mbed`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:mkr_sharky]
platform = ststm32
board = mkr_sharky

upload_protocol = mbed
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

MKR Sharky does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

| Compatible Tools | On-board | Default |
|---|---|---|
| [Black Magic Probe](../../debug-probes/blackmagic.md) |  | Yes |
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) |  |  |
| [J-LINK](../../debug-probes/jlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
