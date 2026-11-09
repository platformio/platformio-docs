---
title: "NXP LPCXpresso55S16"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "NXP LPCXpresso55S16 (LPC55S16, 150MHz, 256KB flash, 96KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-nxplpc-lpcxpresso55s16"></a>

# NXP LPCXpresso55S16

## Hardware

Platform [NXP LPC](../../platforms/nxplpc.md): The NXP LPC is a family of 32-bit microcontroller integrated circuits by NXP Semiconductors. The LPC chips are grouped into related series that are based around the same 32-bit ARM processor core, such as the Cortex-M4F, Cortex-M3, Cortex-M0+, or Cortex-M0. Internally, each microcontroller consists of the processor core, static RAM memory, flash memory, debugging interface, and various peripherals.

| Specification | Value |
|---|---|
| **Microcontroller** | LPC55S16 |
| **Frequency** | 150MHz |
| **Flash** | 256KB |
| **RAM** | 96KB |
| **Vendor** | [NXP](https://www.nxp.com/design/development-boards/lpcxpresso-boards/lpcxpresso55s16-development-board:LPC55S16-EVK?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `lpcxpresso55s16` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:lpcxpresso55s16]
platform = nxplpc
board = lpcxpresso55s16
```

To override a setting of the board manifest [lpcxpresso55s16.json](https://github.com/platformio/platform-nxplpc/blob/master/boards/lpcxpresso55s16.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:lpcxpresso55s16]
platform = nxplpc
board = lpcxpresso55s16

; change microcontroller
board_build.mcu = lpc55s16

; change MCU frequency
board_build.f_cpu = 150000000L
```

## Uploading

NXP LPCXpresso55S16 supports these upload protocols:

- `jlink`
- `mbed`

The default is `jlink`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:lpcxpresso55s16]
platform = nxplpc
board = lpcxpresso55s16

upload_protocol = jlink
```

## Debugging

The NXP LPCXpresso55S16 has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [J-LINK](../../debug-probes/jlink.md) | Yes | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
