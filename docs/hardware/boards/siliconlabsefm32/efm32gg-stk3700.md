---
title: "EFM32GG-STK3700 Giant Gecko"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "EFM32GG-STK3700 Giant Gecko (EFM32GG990F1024, 48MHz, 1MB flash, 128KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# EFM32GG-STK3700 Giant Gecko

## Hardware

Platform [Silicon Labs EFM32](../../platforms/siliconlabsefm32.md): Silicon Labs EFM32 Gecko 32-bit microcontroller (MCU) family includes devices that offer flash memory configurations up to 256 kB, 32 kB of RAM and CPU speeds up to 48 MHz. Based on the powerful ARM Cortex-M core, the Gecko family features innovative low energy techniques, short wake-up time from energy saving modes and a wide selection of peripherals, making it ideal for battery operated applications and other systems requiring high performance and low-energy consumption.

| Specification | Value |
|---|---|
| **Microcontroller** | EFM32GG990F1024 |
| **Frequency** | 48MHz |
| **Flash** | 1MB |
| **RAM** | 128KB |
| **Vendor** | [Silicon Labs](https://www.silabs.com/products/development-tools/mcu/32-bit/efm32-giant-gecko-starter-kit?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `efm32gg_stk3700` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:efm32gg_stk3700]
platform = siliconlabsefm32
board = efm32gg_stk3700
```

To override a setting of the board manifest [efm32gg_stk3700.json](https://github.com/platformio/platform-siliconlabsefm32/blob/master/boards/efm32gg_stk3700.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:efm32gg_stk3700]
platform = siliconlabsefm32
board = efm32gg_stk3700

; change microcontroller
board_build.mcu = efm32gg990f1024

; change MCU frequency
board_build.f_cpu = 48000000L
```

## Uploading

EFM32GG-STK3700 Giant Gecko supports these upload protocols:

- `blackmagic`
- `jlink`
- `mbed`

The default is `mbed`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:efm32gg_stk3700]
platform = siliconlabsefm32
board = efm32gg_stk3700

upload_protocol = mbed
```

## Debugging

The EFM32GG-STK3700 Giant Gecko has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

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
| [Mbed](../../frameworks/mbed.mdx) | Arm Mbed OS is a platform operating system designed for the internet of things |
