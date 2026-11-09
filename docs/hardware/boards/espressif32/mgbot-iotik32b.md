---
title: "MGBOT IOTIK 32B"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "MGBOT IOTIK 32B (ESP32, 240MHz, 4MB flash, 320KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-espressif32-mgbot-iotik32b"></a>

# MGBOT IOTIK 32B

## Hardware

Platform [Espressif 32](../../platforms/espressif32.mdx): ESP32 is a series of low-cost, low-power system on a chip microcontrollers with integrated Wi-Fi and Bluetooth. ESP32 integrates an antenna switch, RF balun, power amplifier, low-noise receive amplifier, filters, and power management modules.

| Specification | Value |
|---|---|
| **Microcontroller** | ESP32 |
| **Frequency** | 240MHz |
| **Flash** | 4MB |
| **RAM** | 320KB |
| **Vendor** | [MGBOT](http://iotik.ru/en/iotik32b/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `mgbot-iotik32b` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:mgbot-iotik32b]
platform = espressif32
board = mgbot-iotik32b
```

To override a setting of the board manifest [mgbot-iotik32b.json](https://github.com/platformio/platform-espressif32/blob/master/boards/mgbot-iotik32b.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:mgbot-iotik32b]
platform = espressif32
board = mgbot-iotik32b

; change microcontroller
board_build.mcu = esp32

; change MCU frequency
board_build.f_cpu = 240000000L
```

## Uploading

MGBOT IOTIK 32B supports these upload protocols:

- `espota`
- `esptool`

The default is `esptool`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:mgbot-iotik32b]
platform = espressif32
board = mgbot-iotik32b

upload_protocol = esptool
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the MGBOT IOTIK 32B yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [Espressif IoT Development Framework](../../frameworks/espidf.mdx) | Espressif IoT Development Framework. Official development framework for ESP32 chip |
