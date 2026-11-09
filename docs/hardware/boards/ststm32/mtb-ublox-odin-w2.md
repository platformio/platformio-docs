---
title: "u-blox ODIN-W2"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-ststm32-mtb-ublox-odin-w2"></a>

# u-blox ODIN-W2

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32F439ZIY6 |
| **Frequency** | 168MHz |
| **Flash** | 2MB |
| **RAM** | 256KB |
| **Vendor** | [u-blox](https://os.mbed.com/modules/u-blox-odin-w2/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `mtb_ublox_odin_w2` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:mtb_ublox_odin_w2]
platform = ststm32
board = mtb_ublox_odin_w2
```

You can override default u-blox ODIN-W2 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [mtb_ublox_odin_w2.json](https://github.com/platformio/platform-ststm32/blob/master/boards/mtb_ublox_odin_w2.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:mtb_ublox_odin_w2]
platform = ststm32
board = mtb_ublox_odin_w2

; change microcontroller
board_build.mcu = stm32f439ziy6

; change MCU frequency
board_build.f_cpu = 168000000L
```

## Uploading

u-blox ODIN-W2 supports the following uploading protocols:

- `blackmagic`
- `cmsis-dap`
- `jlink`
- `stlink`

Default protocol is `stlink`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:mtb_ublox_odin_w2]
platform = ststm32
board = mtb_ublox_odin_w2

upload_protocol = stlink
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

u-blox ODIN-W2 has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

| Compatible Tools | On-board | Default |
|---|---|---|
| [Black Magic Probe](../../debug-probes/blackmagic.md) |  |  |
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) | Yes | Yes |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [ST-LINK](../../debug-probes/stlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [STM32Cube](../../frameworks/stm32cube.mdx) | STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency |
