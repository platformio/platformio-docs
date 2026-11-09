---
title: "Lattice iCEstick FPGA Evaluation Kit"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Lattice iCEstick FPGA Evaluation Kit (ICE40-HX1K-TQ144, 12MHz, 32KB flash, 32KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Lattice iCEstick FPGA Evaluation Kit

## Hardware

Platform [Lattice iCE40](../../platforms/lattice-ice40.md): The iCE40 family of ultra-low power, non-volatile FPGAs has five devices with densities ranging from 384 to 7680 Look-Up Tables (LUTs). In addition to LUT-based,low-cost programmable logic, these devices feature Embedded Block RAM (EBR), Non-volatile Configuration Memory (NVCM) and Phase Locked Loops (PLLs). These features allow the devices to be used in low-cost, high-volume consumer and system applications.

| Specification | Value |
|---|---|
| **Microcontroller** | ICE40-HX1K-TQ144 |
| **Frequency** | 12MHz |
| **Flash** | 32KB |
| **RAM** | 32KB |
| **Vendor** | [Lattice](http://www.latticesemi.com/icestick?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `icestick` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:icestick]
platform = lattice_ice40
board = icestick
```

To override a setting of the board manifest [icestick.json](https://github.com/platformio/platform-lattice_ice40/blob/master/boards/icestick.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:icestick]
platform = lattice_ice40
board = icestick

; change microcontroller
board_build.mcu = iCE40-HX1K-TQ144

; change MCU frequency
board_build.f_cpu = 12000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the Lattice iCEstick FPGA Evaluation Kit yet.
