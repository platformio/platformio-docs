---
title: "Arduino/Genuino 101"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Arduino/Genuino 101 (ARCV2EM, 32MHz, 152KB flash, 80KB RAM): PlatformIO board ID, configuration, uploading and debugging."
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

Use the board ID `genuino101` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:genuino101]
platform = intel_arc32
board = genuino101
```

To override a setting of the board manifest [genuino101.json](https://github.com/platformio/platform-intel_arc32/blob/master/boards/genuino101.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

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

[Debugging](../../../guides/debugging/index.md) does not support the Arduino/Genuino 101 yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
