---
title: "Generic MS51FC0AE"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Generic MS51FC0AE (MS51FC0AE, 16MHz, 32KB flash, 2.25KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-intel-mcs51-ms51fc0ae"></a>

# Generic MS51FC0AE

## Hardware

Platform [Intel MCS-51 (8051)](../../platforms/intel-mcs51.md): The Intel MCS-51 (commonly termed 8051) is an internally Harvard architecture, complex instruction set computer (CISC) instruction set, single chip microcontroller (uC) series developed by Intel in 1980 for use in embedded systems.

| Specification | Value |
|---|---|
| **Microcontroller** | MS51FC0AE |
| **Frequency** | 16MHz |
| **Flash** | 32KB |
| **RAM** | 2.25KB |
| **Vendor** | [Nuvoton](https://www.nuvoton.com/products/microcontrollers/8bit-8051-mcus/industrial-8051-series/ms51fc0ae/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `MS51FC0AE` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:MS51FC0AE]
platform = intel_mcs51
board = MS51FC0AE
```

To override a setting of the board manifest [MS51FC0AE.json](https://github.com/platformio/platform-intel_mcs51/blob/master/boards/MS51FC0AE.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:MS51FC0AE]
platform = intel_mcs51
board = MS51FC0AE

; change microcontroller
board_build.mcu = ms51fc0ae

; change MCU frequency
board_build.f_cpu = 16000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the Generic MS51FC0AE yet.
