---
title: "Generic IAP15F2K61S"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Generic IAP15F2K61S (IAP15F2K61S, 11MHz, 61KB flash, 2KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Generic IAP15F2K61S

## Hardware

Platform [Intel MCS-51 (8051)](../../platforms/intel-mcs51.md): The Intel MCS-51 (commonly termed 8051) is an internally Harvard architecture, complex instruction set computer (CISC) instruction set, single chip microcontroller (uC) series developed by Intel in 1980 for use in embedded systems.

| Specification | Value |
|---|---|
| **Microcontroller** | IAP15F2K61S |
| **Frequency** | 11MHz |
| **Flash** | 61KB |
| **RAM** | 2KB |
| **Vendor** | [STC](http://www.stcmicro.com/STC/STC15F2K32S2.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `IAP15F2K61S` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:IAP15F2K61S]
platform = intel_mcs51
board = IAP15F2K61S
```

To override a setting of the board manifest [IAP15F2K61S.json](https://github.com/platformio/platform-intel_mcs51/blob/master/boards/IAP15F2K61S.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:IAP15F2K61S]
platform = intel_mcs51
board = IAP15F2K61S

; change microcontroller
board_build.mcu = iap15f2k61s

; change MCU frequency
board_build.f_cpu = 11059200L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the Generic IAP15F2K61S yet.
