---
title: "Generic ML51TD1AE"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-intel-mcs51-ml51td1ae"></a>

# Generic ML51TD1AE

## Hardware

Platform [Intel MCS-51 (8051)](../../platforms/intel-mcs51.md): The Intel MCS-51 (commonly termed 8051) is an internally Harvard architecture, complex instruction set computer (CISC) instruction set, single chip microcontroller (uC) series developed by Intel in 1980 for use in embedded systems.

| Specification | Value |
|---|---|
| **Microcontroller** | ML51TD1AE |
| **Frequency** | 24MHz |
| **Flash** | 64KB |
| **RAM** | 4.25KB |
| **Vendor** | [Nuvoton](https://www.nuvoton.com/products/microcontrollers/8bit-8051-mcus/low-power-ml51-series/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `ML51TD1AE` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:ML51TD1AE]
platform = intel_mcs51
board = ML51TD1AE
```

You can override default Generic ML51TD1AE settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [ML51TD1AE.json](https://github.com/platformio/platform-intel_mcs51/blob/master/boards/ML51TD1AE.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:ML51TD1AE]
platform = intel_mcs51
board = ML51TD1AE

; change microcontroller
board_build.mcu = ml51td1ae

; change MCU frequency
board_build.f_cpu = 24000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support Generic ML51TD1AE board.
