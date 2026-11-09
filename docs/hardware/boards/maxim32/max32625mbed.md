---
title: "MAX32625MBED"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-maxim32-max32625mbed"></a>

# MAX32625MBED

## Hardware

Platform [Maxim 32](../../platforms/maxim32.md): Maxim's microcontrollers provide low-power, efficient, and secure solutions for challenging embedded applications. Maxim's processors embed cutting-edge technologies to secure data and intellectual property, proven analog circuitry for real-world applications, and battery-conserving low power operation.

| Specification | Value |
|---|---|
| **Microcontroller** | MAX32625 |
| **Frequency** | 96MHz |
| **Flash** | 512KB |
| **RAM** | 160KB |
| **Vendor** | [Maxim](https://os.mbed.com/platforms/MAX32625MBED/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `max32625mbed` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:max32625mbed]
platform = maxim32
board = max32625mbed
```

You can override default MAX32625MBED settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [max32625mbed.json](https://github.com/platformio/platform-maxim32/blob/master/boards/max32625mbed.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:max32625mbed]
platform = maxim32
board = max32625mbed

; change microcontroller
board_build.mcu = max32625

; change MCU frequency
board_build.f_cpu = 96000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support MAX32625MBED board.

## Frameworks

| Name | Description |
|---|---|
| [Mbed](../../frameworks/mbed.mdx) | Arm Mbed OS is a platform operating system designed for the internet of things |
