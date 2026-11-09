---
title: "RoboHeart Hercules"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-espressif32-roboheart-hercules"></a>

# RoboHeart Hercules

## Hardware

Platform [Espressif 32](../../platforms/espressif32.mdx): ESP32 is a series of low-cost, low-power system on a chip microcontrollers with integrated Wi-Fi and Bluetooth. ESP32 integrates an antenna switch, RF balun, power amplifier, low-noise receive amplifier, filters, and power management modules.

| Specification | Value |
|---|---|
| **Microcontroller** | ESP32 |
| **Frequency** | 240MHz |
| **Flash** | 4MB |
| **RAM** | 320KB |
| **Vendor** | [RoboHeart](https://roboheart.de/en_gb/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `roboheart_hercules` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:roboheart_hercules]
platform = espressif32
board = roboheart_hercules
```

You can override default RoboHeart Hercules settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [roboheart_hercules.json](https://github.com/platformio/platform-espressif32/blob/master/boards/roboheart_hercules.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:roboheart_hercules]
platform = espressif32
board = roboheart_hercules

; change microcontroller
board_build.mcu = esp32

; change MCU frequency
board_build.f_cpu = 240000000L
```

## Uploading

RoboHeart Hercules supports the following uploading protocols:

- `espota`
- `esptool`

Default protocol is `esptool`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:roboheart_hercules]
platform = espressif32
board = roboheart_hercules

upload_protocol = esptool
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support RoboHeart Hercules board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [Espressif IoT Development Framework](../../frameworks/espidf.mdx) | Espressif IoT Development Framework. Official development framework for ESP32 chip |
