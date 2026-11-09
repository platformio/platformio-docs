---
title: "Arduino/Genuino 101"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-intel-arc32-genuino101"></a>

# Arduino/Genuino 101

## Hardware

Platform [Intel ARC32](../../platforms/intel-arc32.md): ARC embedded processors are a family of 32-bit CPUs that are widely used in SoC devices for storage, home, mobile, automotive, and Internet of Things applications.

| Specification | Value |
|---|---|
| **Microcontroller** | ARCV2EM |
| **Frequency** | 32MHz |
| **Flash** | 152KB |
| **RAM** | 80KB |
| **Vendor** | [Intel](https://www.arduino.cc/en/Main/ArduinoBoard101?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `genuino101` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:genuino101]
platform = intel_arc32
board = genuino101
```

You can override default Arduino/Genuino 101 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [genuino101.json](https://github.com/platformio/platform-intel_arc32/blob/master/boards/genuino101.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:genuino101]
platform = intel_arc32
board = genuino101

; change microcontroller
board_build.mcu = ARCv2EM

; change MCU frequency
board_build.f_cpu = 32000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support Arduino/Genuino 101 board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
