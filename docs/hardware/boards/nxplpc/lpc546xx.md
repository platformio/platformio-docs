---
title: "NXP LPCXpresso54608"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "NXP LPCXpresso54608 (LPC54608ET512, 180MHz, 512KB flash, 200KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-nxplpc-lpc546xx"></a>

# NXP LPCXpresso54608

## Hardware

Platform [NXP LPC](../../platforms/nxplpc.md): The NXP LPC is a family of 32-bit microcontroller integrated circuits by NXP Semiconductors. The LPC chips are grouped into related series that are based around the same 32-bit ARM processor core, such as the Cortex-M4F, Cortex-M3, Cortex-M0+, or Cortex-M0. Internally, each microcontroller consists of the processor core, static RAM memory, flash memory, debugging interface, and various peripherals.

| Specification | Value |
|---|---|
| **Microcontroller** | LPC54608ET512 |
| **Frequency** | 180MHz |
| **Flash** | 512KB |
| **RAM** | 200KB |
| **Vendor** | [NXP](https://os.mbed.com/platforms/LPCXpresso54608/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `lpc546xx` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:lpc546xx]
platform = nxplpc
board = lpc546xx
```

To override a setting of the board manifest [lpc546xx.json](https://github.com/platformio/platform-nxplpc/blob/master/boards/lpc546xx.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:lpc546xx]
platform = nxplpc
board = lpc546xx

; change microcontroller
board_build.mcu = lpc54608et512

; change MCU frequency
board_build.f_cpu = 180000000L
```

## Uploading

NXP LPCXpresso54608 supports these upload protocols:

- `jlink`
- `mbed`

The default is `mbed`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:lpc546xx]
platform = nxplpc
board = lpc546xx

upload_protocol = mbed
```

## Debugging

The NXP LPCXpresso54608 has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

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
| [Mbed](../../frameworks/mbed.mdx) | Arm Mbed OS is a platform operating system designed for the internet of things |
