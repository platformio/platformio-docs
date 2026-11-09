---
description: "A custom board MCU (platformio.ini option board_build.mcu)."
---

# `board_build.mcu` {#board-build-mcu}

- **Type:** String
- **Multiple values:** No
- **Deprecated name:** `board_mcu` (still accepted, with a warning)

`board_build.mcu` is a microcontroller(MCU) type that is used by compiler to recognize MCU architecture. The correct type of `board_build.mcu` depends on platform library. For example, the list of `board_build.mcu` for "megaAVR Devices" is described [here](http://www.nongnu.org/avr-libc/user-manual/).

The full list of `board_build.mcu` for the popular embedded platforms you can find in *Boards* section of [Development Platforms](../../../hardware/platforms/index.md). See "Microcontroller" column.
