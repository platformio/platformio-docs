---
title: "Generic STC89C54RD+"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Generic STC89C54RD+ (STC89C54RD+, 11MHz, 16KB flash, 1.25KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Generic STC89C54RD+

## Hardware

Platform [Intel MCS-51 (8051)](../../platforms/intel-mcs51.md): The Intel MCS-51 (commonly termed 8051) is an internally Harvard architecture, complex instruction set computer (CISC) instruction set, single chip microcontroller (uC) series developed by Intel in 1980 for use in embedded systems.

| Specification | Value |
|---|---|
| **Microcontroller** | STC89C54RD+ |
| **Frequency** | 11MHz |
| **Flash** | 16KB |
| **RAM** | 1.25KB |
| **Vendor** | [STC](https://www.stcmicro.com/STC/STC89C52RC.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `STC89C54RD+` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:STC89C54RD+]
platform = intel_mcs51
board = STC89C54RD+
```

To override a setting of the board manifest [STC89C54RD+.json](https://github.com/platformio/platform-intel_mcs51/blob/master/boards/STC89C54RD+.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:STC89C54RD+]
platform = intel_mcs51
board = STC89C54RD+

; change microcontroller
board_build.mcu = stc89c54rd+

; change MCU frequency
board_build.f_cpu = 11059200L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the Generic STC89C54RD+ yet.
