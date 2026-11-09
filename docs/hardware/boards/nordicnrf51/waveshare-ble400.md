---
title: "Waveshare BLE400"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Waveshare BLE400 (NRF51822, 32MHz, 256KB flash, 32KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Waveshare BLE400

## Hardware

Platform [Nordic nRF51](../../platforms/nordicnrf51.md): The Nordic nRF51 Series is a family of highly flexible, multi-protocol, system-on-chip (SoC) devices for ultra-low power wireless applications. nRF51 Series devices support a range of protocol stacks including Bluetooth Smart (previously called Bluetooth low energy), ANT and proprietary 2.4GHz protocols such as Gazell.

| Specification | Value |
|---|---|
| **Microcontroller** | NRF51822 |
| **Frequency** | 32MHz |
| **Flash** | 256KB |
| **RAM** | 32KB |
| **Vendor** | [Waveshare](http://www.waveshare.com/wiki/BLE400?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `waveshare_ble400` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:waveshare_ble400]
platform = nordicnrf51
board = waveshare_ble400
```

To override a setting of the board manifest [waveshare_ble400.json](https://github.com/platformio/platform-nordicnrf51/blob/master/boards/waveshare_ble400.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:waveshare_ble400]
platform = nordicnrf51
board = waveshare_ble400

; change microcontroller
board_build.mcu = nrf51822

; change MCU frequency
board_build.f_cpu = 32000000L
```

## Uploading

Waveshare BLE400 supports these upload protocols:

- `blackmagic`
- `jlink`
- `nrfjprog`
- `stlink`

The default is `jlink`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:waveshare_ble400]
platform = nordicnrf51
board = waveshare_ble400

upload_protocol = jlink
```

## Debugging

The Waveshare BLE400 has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [Black magic probe](../../debug-probes/blackmagic.md) |  | Yes |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [ST-LINK](../../debug-probes/stlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
