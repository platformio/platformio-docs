---
title: "Generic STC8A8K60D4"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-intel-mcs51-stc8a8k60d4"></a>

# Generic STC8A8K60D4

## Hardware

Platform [Intel MCS-51 (8051)](../../platforms/intel-mcs51.md): The Intel MCS-51 (commonly termed 8051) is an internally Harvard architecture, complex instruction set computer (CISC) instruction set, single chip microcontroller (uC) series developed by Intel in 1980 for use in embedded systems.

| Specification | Value |
|---|---|
| **Microcontroller** | STC8A8K60D4 |
| **Frequency** | 11MHz |
| **Flash** | 60KB |
| **RAM** | 8.25KB |
| **Vendor** | [STC](http://www.stcmicro.com/stc/stc51.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `STC8A8K60D4` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:STC8A8K60D4]
platform = intel_mcs51
board = STC8A8K60D4
```

You can override default Generic STC8A8K60D4 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [STC8A8K60D4.json](https://github.com/platformio/platform-intel_mcs51/blob/master/boards/STC8A8K60D4.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:STC8A8K60D4]
platform = intel_mcs51
board = STC8A8K60D4

; change microcontroller
board_build.mcu = stc8a8k60d4

; change MCU frequency
board_build.f_cpu = 11059200L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support Generic STC8A8K60D4 board.
