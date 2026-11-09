---
title: "Seeed Wio 3G"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Seeed Wio 3G (STM32F439VI, 180MHz, 2MB flash, 256KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Seeed Wio 3G

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32F439VI |
| **Frequency** | 180MHz |
| **Flash** | 2MB |
| **RAM** | 256KB |
| **Vendor** | [SeeedStudio](https://os.mbed.com/platforms/Seeed-Wio-3g/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `wio_3g` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:wio_3g]
platform = ststm32
board = wio_3g
```

To override a setting of the board manifest [wio_3g.json](https://github.com/platformio/platform-ststm32/blob/master/boards/wio_3g.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:wio_3g]
platform = ststm32
board = wio_3g

; change microcontroller
board_build.mcu = stm32f439vi

; change MCU frequency
board_build.f_cpu = 180000000L
```

## Uploading

Seeed Wio 3G supports these upload protocols:

- `blackmagic`
- `jlink`
- `stlink`

The default is `stlink`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:wio_3g]
platform = ststm32
board = wio_3g

upload_protocol = stlink
```

## Debugging

The Seeed Wio 3G has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [Black magic probe](../../debug-probes/blackmagic.md) |  |  |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [ST-LINK](../../debug-probes/stlink.md) | Yes | Yes |

## Frameworks

| Name | Description |
|---|---|
| [CMSIS](../../frameworks/cmsis.md) | Vendor-independent hardware abstraction layer for the Cortex-M processor series |
| [LibOpenCM3](../../frameworks/libopencm3.md) | The libopencm3 project aims to create an open-source firmware library for various ARM Cortex-M microcontrollers. |
| [Mbed](../../frameworks/mbed.mdx) | Arm Mbed OS is a platform operating system designed for the internet of things |
| [STM32Cube](../../frameworks/stm32cube.mdx) | STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency |
