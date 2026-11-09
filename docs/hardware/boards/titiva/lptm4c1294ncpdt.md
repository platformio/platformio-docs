---
title: "TI LaunchPad (Tiva C) w/ tm4c129 (120MHz)"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "TI LaunchPad (Tiva C) w/ tm4c129 (120MHz) (LPTM4C1294NCPDT, 120MHz, 1MB flash, 256KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-titiva-lptm4c1294ncpdt"></a>

# TI LaunchPad (Tiva C) w/ tm4c129 (120MHz)

## Hardware

Platform [TI TIVA](../../platforms/titiva.md): Texas Instruments TM4C12x MCUs offer the industrys most popular ARM Cortex-M4 core with scalable memory and package options, unparalleled connectivity peripherals, advanced application functions, industry-leading analog integration, and extensive software solutions.

| Specification | Value |
|---|---|
| **Microcontroller** | LPTM4C1294NCPDT |
| **Frequency** | 120MHz |
| **Flash** | 1MB |
| **RAM** | 256KB |
| **Vendor** | [TI](http://www.ti.com/ww/en/launchpad/launchpads-connected-ek-tm4c1294xl.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `lptm4c1294ncpdt` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:lptm4c1294ncpdt]
platform = titiva
board = lptm4c1294ncpdt
```

To override a setting of the board manifest [lptm4c1294ncpdt.json](https://github.com/platformio/platform-titiva/blob/master/boards/lptm4c1294ncpdt.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:lptm4c1294ncpdt]
platform = titiva
board = lptm4c1294ncpdt

; change microcontroller
board_build.mcu = lptm4c1294ncpdt

; change MCU frequency
board_build.f_cpu = 120000000L
```

## Debugging

The TI LaunchPad (Tiva C) w/ tm4c129 (120MHz) has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [TI-ICDI](../../debug-probes/ti-icdi.md) | Yes | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [LibOpenCM3](../../frameworks/libopencm3.md) | The libopencm3 project aims to create an open-source firmware library for various ARM Cortex-M microcontrollers. |
