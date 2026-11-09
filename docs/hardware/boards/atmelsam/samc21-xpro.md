---
title: "Atmel SAMC21-XPRO"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Atmel SAMC21-XPRO (SAMC21J18A, 48MHz, 256KB flash, 32KB RAM): PlatformIO board ID, configuration, uploading and debugging."
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

Use the board ID `samc21_xpro` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:samc21_xpro]
platform = atmelsam
board = samc21_xpro
```

To override a setting of the board manifest [samc21_xpro.json](https://github.com/platformio/platform-atmelsam/blob/master/boards/samc21_xpro.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

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

Atmel SAMC21-XPRO supports these upload protocols:

- `atmel-ice`
- `blackmagic`
- `cmsis-dap`
- `jlink`

The default is `cmsis-dap`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:samc21_xpro]
platform = atmelsam
board = samc21_xpro

upload_protocol = cmsis-dap
```

## Debugging

The Atmel SAMC21-XPRO has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [Atmel-ICE](../../debug-probes/atmel-ice.md) |  |  |
| [Black magic probe](../../debug-probes/blackmagic.md) |  |  |
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) | Yes | Yes |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
