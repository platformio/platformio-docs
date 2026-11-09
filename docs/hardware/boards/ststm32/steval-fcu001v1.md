---
title: "STEVAL-FCU001V1 Flight controller unit evaluation board"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-ststm32-steval-fcu001v1"></a>

# STEVAL-FCU001V1 Flight controller unit evaluation board

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32F401CCU6 |
| **Frequency** | 84MHz |
| **Flash** | 256KB |
| **RAM** | 64KB |
| **Vendor** | [ST](https://www.st.com/en/evaluation-tools/steval-fcu001v1.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `steval_fcu001v1` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:steval_fcu001v1]
platform = ststm32
board = steval_fcu001v1
```

You can override default STEVAL-FCU001V1 Flight controller unit evaluation board settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [steval_fcu001v1.json](https://github.com/platformio/platform-ststm32/blob/master/boards/steval_fcu001v1.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:steval_fcu001v1]
platform = ststm32
board = steval_fcu001v1

; change microcontroller
board_build.mcu = stm32f401ccu6

; change MCU frequency
board_build.f_cpu = 84000000L
```

## Uploading

STEVAL-FCU001V1 Flight controller unit evaluation board supports the following uploading protocols:

- `blackmagic`
- `cmsis-dap`
- `jlink`
- `stlink`

Default protocol is `stlink`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:steval_fcu001v1]
platform = ststm32
board = steval_fcu001v1

upload_protocol = stlink
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

STEVAL-FCU001V1 Flight controller unit evaluation board does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

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
| [LibOpenCM3](../../frameworks/libopencm3.md) | The libopencm3 project aims to create an open-source firmware library for various ARM Cortex-M microcontrollers. |
| [STM32Cube](../../frameworks/stm32cube.mdx) | STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency |
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
