---
title: "ATtiny416 Xplained Nano"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-atmelmegaavr-xplained-nano-416"></a>

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

Please use `xplained_nano_416` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:xplained_nano_416]
platform = atmelmegaavr
board = xplained_nano_416
```

You can override default ATtiny416 Xplained Nano settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [xplained_nano_416.json](https://github.com/platformio/platform-atmelmegaavr/blob/master/boards/xplained_nano_416.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

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

[Debugging](../../../guides/debugging/index.md) currently does not support ATtiny416 Xplained Nano board.

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
