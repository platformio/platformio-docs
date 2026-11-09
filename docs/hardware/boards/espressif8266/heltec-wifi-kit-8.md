---
title: "Heltec Wifi kit 8"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-espressif8266-heltec-wifi-kit-8"></a>

# Heltec Wifi kit 8

## Hardware

Platform [Espressif 8266](../../platforms/espressif8266.mdx): ESP8266 is a cost-effective and highly integrated Wi-Fi MCU with built-in TCP/IP networking software for IoT applications. ESP8266 integrates an enhanced version of Tensilica’s L106 Diamond series 32-bit processor and on-chip SRAM.

| Specification | Value |
|---|---|
| **Microcontroller** | ESP8266 |
| **Frequency** | 80MHz |
| **Flash** | 4MB |
| **RAM** | 80KB |
| **Vendor** | [Heltec](http://www.heltec.cn/project/wifi_kit_8/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `heltec_wifi_kit_8` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:heltec_wifi_kit_8]
platform = espressif8266
board = heltec_wifi_kit_8
```

You can override default Heltec Wifi kit 8 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [heltec_wifi_kit_8.json](https://github.com/platformio/platform-espressif8266/blob/master/boards/heltec_wifi_kit_8.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:heltec_wifi_kit_8]
platform = espressif8266
board = heltec_wifi_kit_8

; change microcontroller
board_build.mcu = esp8266

; change MCU frequency
board_build.f_cpu = 80000000L
```

## Uploading

Heltec Wifi kit 8 supports the following uploading protocols:

- `espota`
- `esptool`

Default protocol is `esptool`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:heltec_wifi_kit_8]
platform = espressif8266
board = heltec_wifi_kit_8

upload_protocol = esptool
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support Heltec Wifi kit 8 board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [ESP8266 Non-OS SDK](../../frameworks/esp8266-nonos-sdk.md) | Espressif ESP8266 Non-OS SDK |
| [ESP8266 RTOS SDK](../../frameworks/esp8266-rtos-sdk.md) | Espressif ESP8266 SDK based on FreeRTOS |
