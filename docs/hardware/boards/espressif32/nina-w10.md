---
title: "u-blox NINA-W10 series"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-espressif32-nina-w10"></a>

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

Please use `nina_w10` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:nina_w10]
platform = espressif32
board = nina_w10
```

You can override default u-blox NINA-W10 series settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [nina_w10.json](https://github.com/platformio/platform-espressif32/blob/master/boards/nina_w10.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

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

u-blox NINA-W10 series supports the following uploading protocols:

- `espota`
- `esptool`

Default protocol is `esptool`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:nina_w10]
platform = espressif32
board = nina_w10

upload_protocol = esptool
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support u-blox NINA-W10 series board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [Espressif IoT Development Framework](../../frameworks/espidf.mdx) | Espressif IoT Development Framework. Official development framework for ESP32 chip |
