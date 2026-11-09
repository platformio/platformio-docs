---
title: "Shakti SDK"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "The Shakti SDK framework in PlatformIO: configuration, platforms, debugging and boards."
---

<a id="framework-shakti-sdk"></a>

# Shakti SDK

**Configuration:** [framework](../../reference/platformio-ini/env/framework.md) = `shakti-sdk`

A software development kit for developing applications on Shakti class of processors

## Platforms

| Name | Description |
|---|---|
| [Shakti](../platforms/shakti.md) | Shakti is an open-source initiative by the RISE group at IIT-Madras, which is not only building open source, production grade processors, but also associated components like interconnect fabrics, verification tools, storage controllers, peripheral IPs and SOC tools. |

## Examples

- [Shakti SDK for Shakti](https://github.com/platformio/platform-shakti/tree/master/examples?utm_source=platformio.org&utm_medium=docs)

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
| [Artix-7 35T Arty FPGA Evaluation Kit](../boards/shakti/artix7-35t.md) | [Shakti](../platforms/shakti.md) | E-CLASS | 50MHz | 0B | 128KB |
| [Arty A7-100: Artix-7 FPGA Development Board](../boards/shakti/artix7-100t.md) | [Shakti](../platforms/shakti.md) | C-CLASS | 50MHz | 0B | 128MB |
| [Parashu on Artix-7 100T Arty FPGA Evaluation Kit](../boards/shakti/parashu.md) | [Shakti](../platforms/shakti.md) | E-CLASS | 50MHz | 0B | 128KB |
| [Pinaka on Artix-7 35T Arty FPGA Evaluation Kit](../boards/shakti/pinaka.md) | [Shakti](../platforms/shakti.md) | E-CLASS | 50MHz | 0B | 128KB |
| [Vajra on Arty A7-100: Artix-7 FPGA Development Board](../boards/shakti/vajra.md) | [Shakti](../platforms/shakti.md) | C-CLASS | 50MHz | 0B | 128MB |

## Boards

To list the boards from the command line, use [pio boards](../../reference/cli/pio-boards.md).

### Xilinx

| Name | Platform | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|---|
| [Artix-7 35T Arty FPGA Evaluation Kit](../boards/shakti/artix7-35t.md) | [Shakti](../platforms/shakti.md) | On-board | E-CLASS | 50MHz | 0B | 128KB |
| [Arty A7-100: Artix-7 FPGA Development Board](../boards/shakti/artix7-100t.md) | [Shakti](../platforms/shakti.md) | On-board | C-CLASS | 50MHz | 0B | 128MB |
| [Parashu on Artix-7 100T Arty FPGA Evaluation Kit](../boards/shakti/parashu.md) | [Shakti](../platforms/shakti.md) | On-board | E-CLASS | 50MHz | 0B | 128KB |
| [Pinaka on Artix-7 35T Arty FPGA Evaluation Kit](../boards/shakti/pinaka.md) | [Shakti](../platforms/shakti.md) | On-board | E-CLASS | 50MHz | 0B | 128KB |
| [Vajra on Arty A7-100: Artix-7 FPGA Development Board](../boards/shakti/vajra.md) | [Shakti](../platforms/shakti.md) | On-board | C-CLASS | 50MHz | 0B | 128MB |
