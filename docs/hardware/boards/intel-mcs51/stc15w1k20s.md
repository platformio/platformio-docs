---
title: "Generic STC15W1K20S"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-intel-mcs51-stc15w1k20s"></a>

# Generic STC15W1K20S

## Hardware

Platform [Intel MCS-51 (8051)](../../platforms/intel-mcs51.md): The Intel MCS-51 (commonly termed 8051) is an internally Harvard architecture, complex instruction set computer (CISC) instruction set, single chip microcontroller (uC) series developed by Intel in 1980 for use in embedded systems.

| Specification | Value |
|---|---|
| **Microcontroller** | STC15W1K20S |
| **Frequency** | 11MHz |
| **Flash** | 20KB |
| **RAM** | 1KB |
| **Vendor** | [STC](http://www.stcmicro.com/STC/STC15W1K24S.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `STC15W1K20S` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:STC15W1K20S]
platform = intel_mcs51
board = STC15W1K20S
```

You can override default Generic STC15W1K20S settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [STC15W1K20S.json](https://github.com/platformio/platform-intel_mcs51/blob/master/boards/STC15W1K20S.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:STC15W1K20S]
platform = intel_mcs51
board = STC15W1K20S

; change microcontroller
board_build.mcu = stc15w1k20s

; change MCU frequency
board_build.f_cpu = 11059200L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support Generic STC15W1K20S board.
