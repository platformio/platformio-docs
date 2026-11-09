---
title: "IceZUM Alhambra FPGA"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-lattice-ice40-icezum"></a>

# IceZUM Alhambra FPGA

## Hardware

Platform [Lattice iCE40](../../platforms/lattice-ice40.md): The iCE40 family of ultra-low power, non-volatile FPGAs has five devices with densities ranging from 384 to 7680 Look-Up Tables (LUTs). In addition to LUT-based,low-cost programmable logic, these devices feature Embedded Block RAM (EBR), Non-volatile Configuration Memory (NVCM) and Phase Locked Loops (PLLs). These features allow the devices to be used in low-cost, high-volume consumer and system applications.

| Specification | Value |
|---|---|
| **Microcontroller** | ICE40-HX1K-TQ144 |
| **Frequency** | 12MHz |
| **Flash** | 32KB |
| **RAM** | 32KB |
| **Vendor** | [FPGAwars](https://github.com/FPGAwars/icezum/wiki?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `icezum` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:icezum]
platform = lattice_ice40
board = icezum
```

You can override default IceZUM Alhambra FPGA settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [icezum.json](https://github.com/platformio/platform-lattice_ice40/blob/master/boards/icezum.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:icezum]
platform = lattice_ice40
board = icezum

; change microcontroller
board_build.mcu = iCE40-HX1K-TQ144

; change MCU frequency
board_build.f_cpu = 12000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support IceZUM Alhambra FPGA board.
