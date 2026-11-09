---
title: "Espressif ESP32-C6-DevKitC-1"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Espressif ESP32-C6-DevKitC-1 (ESP32C6, 160MHz, 8MB flash, 320KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Espressif ESP32-C6-DevKitC-1

## Hardware

Platform [Espressif 32](../../platforms/espressif32.mdx): ESP32 is a series of low-cost, low-power system on a chip microcontrollers with integrated Wi-Fi and Bluetooth. ESP32 integrates an antenna switch, RF balun, power amplifier, low-noise receive amplifier, filters, and power management modules.

| Specification | Value |
|---|---|
| **Microcontroller** | ESP32C6 |
| **Frequency** | 160MHz |
| **Flash** | 8MB |
| **RAM** | 320KB |
| **Vendor** | [Espressif](https://docs.espressif.com/projects/espressif-esp-dev-kits/en/latest/esp32c6/esp32-c6-devkitc-1/index.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `esp32-c6-devkitc-1` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:esp32-c6-devkitc-1]
platform = espressif32
board = esp32-c6-devkitc-1
```

To override a setting of the board manifest [esp32-c6-devkitc-1.json](https://github.com/platformio/platform-espressif32/blob/master/boards/esp32-c6-devkitc-1.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:esp32-c6-devkitc-1]
platform = espressif32
board = esp32-c6-devkitc-1

; change microcontroller
board_build.mcu = esp32c6

; change MCU frequency
board_build.f_cpu = 160000000L
```

## Uploading

Espressif ESP32-C6-DevKitC-1 supports these upload protocols:

- `espota`
- `esptool`

The default is `esptool`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:esp32-c6-devkitc-1]
platform = espressif32
board = esp32-c6-devkitc-1

upload_protocol = esptool
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the Espressif ESP32-C6-DevKitC-1 yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [Espressif IoT Development Framework](../../frameworks/espidf.mdx) | Espressif IoT Development Framework. Official development framework for ESP32 chip |
