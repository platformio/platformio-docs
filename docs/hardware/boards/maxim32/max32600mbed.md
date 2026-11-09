---
title: "Maxim ARM mbed Enabled Development Platform for MAX32600"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
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

Please use `max32600mbed` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:max32600mbed]
platform = maxim32
board = max32600mbed
```

You can override default Maxim ARM mbed Enabled Development Platform for MAX32600 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [max32600mbed.json](https://github.com/platformio/platform-maxim32/blob/master/boards/max32600mbed.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

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

Maxim ARM mbed Enabled Development Platform for MAX32600 supports the following uploading protocols:

- `cmsis-dap`
- `mbed`

Default protocol is `mbed`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:max32600mbed]
platform = maxim32
board = max32600mbed

upload_protocol = mbed
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

Maxim ARM mbed Enabled Development Platform for MAX32600 has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

| Compatible Tools | On-board | Default |
|---|---|---|
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) | Yes | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Mbed](../../frameworks/mbed.mdx) | Arm Mbed OS is a platform operating system designed for the internet of things |
