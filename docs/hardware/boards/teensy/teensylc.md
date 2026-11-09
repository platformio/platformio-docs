---
title: "Teensy LC"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-teensy-teensylc"></a>

# Teensy LC

## Hardware

Platform [Teensy](../../platforms/teensy.mdx): Teensy is a complete USB-based microcontroller development system, in a very small footprint, capable of implementing many types of projects. All programming is done via the USB port. No special programmer is needed, only a standard USB cable and a PC or Macintosh with a USB port.

| Specification | Value |
|---|---|
| **Microcontroller** | MKL26Z64 |
| **Frequency** | 48MHz |
| **Flash** | 62KB |
| **RAM** | 8KB |
| **Vendor** | [Teensy](http://www.pjrc.com/teensy/teensyLC.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `teensylc` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:teensylc]
platform = teensy
board = teensylc
```

You can override default Teensy LC settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [teensylc.json](https://github.com/platformio/platform-teensy/blob/master/boards/teensylc.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:teensylc]
platform = teensy
board = teensylc

; change microcontroller
board_build.mcu = mkl26z64

; change MCU frequency
board_build.f_cpu = 48000000L
```

## Uploading

Teensy LC supports the following uploading protocols:

- `jlink`
- `teensy-cli`
- `teensy-gui`

Default protocol is `teensy-gui`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:teensylc]
platform = teensy
board = teensylc

upload_protocol = teensy-gui
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

Teensy LC does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

| Compatible Tools | On-board | Default |
|---|---|---|
| [J-LINK](../../debug-probes/jlink.md) |  | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
