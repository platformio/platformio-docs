---
title: "Generic 8051"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Generic 8051 (8051, 11MHz, 4KB flash, 128B RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-intel-mcs51-generic8051"></a>

# Generic 8051

## Hardware

Platform [Intel MCS-51 (8051)](../../platforms/intel-mcs51.md): The Intel MCS-51 (commonly termed 8051) is an internally Harvard architecture, complex instruction set computer (CISC) instruction set, single chip microcontroller (uC) series developed by Intel in 1980 for use in embedded systems.

| Specification | Value |
|---|---|
| **Microcontroller** | 8051 |
| **Frequency** | 11MHz |
| **Flash** | 4KB |
| **RAM** | 128B |
| **Vendor** | [Intel & Licensees](https://en.wikipedia.org/wiki/Intel_8051?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `Generic8051` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:Generic8051]
platform = intel_mcs51
board = Generic8051
```

To override a setting of the board manifest [Generic8051.json](https://github.com/platformio/platform-intel_mcs51/blob/master/boards/Generic8051.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:Generic8051]
platform = intel_mcs51
board = Generic8051

; change microcontroller
board_build.mcu = 8051

; change MCU frequency
board_build.f_cpu = 11059200L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the Generic 8051 yet.
