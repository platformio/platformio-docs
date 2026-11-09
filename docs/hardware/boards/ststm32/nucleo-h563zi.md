---
title: "ST Nucleo H563ZI"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "ST Nucleo H563ZI (STM32H563ZIT6U, 250MHz, 2MB flash, 640KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

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

Use the board ID `nucleo_h563zi` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:nucleo_h563zi]
platform = ststm32
board = nucleo_h563zi
```

To override a setting of the board manifest [nucleo_h563zi.json](https://github.com/platformio/platform-ststm32/blob/master/boards/nucleo_h563zi.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

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

ST Nucleo H563ZI supports these upload protocols:

- `jlink`
- `mbed`

The default is `mbed`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:nucleo_h563zi]
platform = ststm32
board = nucleo_h563zi

upload_protocol = mbed
```

## Debugging

The ST Nucleo H563ZI has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [J-LINK](../../debug-probes/jlink.md) |  | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
