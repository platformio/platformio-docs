---
title: "Adafruit MONSTER M4SK"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-atmelsam-adafruit-monster-m4sk"></a>

# Adafruit MONSTER M4SK

## Hardware

Platform [Atmel SAM](../../platforms/atmelsam.md): Atmel | SMART offers Flash- based ARM products based on the ARM Cortex-M0+, Cortex-M3 and Cortex-M4 architectures, ranging from 8KB to 2MB of Flash including a rich peripheral and feature mix.

| Specification | Value |
|---|---|
| **Microcontroller** | SAMD51G19A |
| **Frequency** | 120MHz |
| **Flash** | 496KB |
| **RAM** | 192KB |
| **Vendor** | [Adafruit](https://www.adafruit.com/product/4343?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `adafruit_monster_m4sk` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:adafruit_monster_m4sk]
platform = atmelsam
board = adafruit_monster_m4sk
```

You can override default Adafruit MONSTER M4SK settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [adafruit_monster_m4sk.json](https://github.com/platformio/platform-atmelsam/blob/master/boards/adafruit_monster_m4sk.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:adafruit_monster_m4sk]
platform = atmelsam
board = adafruit_monster_m4sk

; change microcontroller
board_build.mcu = samd51g19a

; change MCU frequency
board_build.f_cpu = 120000000L
```

## Uploading

Adafruit MONSTER M4SK supports the following uploading protocols:

- `atmel-ice`
- `jlink`
- `sam-ba`

Default protocol is `sam-ba`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:adafruit_monster_m4sk]
platform = atmelsam
board = adafruit_monster_m4sk

upload_protocol = sam-ba
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

Adafruit MONSTER M4SK does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

| Compatible Tools | On-board | Default |
|---|---|---|
| [Atmel-ICE](../../debug-probes/atmel-ice.md) |  | Yes |
| [J-LINK](../../debug-probes/jlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
