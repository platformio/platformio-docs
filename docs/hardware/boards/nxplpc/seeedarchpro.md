---
title: "Seeed Arch Pro"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-nxplpc-seeedarchpro"></a>

# Seeed Arch Pro

## Hardware

Platform [NXP LPC](../../platforms/nxplpc.md): The NXP LPC is a family of 32-bit microcontroller integrated circuits by NXP Semiconductors. The LPC chips are grouped into related series that are based around the same 32-bit ARM processor core, such as the Cortex-M4F, Cortex-M3, Cortex-M0+, or Cortex-M0. Internally, each microcontroller consists of the processor core, static RAM memory, flash memory, debugging interface, and various peripherals.

| Specification | Value |
|---|---|
| **Microcontroller** | LPC1768 |
| **Frequency** | 96MHz |
| **Flash** | 512KB |
| **RAM** | 64KB |
| **Vendor** | [SeeedStudio](https://developer.mbed.org/platforms/Seeeduino-Arch-Pro/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `seeedArchPro` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:seeedArchPro]
platform = nxplpc
board = seeedArchPro
```

You can override default Seeed Arch Pro settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [seeedArchPro.json](https://github.com/platformio/platform-nxplpc/blob/master/boards/seeedArchPro.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:seeedArchPro]
platform = nxplpc
board = seeedArchPro

; change microcontroller
board_build.mcu = lpc1768

; change MCU frequency
board_build.f_cpu = 96000000L
```

## Uploading

Seeed Arch Pro supports the following uploading protocols:

- `cmsis-dap`
- `mbed`

Default protocol is `mbed`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:seeedArchPro]
platform = nxplpc
board = seeedArchPro

upload_protocol = mbed
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

Seeed Arch Pro has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

| Compatible Tools | On-board | Default |
|---|---|---|
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) | Yes | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Mbed](../../frameworks/mbed.mdx) | Arm Mbed OS is a platform operating system designed for the internet of things |
