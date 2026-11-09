---
title: "MAX32625PICO"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "MAX32625PICO (MAX32625, 96MHz, 512KB flash, 160KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

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

Use the board ID `max32625pico` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:max32625pico]
platform = maxim32
board = max32625pico
```

To override a setting of the board manifest [max32625pico.json](https://github.com/platformio/platform-maxim32/blob/master/boards/max32625pico.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

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

[Debugging](../../../guides/debugging/index.md) does not support the MAX32625PICO yet.

## Frameworks

| Name | Description |
|---|---|
| [Mbed](../../frameworks/mbed.mdx) | Arm Mbed OS is a platform operating system designed for the internet of things |
