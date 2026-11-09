---
title: "RVfpga: Digilent Nexys A7"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "RVfpga: Digilent Nexys A7 (, 320MHz, 16MB flash, 1.16MB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-chipsalliance-swervolf-nexys"></a>

# RVfpga: Digilent Nexys A7

## Hardware

Platform [CHIPS Alliance](../../platforms/chipsalliance.md): The CHIPS Alliance develops high-quality, open source hardware designs relevant to silicon devices and FPGAs.

| Specification | Value |
|---|---|
| **Microcontroller** |  |
| **Frequency** | 320MHz |
| **Flash** | 16MB |
| **RAM** | 1.16MB |
| **Vendor** | [Digilent](https://reference.digilentinc.com/reference/programmable-logic/nexys-a7/start?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `swervolf_nexys` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:swervolf_nexys]
platform = chipsalliance
board = swervolf_nexys
```

To override a setting of the board manifest [swervolf_nexys.json](https://github.com/platformio/platform-chipsalliance/blob/master/boards/swervolf_nexys.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:swervolf_nexys]
platform = chipsalliance
board = swervolf_nexys

; change microcontroller
board_build.mcu = 

; change MCU frequency
board_build.f_cpu = 320000000L
```

## Debugging

The RVfpga: Digilent Nexys A7 has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [JTAG-HS1](../../debug-probes/digilent-hs1.md) | Yes | Yes |
| [Olimex ARM-USB-OCD](../../debug-probes/olimex-arm-usb-ocd.md) |  |  |
| [Olimex ARM-USB-OCD-H](../../debug-probes/olimex-arm-usb-ocd-h.md) |  |  |
| [Olimex ARM-USB-TINY-H](../../debug-probes/olimex-arm-usb-tiny-h.md) |  |  |
| [Olimex ARM-USB-TINY](../../debug-probes/olimex-jtag-tiny.md) |  |  |
| [Verilator](../../debug-probes/verilator.md) |  |  |
| [Whisper](../../debug-probes/whisper.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [FreeRTOS](../../frameworks/freertos.md) | FreeRTOS is a real-time operating system kernel for embedded devices that has been ported to 40 microcontroller platforms. |
| [WD-Firmware](../../frameworks/wd-riscv-sdk.md) | The WD Firmware package contains Firmware applications and Processor Support Package (PSP) for various cores, alongside demos which support all features. |
