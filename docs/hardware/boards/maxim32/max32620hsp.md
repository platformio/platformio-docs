---
title: "Maxim Health Sensor Platform"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-maxim32-max32620hsp"></a>

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

Please use `max32620hsp` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:max32620hsp]
platform = maxim32
board = max32620hsp
```

You can override default Maxim Health Sensor Platform settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [max32620hsp.json](https://github.com/platformio/platform-maxim32/blob/master/boards/max32620hsp.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

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

Maxim Health Sensor Platform supports the following uploading protocols:

- `jlink`
- `mbed`

Default protocol is `mbed`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:max32620hsp]
platform = maxim32
board = max32620hsp

upload_protocol = mbed
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

Maxim Health Sensor Platform does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

| Compatible Tools | On-board | Default |
|---|---|---|
| [J-LINK](../../debug-probes/jlink.md) |  | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Mbed](../../frameworks/mbed.mdx) | Arm Mbed OS is a platform operating system designed for the internet of things |
