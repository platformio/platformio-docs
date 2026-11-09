---
title: "4D Systems gen4 IoD Range"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "4D Systems gen4 IoD Range (ESP8266, 80MHz, 512KB flash, 80KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-espressif8266-gen4iod"></a>

# 4D Systems gen4 IoD Range

## Hardware

Platform [Espressif 8266](../../platforms/espressif8266.mdx): ESP8266 is a cost-effective and highly integrated Wi-Fi MCU with built-in TCP/IP networking software for IoT applications. ESP8266 integrates an enhanced version of Tensilica’s L106 Diamond series 32-bit processor and on-chip SRAM.

| Specification | Value |
|---|---|
| **Microcontroller** | ESP8266 |
| **Frequency** | 80MHz |
| **Flash** | 512KB |
| **RAM** | 80KB |
| **Vendor** | [4D Systems](http://www.4dsystems.com.au/product/gen4_IoD/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `gen4iod` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:gen4iod]
platform = espressif8266
board = gen4iod
```

To override a setting of the board manifest [gen4iod.json](https://github.com/platformio/platform-espressif8266/blob/master/boards/gen4iod.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:gen4iod]
platform = espressif8266
board = gen4iod

; change microcontroller
board_build.mcu = esp8266

; change MCU frequency
board_build.f_cpu = 80000000L
```

## Uploading

4D Systems gen4 IoD Range supports these upload protocols:

- `espota`
- `esptool`

The default is `esptool`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:gen4iod]
platform = espressif8266
board = gen4iod

upload_protocol = esptool
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the 4D Systems gen4 IoD Range yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [ESP8266 Non-OS SDK](../../frameworks/esp8266-nonos-sdk.md) | Espressif ESP8266 Non-OS SDK |
| [ESP8266 RTOS SDK](../../frameworks/esp8266-rtos-sdk.md) | Espressif ESP8266 SDK based on FreeRTOS |
