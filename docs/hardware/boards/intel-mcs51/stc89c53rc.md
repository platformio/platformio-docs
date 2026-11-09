---
title: "Generic STC89C53RC"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-intel-mcs51-stc89c53rc"></a>

# Generic STC89C53RC

## Hardware

Platform [Intel MCS-51 (8051)](../../platforms/intel-mcs51.md): The Intel MCS-51 (commonly termed 8051) is an internally Harvard architecture, complex instruction set computer (CISC) instruction set, single chip microcontroller (uC) series developed by Intel in 1980 for use in embedded systems.

| Specification | Value |
|---|---|
| **Microcontroller** | STC89C53RC |
| **Frequency** | 11MHz |
| **Flash** | 13KB |
| **RAM** | 512B |
| **Vendor** | [STC](https://www.stcmicro.com/STC/STC89C52RC.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `STC89C53RC` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:STC89C53RC]
platform = intel_mcs51
board = STC89C53RC
```

You can override default Generic STC89C53RC settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [STC89C53RC.json](https://github.com/platformio/platform-intel_mcs51/blob/master/boards/STC89C53RC.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:STC89C53RC]
platform = intel_mcs51
board = STC89C53RC

; change microcontroller
board_build.mcu = stc89c53rc

; change MCU frequency
board_build.f_cpu = 11059200L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support Generic STC89C53RC board.
