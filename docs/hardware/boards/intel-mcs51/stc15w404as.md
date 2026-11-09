---
title: "Generic STC15W404AS"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-intel-mcs51-stc15w404as"></a>

# Generic STC15W404AS

## Hardware

Platform [Intel MCS-51 (8051)](../../platforms/intel-mcs51.md): The Intel MCS-51 (commonly termed 8051) is an internally Harvard architecture, complex instruction set computer (CISC) instruction set, single chip microcontroller (uC) series developed by Intel in 1980 for use in embedded systems.

| Specification | Value |
|---|---|
| **Microcontroller** | STC15W404AS |
| **Frequency** | 11MHz |
| **Flash** | 4KB |
| **RAM** | 512B |
| **Vendor** | [STC](https://www.stcmicro.com/STC/STC15W408AS.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `STC15W404AS` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:STC15W404AS]
platform = intel_mcs51
board = STC15W404AS
```

You can override default Generic STC15W404AS settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [STC15W404AS.json](https://github.com/platformio/platform-intel_mcs51/blob/master/boards/STC15W404AS.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:STC15W404AS]
platform = intel_mcs51
board = STC15W404AS

; change microcontroller
board_build.mcu = stc15w404as

; change MCU frequency
board_build.f_cpu = 11059200L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) currently does not support Generic STC15W404AS board.
