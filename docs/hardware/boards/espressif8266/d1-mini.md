---
title: "WeMos D1 R2 and mini"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "WeMos D1 R2 and mini (ESP8266, 80MHz, 4MB flash, 80KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# WeMos D1 R2 and mini

## Hardware

Platform [Espressif 8266](../../platforms/espressif8266.mdx): ESP8266 is a cost-effective and highly integrated Wi-Fi MCU with built-in TCP/IP networking software for IoT applications. ESP8266 integrates an enhanced version of Tensilica’s L106 Diamond series 32-bit processor and on-chip SRAM.

| Specification | Value |
|---|---|
| **Microcontroller** | ESP8266 |
| **Frequency** | 80MHz |
| **Flash** | 4MB |
| **RAM** | 80KB |
| **Vendor** | [WEMOS](https://wiki.wemos.cc/products:d1:d1_mini?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `d1_mini` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:d1_mini]
platform = espressif8266
board = d1_mini
```

To override a setting of the board manifest [d1_mini.json](https://github.com/platformio/platform-espressif8266/blob/master/boards/d1_mini.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:d1_mini]
platform = espressif8266
board = d1_mini

; change microcontroller
board_build.mcu = esp8266

; change MCU frequency
board_build.f_cpu = 80000000L
```

## Uploading

WeMos D1 R2 and mini supports these upload protocols:

- `espota`
- `esptool`

The default is `esptool`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:d1_mini]
platform = espressif8266
board = d1_mini

upload_protocol = esptool
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the WeMos D1 R2 and mini yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [ESP8266 Non-OS SDK](../../frameworks/esp8266-nonos-sdk.md) | Espressif ESP8266 Non-OS SDK |
| [ESP8266 RTOS SDK](../../frameworks/esp8266-rtos-sdk.md) | Espressif ESP8266 SDK based on FreeRTOS |
