---
title: "Generic IRC15W1K31S"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "Generic IRC15W1K31S (IRC15W1K31S, 11MHz, 31.50KB flash, 1KB RAM): PlatformIO board ID, configuration, uploading and debugging."
displayed_sidebar: "hardware"
---

<a id="board-intel-mcs51-irc15w1k31s"></a>

# Generic IRC15W1K31S

## Hardware

Platform [Intel MCS-51 (8051)](../../platforms/intel-mcs51.md): The Intel MCS-51 (commonly termed 8051) is an internally Harvard architecture, complex instruction set computer (CISC) instruction set, single chip microcontroller (uC) series developed by Intel in 1980 for use in embedded systems.

| Specification | Value |
|---|---|
| **Microcontroller** | IRC15W1K31S |
| **Frequency** | 11MHz |
| **Flash** | 31.50KB |
| **RAM** | 1KB |
| **Vendor** | [STC](http://www.stcmicro.com/STC/STC15W1K24S.html?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Use the board ID `IRC15W1K31S` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:IRC15W1K31S]
platform = intel_mcs51
board = IRC15W1K31S
```

To override a setting of the board manifest [IRC15W1K31S.json](https://github.com/platformio/platform-intel_mcs51/blob/master/boards/IRC15W1K31S.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

```ini
[env:IRC15W1K31S]
platform = intel_mcs51
board = IRC15W1K31S

; change microcontroller
board_build.mcu = irc15w1k31s

; change MCU frequency
board_build.f_cpu = 11059200L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) does not support the Generic IRC15W1K31S yet.
