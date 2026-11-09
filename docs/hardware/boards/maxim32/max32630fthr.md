---
title: "Maxim MAX32630FTHR Application Platform"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-maxim32-max32630fthr"></a>

# Maxim MAX32630FTHR Application Platform

## Hardware

Platform [Maxim 32](../../platforms/maxim32.md): Maxim's microcontrollers provide low-power, efficient, and secure solutions for challenging embedded applications. Maxim's processors embed cutting-edge technologies to secure data and intellectual property, proven analog circuitry for real-world applications, and battery-conserving low power operation.

| Specification | Value |
|---|---|
| **Microcontroller** | MAX32630 |
| **Frequency** | 96MHz |
| **Flash** | 2MB |
| **RAM** | 512KB |
| **Vendor** | [Maxim](https://developer.mbed.org/platforms/MAX32630FTHR/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `max32630fthr` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:max32630fthr]
platform = maxim32
board = max32630fthr
```

You can override default Maxim MAX32630FTHR Application Platform settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [max32630fthr.json](https://github.com/platformio/platform-maxim32/blob/master/boards/max32630fthr.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:max32630fthr]
platform = maxim32
board = max32630fthr

; change microcontroller
board_build.mcu = max32630

; change MCU frequency
board_build.f_cpu = 96000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support Maxim MAX32630FTHR Application Platform board.

## Frameworks

| Name | Description |
|---|---|
| [Mbed](../../frameworks/mbed.mdx) | Arm Mbed OS is a platform operating system designed for the internet of things |
