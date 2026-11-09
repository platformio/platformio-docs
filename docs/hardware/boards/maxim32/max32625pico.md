---
title: "MAX32625PICO"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-maxim32-max32625pico"></a>

# MAX32625PICO

## Hardware

Platform [Maxim 32](../../platforms/maxim32.md): Maxim's microcontrollers provide low-power, efficient, and secure solutions for challenging embedded applications. Maxim's processors embed cutting-edge technologies to secure data and intellectual property, proven analog circuitry for real-world applications, and battery-conserving low power operation.

| Specification | Value |
|---|---|
| **Microcontroller** | MAX32625 |
| **Frequency** | 96MHz |
| **Flash** | 512KB |
| **RAM** | 160KB |
| **Vendor** | [Maxim](https://www.maximintegrated.com/en/products/microcontrollers/MAX32625PICO.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `max32625pico` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:max32625pico]
platform = maxim32
board = max32625pico
```

You can override default MAX32625PICO settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [max32625pico.json](https://github.com/platformio/platform-maxim32/blob/master/boards/max32625pico.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:max32625pico]
platform = maxim32
board = max32625pico

; change microcontroller
board_build.mcu = max32625

; change MCU frequency
board_build.f_cpu = 96000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support MAX32625PICO board.

## Frameworks

| Name | Description |
|---|---|
| [Mbed](../../frameworks/mbed.mdx) | Arm Mbed OS is a platform operating system designed for the internet of things |
