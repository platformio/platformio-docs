---
title: "NXP i.MX RT1060 Evaluation Kit"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "NXP i.MX RT1060 Evaluation Kit (MIMXRT1062DVL6A, 600MHz, 8MB flash, 32MB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# NXP i.MX RT1060 Evaluation Kit

## Hardware

Platform [NXP i.MX RT](../../platforms/nxpimxrt.md): The i.MX RT series of crossover processors features the Arm Cortex-M core, real-time functionality and MCU usability at a cost-effective price.

| Specification | Value |
|---|---|
| **Microcontroller** | MIMXRT1062DVL6A |
| **Frequency** | 600MHz |
| **Flash** | 8MB |
| **RAM** | 32MB |
| **Vendor** | [NXP](https://www.nxp.com/design/development-boards/i.mx-evaluation-and-development-boards/mimxrt1060-evk-i.mx-rt1060-evaluation-kit:MIMXRT1060-EVK?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `mimxrt1060_evk` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:mimxrt1060_evk]
platform = nxpimxrt
board = mimxrt1060_evk
```

To override a setting of the board manifest [mimxrt1060_evk.json](https://github.com/platformio/platform-nxpimxrt/blob/master/boards/mimxrt1060_evk.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:mimxrt1060_evk]
platform = nxpimxrt
board = mimxrt1060_evk

; change microcontroller
board_build.mcu = mimxrt1062dvl6a

; change MCU frequency
board_build.f_cpu = 600000000L
```

## Uploading

NXP i.MX RT1060 Evaluation Kit supports these upload protocols:

- `blackmagic`
- `jlink`
- `mbed`

The default is `mbed`.

To use another one, set the [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:mimxrt1060_evk]
platform = nxpimxrt
board = mimxrt1060_evk

upload_protocol = mbed
```

## Debugging

The NXP i.MX RT1060 Evaluation Kit has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [Black magic probe](../../debug-probes/blackmagic.md) |  |  |
| [J-LINK](../../debug-probes/jlink.md) | Yes | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
