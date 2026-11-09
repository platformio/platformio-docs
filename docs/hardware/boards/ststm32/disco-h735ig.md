---
title: "STM32H735G-DK Discovery kit"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-ststm32-disco-h735ig"></a>

# STM32H735G-DK Discovery kit

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32H735IGK6 |
| **Frequency** | 550MHz |
| **Flash** | 1MB |
| **RAM** | 432KB |
| **Vendor** | [ST](https://www.st.com/en/evaluation-tools/stm32h735g-dk.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `disco_h735ig` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:disco_h735ig]
platform = ststm32
board = disco_h735ig
```

You can override default STM32H735G-DK Discovery kit settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [disco_h735ig.json](https://github.com/platformio/platform-ststm32/blob/master/boards/disco_h735ig.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:disco_h735ig]
platform = ststm32
board = disco_h735ig

; change microcontroller
board_build.mcu = stm32h735igk6

; change MCU frequency
board_build.f_cpu = 550000000L
```

## Uploading

STM32H735G-DK Discovery kit supports the following uploading protocols:

- `blackmagic`
- `cmsis-dap`
- `jlink`
- `mbed`
- `stlink`

Default protocol is `stlink`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:disco_h735ig]
platform = ststm32
board = disco_h735ig

upload_protocol = stlink
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

STM32H735G-DK Discovery kit has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

| Compatible Tools | On-board | Default |
|---|---|---|
| [Black Magic Probe](../../debug-probes/blackmagic.md) |  |  |
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) |  |  |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [ST-LINK](../../debug-probes/stlink.md) | Yes | Yes |

## Frameworks

| Name | Description |
|---|---|
| [STM32Cube](../../frameworks/stm32cube.mdx) | STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency |
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
