---
title: "Armstrap Eagle 1024"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Armstrap Eagle 1024 (STM32F417VGT6, 168MHz, 1MB flash, 192KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Armstrap Eagle 1024

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32F417VGT6 |
| **Frequency** | 168MHz |
| **Flash** | 1MB |
| **RAM** | 192KB |
| **Vendor** | [Armstrap](http://docs.armstrap.org/en/latest/hardware-overview.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `armstrap_eagle1024` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:armstrap_eagle1024]
platform = ststm32
board = armstrap_eagle1024
```

To override a setting of the board manifest [armstrap_eagle1024.json](https://github.com/platformio/platform-ststm32/blob/master/boards/armstrap_eagle1024.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:armstrap_eagle1024]
platform = ststm32
board = armstrap_eagle1024

; change microcontroller
board_build.mcu = stm32f417vgt6

; change MCU frequency
board_build.f_cpu = 168000000L
```

## Uploading

Armstrap Eagle 1024 supports these upload protocols:

- `blackmagic`
- `cmsis-dap`
- `jlink`
- `stlink`

The default is `blackmagic`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:armstrap_eagle1024]
platform = ststm32
board = armstrap_eagle1024

upload_protocol = blackmagic
```

## Debugging

The Armstrap Eagle 1024 has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [Black magic probe](../../debug-probes/blackmagic.md) | Yes | Yes |
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) |  |  |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [ST-LINK](../../debug-probes/stlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [CMSIS](../../frameworks/cmsis.md) | Vendor-independent hardware abstraction layer for the Cortex-M processor series |
| [LibOpenCM3](../../frameworks/libopencm3.md) | The libopencm3 project aims to create an open-source firmware library for various ARM Cortex-M microcontrollers. |
| [Standard Peripheral Library](../../frameworks/spl.mdx) | Standard Peripheral Library for ST STM32 microcontrollers |
| [STM32Cube](../../frameworks/stm32cube.mdx) | STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency |
