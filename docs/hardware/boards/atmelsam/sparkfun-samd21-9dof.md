---
title: "SparkFun 9DoF Razor IMU M0"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-atmelsam-sparkfun-samd21-9dof"></a>

# SparkFun 9DoF Razor IMU M0

## Hardware

Platform [Atmel SAM](../../platforms/atmelsam.md): Atmel | SMART offers Flash- based ARM products based on the ARM Cortex-M0+, Cortex-M3 and Cortex-M4 architectures, ranging from 8KB to 2MB of Flash including a rich peripheral and feature mix.

| Specification | Value |
|---|---|
| **Microcontroller** | SAMD21G18A |
| **Frequency** | 48MHz |
| **Flash** | 256KB |
| **RAM** | 32KB |
| **Vendor** | [SparkFun](https://www.sparkfun.com/products/14001?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `sparkfun_samd21_9dof` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:sparkfun_samd21_9dof]
platform = atmelsam
board = sparkfun_samd21_9dof
```

You can override default SparkFun 9DoF Razor IMU M0 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [sparkfun_samd21_9dof.json](https://github.com/platformio/platform-atmelsam/blob/master/boards/sparkfun_samd21_9dof.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:sparkfun_samd21_9dof]
platform = atmelsam
board = sparkfun_samd21_9dof

; change microcontroller
board_build.mcu = samd21g18a

; change MCU frequency
board_build.f_cpu = 48000000L
```

## Uploading

SparkFun 9DoF Razor IMU M0 supports the following uploading protocols:

- `atmel-ice`
- `blackmagic`
- `jlink`
- `sam-ba`

Default protocol is `sam-ba`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:sparkfun_samd21_9dof]
platform = atmelsam
board = sparkfun_samd21_9dof

upload_protocol = sam-ba
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

SparkFun 9DoF Razor IMU M0 does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

| Compatible Tools | On-board | Default |
|---|---|---|
| [Atmel-ICE](../../debug-probes/atmel-ice.md) |  | Yes |
| [Black Magic Probe](../../debug-probes/blackmagic.md) |  |  |
| [J-LINK](../../debug-probes/jlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
