---
title: "Atmel ATSAMW25-XPRO"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-atmelsam-samd21g18a"></a>

# Atmel ATSAMW25-XPRO

## Hardware

Platform [Atmel SAM](../../platforms/atmelsam.md): Atmel | SMART offers Flash- based ARM products based on the ARM Cortex-M0+, Cortex-M3 and Cortex-M4 architectures, ranging from 8KB to 2MB of Flash including a rich peripheral and feature mix.

| Specification | Value |
|---|---|
| **Microcontroller** | SAMD21G18A |
| **Frequency** | 48MHz |
| **Flash** | 256KB |
| **RAM** | 32KB |
| **Vendor** | [Atmel](https://www.microchip.com/en-us/development-tool/atsamw25-xpro?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `samd21g18a` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:samd21g18a]
platform = atmelsam
board = samd21g18a
```

You can override default Atmel ATSAMW25-XPRO settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [samd21g18a.json](https://github.com/platformio/platform-atmelsam/blob/master/boards/samd21g18a.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:samd21g18a]
platform = atmelsam
board = samd21g18a

; change microcontroller
board_build.mcu = samd21g18a

; change MCU frequency
board_build.f_cpu = 48000000L
```

## Uploading

Atmel ATSAMW25-XPRO supports the following uploading protocols:

- `atmel-ice`
- `blackmagic`
- `cmsis-dap`
- `jlink`

Default protocol is `cmsis-dap`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:samd21g18a]
platform = atmelsam
board = samd21g18a

upload_protocol = cmsis-dap
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

Atmel ATSAMW25-XPRO has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

| Compatible Tools | On-board | Default |
|---|---|---|
| [Atmel-ICE](../../debug-probes/atmel-ice.md) |  |  |
| [Black Magic Probe](../../debug-probes/blackmagic.md) |  |  |
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) | Yes | Yes |
| [J-LINK](../../debug-probes/jlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
