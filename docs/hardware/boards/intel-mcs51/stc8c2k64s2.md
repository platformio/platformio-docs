---
title: "Generic STC8C2K64S2"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Generic STC8C2K64S2 (STC8C2K64S2, 11MHz, 64KB flash, 2.25KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-intel-mcs51-stc8c2k64s2"></a>

# Generic STC8C2K64S2

## Hardware

Platform [Intel MCS-51 (8051)](../../platforms/intel-mcs51.md): The Intel MCS-51 (commonly termed 8051) is an internally Harvard architecture, complex instruction set computer (CISC) instruction set, single chip microcontroller (uC) series developed by Intel in 1980 for use in embedded systems.

| Specification | Value |
|---|---|
| **Microcontroller** | STC8C2K64S2 |
| **Frequency** | 11MHz |
| **Flash** | 64KB |
| **RAM** | 2.25KB |
| **Vendor** | [STC](http://www.stcmicro.com/stc/stc51.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `STC8C2K64S2` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:STC8C2K64S2]
platform = intel_mcs51
board = STC8C2K64S2
```

To override a setting of the board manifest [STC8C2K64S2.json](https://github.com/platformio/platform-intel_mcs51/blob/master/boards/STC8C2K64S2.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:STC8C2K64S2]
platform = intel_mcs51
board = STC8C2K64S2

; change microcontroller
board_build.mcu = stc8c2k64s2

; change MCU frequency
board_build.f_cpu = 11059200L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the Generic STC8C2K64S2 yet.
