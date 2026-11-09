---
title: "GAPuino GAP8"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
displayed_sidebar: "hardware"
---

<a id="board-riscv-gap-gapuino"></a>

# GAPuino GAP8

## Hardware

Platform [RISC-V GAP](../../platforms/riscv-gap.mdx): GreenWaves GAP8 IoT application processor enables the cost-effective development, deployment and autonomous operation of intelligent sensing devices that capture, analyze, classify and act on the fusion of rich data sources such as images, sounds or vibrations.

| Specification | Value |
|---|---|
| **Microcontroller** | GAP8 |
| **Frequency** | 250MHz |
| **Flash** | 64MB |
| **RAM** | 8MB |
| **Vendor** | [GreenWaves Technologies](https://greenwaves-technologies.com/product/gapduino/?utm_source=platformio.org&utm_medium=docs) |

## Configuration

Please use `gapuino` ID for [board](../../../reference/platformio-ini/env/board.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md):

```ini
[env:gapuino]
platform = riscv_gap
board = gapuino
```

You can override default GAPuino GAP8 settings per build environment using `board_***` option, where `***` is a JSON object path from board manifest [gapuino.json](https://github.com/platformio/platform-riscv_gap/blob/master/boards/gapuino.json). For example, `board_build.mcu`, `board_build.f_cpu`, etc.

```ini
[env:gapuino]
platform = riscv_gap
board = gapuino

; change microcontroller
board_build.mcu = gap8

; change MCU frequency
board_build.f_cpu = 250000000L
```

## Debugging

[Debugging](../../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions and configuration information.

:::

You can switch between debugging [Tools & Debug Probes](../../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md).

GAPuino GAP8 has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

| Compatible Tools | On-board | Default |
|---|---|---|
| [FTDI Chip](../../debug-probes/ftdi.md) | Yes | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Mbed](../../frameworks/mbed.mdx) | Arm Mbed OS is a platform operating system designed for the internet of things |
| [PULP OS](../../frameworks/pulp-os.md) | SDK for Greenwaves Technologies' GAP8 IoT Application Processor |
