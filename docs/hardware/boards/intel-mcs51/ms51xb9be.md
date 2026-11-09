---
title: "Generic MS51XB9BE"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-intel-mcs51-ms51xb9be"></a>

# Generic MS51XB9BE

## Hardware

Platform [Intel MCS-51 (8051)](../../platforms/intel-mcs51.md): The Intel MCS-51 (commonly termed 8051) is an internally Harvard architecture, complex instruction set computer (CISC) instruction set, single chip microcontroller (uC) series developed by Intel in 1980 for use in embedded systems.

| Specification | Value |
|---|---|
| **Microcontroller** | MS51XB9BE |
| **Frequency** | 16MHz |
| **Flash** | 16KB |
| **RAM** | 1.25KB |
| **Vendor** | [Nuvoton](https://www.nuvoton.com/products/microcontrollers/8bit-8051-mcus/industrial-8051-series/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `MS51XB9BE` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:MS51XB9BE]
platform = intel_mcs51
board = MS51XB9BE
```

You can override default Generic MS51XB9BE settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [MS51XB9BE.json](https://github.com/platformio/platform-intel_mcs51/blob/master/boards/MS51XB9BE.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:MS51XB9BE]
platform = intel_mcs51
board = MS51XB9BE

; change microcontroller
board_build.mcu = ms51xb9be

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support Generic MS51XB9BE board.
