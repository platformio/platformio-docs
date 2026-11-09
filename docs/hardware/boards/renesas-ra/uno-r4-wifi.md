---
title: "Arduino Uno R4 WiFi"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-renesas-ra-uno-r4-wifi"></a>

# Arduino Uno R4 WiFi

## Hardware

Platform [Renesas RA](../../platforms/renesas-ra.md): Renesas Advanced (RA) 32-bit microcontrollers with the Arm Cortex-M33, -M23 and -M4 processor cores deliver key advantages compared to competitive Arm Cortex-M MCUs by providing stronger embedded security, superior CoreMark performance and ultra-low power operation.

| Specification | Value |
|---|---|
| **Microcontroller** | RA4M1 |
| **Frequency** | 48MHz |
| **Flash** | 256KB |
| **RAM** | 32KB |
| **Vendor** | [Arduino](https://docs.arduino.cc/hardware/uno-r4-wifi?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `uno_r4_wifi` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:uno_r4_wifi]
platform = renesas-ra
board = uno_r4_wifi
```

You can override default Arduino Uno R4 WiFi settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [uno_r4_wifi.json](https://github.com/platformio/platform-renesas-ra/blob/master/boards/uno_r4_wifi.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:uno_r4_wifi]
platform = renesas-ra
board = uno_r4_wifi

; change microcontroller
board_build.mcu = ra4m1

; change MCU frequency
board_build.f_cpu = 48000000L
```

## Uploading

Arduino Uno R4 WiFi supports the following uploading protocols:

- `cmsis-dap`
- `jlink`
- `sam-ba`

Default protocol is `sam-ba`

You can change upload protocol using [upload_protocol](../../../reference/platformio-ini/env/upload-protocol.md) option:

```ini
[env:uno_r4_wifi]
platform = renesas-ra
board = uno_r4_wifi

upload_protocol = sam-ba
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

Arduino Uno R4 WiFi has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

| Compatible Tools | On-board | Default |
|---|---|---|
| [CMSIS-DAP](../../debug-probes/cmsis-dap.md) | Yes | Yes |
| [J-LINK](../../debug-probes/jlink.md) |  |  |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [CMSIS](../../frameworks/cmsis.md) | Vendor-independent hardware abstraction layer for the Cortex-M processor series |
| [Renesas Flexible Software Package](../../frameworks/fsp.md) | The Renesas Flexible Software Package (FSP) is an enhanced software package designed to provide easy-to-use, scalable, high-quality software for embedded system designs using Renesas RA family of Arm Microcontrollers. |
