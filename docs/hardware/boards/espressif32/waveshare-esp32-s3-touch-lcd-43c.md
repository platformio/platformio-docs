---
title: "Waveshare ESP32-S3-Touch-LCD-4.3C"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-espressif32-waveshare-esp32-s3-touch-lcd-43c"></a>

# Waveshare ESP32-S3-Touch-LCD-4.3C

## Hardware

Platform [Espressif 32](../../platforms/espressif32.mdx): ESP32 is a series of low-cost, low-power system on a chip microcontrollers with integrated Wi-Fi and Bluetooth. ESP32 integrates an antenna switch, RF balun, power amplifier, low-noise receive amplifier, filters, and power management modules.

| Specification | Value |
|---|---|
| **Microcontroller** | ESP32S3 |
| **Frequency** | 240MHz |
| **Flash** | 16MB |
| **RAM** | 320KB |
| **Vendor** | [Waveshare](https://www.waveshare.com/esp32-s3-touch-lcd-4.3c.htm?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `waveshare_esp32_s3_touch_lcd_43C` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:waveshare_esp32_s3_touch_lcd_43C]
platform = espressif32
board = waveshare_esp32_s3_touch_lcd_43C
```

You can override default Waveshare ESP32-S3-Touch-LCD-4.3C settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [waveshare_esp32_s3_touch_lcd_43C.json](https://github.com/platformio/platform-espressif32/blob/master/boards/waveshare_esp32_s3_touch_lcd_43C.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:waveshare_esp32_s3_touch_lcd_43C]
platform = espressif32
board = waveshare_esp32_s3_touch_lcd_43C

; change microcontroller
board_build.mcu = esp32s3

; change MCU frequency
board_build.f_cpu = 240000000L
```

## Uploading

Waveshare ESP32-S3-Touch-LCD-4.3C supports the following uploading protocols:

- `cmsis-dap`
- `esp-bridge`
- `esp-builtin`
- `esp-prog`
- `espota`
- `esptool`
- `iot-bus-jtag`
- `jlink`
- `minimodule`
- `olimex-arm-usb-ocd`
- `olimex-arm-usb-ocd-h`
- `olimex-arm-usb-tiny-h`
- `olimex-jtag-tiny`
- `tumpa`

Default protocol is `esptool`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:waveshare_esp32_s3_touch_lcd_43C]
platform = espressif32
board = waveshare_esp32_s3_touch_lcd_43C

upload_protocol = esptool
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

Waveshare ESP32-S3-Touch-LCD-4.3C does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

| Compatible Tools | On-board | Default |
|---|---|---|
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) |  | Yes |
| `esp-bridge` |  |  |
| `esp-builtin` |  |  |
| [ESP-Prog](../../debug-probes/esp-prog.md) |  |  |
| [oddWires IOT-Bus JTAG](../../debug-probes/iot-bus-jtag.md) |  |  |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [Mini-Module FT2232H](../../debug-probes/minimodule.md) |  |  |
| [Olimex ARM-USB-OCD](../../debug-probes/olimex-arm-usb-ocd.md) |  |  |
| [Olimex ARM-USB-OCD-H](../../debug-probes/olimex-arm-usb-ocd-h.md) |  |  |
| [Olimex ARM-USB-TINY-H](../../debug-probes/olimex-arm-usb-tiny-h.md) |  |  |
| [Olimex ARM-USB-TINY](../../debug-probes/olimex-jtag-tiny.md) |  |  |
| [TIAO USB Multi-Protocol Adapter (TUMPA)](../../debug-probes/tumpa.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [Espressif IoT Development Framework](../../frameworks/espidf.mdx) | Espressif IoT Development Framework. Official development framework for ESP32 chip |
