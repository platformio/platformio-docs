---
title: "LowPowerLab CurrentRanger"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-atmelsam-current-ranger"></a>

# LowPowerLab CurrentRanger

## Hardware

Platform [Atmel SAM](../../platforms/atmelsam.md): Atmel | SMART offers Flash- based ARM products based on the ARM Cortex-M0+, Cortex-M3 and Cortex-M4 architectures, ranging from 8KB to 2MB of Flash including a rich peripheral and feature mix.

| Specification | Value |
|---|---|
| **Microcontroller** | SAMD21G18A |
| **Frequency** | 48MHz |
| **Flash** | 256KB |
| **RAM** | 32KB |
| **Vendor** | [LowPowerLab](https://lowpowerlab.com/shop/product/152?search=CurrentRanger&utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `current_ranger` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:current_ranger]
platform = atmelsam
board = current_ranger
```

You can override default LowPowerLab CurrentRanger settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [current_ranger.json](https://github.com/platformio/platform-atmelsam/blob/master/boards/current_ranger.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:current_ranger]
platform = atmelsam
board = current_ranger

; change microcontroller
board_build.mcu = samd21g18a

; change MCU frequency
board_build.f_cpu = 48000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support LowPowerLab CurrentRanger board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
