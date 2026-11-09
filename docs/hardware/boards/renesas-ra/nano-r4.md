---
title: "Arduino Nano R4"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-renesas-ra-nano-r4"></a>

# Arduino Nano R4

## Hardware

Platform [Renesas RA](../../platforms/renesas-ra.md): Renesas Advanced (RA) 32-bit microcontrollers with the Arm Cortex-M33, -M23 and -M4 processor cores deliver key advantages compared to competitive Arm Cortex-M MCUs by providing stronger embedded security, superior CoreMark performance and ultra-low power operation.

| Specification | Value |
|---|---|
| **Microcontroller** | RA4M1 |
| **Frequency** | 48MHz |
| **Flash** | 256KB |
| **RAM** | 32KB |
| **Vendor** | [Arduino](https://docs.arduino.cc/hardware/nano-r4/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `nano_r4` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:nano_r4]
platform = renesas-ra
board = nano_r4
```

You can override default Arduino Nano R4 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [nano_r4.json](https://github.com/platformio/platform-renesas-ra/blob/master/boards/nano_r4.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:nano_r4]
platform = renesas-ra
board = nano_r4

; change microcontroller
board_build.mcu = ra4m1

; change MCU frequency
board_build.f_cpu = 48000000L
```

## Uploading

Arduino Nano R4 supports the following uploading protocols:

- `cmsis-dap`
- `dfu`
- `jlink`

Default protocol is `dfu`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:nano_r4]
platform = renesas-ra
board = nano_r4

upload_protocol = dfu
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

Arduino Nano R4 does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

| Compatible Tools | On-board | Default |
|---|---|---|
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) |  | Yes |
| [J-LINK](../../debug-probes/jlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [CMSIS](../../frameworks/cmsis.md) | Vendor-independent hardware abstraction layer for the Cortex-M processor series |
| [Renesas Flexible Software Package](../../frameworks/fsp.md) | The Renesas Flexible Software Package (FSP) is an enhanced software package designed to provide easy-to-use, scalable, high-quality software for embedded system designs using Renesas RA family of Arm Microcontrollers. |
