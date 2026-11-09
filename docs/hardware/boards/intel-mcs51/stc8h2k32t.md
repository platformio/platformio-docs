---
title: "Generic STC8H2K32T"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-intel-mcs51-stc8h2k32t"></a>

# Generic STC8H2K32T

## Hardware

Platform [Intel MCS-51 (8051)](../../platforms/intel-mcs51.md): The Intel MCS-51 (commonly termed 8051) is an internally Harvard architecture, complex instruction set computer (CISC) instruction set, single chip microcontroller (uC) series developed by Intel in 1980 for use in embedded systems.

| Specification | Value |
|---|---|
| **Microcontroller** | STC8H2K32T |
| **Frequency** | 11MHz |
| **Flash** | 32KB |
| **RAM** | 2.25KB |
| **Vendor** | [STC](http://www.stcmicro.com/stc/stc51.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `STC8H2K32T` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:STC8H2K32T]
platform = intel_mcs51
board = STC8H2K32T
```

You can override default Generic STC8H2K32T settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [STC8H2K32T.json](https://github.com/platformio/platform-intel_mcs51/blob/master/boards/STC8H2K32T.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:STC8H2K32T]
platform = intel_mcs51
board = STC8H2K32T

; change microcontroller
board_build.mcu = stc8h2k32t

; change MCU frequency
board_build.f_cpu = 11059200L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support Generic STC8H2K32T board.
