---
title: "Teensy 3.0"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Teensy 3.0 (MK20DX128, 48MHz, 128KB flash, 16KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Teensy 3.0

## Hardware

Platform [Teensy](../../platforms/teensy.mdx): Teensy is a complete USB-based microcontroller development system, in a very small footprint, capable of implementing many types of projects. All programming is done via the USB port. No special programmer is needed, only a standard USB cable and a PC or Macintosh with a USB port.

| Specification | Value |
|---|---|
| **Microcontroller** | MK20DX128 |
| **Frequency** | 48MHz |
| **Flash** | 128KB |
| **RAM** | 16KB |
| **Vendor** | [Teensy](https://www.pjrc.com/store/teensy3.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `teensy30` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:teensy30]
platform = teensy
board = teensy30
```

To override a setting of the board manifest [teensy30.json](https://github.com/platformio/platform-teensy/blob/master/boards/teensy30.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:teensy30]
platform = teensy
board = teensy30

; change microcontroller
board_build.mcu = mk20dx128

; change MCU frequency
board_build.f_cpu = 48000000L
```

## Uploading

Teensy 3.0 supports these upload protocols:

- `teensy-cli`
- `teensy-gui`

The default is `teensy-gui`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:teensy30]
platform = teensy
board = teensy30

upload_protocol = teensy-gui
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the Teensy 3.0 yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
