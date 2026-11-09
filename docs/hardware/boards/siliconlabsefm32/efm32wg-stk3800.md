---
title: "EFM32WG-STK3800 Wonder Gecko"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-siliconlabsefm32-efm32wg-stk3800"></a>

# EFM32WG-STK3800 Wonder Gecko

## Hardware

Platform [Silicon Labs EFM32](../../platforms/siliconlabsefm32.md): Silicon Labs EFM32 Gecko 32-bit microcontroller (MCU) family includes devices that offer flash memory configurations up to 256 kB, 32 kB of RAM and CPU speeds up to 48 MHz. Based on the powerful ARM Cortex-M core, the Gecko family features innovative low energy techniques, short wake-up time from energy saving modes and a wide selection of peripherals, making it ideal for battery operated applications and other systems requiring high performance and low-energy consumption.

| Specification | Value |
|---|---|
| **Microcontroller** | EFM32WG990F256 |
| **Frequency** | 48MHz |
| **Flash** | 256KB |
| **RAM** | 32KB |
| **Vendor** | [Silicon Labs](https://www.silabs.com/products/development-tools/mcu/32-bit/efm32-wonder-gecko-starter-kit?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `efm32wg_stk3800` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:efm32wg_stk3800]
platform = siliconlabsefm32
board = efm32wg_stk3800
```

You can override default EFM32WG-STK3800 Wonder Gecko settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [efm32wg_stk3800.json](https://github.com/platformio/platform-siliconlabsefm32/blob/master/boards/efm32wg_stk3800.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:efm32wg_stk3800]
platform = siliconlabsefm32
board = efm32wg_stk3800

; change microcontroller
board_build.mcu = efm32wg990f256

; change MCU frequency
board_build.f_cpu = 48000000L
```

## Uploading

EFM32WG-STK3800 Wonder Gecko supports the following uploading protocols:

- `blackmagic`
- `jlink`
- `mbed`

Default protocol is `mbed`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:efm32wg_stk3800]
platform = siliconlabsefm32
board = efm32wg_stk3800

upload_protocol = mbed
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

EFM32WG-STK3800 Wonder Gecko has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

| Compatible Tools | On-board | Default |
|---|---|---|
| [Black Magic Probe](../../debug-probes/blackmagic.md) |  |  |
| [J-LINK](../../debug-probes/jlink.md) | Yes | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
