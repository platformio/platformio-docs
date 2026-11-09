---
title: "Big Tree Tech EBB42 V1.1"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Big Tree Tech EBB42 V1.1 (STM32G0B1RET6, 64MHz, 128KB flash, 144KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Big Tree Tech EBB42 V1.1

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32G0B1RET6 |
| **Frequency** | 64MHz |
| **Flash** | 128KB |
| **RAM** | 144KB |
| **Vendor** | [Big Tree Tech](https://github.com/bigtreetech/EBB/tree/master/EBB%20CAN%20V1.1%20(STM32G0B1)/EBB42%20CAN%20V1.1?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `btt_ebb42_v1_1` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:btt_ebb42_v1_1]
platform = ststm32
board = btt_ebb42_v1_1
```

To override a setting of the board manifest [btt_ebb42_v1_1.json](https://github.com/platformio/platform-ststm32/blob/master/boards/btt_ebb42_v1_1.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:btt_ebb42_v1_1]
platform = ststm32
board = btt_ebb42_v1_1

; change microcontroller
board_build.mcu = stm32g0b1ret6

; change MCU frequency
board_build.f_cpu = 64000000L
```

## Uploading

Big Tree Tech EBB42 V1.1 supports these upload protocols:

- `blackmagic`
- `cmsis-dap`
- `dfu`
- `jlink`
- `mbed`
- `serial`
- `stlink`

The default is `stlink`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:btt_ebb42_v1_1]
platform = ststm32
board = btt_ebb42_v1_1

upload_protocol = stlink
```

## Debugging

The Big Tree Tech EBB42 V1.1 has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

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
| [STM32Cube](../../frameworks/stm32cube.mdx) | STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency |
