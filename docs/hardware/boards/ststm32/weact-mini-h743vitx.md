---
title: "WeAct Studio MiniSTM32H743VITX"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "WeAct Studio MiniSTM32H743VITX (STM32H743VIT6, 480MHz, 2MB flash, 512KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-ststm32-weact-mini-h743vitx"></a>

# WeAct Studio MiniSTM32H743VITX

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32H743VIT6 |
| **Frequency** | 480MHz |
| **Flash** | 2MB |
| **RAM** | 512KB |
| **Vendor** | [WeAct Studio](https://github.com/WeActStudio/MiniSTM32H7xx?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `weact_mini_h743vitx` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:weact_mini_h743vitx]
platform = ststm32
board = weact_mini_h743vitx
```

To override a setting of the board manifest [weact_mini_h743vitx.json](https://github.com/platformio/platform-ststm32/blob/master/boards/weact_mini_h743vitx.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:weact_mini_h743vitx]
platform = ststm32
board = weact_mini_h743vitx

; change microcontroller
board_build.mcu = stm32h743vit6

; change MCU frequency
board_build.f_cpu = 480000000L
```

## Uploading

WeAct Studio MiniSTM32H743VITX supports these upload protocols:

- `blackmagic`
- `cmsis-dap`
- `dfu`
- `jlink`
- `stlink`

The default is `stlink`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:weact_mini_h743vitx]
platform = ststm32
board = weact_mini_h743vitx

upload_protocol = stlink
```

## Debugging

The WeAct Studio MiniSTM32H743VITX has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [Black magic probe](../../debug-probes/blackmagic.md) |  | Yes |
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) |  |  |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [ST-LINK](../../debug-probes/stlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [CMSIS](../../frameworks/cmsis.md) | Vendor-independent hardware abstraction layer for the Cortex-M processor series |
| [STM32Cube](../../frameworks/stm32cube.mdx) | STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency |
