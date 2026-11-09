---
title: "ST Nucleo C071RB"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "ST Nucleo C071RB (STM32C071RBT6, 48MHz, 128KB flash, 24KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# ST Nucleo C071RB

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32C071RBT6 |
| **Frequency** | 48MHz |
| **Flash** | 128KB |
| **RAM** | 24KB |
| **Vendor** | [ST](https://www.st.com/en/evaluation-tools/nucleo-c071rb.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `nucleo_c071rb` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:nucleo_c071rb]
platform = ststm32
board = nucleo_c071rb
```

To override a setting of the board manifest [nucleo_c071rb.json](https://github.com/platformio/platform-ststm32/blob/master/boards/nucleo_c071rb.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:nucleo_c071rb]
platform = ststm32
board = nucleo_c071rb

; change microcontroller
board_build.mcu = stm32c071rbt6

; change MCU frequency
board_build.f_cpu = 48000000L
```

## Uploading

ST Nucleo C071RB supports these upload protocols:

- `cmsis-dap`
- `jlink`
- `mbed`
- `stlink`

The default is `stlink`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:nucleo_c071rb]
platform = ststm32
board = nucleo_c071rb

upload_protocol = stlink
```

## Debugging

The ST Nucleo C071RB has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) |  |  |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [ST-LINK](../../debug-probes/stlink.md) | Yes | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [STM32Cube](../../frameworks/stm32cube.mdx) | STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency |
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
