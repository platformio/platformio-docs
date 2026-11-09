---
title: "Generic STC15F205EA"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Generic STC15F205EA (STC15F205EA, 11MHz, 5KB flash, 256B RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Generic STC15F205EA

## Hardware

Platform [Intel MCS-51 (8051)](../../platforms/intel-mcs51.md): The Intel MCS-51 (commonly termed 8051) is an internally Harvard architecture, complex instruction set computer (CISC) instruction set, single chip microcontroller (uC) series developed by Intel in 1980 for use in embedded systems.

| Specification | Value |
|---|---|
| **Microcontroller** | STC15F205EA |
| **Frequency** | 11MHz |
| **Flash** | 5KB |
| **RAM** | 256B |
| **Vendor** | [STC](https://www.stcmicro.com/STC/STC15F204EA.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `STC15F205EA` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:STC15F205EA]
platform = intel_mcs51
board = STC15F205EA
```

To override a setting of the board manifest [STC15F205EA.json](https://github.com/platformio/platform-intel_mcs51/blob/master/boards/STC15F205EA.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:STC15F205EA]
platform = intel_mcs51
board = STC15F205EA

; change microcontroller
board_build.mcu = stc15f205ea

; change MCU frequency
board_build.f_cpu = 11059200L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the Generic STC15F205EA yet.
