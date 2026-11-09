---
title: "WeMos D1 mini Lite"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "WeMos D1 mini Lite (ESP8266, 80MHz, 1MB flash, 80KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-espressif8266-d1-mini-lite"></a>

# WeMos D1 mini Lite

## Hardware

Platform [Espressif 8266](../../platforms/espressif8266.mdx): ESP8266 is a cost-effective and highly integrated Wi-Fi MCU with built-in TCP/IP networking software for IoT applications. ESP8266 integrates an enhanced version of Tensilica’s L106 Diamond series 32-bit processor and on-chip SRAM.

| Specification | Value |
|---|---|
| **Microcontroller** | ESP8266 |
| **Frequency** | 80MHz |
| **Flash** | 1MB |
| **RAM** | 80KB |
| **Vendor** | [WEMOS](https://wiki.wemos.cc/products:d1:d1_mini_lite?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `d1_mini_lite` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:d1_mini_lite]
platform = espressif8266
board = d1_mini_lite
```

To override a setting of the board manifest [d1_mini_lite.json](https://github.com/platformio/platform-espressif8266/blob/master/boards/d1_mini_lite.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:d1_mini_lite]
platform = espressif8266
board = d1_mini_lite

; change microcontroller
board_build.mcu = esp8266

; change MCU frequency
board_build.f_cpu = 80000000L
```

## Uploading

WeMos D1 mini Lite supports these upload protocols:

- `espota`
- `esptool`

The default is `esptool`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:d1_mini_lite]
platform = espressif8266
board = d1_mini_lite

upload_protocol = esptool
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the WeMos D1 mini Lite yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
