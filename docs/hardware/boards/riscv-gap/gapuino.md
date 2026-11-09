---
title: "GAPuino GAP8"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "GAPuino GAP8 (GAP8, 250MHz, 64MB flash, 8MB RAM): PlatformIO board ID, configuration, uploading and debugging."
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

Use the board ID `gapuino` in the [board](../../../reference/platformio-ini/env/board.md) option of [platformio.ini](../../../reference/platformio-ini/index.md):

```ini
[env:gapuino]
platform = riscv_gap
board = gapuino
```

To override a setting of the board manifest [gapuino.json](https://github.com/platformio/platform-riscv_gap/blob/master/boards/gapuino.json) in a project environment, use an option named `board_` followed by the setting's JSON path, for example `board_build.mcu` or `board_build.f_cpu`:

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

The GAPuino GAP8 has an on-board debug probe: [Debugging](../../../guides/debugging/index.md) works without extra hardware.

Select the probe with the [debug_tool](../../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../../reference/platformio-ini/index.md). If you do not set it, the probe marked as default is used.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

| Compatible probes | On-board | Default |
|---|---|---|
| [FTDI chip](../../debug-probes/ftdi.md) | Yes | Yes |

## Frameworks

| Name | Description |
|---|---|
| [Mbed](../../frameworks/mbed.mdx) | Arm Mbed OS is a platform operating system designed for the internet of things |
| [PULP OS](../../frameworks/pulp-os.md) | SDK for Greenwaves Technologies' GAP8 IoT Application Processor |
