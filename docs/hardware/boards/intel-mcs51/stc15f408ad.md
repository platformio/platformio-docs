---
title: "Generic STC15F408AD"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Generic STC15F408AD (STC15F408AD, 11MHz, 8KB flash, 512B RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Generic STC15F408AD

## Hardware

Platform [Intel MCS-51 (8051)](../../platforms/intel-mcs51.md): The Intel MCS-51 (commonly termed 8051) is an internally Harvard architecture, complex instruction set computer (CISC) instruction set, single chip microcontroller (uC) series developed by Intel in 1980 for use in embedded systems.

| Specification | Value |
|---|---|
| **Microcontroller** | STC15F408AD |
| **Frequency** | 11MHz |
| **Flash** | 8KB |
| **RAM** | 512B |
| **Vendor** | [STC](http://www.stcmicro.com/STC/STC15F408AD.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `STC15F408AD` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:STC15F408AD]
platform = intel_mcs51
board = STC15F408AD
```

To override a setting of the board manifest [STC15F408AD.json](https://github.com/platformio/platform-intel_mcs51/blob/master/boards/STC15F408AD.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:STC15F408AD]
platform = intel_mcs51
board = STC15F408AD

; change microcontroller
board_build.mcu = stc15f408ad

; change MCU frequency
board_build.f_cpu = 11059200L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the Generic STC15F408AD yet.
