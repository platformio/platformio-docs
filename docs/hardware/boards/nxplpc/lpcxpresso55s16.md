---
title: "NXP LPCXpresso55S16"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-nxplpc-lpcxpresso55s16"></a>

# NXP LPCXpresso55S16

## Hardware

Platform [NXP LPC](../../platforms/nxplpc.md): The NXP LPC is a family of 32-bit microcontroller integrated circuits by NXP Semiconductors. The LPC chips are grouped into related series that are based around the same 32-bit ARM processor core, such as the Cortex-M4F, Cortex-M3, Cortex-M0+, or Cortex-M0. Internally, each microcontroller consists of the processor core, static RAM memory, flash memory, debugging interface, and various peripherals.

| Specification | Value |
|---|---|
| **Microcontroller** | LPC55S16 |
| **Frequency** | 150MHz |
| **Flash** | 256KB |
| **RAM** | 96KB |
| **Vendor** | [NXP](https://www.nxp.com/design/development-boards/lpcxpresso-boards/lpcxpresso55s16-development-board:LPC55S16-EVK?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `lpcxpresso55s16` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:lpcxpresso55s16]
platform = nxplpc
board = lpcxpresso55s16
```

You can override default NXP LPCXpresso55S16 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [lpcxpresso55s16.json](https://github.com/platformio/platform-nxplpc/blob/master/boards/lpcxpresso55s16.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:lpcxpresso55s16]
platform = nxplpc
board = lpcxpresso55s16

; change microcontroller
board_build.mcu = lpc55s16

; change MCU frequency
board_build.f_cpu = 150000000L
```

## Uploading

NXP LPCXpresso55S16 supports the following uploading protocols:

- `jlink`
- `mbed`

Default protocol is `jlink`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:lpcxpresso55s16]
platform = nxplpc
board = lpcxpresso55s16

upload_protocol = jlink
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

NXP LPCXpresso55S16 has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

| Compatible Tools | On-board | Default |
|---|---|---|
| [J-LINK](../../debug-probes/jlink.md) | Yes | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
