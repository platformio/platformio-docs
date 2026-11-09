---
title: "Arduino Giga R1 (M4 core)"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-ststm32-giga-r1-m4"></a>

# Arduino Giga R1 (M4 core)

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32H747XIH6 |
| **Frequency** | 480MHz |
| **Flash** | 1MB |
| **RAM** | 287.35KB |
| **Vendor** | [Arduino](https://docs.arduino.cc/hardware/giga-r1-wifi?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `giga_r1_m4` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:giga_r1_m4]
platform = ststm32
board = giga_r1_m4
```

You can override default Arduino Giga R1 (M4 core) settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [giga_r1_m4.json](https://github.com/platformio/platform-ststm32/blob/master/boards/giga_r1_m4.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:giga_r1_m4]
platform = ststm32
board = giga_r1_m4

; change microcontroller
board_build.mcu = stm32h747xih6

; change MCU frequency
board_build.f_cpu = 480000000L
```

## Uploading

Arduino Giga R1 (M4 core) supports the following uploading protocols:

- `cmsis-dap`
- `dfu`
- `jlink`
- `mbed`
- `stlink`

Default protocol is `dfu`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:giga_r1_m4]
platform = ststm32
board = giga_r1_m4

upload_protocol = dfu
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

Arduino Giga R1 (M4 core) does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

| Compatible Tools | On-board | Default |
|---|---|---|
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) |  | Yes |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [ST-LINK](../../debug-probes/stlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
