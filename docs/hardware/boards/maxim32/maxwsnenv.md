---
title: "Maxim Wireless Sensor Node Demonstrator"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
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

Please use `maxwsnenv` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:maxwsnenv]
platform = maxim32
board = maxwsnenv
```

You can override default Maxim Wireless Sensor Node Demonstrator settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [maxwsnenv.json](https://github.com/platformio/platform-maxim32/blob/master/boards/maxwsnenv.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

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

Maxim Wireless Sensor Node Demonstrator supports the following uploading protocols:

- `cmsis-dap`
- `mbed`

Default protocol is `mbed`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:maxwsnenv]
platform = maxim32
board = maxwsnenv

upload_protocol = mbed
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

Maxim Wireless Sensor Node Demonstrator does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

| Compatible Tools | On-board | Default |
|---|---|---|
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) |  | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Mbed](../../frameworks/mbed.mdx) | Arm Mbed OS is a platform operating system designed for the internet of things |
