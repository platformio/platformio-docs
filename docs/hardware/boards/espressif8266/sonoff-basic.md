---
title: "Sonoff Basic"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-espressif8266-sonoff-basic"></a>

# Sonoff Basic

## Hardware

Platform [Espressif 8266](../../platforms/espressif8266.mdx): ESP8266 is a cost-effective and highly integrated Wi-Fi MCU with built-in TCP/IP networking software for IoT applications. ESP8266 integrates an enhanced version of Tensilica’s L106 Diamond series 32-bit processor and on-chip SRAM.

| Specification | Value |
|---|---|
| **Microcontroller** | ESP8266 |
| **Frequency** | 80MHz |
| **Flash** | 1MB |
| **RAM** | 80KB |
| **Vendor** | [ITEAD](https://www.itead.cc/sonoff-wifi-wireless-switch.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `sonoff_basic` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:sonoff_basic]
platform = espressif8266
board = sonoff_basic
```

You can override default Sonoff Basic settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [sonoff_basic.json](https://github.com/platformio/platform-espressif8266/blob/master/boards/sonoff_basic.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:sonoff_basic]
platform = espressif8266
board = sonoff_basic

; change microcontroller
board_build.mcu = esp8266

; change MCU frequency
board_build.f_cpu = 80000000L
```

## Uploading

Sonoff Basic supports the following uploading protocols:

- `espota`
- `esptool`

Default protocol is `esptool`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:sonoff_basic]
platform = espressif8266
board = sonoff_basic

upload_protocol = esptool
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support Sonoff Basic board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [ESP8266 Non-OS SDK](../../frameworks/esp8266-nonos-sdk.md) | Espressif ESP8266 Non-OS SDK |
| [ESP8266 RTOS SDK](../../frameworks/esp8266-rtos-sdk.md) | Espressif ESP8266 SDK based on FreeRTOS |
