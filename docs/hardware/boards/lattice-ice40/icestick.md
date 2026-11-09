---
title: "Lattice iCEstick FPGA Evaluation Kit"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-lattice-ice40-icestick"></a>

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

Please use `icestick` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:icestick]
platform = lattice_ice40
board = icestick
```

You can override default Lattice iCEstick FPGA Evaluation Kit settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [icestick.json](https://github.com/platformio/platform-lattice_ice40/blob/master/boards/icestick.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

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

[Debugging](../../../guides/debugging/index.md) currently does not support Lattice iCEstick FPGA Evaluation Kit board.
