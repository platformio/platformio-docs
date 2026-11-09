---
title: "Maxim Health Sensor Platform"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Maxim Health Sensor Platform (MAX32620, 96MHz, 2MB flash, 256KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Maxim Health Sensor Platform

## Hardware

Platform [Maxim 32](../../platforms/maxim32.md): Maxim's microcontrollers provide low-power, efficient, and secure solutions for challenging embedded applications. Maxim's processors embed cutting-edge technologies to secure data and intellectual property, proven analog circuitry for real-world applications, and battery-conserving low power operation.

| Specification | Value |
|---|---|
| **Microcontroller** | MAX32620 |
| **Frequency** | 96MHz |
| **Flash** | 2MB |
| **RAM** | 256KB |
| **Vendor** | [Maxim](https://developer.mbed.org/platforms/MAX32620HSP/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `max32620hsp` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:max32620hsp]
platform = maxim32
board = max32620hsp
```

To override a setting of the board manifest [max32620hsp.json](https://github.com/platformio/platform-maxim32/blob/master/boards/max32620hsp.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:max32620hsp]
platform = maxim32
board = max32620hsp

; change microcontroller
board_build.mcu = max32620

; change MCU frequency
board_build.f_cpu = 96000000L
```

## Uploading

Maxim Health Sensor Platform supports these upload protocols:

- `jlink`
- `mbed`

The default is `mbed`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:max32620hsp]
platform = maxim32
board = max32620hsp

upload_protocol = mbed
```

## Debugging

The Maxim Health Sensor Platform has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

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
| [Mbed](../../frameworks/mbed.mdx) | Arm Mbed OS is a platform operating system designed for the internet of things |
