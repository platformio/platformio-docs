---
title: "Generic STC8H2K48T"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Generic STC8H2K48T (STC8H2K48T, 11MHz, 48KB flash, 2.25KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-intel-mcs51-stc8h2k48t"></a>

# Generic STC8H2K48T

## Hardware

Platform [Intel MCS-51 (8051)](../../platforms/intel-mcs51.md): The Intel MCS-51 (commonly termed 8051) is an internally Harvard architecture, complex instruction set computer (CISC) instruction set, single chip microcontroller (uC) series developed by Intel in 1980 for use in embedded systems.

| Specification | Value |
|---|---|
| **Microcontroller** | STC8H2K48T |
| **Frequency** | 11MHz |
| **Flash** | 48KB |
| **RAM** | 2.25KB |
| **Vendor** | [STC](http://www.stcmicro.com/stc/stc51.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `STC8H2K48T` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:STC8H2K48T]
platform = intel_mcs51
board = STC8H2K48T
```

To override a setting of the board manifest [STC8H2K48T.json](https://github.com/platformio/platform-intel_mcs51/blob/master/boards/STC8H2K48T.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:STC8H2K48T]
platform = intel_mcs51
board = STC8H2K48T

; change microcontroller
board_build.mcu = stc8h2k48t

; change MCU frequency
board_build.f_cpu = 11059200L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the Generic STC8H2K48T yet.
