---
title: "Teensy 3.1 / 3.2"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-teensy-teensy31"></a>

# Teensy 3.1 / 3.2

## Hardware

Platform [Teensy](../../platforms/teensy.mdx): Teensy is a complete USB-based microcontroller development system, in a very small footprint, capable of implementing many types of projects. All programming is done via the USB port. No special programmer is needed, only a standard USB cable and a PC or Macintosh with a USB port.

| Specification | Value |
|---|---|
| **Microcontroller** | MK20DX256 |
| **Frequency** | 72MHz |
| **Flash** | 256KB |
| **RAM** | 64KB |
| **Vendor** | [Teensy](https://www.pjrc.com/store/teensy31.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `teensy31` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:teensy31]
platform = teensy
board = teensy31
```

You can override default Teensy 3.1 / 3.2 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [teensy31.json](https://github.com/platformio/platform-teensy/blob/master/boards/teensy31.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:teensy31]
platform = teensy
board = teensy31

; change microcontroller
board_build.mcu = mk20dx256

; change MCU frequency
board_build.f_cpu = 72000000L
```

## Uploading

Teensy 3.1 / 3.2 supports the following uploading protocols:

- `jlink`
- `teensy-cli`
- `teensy-gui`

Default protocol is `teensy-gui`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:teensy31]
platform = teensy
board = teensy31

upload_protocol = teensy-gui
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

Teensy 3.1 / 3.2 does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

| Compatible Tools | On-board | Default |
|---|---|---|
| [J-LINK](../../debug-probes/jlink.md) |  | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
