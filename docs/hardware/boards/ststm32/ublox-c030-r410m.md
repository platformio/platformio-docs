---
title: "u-blox C030-R410M IoT"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "u-blox C030-R410M IoT (STM32F437VG, 180MHz, 1MB flash, 256KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# u-blox C030-R410M IoT

## Hardware

Platform [ST STM32](../../platforms/ststm32.mdx): The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M processor is designed to offer new degrees of freedom to MCU users. It offers a 32-bit product range that combines very high performance, real-time capabilities, digital signal processing, and low-power, low-voltage operation, while maintaining full integration and ease of development.

| Specification | Value |
|---|---|
| **Microcontroller** | STM32F437VG |
| **Frequency** | 180MHz |
| **Flash** | 1MB |
| **RAM** | 256KB |
| **Vendor** | [u-blox](https://os.mbed.com/platforms/ublox-C030-R410M/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `ublox_c030_r410m` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:ublox_c030_r410m]
platform = ststm32
board = ublox_c030_r410m
```

To override a setting of the board manifest [ublox_c030_r410m.json](https://github.com/platformio/platform-ststm32/blob/master/boards/ublox_c030_r410m.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:ublox_c030_r410m]
platform = ststm32
board = ublox_c030_r410m

; change microcontroller
board_build.mcu = stm32f437vg

; change MCU frequency
board_build.f_cpu = 180000000L
```

## Uploading

u-blox C030-R410M IoT supports these upload protocols:

- `blackmagic`
- `jlink`
- `stlink`

The default is `stlink`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:ublox_c030_r410m]
platform = ststm32
board = ublox_c030_r410m

upload_protocol = stlink
```

## Debugging

The u-blox C030-R410M IoT has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

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
| [STM32Cube](../../frameworks/stm32cube.mdx) | STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency |
