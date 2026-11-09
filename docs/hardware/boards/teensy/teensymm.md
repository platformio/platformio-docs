---
title: "SparkFun MicroMod Teensy"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "SparkFun MicroMod Teensy (IMXRT1062, 600MHz, 7.75MB flash, 512KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# SparkFun MicroMod Teensy

## Hardware

Platform [Teensy](../../platforms/teensy.mdx): Teensy is a complete USB-based microcontroller development system, in a very small footprint, capable of implementing many types of projects. All programming is done via the USB port. No special programmer is needed, only a standard USB cable and a PC or Macintosh with a USB port.

| Specification | Value |
|---|---|
| **Microcontroller** | IMXRT1062 |
| **Frequency** | 600MHz |
| **Flash** | 7.75MB |
| **RAM** | 512KB |
| **Vendor** | [SparkFun](https://www.sparkfun.com/products/16402?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `teensymm` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:teensymm]
platform = teensy
board = teensymm
```

To override a setting of the board manifest [teensymm.json](https://github.com/platformio/platform-teensy/blob/master/boards/teensymm.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:teensymm]
platform = teensy
board = teensymm

; change microcontroller
board_build.mcu = imxrt1062

; change MCU frequency
board_build.f_cpu = 600000000L
```

## Uploading

SparkFun MicroMod Teensy supports these upload protocols:

- `jlink`
- `teensy-cli`
- `teensy-gui`

The default is `teensy-gui`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:teensymm]
platform = teensy
board = teensymm

upload_protocol = teensy-gui
```

## Debugging

The SparkFun MicroMod Teensy has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

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
