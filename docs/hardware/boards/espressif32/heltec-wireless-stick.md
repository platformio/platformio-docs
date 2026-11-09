---
title: "Heltec Wireless Stick"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Heltec Wireless Stick (ESP32, 240MHz, 8MB flash, 320KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Heltec Wireless Stick

## Hardware

Platform [Espressif 32](../../platforms/espressif32.mdx): ESP32 is a series of low-cost, low-power system on a chip microcontrollers with integrated Wi-Fi and Bluetooth. ESP32 integrates an antenna switch, RF balun, power amplifier, low-noise receive amplifier, filters, and power management modules.

| Specification | Value |
|---|---|
| **Microcontroller** | ESP32 |
| **Frequency** | 240MHz |
| **Flash** | 8MB |
| **RAM** | 320KB |
| **Vendor** | [Heltec Automation](http://www.heltec.cn/project/wireless-stick/?lang=en&utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `heltec_wireless_stick` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:heltec_wireless_stick]
platform = espressif32
board = heltec_wireless_stick
```

To override a setting of the board manifest [heltec_wireless_stick.json](https://github.com/platformio/platform-espressif32/blob/master/boards/heltec_wireless_stick.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:heltec_wireless_stick]
platform = espressif32
board = heltec_wireless_stick

; change microcontroller
board_build.mcu = esp32

; change MCU frequency
board_build.f_cpu = 240000000L
```

## Uploading

Heltec Wireless Stick supports these upload protocols:

- `cmsis-dap`
- `esp-bridge`
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

The default is `esptool`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:heltec_wireless_stick]
platform = espressif32
board = heltec_wireless_stick

upload_protocol = esptool
```

## Debugging

The Heltec Wireless Stick has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) |  | Yes |
| `esp-bridge` |  |  |
| [ESP-Prog](../../debug-probes/esp-prog.md) |  |  |
| [oddWires IOT-Bus JTAG](../../debug-probes/iot-bus-jtag.md) |  |  |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [Mini-Module FT2232H](../../debug-probes/minimodule.md) |  |  |
| [Olimex ARM-USB-OCD](../../debug-probes/olimex-arm-usb-ocd.md) |  |  |
| [Olimex ARM-USB-OCD-H](../../debug-probes/olimex-arm-usb-ocd-h.md) |  |  |
| [Olimex ARM-USB-TINY-H](../../debug-probes/olimex-arm-usb-tiny-h.md) |  |  |
| [Olimex ARM-USB-TINY](../../debug-probes/olimex-jtag-tiny.md) |  |  |
| [TIAO USB Multi-Protocol adapter (TUMPA)](../../debug-probes/tumpa.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [Espressif IoT Development Framework](../../frameworks/espidf.mdx) | Espressif IoT Development Framework. Official development framework for ESP32 chip |
