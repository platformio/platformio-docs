---
title: "Arduino Uno R4 WiFi"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Arduino Uno R4 WiFi (RA4M1, 48MHz, 256KB flash, 32KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Arduino Uno R4 WiFi

## Hardware

Platform [Renesas RA](../../platforms/renesas-ra.md): Renesas Advanced (RA) 32-bit microcontrollers with the Arm Cortex-M33, -M23 and -M4 processor cores deliver key advantages compared to competitive Arm Cortex-M MCUs by providing stronger embedded security, superior CoreMark performance and ultra-low power operation.

| Specification | Value |
|---|---|
| **Microcontroller** | RA4M1 |
| **Frequency** | 48MHz |
| **Flash** | 256KB |
| **RAM** | 32KB |
| **Vendor** | [Arduino](https://docs.arduino.cc/hardware/uno-r4-wifi?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `uno_r4_wifi` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:uno_r4_wifi]
platform = renesas-ra
board = uno_r4_wifi
```

To override a setting of the board manifest [uno_r4_wifi.json](https://github.com/platformio/platform-renesas-ra/blob/master/boards/uno_r4_wifi.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:uno_r4_wifi]
platform = renesas-ra
board = uno_r4_wifi

; change microcontroller
board_build.mcu = ra4m1

; change MCU frequency
board_build.f_cpu = 48000000L
```

## Uploading

Arduino Uno R4 WiFi supports these upload protocols:

- `cmsis-dap`
- `jlink`
- `sam-ba`

The default is `sam-ba`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:uno_r4_wifi]
platform = renesas-ra
board = uno_r4_wifi

upload_protocol = sam-ba
```

## Debugging

The Arduino Uno R4 WiFi has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

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
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [CMSIS](../../frameworks/cmsis.md) | Vendor-independent hardware abstraction layer for the Cortex-M processor series |
| [Renesas Flexible Software Package](../../frameworks/fsp.md) | The Renesas Flexible Software Package (FSP) is an enhanced software package designed to provide easy-to-use, scalable, high-quality software for embedded system designs using Renesas RA family of Arm Microcontrollers. |
