---
title: "Arduino Portenta H7 (M7 core)"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Arduino Portenta H7 (M7 core) (STM32H747XIH6, 480MHz, 768KB flash, 511.35KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-ststm32-portenta-h7-m7"></a>

# Arduino Portenta H7 (M7 core)

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32H747XIH6 |
| **Frequency** | 480MHz |
| **Flash** | 768KB |
| **RAM** | 511.35KB |
| **Vendor** | [Arduino](https://www.arduino.cc/pro/hardware/product/portenta-h7?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `portenta_h7_m7` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:portenta_h7_m7]
platform = ststm32
board = portenta_h7_m7
```

To override a setting of the board manifest [portenta_h7_m7.json](https://github.com/platformio/platform-ststm32/blob/master/boards/portenta_h7_m7.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:portenta_h7_m7]
platform = ststm32
board = portenta_h7_m7

; change microcontroller
board_build.mcu = stm32h747xih6

; change MCU frequency
board_build.f_cpu = 480000000L
```

## Uploading

Arduino Portenta H7 (M7 core) supports these upload protocols:

- `cmsis-dap`
- `dfu`
- `jlink`
- `mbed`
- `stlink`

The default is `dfu`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:portenta_h7_m7]
platform = ststm32
board = portenta_h7_m7

upload_protocol = dfu
```

## Debugging

The Arduino Portenta H7 (M7 core) has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) |  | Yes |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [ST-LINK](../../debug-probes/stlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
