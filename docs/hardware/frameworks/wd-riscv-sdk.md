---
title: "WD-Firmware"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
---

<a id="framework-wd-riscv-sdk"></a>

# WD-Firmware

**Configuration:** [framework](../../reference/platformio-ini/env/framework.md) = `wd-riscv-sdk`

The WD Firmware package contains Firmware applications and Processor Support Package (PSP) for various cores, alongside demos which support all features.

## Platforms

| Name | Description |
|---|---|
| [CHIPS Alliance](../platforms/chipsalliance.md) | The CHIPS Alliance develops high-quality, open source hardware designs relevant to silicon devices and FPGAs. |

## Examples

- [WD-Firmware for CHIPS Alliance](https://github.com/platformio/platform-chipsalliance/tree/master/examples?utm_source=platformio.org&utm_medium=docs)

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
| [RVfpga: Digilent Nexys A7](../boards/chipsalliance/swervolf-nexys.md) | [CHIPS Alliance](../platforms/chipsalliance.md) |  | 320MHz | 16MB | 1.16MB |

## Boards

:::note

- You can list pre-configured boards by [pio boards](../../reference/cli/pio-boards.md) command
- For more detailed `board` information please scroll the tables below by horizontally.

:::

### Digilent

| Name | Platform | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|---|
| [RVfpga: Digilent Nexys A7](../boards/chipsalliance/swervolf-nexys.md) | [CHIPS Alliance](../platforms/chipsalliance.md) | On-board |  | 320MHz | 16MB | 1.16MB |
