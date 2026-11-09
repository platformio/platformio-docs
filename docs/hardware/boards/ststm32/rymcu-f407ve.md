---
title: "RYMCU STM32F407VE (192k RAM. 512k Flash)"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "RYMCU STM32F407VE (192k RAM. 512k Flash) (STM32F407VET6, 168MHz, 502.23KB flash, 128KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# RYMCU STM32F407VE (192k RAM. 512k Flash)

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32F407VET6 |
| **Frequency** | 168MHz |
| **Flash** | 502.23KB |
| **RAM** | 128KB |
| **Vendor** | [RYMCU](https://rymcu.com/products?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `rymcu_f407ve` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:rymcu_f407ve]
platform = ststm32
board = rymcu_f407ve
```

To override a setting of the board manifest [rymcu_f407ve.json](https://github.com/platformio/platform-ststm32/blob/master/boards/rymcu_f407ve.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:rymcu_f407ve]
platform = ststm32
board = rymcu_f407ve

; change microcontroller
board_build.mcu = stm32f407vet6

; change MCU frequency
board_build.f_cpu = 168000000L
```

## Uploading

RYMCU STM32F407VE (192k RAM. 512k Flash) supports these upload protocols:

- `blackmagic`
- `cmsis-dap`
- `dfu`
- `jlink`
- `serial`
- `stlink`

The default is `stlink`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:rymcu_f407ve]
platform = ststm32
board = rymcu_f407ve

upload_protocol = stlink
```

## Debugging

The RYMCU STM32F407VE (192k RAM. 512k Flash) has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [Black magic probe](../../debug-probes/blackmagic.md) |  |  |
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) |  |  |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [ST-LINK](../../debug-probes/stlink.md) |  | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [CMSIS](../../frameworks/cmsis.md) | Vendor-independent hardware abstraction layer for the Cortex-M processor series |
| [LibOpenCM3](../../frameworks/libopencm3.md) | The libopencm3 project aims to create an open-source firmware library for various ARM Cortex-M microcontrollers. |
| [STM32Cube](../../frameworks/stm32cube.mdx) | STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency |
