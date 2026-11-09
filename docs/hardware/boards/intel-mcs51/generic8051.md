---
title: "Generic 8051"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-intel-mcs51-generic8051"></a>

# Generic 8051

## Hardware

Platform [Intel MCS-51 (8051)](../../platforms/intel-mcs51.md): The Intel MCS-51 (commonly termed 8051) is an internally Harvard architecture, complex instruction set computer (CISC) instruction set, single chip microcontroller (uC) series developed by Intel in 1980 for use in embedded systems.

| Specification | Value |
|---|---|
| **Microcontroller** | 8051 |
| **Frequency** | 11MHz |
| **Flash** | 4KB |
| **RAM** | 128B |
| **Vendor** | [Intel & Licensees](https://en.wikipedia.org/wiki/Intel_8051?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `Generic8051` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:Generic8051]
platform = intel_mcs51
board = Generic8051
```

You can override default Generic 8051 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [Generic8051.json](https://github.com/platformio/platform-intel_mcs51/blob/master/boards/Generic8051.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:Generic8051]
platform = intel_mcs51
board = Generic8051

; change microcontroller
board_build.mcu = 8051

; change MCU frequency
board_build.f_cpu = 11059200L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support Generic 8051 board.
