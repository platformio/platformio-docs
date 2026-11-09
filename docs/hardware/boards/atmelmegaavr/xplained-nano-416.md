---
title: "ATtiny416 Xplained Nano"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "ATtiny416 Xplained Nano (ATTINY416, 20MHz, 4KB flash, 256B RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# ATtiny416 Xplained Nano

## Hardware

Platform [Atmel megaAVR](../../platforms/atmelmegaavr.mdx): 8-bit MCUs Built for Real-time Control with Core Independent Peripherals combining intelligent hardware peripherals along with the low-power capability of an AVR core, megaAVR microcontrollers (MCUs) broaden the effectiveness of your real-time control systems.

| Specification | Value |
|---|---|
| **Microcontroller** | ATTINY416 |
| **Frequency** | 20MHz |
| **Flash** | 4KB |
| **RAM** | 256B |
| **Vendor** | [Microchip](https://www.microchip.com/wwwproducts/en/ATTINY416?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `xplained_nano_416` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:xplained_nano_416]
platform = atmelmegaavr
board = xplained_nano_416
```

To override a setting of the board manifest [xplained_nano_416.json](https://github.com/platformio/platform-atmelmegaavr/blob/master/boards/xplained_nano_416.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:xplained_nano_416]
platform = atmelmegaavr
board = xplained_nano_416

; change microcontroller
board_build.mcu = attiny416

; change MCU frequency
board_build.f_cpu = 20000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the ATtiny416 Xplained Nano yet.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
