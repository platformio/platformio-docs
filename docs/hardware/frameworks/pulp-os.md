---
title: "PULP OS"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "The PULP OS framework in PlatformIO: configuration, platforms, debugging and boards."
---

<a id="framework-pulp-os"></a>

# PULP OS

**Configuration:** [framework](../../reference/platformio-ini/env/framework.md) = `pulp-os`

SDK for Greenwaves Technologies' GAP8 IoT Application Processor

## Platforms

| Name | Description |
|---|---|
| [RISC-V GAP](../platforms/riscv-gap.mdx) | GreenWaves GAP8 IoT application processor enables the cost-effective development, deployment and autonomous operation of intelligent sensing devices that capture, analyze, classify and act on the fusion of rich data sources such as images, sounds or vibrations. |

## Examples

- [PULP OS for RISC-V GAP](https://github.com/platformio/platform-riscv_gap/tree/master/examples?utm_source=platformio.org&utm_medium=docs)

## Debugging

[Debugging](../../guides/debugging/index.md) works with the boards below without extra configuration.

### Debug probes

Select a [debug probe](../../guides/debugging/index.md#debugging-tools) with the [debug_tool](../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../reference/platformio-ini/index.md). Each board's page lists its compatible probes.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

#### Boards with an on-board debug probe

These boards are ready for debugging; no external probe is needed.

| Name | Platform | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [GAPuino GAP8](../boards/riscv-gap/gapuino.md) | [RISC-V GAP](../platforms/riscv-gap.mdx) | GAP8 | 250MHz | 64MB | 8MB |

## Boards

To list the boards from the command line, use [pio boards](../../reference/cli/pio-boards.md).

### GreenWaves Technologies

| Name | Platform | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|---|
| [GAPuino GAP8](../boards/riscv-gap/gapuino.md) | [RISC-V GAP](../platforms/riscv-gap.mdx) | On-board | GAP8 | 250MHz | 64MB | 8MB |
