---
title: "Generic IRC15W415AS"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Generic IRC15W415AS (IRC15W415AS, 11MHz, 15.50KB flash, 512B RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

# Generic IRC15W415AS

## Hardware

Platform [Intel MCS-51 (8051)](../../platforms/intel-mcs51.md): The Intel MCS-51 (commonly termed 8051) is an internally Harvard architecture, complex instruction set computer (CISC) instruction set, single chip microcontroller (uC) series developed by Intel in 1980 for use in embedded systems.

| Specification | Value |
|---|---|
| **Microcontroller** | IRC15W415AS |
| **Frequency** | 11MHz |
| **Flash** | 15.50KB |
| **RAM** | 512B |
| **Vendor** | [STC](https://www.stcmicro.com/STC/STC15W408AS.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `IRC15W415AS` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:IRC15W415AS]
platform = intel_mcs51
board = IRC15W415AS
```

To override a setting of the board manifest [IRC15W415AS.json](https://github.com/platformio/platform-intel_mcs51/blob/master/boards/IRC15W415AS.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:IRC15W415AS]
platform = intel_mcs51
board = IRC15W415AS

; change microcontroller
board_build.mcu = irc15w415as

; change MCU frequency
board_build.f_cpu = 11059200L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the Generic IRC15W415AS yet.
