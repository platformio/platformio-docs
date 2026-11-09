---
title: "Generic IRC15W415AS"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-intel-mcs51-irc15w415as"></a>

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

Please use `IRC15W415AS` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:IRC15W415AS]
platform = intel_mcs51
board = IRC15W415AS
```

You can override default Generic IRC15W415AS settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [IRC15W415AS.json](https://github.com/platformio/platform-intel_mcs51/blob/master/boards/IRC15W415AS.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

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

[Debugging](../../../guides/debugging/index.md) currently does not support Generic IRC15W415AS board.
