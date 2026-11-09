---
title: "ProtoCentral HealthyPi 4"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-espressif32-healthypi4"></a>

# ProtoCentral HealthyPi 4

## Hardware

Platform [Espressif 32](../../platforms/espressif32.mdx): ESP32 is a series of low-cost, low-power system on a chip microcontrollers with integrated Wi-Fi and Bluetooth. ESP32 integrates an antenna switch, RF balun, power amplifier, low-noise receive amplifier, filters, and power management modules.

| Specification | Value |
|---|---|
| **Microcontroller** | ESP32 |
| **Frequency** | 240MHz |
| **Flash** | 4MB |
| **RAM** | 320KB |
| **Vendor** | [ProtoCentral](https://healthypi.protocentral.com?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `healthypi4` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:healthypi4]
platform = espressif32
board = healthypi4
```

You can override default ProtoCentral HealthyPi 4 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [healthypi4.json](https://github.com/platformio/platform-espressif32/blob/master/boards/healthypi4.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:healthypi4]
platform = espressif32
board = healthypi4

; change microcontroller
board_build.mcu = esp32

; change MCU frequency
board_build.f_cpu = 240000000L
```

## Uploading

ProtoCentral HealthyPi 4 supports the following uploading protocols:

- `espota`
- `esptool`

Default protocol is `esptool`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:healthypi4]
platform = espressif32
board = healthypi4

upload_protocol = esptool
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support ProtoCentral HealthyPi 4 board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [Espressif IoT Development Framework](../../frameworks/espidf.mdx) | Espressif IoT Development Framework. Official development framework for ESP32 chip |
