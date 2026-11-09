---
title: "Vajra on Arty A7-100: Artix-7 FPGA Development Board"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Vajra on Arty A7-100: Artix-7 FPGA Development Board (C-CLASS, 50MHz, 0B flash, 128MB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Vajra on Arty A7-100: Artix-7 FPGA Development Board

## Hardware

Platform [Shakti](../../platforms/shakti.md): Shakti is an open-source initiative by the RISE group at IIT-Madras, which is not only building open source, production grade processors, but also associated components like interconnect fabrics, verification tools, storage controllers, peripheral IPs and SOC tools.

| Specification | Value |
|---|---|
| **Microcontroller** | C-CLASS |
| **Frequency** | 50MHz |
| **Flash** | 0B |
| **RAM** | 128MB |
| **Vendor** | [Xilinx](https://www.xilinx.com/products/boards-and-kits/1-w51quh.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `vajra` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:vajra]
platform = shakti
board = vajra
```

To override a setting of the board manifest [vajra.json](https://github.com/platformio/platform-shakti/blob/master/boards/vajra.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:vajra]
platform = shakti
board = vajra

; change microcontroller
board_build.mcu = C-Class

; change MCU frequency
board_build.f_cpu = 50000000L
```

## Uploading

Vajra on Arty A7-100: Artix-7 FPGA Development Board supports these upload protocols:

- `ftdi`
- `ftdi`
- `jlink`
- `jlink`

The default is `ftdi`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:vajra]
platform = shakti
board = vajra

upload_protocol = ftdi
```

## Debugging

The Vajra on Arty A7-100: Artix-7 FPGA Development Board has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [FTDI chip](../../debug-probes/ftdi.md) | Yes | Yes |
| [J-LINK](../../debug-probes/jlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Shakti SDK](../../frameworks/shakti-sdk.md) | A software development kit for developing applications on Shakti class of processors |
