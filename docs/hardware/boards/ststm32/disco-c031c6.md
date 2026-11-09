---
title: "ST STM32C0316-DK Discovery Kit"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-ststm32-disco-c031c6"></a>

# ST STM32C0316-DK Discovery Kit

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32C031C6T6 |
| **Frequency** | 48MHz |
| **Flash** | 32KB |
| **RAM** | 12KB |
| **Vendor** | [ST](https://www.st.com/en/evaluation-tools/stm32c0316-dk.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `disco_c031c6` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:disco_c031c6]
platform = ststm32
board = disco_c031c6
```

You can override default ST STM32C0316-DK Discovery Kit settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [disco_c031c6.json](https://github.com/platformio/platform-ststm32/blob/master/boards/disco_c031c6.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:disco_c031c6]
platform = ststm32
board = disco_c031c6

; change microcontroller
board_build.mcu = stm32c031c6t6

; change MCU frequency
board_build.f_cpu = 48000000L
```

## Uploading

ST STM32C0316-DK Discovery Kit supports the following uploading protocols:

- `cmsis-dap`
- `jlink`
- `stlink`

Default protocol is `stlink`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:disco_c031c6]
platform = ststm32
board = disco_c031c6

upload_protocol = stlink
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

ST STM32C0316-DK Discovery Kit has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

| Compatible Tools | On-board | Default |
|---|---|---|
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) |  |  |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [ST-LINK](../../debug-probes/stlink.md) | Yes | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [STM32Cube](../../frameworks/stm32cube.mdx) | STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency |
