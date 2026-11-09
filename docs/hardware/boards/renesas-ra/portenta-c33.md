---
title: "Arduino Portenta C33"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Arduino Portenta C33 (R7FA6M5BH2CBG, 200MHz, 2MB flash, 511.35KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-renesas-ra-portenta-c33"></a>

# Arduino Portenta C33

## Hardware

Platform [Renesas RA](../../platforms/renesas-ra.md): Renesas Advanced (RA) 32-bit microcontrollers with the Arm Cortex-M33, -M23 and -M4 processor cores deliver key advantages compared to competitive Arm Cortex-M MCUs by providing stronger embedded security, superior CoreMark performance and ultra-low power operation.

| Specification | Value |
|---|---|
| **Microcontroller** | R7FA6M5BH2CBG |
| **Frequency** | 200MHz |
| **Flash** | 2MB |
| **RAM** | 511.35KB |
| **Vendor** | [Arduino](https://www.arduino.cc/pro/hardware-product-portenta-c33?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `portenta_c33` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:portenta_c33]
platform = renesas-ra
board = portenta_c33
```

To override a setting of the board manifest [portenta_c33.json](https://github.com/platformio/platform-renesas-ra/blob/master/boards/portenta_c33.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:portenta_c33]
platform = renesas-ra
board = portenta_c33

; change microcontroller
board_build.mcu = r7fa6m5bh2cbg

; change MCU frequency
board_build.f_cpu = 200000000L
```

## Uploading

Arduino Portenta C33 supports these upload protocols:

- `dfu`
- `jlink`

The default is `dfu`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:portenta_c33]
platform = renesas-ra
board = portenta_c33

upload_protocol = dfu
```

## Debugging

The Arduino Portenta C33 has no on-board debug probe: [Debugging](../../../guides/debugging/index.md) needs one of the external probes below.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [J-LINK](../../debug-probes/jlink.md) |  | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [CMSIS](../../frameworks/cmsis.md) | Vendor-independent hardware abstraction layer for the Cortex-M processor series |
| [Renesas Flexible Software Package](../../frameworks/fsp.md) | The Renesas Flexible Software Package (FSP) is an enhanced software package designed to provide easy-to-use, scalable, high-quality software for embedded system designs using Renesas RA family of Arm Microcontrollers. |
