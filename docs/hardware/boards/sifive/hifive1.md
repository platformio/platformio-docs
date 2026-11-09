---
title: "HiFive1"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-sifive-hifive1"></a>

# HiFive1

## Hardware

Platform [SiFive](../../platforms/sifive.md): SiFive brings the power of open source and software automation to the semiconductor industry, making it possible to develop new hardware faster and more affordably than ever before.

| Specification | Value |
|---|---|
| **Microcontroller** | FE310 |
| **Frequency** | 320MHz |
| **Flash** | 16MB |
| **RAM** | 16KB |
| **Vendor** | [SiFive](https://www.sifive.com/products/hifive1/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `hifive1` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:hifive1]
platform = sifive
board = hifive1
```

You can override default HiFive1 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [hifive1.json](https://github.com/platformio/platform-sifive/blob/master/boards/hifive1.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:hifive1]
platform = sifive
board = hifive1

; change microcontroller
board_build.mcu = fe310

; change MCU frequency
board_build.f_cpu = 320000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

HiFive1 has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

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
| [Zephyr](../../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
