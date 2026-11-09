---
title: "u-blox NINA-W10 series"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "u-blox NINA-W10 series (ESP32, 240MHz, 2MB flash, 320KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# u-blox NINA-W10 series

## Hardware

Platform [Espressif 32](../../platforms/espressif32.mdx): ESP32 is a series of low-cost, low-power system on a chip microcontrollers with integrated Wi-Fi and Bluetooth. ESP32 integrates an antenna switch, RF balun, power amplifier, low-noise receive amplifier, filters, and power management modules.

| Specification | Value |
|---|---|
| **Microcontroller** | ESP32 |
| **Frequency** | 240MHz |
| **Flash** | 2MB |
| **RAM** | 320KB |
| **Vendor** | [u-blox](https://www.u-blox.com/en/product/nina-w10-series?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `nina_w10` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:nina_w10]
platform = espressif32
board = nina_w10
```

To override a setting of the board manifest [nina_w10.json](https://github.com/platformio/platform-espressif32/blob/master/boards/nina_w10.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:nina_w10]
platform = espressif32
board = nina_w10

; change microcontroller
board_build.mcu = esp32

; change MCU frequency
board_build.f_cpu = 240000000L
```

## Uploading

u-blox NINA-W10 series supports these upload protocols:

- `espota`
- `esptool`

The default is `esptool`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:nina_w10]
platform = espressif32
board = nina_w10

upload_protocol = esptool
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the u-blox NINA-W10 series yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [Espressif IoT Development Framework](../../frameworks/espidf.mdx) | Espressif IoT Development Framework. Official development framework for ESP32 chip |
