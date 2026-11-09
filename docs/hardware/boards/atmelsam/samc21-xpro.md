---
title: "Atmel SAMC21-XPRO"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-atmelsam-samc21-xpro"></a>

# Atmel SAMC21-XPRO

## Hardware

Platform [Atmel SAM](../../platforms/atmelsam.md): Atmel | SMART offers Flash- based ARM products based on the ARM Cortex-M0+, Cortex-M3 and Cortex-M4 architectures, ranging from 8KB to 2MB of Flash including a rich peripheral and feature mix.

| Specification | Value |
|---|---|
| **Microcontroller** | SAMC21J18A |
| **Frequency** | 48MHz |
| **Flash** | 256KB |
| **RAM** | 32KB |
| **Vendor** | [Atmel](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/ATSAMC21-XPRO?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `samc21_xpro` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:samc21_xpro]
platform = atmelsam
board = samc21_xpro
```

You can override default Atmel SAMC21-XPRO settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [samc21_xpro.json](https://github.com/platformio/platform-atmelsam/blob/master/boards/samc21_xpro.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:samc21_xpro]
platform = atmelsam
board = samc21_xpro

; change microcontroller
board_build.mcu = samc21j18a

; change MCU frequency
board_build.f_cpu = 48000000L
```

## Uploading

Atmel SAMC21-XPRO supports the following uploading protocols:

- `atmel-ice`
- `blackmagic`
- `cmsis-dap`
- `jlink`

Default protocol is `cmsis-dap`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:samc21_xpro]
platform = atmelsam
board = samc21_xpro

upload_protocol = cmsis-dap
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

Atmel SAMC21-XPRO has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

| Compatible Tools | On-board | Default |
|---|---|---|
| [Atmel-ICE](../../debug-probes/atmel-ice.md) |  |  |
| [Black Magic Probe](../../debug-probes/blackmagic.md) |  |  |
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) | Yes | Yes |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
