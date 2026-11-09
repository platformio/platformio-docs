---
title: "HiFive Unleashed"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-sifive-hifive-unleashed"></a>

# HiFive Unleashed

## Hardware

Platform [SiFive](../../platforms/sifive.md): SiFive brings the power of open source and software automation to the semiconductor industry, making it possible to develop new hardware faster and more affordably than ever before.

| Specification | Value |
|---|---|
| **Microcontroller** | FU540 |
| **Frequency** | 1500MHz |
| **Flash** | 32MB |
| **RAM** | 8GB |
| **Vendor** | [SiFive](https://www.sifive.com/boards/hifive-unleashed?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `hifive-unleashed` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:hifive-unleashed]
platform = sifive
board = hifive-unleashed
```

You can override default HiFive Unleashed settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [hifive-unleashed.json](https://github.com/platformio/platform-sifive/blob/master/boards/hifive-unleashed.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:hifive-unleashed]
platform = sifive
board = hifive-unleashed

; change microcontroller
board_build.mcu = fu540

; change MCU frequency
board_build.f_cpu = 1500000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

HiFive Unleashed has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

| Compatible Tools | On-board | Default |
|---|---|---|
| [FTDI Chip](../../debug-probes/ftdi.md) | Yes | Yes |
| [QEMU](../../debug-probes/qemu.md) | Yes |  |
| [Renode](../../debug-probes/renode.md) | Yes |  |

## Frameworks

| Name | Description |
|---|---|
| [Freedom E SDK](../../frameworks/freedom-e-sdk.mdx) | Open Source Software for Developing on the SiFive Freedom E Platform |
| [FreeRTOS](../../frameworks/freertos.md) | FreeRTOS is a real-time operating system kernel for embedded devices that has been ported to 40 microcontroller platforms. |
