---
title: "MKR Sharky"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "MKR Sharky (STM32WB55CG, 64MHz, 512KB flash, 192KB RAM): PlatformIO board ID, configuration, uploading and debugging."
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

Use the board ID `mkr_sharky` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:mkr_sharky]
platform = ststm32
board = mkr_sharky
```

To override a setting of the board manifest [mkr_sharky.json](https://github.com/platformio/platform-ststm32/blob/master/boards/mkr_sharky.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

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

MKR Sharky supports these upload protocols:

- `blackmagic`
- `cmsis-dap`
- `dfu`
- `jlink`
- `mbed`
- `serial`

The default is `mbed`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:mkr_sharky]
platform = ststm32
board = mkr_sharky

upload_protocol = mbed
```

## Debugging

The MKR Sharky has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [Black magic probe](../../debug-probes/blackmagic.md) |  | Yes |
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) |  |  |
| [J-LINK](../../debug-probes/jlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
