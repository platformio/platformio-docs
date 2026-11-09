---
title: "Generic MS51XB9AE"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Generic MS51XB9AE (MS51XB9AE, 16MHz, 16KB flash, 1.25KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-intel-mcs51-ms51xb9ae"></a>

# Generic MS51XB9AE

## Hardware

Platform [Intel MCS-51 (8051)](../../platforms/intel-mcs51.md): The Intel MCS-51 (commonly termed 8051) is an internally Harvard architecture, complex instruction set computer (CISC) instruction set, single chip microcontroller (uC) series developed by Intel in 1980 for use in embedded systems.

| Specification | Value |
|---|---|
| **Microcontroller** | MS51XB9AE |
| **Frequency** | 16MHz |
| **Flash** | 16KB |
| **RAM** | 1.25KB |
| **Vendor** | [Nuvoton](https://www.nuvoton.com/products/microcontrollers/8bit-8051-mcus/industrial-8051-series/ms51xb9ae/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `MS51XB9AE` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:MS51XB9AE]
platform = intel_mcs51
board = MS51XB9AE
```

To override a setting of the board manifest [MS51XB9AE.json](https://github.com/platformio/platform-intel_mcs51/blob/master/boards/MS51XB9AE.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:MS51XB9AE]
platform = intel_mcs51
board = MS51XB9AE

; change microcontroller
board_build.mcu = ms51xb9ae

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the Generic MS51XB9AE yet.
