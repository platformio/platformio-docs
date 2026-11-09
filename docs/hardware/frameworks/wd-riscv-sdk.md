---
title: "WD-Firmware"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "The WD-Firmware framework in PlatformIO: configuration, platforms, debugging and boards."
---

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
| [RVfpga: Digilent Nexys A7](../boards/chipsalliance/swervolf-nexys.md) | [CHIPS Alliance](../platforms/chipsalliance.md) |  | 320MHz | 16MB | 1.16MB |

## Boards

To list the boards from the command line, use [pio boards](../../reference/cli/pio-boards.md).

### Digilent

| Name | Platform | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|---|
| [RVfpga: Digilent Nexys A7](../boards/chipsalliance/swervolf-nexys.md) | [CHIPS Alliance](../platforms/chipsalliance.md) | On-board |  | 320MHz | 16MB | 1.16MB |
