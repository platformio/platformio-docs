---
title: "Generic STC15F203EA"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-intel-mcs51-stc15f203ea"></a>

# Generic STC15F203EA

## Hardware

Platform [Intel MCS-51 (8051)](../../platforms/intel-mcs51.md): The Intel MCS-51 (commonly termed 8051) is an internally Harvard architecture, complex instruction set computer (CISC) instruction set, single chip microcontroller (uC) series developed by Intel in 1980 for use in embedded systems.

| Specification | Value |
|---|---|
| **Microcontroller** | STC15F203EA |
| **Frequency** | 11MHz |
| **Flash** | 3KB |
| **RAM** | 256B |
| **Vendor** | [STC](https://www.stcmicro.com/STC/STC15F204EA.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `STC15F203EA` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:STC15F203EA]
platform = intel_mcs51
board = STC15F203EA
```

You can override default Generic STC15F203EA settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [STC15F203EA.json](https://github.com/platformio/platform-intel_mcs51/blob/master/boards/STC15F203EA.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:STC15F203EA]
platform = intel_mcs51
board = STC15F203EA

; change microcontroller
board_build.mcu = stc15f203ea

; change MCU frequency
board_build.f_cpu = 11059200L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support Generic STC15F203EA board.
