---
title: "Generic STC8G1K12A"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Generic STC8G1K12A (STC8G1K12A, 11MHz, 12KB flash, 1.25KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Generic STC8G1K12A

## Hardware

Platform [Intel MCS-51 (8051)](../../platforms/intel-mcs51.md): The Intel MCS-51 (commonly termed 8051) is an internally Harvard architecture, complex instruction set computer (CISC) instruction set, single chip microcontroller (uC) series developed by Intel in 1980 for use in embedded systems.

| Specification | Value |
|---|---|
| **Microcontroller** | STC8G1K12A |
| **Frequency** | 11MHz |
| **Flash** | 12KB |
| **RAM** | 1.25KB |
| **Vendor** | [STC](http://www.stcmicro.com/stc/stc51.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `STC8G1K12A` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:STC8G1K12A]
platform = intel_mcs51
board = STC8G1K12A
```

To override a setting of the board manifest [STC8G1K12A.json](https://github.com/platformio/platform-intel_mcs51/blob/master/boards/STC8G1K12A.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:STC8G1K12A]
platform = intel_mcs51
board = STC8G1K12A

; change microcontroller
board_build.mcu = stc8g1k12a

; change MCU frequency
board_build.f_cpu = 11059200L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the Generic STC8G1K12A yet.
