---
title: "Teensy 4.0"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Teensy 4.0 (IMXRT1062, 600MHz, 1.94MB flash, 512KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Teensy 4.0

## Hardware

Platform [Teensy](../../platforms/teensy.mdx): Teensy is a complete USB-based microcontroller development system, in a very small footprint, capable of implementing many types of projects. All programming is done via the USB port. No special programmer is needed, only a standard USB cable and a PC or Macintosh with a USB port.

| Specification | Value |
|---|---|
| **Microcontroller** | IMXRT1062 |
| **Frequency** | 600MHz |
| **Flash** | 1.94MB |
| **RAM** | 512KB |
| **Vendor** | [Teensy](https://www.pjrc.com/store/teensy40.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `teensy40` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:teensy40]
platform = teensy
board = teensy40
```

To override a setting of the board manifest [teensy40.json](https://github.com/platformio/platform-teensy/blob/master/boards/teensy40.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:teensy40]
platform = teensy
board = teensy40

; change microcontroller
board_build.mcu = imxrt1062

; change MCU frequency
board_build.f_cpu = 600000000L
```

## Uploading

Teensy 4.0 supports these upload protocols:

- `jlink`
- `teensy-cli`
- `teensy-gui`

The default is `teensy-gui`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:teensy40]
platform = teensy
board = teensy40

upload_protocol = teensy-gui
```

## Debugging

The Teensy 4.0 has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

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
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
