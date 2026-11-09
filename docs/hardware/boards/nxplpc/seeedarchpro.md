---
title: "Seeed Arch Pro"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Seeed Arch Pro (LPC1768, 96MHz, 512KB flash, 64KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-nxplpc-seeedarchpro"></a>

# Seeed Arch Pro

## Hardware

Platform [NXP LPC](../../platforms/nxplpc.md): The NXP LPC is a family of 32-bit microcontroller integrated circuits by NXP Semiconductors. The LPC chips are grouped into related series that are based around the same 32-bit ARM processor core, such as the Cortex-M4F, Cortex-M3, Cortex-M0+, or Cortex-M0. Internally, each microcontroller consists of the processor core, static RAM memory, flash memory, debugging interface, and various peripherals.

| Specification | Value |
|---|---|
| **Microcontroller** | LPC1768 |
| **Frequency** | 96MHz |
| **Flash** | 512KB |
| **RAM** | 64KB |
| **Vendor** | [SeeedStudio](https://developer.mbed.org/platforms/Seeeduino-Arch-Pro/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `seeedArchPro` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:seeedArchPro]
platform = nxplpc
board = seeedArchPro
```

To override a setting of the board manifest [seeedArchPro.json](https://github.com/platformio/platform-nxplpc/blob/master/boards/seeedArchPro.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:seeedArchPro]
platform = nxplpc
board = seeedArchPro

; change microcontroller
board_build.mcu = lpc1768

; change MCU frequency
board_build.f_cpu = 96000000L
```

## Uploading

Seeed Arch Pro supports these upload protocols:

- `cmsis-dap`
- `mbed`

The default is `mbed`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:seeedArchPro]
platform = nxplpc
board = seeedArchPro

upload_protocol = mbed
```

## Debugging

The Seeed Arch Pro has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) | Yes | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Mbed](../../frameworks/mbed.mdx) | Arm Mbed OS is a platform operating system designed for the internet of things |
