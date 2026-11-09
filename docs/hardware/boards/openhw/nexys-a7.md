---
title: "Digilent Nexys A7"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-openhw-nexys-a7"></a>

# Digilent Nexys A7

## Hardware

Platform [OpenHW Group](../../platforms/openhw.md): OpenHW Group is a not-for-profit, global organization that provides an infrastructure for hosting high quality open-source HW developments in line with industry best practices. The OpenHW CV32E40P RISC-V core is the first open-source core for high-volume chips verified with the state-of-the-art process required for high-integrity, commercial SoCs.

| Specification | Value |
|---|---|
| **Microcontroller** |  |
| **Frequency** | 320MHz |
| **Flash** | 16MB |
| **RAM** | 1.16MB |
| **Vendor** | [Digilent](https://reference.digilentinc.com/reference/programmable-logic/nexys-a7/start?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `nexys_a7` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:nexys_a7]
platform = openhw
board = nexys_a7
```

You can override default Digilent Nexys A7 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [nexys_a7.json](https://github.com/platformio/platform-openhw/blob/master/boards/nexys_a7.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:nexys_a7]
platform = openhw
board = nexys_a7

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

Digilent Nexys A7 has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

| Compatible Tools | On-board | Default |
|---|---|---|
| [JTAG-HS1](../../debug-probes/digilent-hs1.md) | Yes | Yes |
| [JTAG-HS2](../../debug-probes/digilent-hs2.md) |  |  |
| [Olimex ARM-USB-OCD](../../debug-probes/olimex-arm-usb-ocd.md) |  |  |
| [Olimex ARM-USB-OCD-H](../../debug-probes/olimex-arm-usb-ocd-h.md) |  |  |
| [Olimex ARM-USB-TINY-H](../../debug-probes/olimex-arm-usb-tiny-h.md) |  |  |
| [Olimex ARM-USB-TINY](../../debug-probes/olimex-jtag-tiny.md) |  |  |
| [OVPsim](../../debug-probes/ovpsim.md) | Yes |  |
| [Renode](../../debug-probes/renode.md) | Yes |  |

## Frameworks

| Name | Description |
|---|---|
| [PULP Runtime Environment](../../frameworks/pulp-runtime.md) | Runtime Environment for Parallel Ultra Low Power platform |
| [PULP SDK](../../frameworks/pulp-sdk.md) | Software Development Kit for Parallel Ultra Low Power platform |
