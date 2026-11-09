---
title: "Maxim ARM mbed Enabled Development Platform for MAX32600"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Maxim ARM mbed Enabled Development Platform for MAX32600 (MAX32600, 24MHz, 256KB flash, 32KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-maxim32-max32600mbed"></a>

# Maxim ARM mbed Enabled Development Platform for MAX32600

## Hardware

Platform [Maxim 32](../../platforms/maxim32.md): Maxim's microcontrollers provide low-power, efficient, and secure solutions for challenging embedded applications. Maxim's processors embed cutting-edge technologies to secure data and intellectual property, proven analog circuitry for real-world applications, and battery-conserving low power operation.

| Specification | Value |
|---|---|
| **Microcontroller** | MAX32600 |
| **Frequency** | 24MHz |
| **Flash** | 256KB |
| **RAM** | 32KB |
| **Vendor** | [Maxim](https://developer.mbed.org/platforms/MAX32600mbed/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `max32600mbed` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:max32600mbed]
platform = maxim32
board = max32600mbed
```

To override a setting of the board manifest [max32600mbed.json](https://github.com/platformio/platform-maxim32/blob/master/boards/max32600mbed.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:max32600mbed]
platform = maxim32
board = max32600mbed

; change microcontroller
board_build.mcu = max32600

; change MCU frequency
board_build.f_cpu = 24000000L
```

## Uploading

Maxim ARM mbed Enabled Development Platform for MAX32600 supports these upload protocols:

- `cmsis-dap`
- `mbed`

The default is `mbed`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:max32600mbed]
platform = maxim32
board = max32600mbed

upload_protocol = mbed
```

## Debugging

The Maxim ARM mbed Enabled Development Platform for MAX32600 has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) | Yes | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Mbed](../../frameworks/mbed.mdx) | Arm Mbed OS is a platform operating system designed for the internet of things |
