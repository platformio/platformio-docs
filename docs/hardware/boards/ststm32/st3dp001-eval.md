---
title: "3DP001V1 Evaluation board for 3D printer"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "3DP001V1 Evaluation board for 3D printer (STM32F401VET6, 84MHz, 512KB flash, 96KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-ststm32-st3dp001-eval"></a>

# 3DP001V1 Evaluation board for 3D printer

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32F401VET6 |
| **Frequency** | 84MHz |
| **Flash** | 512KB |
| **RAM** | 96KB |
| **Vendor** | [ST](https://www.st.com/en/evaluation-tools/steval-3dp001v1.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `st3dp001_eval` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:st3dp001_eval]
platform = ststm32
board = st3dp001_eval
```

To override a setting of the board manifest [st3dp001_eval.json](https://github.com/platformio/platform-ststm32/blob/master/boards/st3dp001_eval.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:st3dp001_eval]
platform = ststm32
board = st3dp001_eval

; change microcontroller
board_build.mcu = stm32f401vet6

; change MCU frequency
board_build.f_cpu = 84000000L
```

## Uploading

3DP001V1 Evaluation board for 3D printer supports these upload protocols:

- `blackmagic`
- `cmsis-dap`
- `jlink`
- `stlink`

The default is `stlink`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:st3dp001_eval]
platform = ststm32
board = st3dp001_eval

upload_protocol = stlink
```

## Debugging

The 3DP001V1 Evaluation board for 3D printer has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

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
| [CMSIS](../../frameworks/cmsis.md) | Vendor-independent hardware abstraction layer for the Cortex-M processor series |
| [STM32Cube](../../frameworks/stm32cube.mdx) | STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency |
