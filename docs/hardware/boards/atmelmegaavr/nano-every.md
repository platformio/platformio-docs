---
title: "Arduino Nano Every"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Arduino Nano Every (ATMEGA4809, 16MHz, 47.50KB flash, 6KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-atmelmegaavr-nano-every"></a>

# Arduino Nano Every

## Hardware

Platform [Atmel megaAVR](../../platforms/atmelmegaavr.mdx): 8-bit MCUs Built for Real-time Control with Core Independent Peripherals combining intelligent hardware peripherals along with the low-power capability of an AVR core, megaAVR microcontrollers (MCUs) broaden the effectiveness of your real-time control systems.

| Specification | Value |
|---|---|
| **Microcontroller** | ATMEGA4809 |
| **Frequency** | 16MHz |
| **Flash** | 47.50KB |
| **RAM** | 6KB |
| **Vendor** | [Arduino](https://www.arduino.cc/en/Guide/NANOEvery?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `nano_every` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:nano_every]
platform = atmelmegaavr
board = nano_every
```

To override a setting of the board manifest [nano_every.json](https://github.com/platformio/platform-atmelmegaavr/blob/master/boards/nano_every.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:nano_every]
platform = atmelmegaavr
board = nano_every

; change microcontroller
board_build.mcu = atmega4809

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the Arduino Nano Every yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
