---
title: "u-blox EVK-ODIN-W2"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "u-blox EVK-ODIN-W2 (STM32F439ZIY6, 168MHz, 2MB flash, 256KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-ststm32-ublox-evk-odin-w2"></a>

# u-blox EVK-ODIN-W2

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32F439ZIY6 |
| **Frequency** | 168MHz |
| **Flash** | 2MB |
| **RAM** | 256KB |
| **Vendor** | [u-blox](https://developer.mbed.org/platforms/ublox-EVK-ODIN-W2/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `ublox_evk_odin_w2` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:ublox_evk_odin_w2]
platform = ststm32
board = ublox_evk_odin_w2
```

To override a setting of the board manifest [ublox_evk_odin_w2.json](https://github.com/platformio/platform-ststm32/blob/master/boards/ublox_evk_odin_w2.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:ublox_evk_odin_w2]
platform = ststm32
board = ublox_evk_odin_w2

; change microcontroller
board_build.mcu = stm32f439ziy6

; change MCU frequency
board_build.f_cpu = 168000000L
```

## Uploading

u-blox EVK-ODIN-W2 supports these upload protocols:

- `blackmagic`
- `cmsis-dap`
- `jlink`
- `stlink`

The default is `stlink`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:ublox_evk_odin_w2]
platform = ststm32
board = ublox_evk_odin_w2

upload_protocol = stlink
```

## Debugging

The u-blox EVK-ODIN-W2 has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

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
| [STM32Cube](../../frameworks/stm32cube.mdx) | STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency |
