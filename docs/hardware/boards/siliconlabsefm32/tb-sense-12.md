---
title: "Thunderboard Sense 2 Sensor-to-Cloud Advanced IoT"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Thunderboard Sense 2 Sensor-to-Cloud Advanced IoT (EFR32MG12P432F1024, 40MHz, 1MB flash, 256KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-siliconlabsefm32-tb-sense-12"></a>

# Thunderboard Sense 2 Sensor-to-Cloud Advanced IoT

## Hardware

Platform [Silicon Labs EFM32](../../platforms/siliconlabsefm32.md): Silicon Labs EFM32 Gecko 32-bit microcontroller (MCU) family includes devices that offer flash memory configurations up to 256 kB, 32 kB of RAM and CPU speeds up to 48 MHz. Based on the powerful ARM Cortex-M core, the Gecko family features innovative low energy techniques, short wake-up time from energy saving modes and a wide selection of peripherals, making it ideal for battery operated applications and other systems requiring high performance and low-energy consumption.

| Specification | Value |
|---|---|
| **Microcontroller** | EFR32MG12P432F1024 |
| **Frequency** | 40MHz |
| **Flash** | 1MB |
| **RAM** | 256KB |
| **Vendor** | [Silicon Labs](https://www.silabs.com/products/development-tools/thunderboard/thunderboard-sense-two-kit?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `tb_sense_12` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:tb_sense_12]
platform = siliconlabsefm32
board = tb_sense_12
```

To override a setting of the board manifest [tb_sense_12.json](https://github.com/platformio/platform-siliconlabsefm32/blob/master/boards/tb_sense_12.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:tb_sense_12]
platform = siliconlabsefm32
board = tb_sense_12

; change microcontroller
board_build.mcu = EFR32MG12P432F1024

; change MCU frequency
board_build.f_cpu = 40000000L
```

## Uploading

Thunderboard Sense 2 Sensor-to-Cloud Advanced IoT supports these upload protocols:

- `blackmagic`
- `jlink`
- `mbed`

The default is `mbed`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:tb_sense_12]
platform = siliconlabsefm32
board = tb_sense_12

upload_protocol = mbed
```

## Debugging

The Thunderboard Sense 2 Sensor-to-Cloud Advanced IoT has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

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
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
