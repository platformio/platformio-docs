---
title: "ST Nucleo H563ZI"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-ststm32-nucleo-h563zi"></a>

# ST Nucleo H563ZI

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32H563ZIT6U |
| **Frequency** | 250MHz |
| **Flash** | 2MB |
| **RAM** | 640KB |
| **Vendor** | [ST](https://www.st.com/en/evaluation-tools/nucleo-h563zi.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `nucleo_h563zi` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:nucleo_h563zi]
platform = ststm32
board = nucleo_h563zi
```

You can override default ST Nucleo H563ZI settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [nucleo_h563zi.json](https://github.com/platformio/platform-ststm32/blob/master/boards/nucleo_h563zi.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:nucleo_h563zi]
platform = ststm32
board = nucleo_h563zi

; change microcontroller
board_build.mcu = stm32h563zit6u

; change MCU frequency
board_build.f_cpu = 250000000L
```

## Uploading

ST Nucleo H563ZI supports the following uploading protocols:

- `jlink`
- `mbed`

Default protocol is `mbed`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:nucleo_h563zi]
platform = ststm32
board = nucleo_h563zi

upload_protocol = mbed
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

ST Nucleo H563ZI does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

| Compatible Tools | On-board | Default |
|---|---|---|
| [J-LINK](../../debug-probes/jlink.md) |  | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
