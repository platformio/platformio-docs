---
title: "RedBearLab BLE Nano 1.5"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "RedBearLab BLE Nano 1.5 (NRF51822, 16MHz, 256KB flash, 32KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-nordicnrf51-redbearlabblenano"></a>

# RedBearLab BLE Nano 1.5

## Hardware

Platform [Nordic nRF51](../../platforms/nordicnrf51.md): The Nordic nRF51 Series is a family of highly flexible, multi-protocol, system-on-chip (SoC) devices for ultra-low power wireless applications. nRF51 Series devices support a range of protocol stacks including Bluetooth Smart (previously called Bluetooth low energy), ANT and proprietary 2.4GHz protocols such as Gazell.

| Specification | Value |
|---|---|
| **Microcontroller** | NRF51822 |
| **Frequency** | 16MHz |
| **Flash** | 256KB |
| **RAM** | 32KB |
| **Vendor** | [RedBearLab](https://www.sparkfun.com/products/retired/13730?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `redBearLabBLENano` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:redBearLabBLENano]
platform = nordicnrf51
board = redBearLabBLENano
```

To override a setting of the board manifest [redBearLabBLENano.json](https://github.com/platformio/platform-nordicnrf51/blob/master/boards/redBearLabBLENano.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:redBearLabBLENano]
platform = nordicnrf51
board = redBearLabBLENano

; change microcontroller
board_build.mcu = nrf51822

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Uploading

RedBearLab BLE Nano 1.5 supports these upload protocols:

- `blackmagic`
- `cmsis-dap`
- `jlink`
- `nrfjprog`
- `stlink`

The default is `cmsis-dap`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:redBearLabBLENano]
platform = nordicnrf51
board = redBearLabBLENano

upload_protocol = cmsis-dap
```

## Debugging

The RedBearLab BLE Nano 1.5 has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [Black magic probe](../../debug-probes/blackmagic.md) |  |  |
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) | Yes | Yes |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [ST-LINK](../../debug-probes/stlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
