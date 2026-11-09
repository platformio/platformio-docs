---
title: "Generic STC15W1K16S"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Generic STC15W1K16S (STC15W1K16S, 11MHz, 16KB flash, 1KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Generic STC15W1K16S

## Hardware

Platform [Intel MCS-51 (8051)](../../platforms/intel-mcs51.md): The Intel MCS-51 (commonly termed 8051) is an internally Harvard architecture, complex instruction set computer (CISC) instruction set, single chip microcontroller (uC) series developed by Intel in 1980 for use in embedded systems.

| Specification | Value |
|---|---|
| **Microcontroller** | STC15W1K16S |
| **Frequency** | 11MHz |
| **Flash** | 16KB |
| **RAM** | 1KB |
| **Vendor** | [STC](http://www.stcmicro.com/STC/STC15W1K24S.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `STC15W1K16S` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:STC15W1K16S]
platform = intel_mcs51
board = STC15W1K16S
```

To override a setting of the board manifest [STC15W1K16S.json](https://github.com/platformio/platform-intel_mcs51/blob/master/boards/STC15W1K16S.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:STC15W1K16S]
platform = intel_mcs51
board = STC15W1K16S

; change microcontroller
board_build.mcu = stc15w1k16s

; change MCU frequency
board_build.f_cpu = 11059200L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the Generic STC15W1K16S yet.
