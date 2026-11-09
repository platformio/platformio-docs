---
title: "Teensy 3.1 / 3.2"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Teensy 3.1 / 3.2 (MK20DX256, 72MHz, 256KB flash, 64KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

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

Use the board ID `teensy31` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:teensy31]
platform = teensy
board = teensy31
```

To override a setting of the board manifest [teensy31.json](https://github.com/platformio/platform-teensy/blob/master/boards/teensy31.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

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

Teensy 3.1 / 3.2 supports these upload protocols:

- `jlink`
- `teensy-cli`
- `teensy-gui`

The default is `teensy-gui`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:teensy31]
platform = teensy
board = teensy31

upload_protocol = teensy-gui
```

## Debugging

The Teensy 3.1 / 3.2 has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

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
