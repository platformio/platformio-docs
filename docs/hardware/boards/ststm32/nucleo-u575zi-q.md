---
title: "ST Nucleo U575ZI-Q"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "ST Nucleo U575ZI-Q (STM32U575ZIT6Q, 160MHz, 2MB flash, 768KB RAM): PlatformIO board ID, configuration, uploading and debugging."
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

Use the board ID `nucleo_u575zi_q` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:nucleo_u575zi_q]
platform = ststm32
board = nucleo_u575zi_q
```

To override a setting of the board manifest [nucleo_u575zi_q.json](https://github.com/platformio/platform-ststm32/blob/master/boards/nucleo_u575zi_q.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

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

ST Nucleo U575ZI-Q supports these upload protocols:

- `blackmagic`
- `cmsis-dap`
- `jlink`
- `mbed`
- `stlink`

The default is `stlink`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:nucleo_u575zi_q]
platform = ststm32
board = nucleo_u575zi_q

upload_protocol = stlink
```

## Debugging

The ST Nucleo U575ZI-Q has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [Black magic probe](../../debug-probes/blackmagic.md) |  |  |
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) |  |  |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [ST-LINK](../../debug-probes/stlink.md) | Yes | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [Mbed](../../frameworks/mbed.mdx) | Arm Mbed OS is a platform operating system designed for the internet of things |
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
