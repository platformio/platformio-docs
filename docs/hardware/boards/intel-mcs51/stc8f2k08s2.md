---
title: "Generic STC8F2K08S2"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-intel-mcs51-stc8f2k08s2"></a>

# Generic STC8F2K08S2

## Hardware

Platform [Intel MCS-51 (8051)](../../platforms/intel-mcs51.md): The Intel MCS-51 (commonly termed 8051) is an internally Harvard architecture, complex instruction set computer (CISC) instruction set, single chip microcontroller (uC) series developed by Intel in 1980 for use in embedded systems.

| Specification | Value |
|---|---|
| **Microcontroller** | STC8F2K08S2 |
| **Frequency** | 11MHz |
| **Flash** | 8KB |
| **RAM** | 2.25KB |
| **Vendor** | [STC](http://www.stcmicro.com/STC/STC8F1K08S2.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `STC8F2K08S2` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:STC8F2K08S2]
platform = intel_mcs51
board = STC8F2K08S2
```

You can override default Generic STC8F2K08S2 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [STC8F2K08S2.json](https://github.com/platformio/platform-intel_mcs51/blob/master/boards/STC8F2K08S2.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:STC8F2K08S2]
platform = intel_mcs51
board = STC8F2K08S2

; change microcontroller
board_build.mcu = stc8f2k08s2

; change MCU frequency
board_build.f_cpu = 11059200L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support Generic STC8F2K08S2 board.
