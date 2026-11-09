---
title: "Schirmilabs Eduino WiFi"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-espressif8266-eduinowifi"></a>

# Schirmilabs Eduino WiFi

## Hardware

Platform [Espressif 8266](../../platforms/espressif8266.mdx): ESP8266 is a cost-effective and highly integrated Wi-Fi MCU with built-in TCP/IP networking software for IoT applications. ESP8266 integrates an enhanced version of Tensilica’s L106 Diamond series 32-bit processor and on-chip SRAM.

| Specification | Value |
|---|---|
| **Microcontroller** | ESP8266 |
| **Frequency** | 80MHz |
| **Flash** | 4MB |
| **RAM** | 80KB |
| **Vendor** | [Schirmilabs](https://github.com/schirmilabs/Eduino-WiFi?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `eduinowifi` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:eduinowifi]
platform = espressif8266
board = eduinowifi
```

You can override default Schirmilabs Eduino WiFi settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [eduinowifi.json](https://github.com/platformio/platform-espressif8266/blob/master/boards/eduinowifi.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:eduinowifi]
platform = espressif8266
board = eduinowifi

; change microcontroller
board_build.mcu = esp8266

; change MCU frequency
board_build.f_cpu = 80000000L
```

## Uploading

Schirmilabs Eduino WiFi supports the following uploading protocols:

- `espota`
- `esptool`

Default protocol is `esptool`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:eduinowifi]
platform = espressif8266
board = eduinowifi

upload_protocol = esptool
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support Schirmilabs Eduino WiFi board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [ESP8266 Non-OS SDK](../../frameworks/esp8266-nonos-sdk.md) | Espressif ESP8266 Non-OS SDK |
| [ESP8266 RTOS SDK](../../frameworks/esp8266-rtos-sdk.md) | Espressif ESP8266 SDK based on FreeRTOS |
