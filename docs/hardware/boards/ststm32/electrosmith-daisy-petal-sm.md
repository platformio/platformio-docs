---
title: "Electrosmith Daisy Petal SM"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-ststm32-electrosmith-daisy-petal-sm"></a>

# Electrosmith Daisy Petal SM

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32H750IBK6 |
| **Frequency** | 400MHz |
| **Flash** | 128KB |
| **RAM** | 512KB |
| **Vendor** | [Electrosmith](https://www.electro-smith.com/daisy?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `electrosmith_daisy_petal_sm` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:electrosmith_daisy_petal_sm]
platform = ststm32
board = electrosmith_daisy_petal_sm
```

You can override default Electrosmith Daisy Petal SM settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [electrosmith_daisy_petal_sm.json](https://github.com/platformio/platform-ststm32/blob/master/boards/electrosmith_daisy_petal_sm.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:electrosmith_daisy_petal_sm]
platform = ststm32
board = electrosmith_daisy_petal_sm

; change microcontroller
board_build.mcu = stm32h750ibk6

; change MCU frequency
board_build.f_cpu = 400000000L
```

## Uploading

Electrosmith Daisy Petal SM supports the following uploading protocols:

- `blackmagic`
- `cmsis-dap`
- `jlink`
- `mbed`
- `stlink`

Default protocol is `stlink`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:electrosmith_daisy_petal_sm]
platform = ststm32
board = electrosmith_daisy_petal_sm

upload_protocol = stlink
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

Electrosmith Daisy Petal SM does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

| Compatible Tools | On-board | Default |
|---|---|---|
| [Black Magic Probe](../../debug-probes/blackmagic.md) |  | Yes |
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) |  |  |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [ST-LINK](../../debug-probes/stlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [CMSIS](../../frameworks/cmsis.md) | Vendor-independent hardware abstraction layer for the Cortex-M processor series |
| [STM32Cube](../../frameworks/stm32cube.mdx) | STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency |
