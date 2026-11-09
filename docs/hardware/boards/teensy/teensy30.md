---
title: "Teensy 3.0"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-teensy-teensy30"></a>

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

Please use `teensy30` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:teensy30]
platform = teensy
board = teensy30
```

You can override default Teensy 3.0 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [teensy30.json](https://github.com/platformio/platform-teensy/blob/master/boards/teensy30.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

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

Teensy 3.0 supports the following uploading protocols:

- `teensy-cli`
- `teensy-gui`

Default protocol is `teensy-gui`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:teensy30]
platform = teensy
board = teensy30

upload_protocol = teensy-gui
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support Teensy 3.0 board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
