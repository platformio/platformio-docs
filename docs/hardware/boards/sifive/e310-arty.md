---
title: "Arty FPGA Dev Kit"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Arty FPGA Dev Kit (FE310, 450MHz, 16MB flash, 256MB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-sifive-e310-arty"></a>

# Arty FPGA Dev Kit

## Hardware

Platform [SiFive](../../platforms/sifive.md): SiFive brings the power of open source and software automation to the semiconductor industry, making it possible to develop new hardware faster and more affordably than ever before.

| Specification | Value |
|---|---|
| **Microcontroller** | FE310 |
| **Frequency** | 450MHz |
| **Flash** | 16MB |
| **RAM** | 256MB |
| **Vendor** | [Xilinx](https://store.digilentinc.com/arty-a7-artix-7-fpga-development-board-for-makers-and-hobbyists/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `e310-arty` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:e310-arty]
platform = sifive
board = e310-arty
```

To override a setting of the board manifest [e310-arty.json](https://github.com/platformio/platform-sifive/blob/master/boards/e310-arty.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:e310-arty]
platform = sifive
board = e310-arty

; change microcontroller
board_build.mcu = fe310

; change MCU frequency
board_build.f_cpu = 450000000L
```

## Uploading

Arty FPGA Dev Kit supports these upload protocols:

- `ftdi`
- `jlink`
- `minimodule`
- `olimex-arm-usb-ocd`
- `olimex-arm-usb-ocd-h`
- `olimex-arm-usb-tiny-h`
- `olimex-jtag-tiny`
- `tumpa`

The default is `ftdi`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:e310-arty]
platform = sifive
board = e310-arty

upload_protocol = ftdi
```

## Debugging

The Arty FPGA Dev Kit has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [FTDI chip](../../debug-probes/ftdi.md) | Yes | Yes |
| [J-LINK](../../debug-probes/jlink.md) |  |  |
| [Mini-Module FT2232H](../../debug-probes/minimodule.md) |  |  |
| [Olimex ARM-USB-OCD](../../debug-probes/olimex-arm-usb-ocd.md) |  |  |
| [Olimex ARM-USB-OCD-H](../../debug-probes/olimex-arm-usb-ocd-h.md) |  |  |
| [Olimex ARM-USB-TINY-H](../../debug-probes/olimex-arm-usb-tiny-h.md) |  |  |
| [Olimex ARM-USB-TINY](../../debug-probes/olimex-jtag-tiny.md) |  |  |
| [QEMU](../../debug-probes/qemu.md) | Yes |  |
| [Renode](../../debug-probes/renode.md) | Yes |  |
| [TIAO USB Multi-Protocol adapter (TUMPA)](../../debug-probes/tumpa.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Freedom E SDK](../../frameworks/freedom-e-sdk.mdx) | Open Source Software for Developing on the SiFive Freedom E Platform |
| [FreeRTOS](../../frameworks/freertos.md) | FreeRTOS is a real-time operating system kernel for embedded devices that has been ported to 40 microcontroller platforms. |
