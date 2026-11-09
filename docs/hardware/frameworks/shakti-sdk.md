---
title: "Shakti SDK"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
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
| [Artix-7 35T Arty FPGA Evaluation Kit](../boards/shakti/artix7-35t.md) | [Shakti](../platforms/shakti.md) | E-CLASS | 50MHz | 0B | 128KB |
| [Arty A7-100: Artix-7 FPGA Development Board](../boards/shakti/artix7-100t.md) | [Shakti](../platforms/shakti.md) | C-CLASS | 50MHz | 0B | 128MB |
| [Parashu on Artix-7 100T Arty FPGA Evaluation Kit](../boards/shakti/parashu.md) | [Shakti](../platforms/shakti.md) | E-CLASS | 50MHz | 0B | 128KB |
| [Pinaka on Artix-7 35T Arty FPGA Evaluation Kit](../boards/shakti/pinaka.md) | [Shakti](../platforms/shakti.md) | E-CLASS | 50MHz | 0B | 128KB |
| [Vajra on Arty A7-100: Artix-7 FPGA Development Board](../boards/shakti/vajra.md) | [Shakti](../platforms/shakti.md) | C-CLASS | 50MHz | 0B | 128MB |

## Boards

:::note

- You can list pre-configured boards by [pio boards](../../reference/cli/pio-boards.md) command
- For more detailed `board` information please scroll the tables below by horizontally.

:::

### Xilinx

| Name | Platform | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|---|
| [Artix-7 35T Arty FPGA Evaluation Kit](../boards/shakti/artix7-35t.md) | [Shakti](../platforms/shakti.md) | On-board | E-CLASS | 50MHz | 0B | 128KB |
| [Arty A7-100: Artix-7 FPGA Development Board](../boards/shakti/artix7-100t.md) | [Shakti](../platforms/shakti.md) | On-board | C-CLASS | 50MHz | 0B | 128MB |
| [Parashu on Artix-7 100T Arty FPGA Evaluation Kit](../boards/shakti/parashu.md) | [Shakti](../platforms/shakti.md) | On-board | E-CLASS | 50MHz | 0B | 128KB |
| [Pinaka on Artix-7 35T Arty FPGA Evaluation Kit](../boards/shakti/pinaka.md) | [Shakti](../platforms/shakti.md) | On-board | E-CLASS | 50MHz | 0B | 128KB |
| [Vajra on Arty A7-100: Artix-7 FPGA Development Board](../boards/shakti/vajra.md) | [Shakti](../platforms/shakti.md) | On-board | C-CLASS | 50MHz | 0B | 128MB |
