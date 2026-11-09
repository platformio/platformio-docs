---
title: "TI LaunchPad (Tiva C) w/ tm4c123 (80MHz)"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-titiva-lptm4c123gh6pm"></a>

# TI LaunchPad (Tiva C) w/ tm4c123 (80MHz)

## Hardware

Platform [TI TIVA](../../platforms/titiva.md): Texas Instruments TM4C12x MCUs offer the industrys most popular ARM Cortex-M4 core with scalable memory and package options, unparalleled connectivity peripherals, advanced application functions, industry-leading analog integration, and extensive software solutions.

| Specification | Value |
|---|---|
| **Microcontroller** | LPTM4C123GH6PM |
| **Frequency** | 80MHz |
| **Flash** | 256KB |
| **RAM** | 32KB |
| **Vendor** | [TI](http://www.ti.com/ww/en/launchpad/launchpads-connected-ek-tm4c123gxl.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `lptm4c123gh6pm` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:lptm4c123gh6pm]
platform = titiva
board = lptm4c123gh6pm
```

You can override default TI LaunchPad (Tiva C) w/ tm4c123 (80MHz) settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [lptm4c123gh6pm.json](https://github.com/platformio/platform-titiva/blob/master/boards/lptm4c123gh6pm.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:lptm4c123gh6pm]
platform = titiva
board = lptm4c123gh6pm

; change microcontroller
board_build.mcu = lptm4c123gh6pm

; change MCU frequency
board_build.f_cpu = 80000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

TI LaunchPad (Tiva C) w/ tm4c123 (80MHz) has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

| Compatible Tools | On-board | Default |
|---|---|---|
| [TI-ICDI](../../debug-probes/ti-icdi.md) | Yes | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [LibOpenCM3](../../frameworks/libopencm3.md) | The libopencm3 project aims to create an open-source firmware library for various ARM Cortex-M microcontrollers. |
