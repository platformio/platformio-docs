---
title: "Generic ML51FB9AE"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Generic ML51FB9AE (ML51FB9AE, 24MHz, 16KB flash, 1.25KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-intel-mcs51-ml51fb9ae"></a>

# Generic ML51FB9AE

## Hardware

Platform [Intel MCS-51 (8051)](../../platforms/intel-mcs51.md): The Intel MCS-51 (commonly termed 8051) is an internally Harvard architecture, complex instruction set computer (CISC) instruction set, single chip microcontroller (uC) series developed by Intel in 1980 for use in embedded systems.

| Specification | Value |
|---|---|
| **Microcontroller** | ML51FB9AE |
| **Frequency** | 24MHz |
| **Flash** | 16KB |
| **RAM** | 1.25KB |
| **Vendor** | [Nuvoton](https://www.nuvoton.com/products/microcontrollers/8bit-8051-mcus/low-power-ml51-series/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `ML51FB9AE` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:ML51FB9AE]
platform = intel_mcs51
board = ML51FB9AE
```

To override a setting of the board manifest [ML51FB9AE.json](https://github.com/platformio/platform-intel_mcs51/blob/master/boards/ML51FB9AE.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:ML51FB9AE]
platform = intel_mcs51
board = ML51FB9AE

; change microcontroller
board_build.mcu = ml51fb9ae

; change MCU frequency
board_build.f_cpu = 24000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the Generic ML51FB9AE yet.
