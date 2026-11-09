---
title: "PULP Runtime Environment"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "The PULP Runtime Environment framework in PlatformIO: configuration, platforms, debugging and boards."
---

# PULP Runtime Environment

**Configuration:** [framework](../../reference/platformio-ini/env/framework.md) = `pulp-runtime`

Runtime Environment for Parallel Ultra Low Power platform

## Platforms

| Name | Description |
|---|---|
| [OpenHW Group](../platforms/openhw.md) | OpenHW Group is a not-for-profit, global organization that provides an infrastructure for hosting high quality open-source HW developments in line with industry best practices. The OpenHW CV32E40P RISC-V core is the first open-source core for high-volume chips verified with the state-of-the-art process required for high-integrity, commercial SoCs. |

## Examples

- [PULP Runtime Environment for OpenHW Group](https://github.com/platformio/platform-openhw/tree/master/examples?utm_source=platformio.org&utm_medium=docs)

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
| [Digilent Nexys A7](../boards/openhw/nexys-a7.md) | [OpenHW Group](../platforms/openhw.md) |  | 320MHz | 16MB | 1.16MB |

## Boards

To list the boards from the command line, use [pio boards](../../reference/cli/pio-boards.md).

### Digilent

| Name | Platform | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|---|
| [Digilent Nexys A7](../boards/openhw/nexys-a7.md) | [OpenHW Group](../platforms/openhw.md) | On-board |  | 320MHz | 16MB | 1.16MB |
