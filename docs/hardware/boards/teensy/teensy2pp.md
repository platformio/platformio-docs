---
title: "Teensy++ 2.0"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Teensy++ 2.0 (AT90USB1286, 16MHz, 127KB flash, 8KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-teensy-teensy2pp"></a>

# Teensy++ 2.0

## Hardware

Platform [Teensy](../../platforms/teensy.mdx): Teensy is a complete USB-based microcontroller development system, in a very small footprint, capable of implementing many types of projects. All programming is done via the USB port. No special programmer is needed, only a standard USB cable and a PC or Macintosh with a USB port.

| Specification | Value |
|---|---|
| **Microcontroller** | AT90USB1286 |
| **Frequency** | 16MHz |
| **Flash** | 127KB |
| **RAM** | 8KB |
| **Vendor** | [Teensy](https://www.pjrc.com/store/teensypp.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `teensy2pp` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:teensy2pp]
platform = teensy
board = teensy2pp
```

To override a setting of the board manifest [teensy2pp.json](https://github.com/platformio/platform-teensy/blob/master/boards/teensy2pp.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:teensy2pp]
platform = teensy
board = teensy2pp

; change microcontroller
board_build.mcu = at90usb1286

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Uploading

Teensy++ 2.0 supports these upload protocols:

- `teensy-cli`
- `teensy-gui`

The default is `teensy-gui`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:teensy2pp]
platform = teensy
board = teensy2pp

upload_protocol = teensy-gui
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the Teensy++ 2.0 yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
