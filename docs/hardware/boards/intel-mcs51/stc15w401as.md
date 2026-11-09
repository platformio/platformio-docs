---
title: "Generic STC15W401AS"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Generic STC15W401AS (STC15W401AS, 11MHz, 1KB flash, 512B RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-intel-mcs51-stc15w401as"></a>

# Generic STC15W401AS

## Hardware

Platform [Intel MCS-51 (8051)](../../platforms/intel-mcs51.md): The Intel MCS-51 (commonly termed 8051) is an internally Harvard architecture, complex instruction set computer (CISC) instruction set, single chip microcontroller (uC) series developed by Intel in 1980 for use in embedded systems.

| Specification | Value |
|---|---|
| **Microcontroller** | STC15W401AS |
| **Frequency** | 11MHz |
| **Flash** | 1KB |
| **RAM** | 512B |
| **Vendor** | [STC](https://www.stcmicro.com/STC/STC15W408AS.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `STC15W401AS` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:STC15W401AS]
platform = intel_mcs51
board = STC15W401AS
```

To override a setting of the board manifest [STC15W401AS.json](https://github.com/platformio/platform-intel_mcs51/blob/master/boards/STC15W401AS.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:STC15W401AS]
platform = intel_mcs51
board = STC15W401AS

; change microcontroller
board_build.mcu = stc15w401as

; change MCU frequency
board_build.f_cpu = 11059200L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the Generic STC15W401AS yet.
