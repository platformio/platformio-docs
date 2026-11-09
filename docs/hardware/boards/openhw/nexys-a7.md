---
title: "Digilent Nexys A7"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Digilent Nexys A7 (, 320MHz, 16MB flash, 1.16MB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

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

Use the board ID `nexys_a7` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:nexys_a7]
platform = openhw
board = nexys_a7
```

To override a setting of the board manifest [nexys_a7.json](https://github.com/platformio/platform-openhw/blob/master/boards/nexys_a7.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

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

The Digilent Nexys A7 has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
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
