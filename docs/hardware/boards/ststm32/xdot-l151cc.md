---
title: "MultiTech xDot"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "MultiTech xDot (STM32L151CCU6, 32MHz, 256KB flash, 32KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# MultiTech xDot

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32L151CCU6 |
| **Frequency** | 32MHz |
| **Flash** | 256KB |
| **RAM** | 32KB |
| **Vendor** | [MultiTech](https://developer.mbed.org/platforms/MTS-xDot-L151CC/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `xdot_l151cc` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:xdot_l151cc]
platform = ststm32
board = xdot_l151cc
```

To override a setting of the board manifest [xdot_l151cc.json](https://github.com/platformio/platform-ststm32/blob/master/boards/xdot_l151cc.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:xdot_l151cc]
platform = ststm32
board = xdot_l151cc

; change microcontroller
board_build.mcu = stm32l151ccu6

; change MCU frequency
board_build.f_cpu = 32000000L
```

## Uploading

MultiTech xDot supports these upload protocols:

- `blackmagic`
- `cmsis-dap`
- `jlink`
- `stlink`

The default is `stlink`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:xdot_l151cc]
platform = ststm32
board = xdot_l151cc

upload_protocol = stlink
```

## Debugging

The MultiTech xDot has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [Black magic probe](../../debug-probes/blackmagic.md) |  | Yes |
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) |  |  |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [ST-LINK](../../debug-probes/stlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [CMSIS](../../frameworks/cmsis.md) | Vendor-independent hardware abstraction layer for the Cortex-M processor series |
| [LibOpenCM3](../../frameworks/libopencm3.md) | The libopencm3 project aims to create an open-source firmware library for various ARM Cortex-M microcontrollers. |
| [Mbed](../../frameworks/mbed.mdx) | Arm Mbed OS is a platform operating system designed for the internet of things |
| [STM32Cube](../../frameworks/stm32cube.mdx) | STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency |
