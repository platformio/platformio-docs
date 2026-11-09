---
title: "STM32F373RC (32k RAM. 256k Flash)"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-ststm32-genericstm32f373rc"></a>

# STM32F373RC (32k RAM. 256k Flash)

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32F373RCT6 |
| **Frequency** | 72MHz |
| **Flash** | 256KB |
| **RAM** | 32KB |
| **Vendor** | [Generic](https://www.st.com/en/microcontrollers/stm32f373rc.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `genericSTM32F373RC` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:genericSTM32F373RC]
platform = ststm32
board = genericSTM32F373RC
```

You can override default STM32F373RC (32k RAM. 256k Flash) settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [genericSTM32F373RC.json](https://github.com/platformio/platform-ststm32/blob/master/boards/genericSTM32F373RC.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:genericSTM32F373RC]
platform = ststm32
board = genericSTM32F373RC

; change microcontroller
board_build.mcu = stm32f373rct6

; change MCU frequency
board_build.f_cpu = 72000000L
```

## Uploading

STM32F373RC (32k RAM. 256k Flash) supports the following uploading protocols:

- `blackmagic`
- `cmsis-dap`
- `jlink`
- `stlink`

Default protocol is `stlink`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:genericSTM32F373RC]
platform = ststm32
board = genericSTM32F373RC

upload_protocol = stlink
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

STM32F373RC (32k RAM. 256k Flash) does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

| Compatible Tools | On-board | Default |
|---|---|---|
| [Black Magic Probe](../../debug-probes/blackmagic.md) |  | Yes |
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) |  |  |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [ST-LINK](../../debug-probes/stlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [CMSIS](../../frameworks/cmsis.md) | Vendor-independent hardware abstraction layer for the Cortex-M processor series |
| [STM32Cube](../../frameworks/stm32cube.mdx) | STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency |
