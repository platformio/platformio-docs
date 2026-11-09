---
title: "WeMos D1 mini Lite"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
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

Please use `d1_mini_lite` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:d1_mini_lite]
platform = espressif8266
board = d1_mini_lite
```

You can override default WeMos D1 mini Lite settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [d1_mini_lite.json](https://github.com/platformio/platform-espressif8266/blob/master/boards/d1_mini_lite.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

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

WeMos D1 mini Lite supports the following uploading protocols:

- `espota`
- `esptool`

Default protocol is `esptool`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:d1_mini_lite]
platform = espressif8266
board = d1_mini_lite

upload_protocol = esptool
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support WeMos D1 mini Lite board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
