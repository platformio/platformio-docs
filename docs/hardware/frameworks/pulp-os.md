---
title: "PULP OS"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
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

[Debugging](../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

### Tools & Debug Probes

Supported debugging tools are listed in "Debug" column. For more detailed information, please scroll table by horizontal. You can switch between debugging [Tools & Debug Probes](../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md).

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions.

:::

#### On-Board Debug Tools

Boards listed below have on-board debug probe and **ARE READY** for debugging! You do not need to use/buy external debug probe.

| Name | Platform | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [GAPuino GAP8](../boards/riscv-gap/gapuino.md) | [RISC-V GAP](../platforms/riscv-gap.mdx) | GAP8 | 250MHz | 64MB | 8MB |

## Boards

:::note

- You can list pre-configured boards by [pio boards](../../reference/cli/pio-boards.md) command
- For more detailed `board` information please scroll the tables below by horizontally.

:::

### GreenWaves Technologies

| Name | Platform | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|---|
| [GAPuino GAP8](../boards/riscv-gap/gapuino.md) | [RISC-V GAP](../platforms/riscv-gap.mdx) | On-board | GAP8 | 250MHz | 64MB | 8MB |
