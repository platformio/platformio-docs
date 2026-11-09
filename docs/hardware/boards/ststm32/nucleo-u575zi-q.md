---
title: "ST Nucleo U575ZI-Q"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-ststm32-nucleo-u575zi-q"></a>

# ST Nucleo U575ZI-Q

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32U575ZIT6Q |
| **Frequency** | 160MHz |
| **Flash** | 2MB |
| **RAM** | 768KB |
| **Vendor** | [ST](https://www.st.com/en/evaluation-tools/nucleo-u575zi-q.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `nucleo_u575zi_q` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:nucleo_u575zi_q]
platform = ststm32
board = nucleo_u575zi_q
```

You can override default ST Nucleo U575ZI-Q settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [nucleo_u575zi_q.json](https://github.com/platformio/platform-ststm32/blob/master/boards/nucleo_u575zi_q.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:nucleo_u575zi_q]
platform = ststm32
board = nucleo_u575zi_q

; change microcontroller
board_build.mcu = stm32u575zit6q

; change MCU frequency
board_build.f_cpu = 160000000L
```

## Uploading

ST Nucleo U575ZI-Q supports the following uploading protocols:

- `blackmagic`
- `cmsis-dap`
- `jlink`
- `mbed`
- `stlink`

Default protocol is `stlink`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:nucleo_u575zi_q]
platform = ststm32
board = nucleo_u575zi_q

upload_protocol = stlink
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

ST Nucleo U575ZI-Q has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

| Compatible Tools | On-board | Default |
|---|---|---|
| [Black Magic Probe](../../debug-probes/blackmagic.md) |  |  |
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) |  |  |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [ST-LINK](../../debug-probes/stlink.md) | Yes | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [Mbed](../../frameworks/mbed.mdx) | Arm Mbed OS is a platform operating system designed for the internet of things |
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
