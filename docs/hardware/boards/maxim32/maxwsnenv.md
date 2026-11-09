---
title: "Maxim Wireless Sensor Node Demonstrator"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Maxim Wireless Sensor Node Demonstrator (MAX32610, 24MHz, 256KB flash, 32KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-maxim32-maxwsnenv"></a>

# Maxim Wireless Sensor Node Demonstrator

## Hardware

Platform [Maxim 32](../../platforms/maxim32.md): Maxim's microcontrollers provide low-power, efficient, and secure solutions for challenging embedded applications. Maxim's processors embed cutting-edge technologies to secure data and intellectual property, proven analog circuitry for real-world applications, and battery-conserving low power operation.

| Specification | Value |
|---|---|
| **Microcontroller** | MAX32610 |
| **Frequency** | 24MHz |
| **Flash** | 256KB |
| **RAM** | 32KB |
| **Vendor** | [Maxim](https://developer.mbed.org/platforms/MAXWSNENV/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `maxwsnenv` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:maxwsnenv]
platform = maxim32
board = maxwsnenv
```

To override a setting of the board manifest [maxwsnenv.json](https://github.com/platformio/platform-maxim32/blob/master/boards/maxwsnenv.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:maxwsnenv]
platform = maxim32
board = maxwsnenv

; change microcontroller
board_build.mcu = max32610

; change MCU frequency
board_build.f_cpu = 24000000L
```

## Uploading

Maxim Wireless Sensor Node Demonstrator supports these upload protocols:

- `cmsis-dap`
- `mbed`

The default is `mbed`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:maxwsnenv]
platform = maxim32
board = maxwsnenv

upload_protocol = mbed
```

## Debugging

The Maxim Wireless Sensor Node Demonstrator has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) |  | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Mbed](../../frameworks/mbed.mdx) | Arm Mbed OS is a platform operating system designed for the internet of things |
