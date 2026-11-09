---
title: "STM32H735G-DK Discovery kit"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "STM32H735G-DK Discovery kit (STM32H735IGK6, 550MHz, 1MB flash, 432KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# STM32H735G-DK Discovery kit

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32H735IGK6 |
| **Frequency** | 550MHz |
| **Flash** | 1MB |
| **RAM** | 432KB |
| **Vendor** | [ST](https://www.st.com/en/evaluation-tools/stm32h735g-dk.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `disco_h735ig` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:disco_h735ig]
platform = ststm32
board = disco_h735ig
```

To override a setting of the board manifest [disco_h735ig.json](https://github.com/platformio/platform-ststm32/blob/master/boards/disco_h735ig.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:disco_h735ig]
platform = ststm32
board = disco_h735ig

; change microcontroller
board_build.mcu = stm32h735igk6

; change MCU frequency
board_build.f_cpu = 550000000L
```

## Uploading

STM32H735G-DK Discovery kit supports these upload protocols:

- `blackmagic`
- `cmsis-dap`
- `jlink`
- `mbed`
- `stlink`

The default is `stlink`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:disco_h735ig]
platform = ststm32
board = disco_h735ig

upload_protocol = stlink
```

## Debugging

The STM32H735G-DK Discovery kit has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

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
| [STM32Cube](../../frameworks/stm32cube.mdx) | STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency |
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
