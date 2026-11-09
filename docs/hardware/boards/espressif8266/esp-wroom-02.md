---
title: "Espressif ESP-WROOM-02"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Espressif ESP-WROOM-02 (ESP8266, 80MHz, 2MB flash, 80KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-espressif8266-esp-wroom-02"></a>

# Espressif ESP-WROOM-02

## Hardware

Platform [Espressif 8266](../../platforms/espressif8266.mdx): ESP8266 is a cost-effective and highly integrated Wi-Fi MCU with built-in TCP/IP networking software for IoT applications. ESP8266 integrates an enhanced version of Tensilica’s L106 Diamond series 32-bit processor and on-chip SRAM.

| Specification | Value |
|---|---|
| **Microcontroller** | ESP8266 |
| **Frequency** | 80MHz |
| **Flash** | 2MB |
| **RAM** | 80KB |
| **Vendor** | [Espressif](http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family&utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `esp_wroom_02` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:esp_wroom_02]
platform = espressif8266
board = esp_wroom_02
```

To override a setting of the board manifest [esp_wroom_02.json](https://github.com/platformio/platform-espressif8266/blob/master/boards/esp_wroom_02.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:esp_wroom_02]
platform = espressif8266
board = esp_wroom_02

; change microcontroller
board_build.mcu = esp8266

; change MCU frequency
board_build.f_cpu = 80000000L
```

## Uploading

Espressif ESP-WROOM-02 supports these upload protocols:

- `espota`
- `esptool`

The default is `esptool`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:esp_wroom_02]
platform = espressif8266
board = esp_wroom_02

upload_protocol = esptool
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the Espressif ESP-WROOM-02 yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [ESP8266 Non-OS SDK](../../frameworks/esp8266-nonos-sdk.md) | Espressif ESP8266 Non-OS SDK |
| [ESP8266 RTOS SDK](../../frameworks/esp8266-rtos-sdk.md) | Espressif ESP8266 SDK based on FreeRTOS |
