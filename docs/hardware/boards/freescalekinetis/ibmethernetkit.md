---
title: "Ethernet IoT Starter Kit"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Ethernet IoT Starter Kit (MK64FN1M0VLL12, 120MHz, 1MB flash, 256KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-freescalekinetis-ibmethernetkit"></a>

# Ethernet IoT Starter Kit

## Hardware

Platform [Freescale Kinetis](../../platforms/freescalekinetis.md): Freescale Kinetis Microcontrollers is family of multiple hardware- and software-compatible ARM Cortex-M0+, Cortex-M4 and Cortex-M7-based MCU series. Kinetis MCUs offer exceptional low-power performance, scalability and feature integration.

| Specification | Value |
|---|---|
| **Microcontroller** | MK64FN1M0VLL12 |
| **Frequency** | 120MHz |
| **Flash** | 1MB |
| **RAM** | 256KB |
| **Vendor** | [Freescale](http://developer.mbed.org/platforms/IBMEthernetKit/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `IBMEthernetKit` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:IBMEthernetKit]
platform = freescalekinetis
board = IBMEthernetKit
```

To override a setting of the board manifest [IBMEthernetKit.json](https://github.com/platformio/platform-freescalekinetis/blob/master/boards/IBMEthernetKit.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:IBMEthernetKit]
platform = freescalekinetis
board = IBMEthernetKit

; change microcontroller
board_build.mcu = mk64fn1m0vll12

; change MCU frequency
board_build.f_cpu = 120000000L
```

## Uploading

Ethernet IoT Starter Kit supports these upload protocols:

- `cmsis-dap`
- `jlink`
- `mbed`

The default is `mbed`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:IBMEthernetKit]
platform = freescalekinetis
board = IBMEthernetKit

upload_protocol = mbed
```

## Debugging

The Ethernet IoT Starter Kit has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) | Yes | Yes |
| [J-LINK](../../debug-probes/jlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Mbed](../../frameworks/mbed.mdx) | Arm Mbed OS is a platform operating system designed for the internet of things |
