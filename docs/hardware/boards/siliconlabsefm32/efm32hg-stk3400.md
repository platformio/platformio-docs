---
title: "SLSTK3400A USB-enabled Happy Gecko"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "SLSTK3400A USB-enabled Happy Gecko (EFM32HG322F64, 25MHz, 64KB flash, 8KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# SLSTK3400A USB-enabled Happy Gecko

## Hardware

Platform [Silicon Labs EFM32](../../platforms/siliconlabsefm32.md): Silicon Labs EFM32 Gecko 32-bit microcontroller (MCU) family includes devices that offer flash memory configurations up to 256 kB, 32 kB of RAM and CPU speeds up to 48 MHz. Based on the powerful ARM Cortex-M core, the Gecko family features innovative low energy techniques, short wake-up time from energy saving modes and a wide selection of peripherals, making it ideal for battery operated applications and other systems requiring high performance and low-energy consumption.

| Specification | Value |
|---|---|
| **Microcontroller** | EFM32HG322F64 |
| **Frequency** | 25MHz |
| **Flash** | 64KB |
| **RAM** | 8KB |
| **Vendor** | [Silicon Labs](https://www.silabs.com/products/development-tools/mcu/32-bit/efm32-happy-gecko-starter-kit?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `efm32hg_stk3400` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:efm32hg_stk3400]
platform = siliconlabsefm32
board = efm32hg_stk3400
```

To override a setting of the board manifest [efm32hg_stk3400.json](https://github.com/platformio/platform-siliconlabsefm32/blob/master/boards/efm32hg_stk3400.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:efm32hg_stk3400]
platform = siliconlabsefm32
board = efm32hg_stk3400

; change microcontroller
board_build.mcu = efm32hg322f64

; change MCU frequency
board_build.f_cpu = 25000000L
```

## Uploading

SLSTK3400A USB-enabled Happy Gecko supports these upload protocols:

- `blackmagic`
- `jlink`
- `mbed`

The default is `mbed`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:efm32hg_stk3400]
platform = siliconlabsefm32
board = efm32hg_stk3400

upload_protocol = mbed
```

## Debugging

The SLSTK3400A USB-enabled Happy Gecko has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [Black magic probe](../../debug-probes/blackmagic.md) |  |  |
| [J-LINK](../../debug-probes/jlink.md) | Yes | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
