---
title: "RVfpga: Digilent Nexys A7"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
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

Please use `swervolf_nexys` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:swervolf_nexys]
platform = chipsalliance
board = swervolf_nexys
```

You can override default RVfpga: Digilent Nexys A7 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [swervolf_nexys.json](https://github.com/platformio/platform-chipsalliance/blob/master/boards/swervolf_nexys.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

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

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

RVfpga: Digilent Nexys A7 has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

| Compatible Tools | On-board | Default |
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
