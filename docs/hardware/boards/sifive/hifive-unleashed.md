---
title: "HiFive Unleashed"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "HiFive Unleashed (FU540, 1500MHz, 32MB flash, 8GB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# HiFive Unleashed

## Hardware

Platform [SiFive](../../platforms/sifive.md): SiFive brings the power of open source and software automation to the semiconductor industry, making it possible to develop new hardware faster and more affordably than ever before.

| Specification | Value |
|---|---|
| **Microcontroller** | FU540 |
| **Frequency** | 1500MHz |
| **Flash** | 32MB |
| **RAM** | 8GB |
| **Vendor** | [SiFive](https://www.sifive.com/boards/hifive-unleashed?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `hifive-unleashed` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:hifive-unleashed]
platform = sifive
board = hifive-unleashed
```

To override a setting of the board manifest [hifive-unleashed.json](https://github.com/platformio/platform-sifive/blob/master/boards/hifive-unleashed.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:hifive-unleashed]
platform = sifive
board = hifive-unleashed

; change microcontroller
board_build.mcu = fu540

; change MCU frequency
board_build.f_cpu = 1500000000L
```

## Debugging

The HiFive Unleashed has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [FTDI chip](../../debug-probes/ftdi.md) | Yes | Yes |
| [QEMU](../../debug-probes/qemu.md) | Yes |  |
| [Renode](../../debug-probes/renode.md) | Yes |  |

## Frameworks

| Name | Description |
|---|---|
| [Freedom E SDK](../../frameworks/freedom-e-sdk.mdx) | Open Source Software for Developing on the SiFive Freedom E Platform |
| [FreeRTOS](../../frameworks/freertos.md) | FreeRTOS is a real-time operating system kernel for embedded devices that has been ported to 40 microcontroller platforms. |
