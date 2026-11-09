---
title: "Teensy LC"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Teensy LC (MKL26Z64, 48MHz, 62KB flash, 8KB RAM): PlatformIO board ID, configuration, uploading and debugging."
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

Use the board ID `teensylc` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:teensylc]
platform = teensy
board = teensylc
```

To override a setting of the board manifest [teensylc.json](https://github.com/platformio/platform-teensy/blob/master/boards/teensylc.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

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

Teensy LC supports these upload protocols:

- `jlink`
- `teensy-cli`
- `teensy-gui`

The default is `teensy-gui`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:teensylc]
platform = teensy
board = teensylc

upload_protocol = teensy-gui
```

## Debugging

The Teensy LC has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [J-LINK](../../debug-probes/jlink.md) |  | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
