---
title: "ST 32F469IDISCOVERY"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "ST 32F469IDISCOVERY (STM32F469NIH6, 180MHz, 2MB flash, 384KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# ST 32F469IDISCOVERY

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32F469NIH6 |
| **Frequency** | 180MHz |
| **Flash** | 2MB |
| **RAM** | 384KB |
| **Vendor** | [ST](http://www.st.com/web/catalog/tools/FM116/CL1620/SC959/SS1532/LN1848/PF262395?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `disco_f469ni` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:disco_f469ni]
platform = ststm32
board = disco_f469ni
```

To override a setting of the board manifest [disco_f469ni.json](https://github.com/platformio/platform-ststm32/blob/master/boards/disco_f469ni.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:disco_f469ni]
platform = ststm32
board = disco_f469ni

; change microcontroller
board_build.mcu = stm32f469nih6

; change MCU frequency
board_build.f_cpu = 180000000L
```

## Uploading

ST 32F469IDISCOVERY supports these upload protocols:

- `blackmagic`
- `cmsis-dap`
- `jlink`
- `mbed`
- `stlink`

The default is `stlink`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:disco_f469ni]
platform = ststm32
board = disco_f469ni

upload_protocol = stlink
```

## Debugging

The ST 32F469IDISCOVERY has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

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
| [CMSIS](../../frameworks/cmsis.md) | Vendor-independent hardware abstraction layer for the Cortex-M processor series |
| [LibOpenCM3](../../frameworks/libopencm3.md) | The libopencm3 project aims to create an open-source firmware library for various ARM Cortex-M microcontrollers. |
| [Mbed](../../frameworks/mbed.mdx) | Arm Mbed OS is a platform operating system designed for the internet of things |
| [STM32Cube](../../frameworks/stm32cube.mdx) | STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency |
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
