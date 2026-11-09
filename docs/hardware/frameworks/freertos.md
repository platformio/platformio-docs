---
title: "FreeRTOS"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "The FreeRTOS framework in PlatformIO: configuration, platforms, debugging and boards."
---

# FreeRTOS

**Configuration:** [framework](../../reference/platformio-ini/env/framework.md) = `freertos`

FreeRTOS is a real-time operating system kernel for embedded devices that has been ported to 40 microcontroller platforms.

## Platforms

| Name | Description |
|---|---|
| [CHIPS Alliance](../platforms/chipsalliance.md) | The CHIPS Alliance develops high-quality, open source hardware designs relevant to silicon devices and FPGAs. |
| [SiFive](../platforms/sifive.md) | SiFive brings the power of open source and software automation to the semiconductor industry, making it possible to develop new hardware faster and more affordably than ever before. |

## Examples

- [FreeRTOS for CHIPS Alliance](https://github.com/platformio/platform-chipsalliance/tree/master/examples?utm_source=platformio.org&utm_medium=docs)
- [FreeRTOS for SiFive](https://github.com/platformio/platform-sifive/tree/master/examples?utm_source=platformio.org&utm_medium=docs)

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
| [Arty FPGA Dev Kit](../boards/sifive/e310-arty.md) | [SiFive](../platforms/sifive.md) | FE310 | 450MHz | 16MB | 256MB |
| [HiFive Unleashed](../boards/sifive/hifive-unleashed.md) | [SiFive](../platforms/sifive.md) | FU540 | 1500MHz | 32MB | 8GB |
| [HiFive1](../boards/sifive/hifive1.md) | [SiFive](../platforms/sifive.md) | FE310 | 320MHz | 16MB | 16KB |
| [HiFive1 Rev B](../boards/sifive/hifive1-revb.md) | [SiFive](../platforms/sifive.md) | FE310 | 320MHz | 16MB | 16KB |
| [RVfpga: Digilent Nexys A7](../boards/chipsalliance/swervolf-nexys.md) | [CHIPS Alliance](../platforms/chipsalliance.md) |  | 320MHz | 16MB | 1.16MB |
| [SparkFun RED-V RedBoard](../boards/sifive/sparkfun-redboard-v.md) | [SiFive](../platforms/sifive.md) | FE310 | 320MHz | 16MB | 16KB |
| [SparkFun RED-V Thing Plus](../boards/sifive/sparkfun-thing-plus-v.md) | [SiFive](../platforms/sifive.md) | FE310 | 320MHz | 16MB | 16KB |

## Boards

To list the boards from the command line, use [pio boards](../../reference/cli/pio-boards.md).

### Digilent

| Name | Platform | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|---|
| [RVfpga: Digilent Nexys A7](../boards/chipsalliance/swervolf-nexys.md) | [CHIPS Alliance](../platforms/chipsalliance.md) | On-board |  | 320MHz | 16MB | 1.16MB |

### SiFive

| Name | Platform | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|---|
| [HiFive Unleashed](../boards/sifive/hifive-unleashed.md) | [SiFive](../platforms/sifive.md) | On-board | FU540 | 1500MHz | 32MB | 8GB |
| [HiFive1](../boards/sifive/hifive1.md) | [SiFive](../platforms/sifive.md) | On-board | FE310 | 320MHz | 16MB | 16KB |
| [HiFive1 Rev B](../boards/sifive/hifive1-revb.md) | [SiFive](../platforms/sifive.md) | On-board | FE310 | 320MHz | 16MB | 16KB |

### SparkFun

| Name | Platform | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|---|
| [SparkFun RED-V RedBoard](../boards/sifive/sparkfun-redboard-v.md) | [SiFive](../platforms/sifive.md) | On-board | FE310 | 320MHz | 16MB | 16KB |
| [SparkFun RED-V Thing Plus](../boards/sifive/sparkfun-thing-plus-v.md) | [SiFive](../platforms/sifive.md) | On-board | FE310 | 320MHz | 16MB | 16KB |

### Xilinx

| Name | Platform | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|---|
| [Arty FPGA Dev Kit](../boards/sifive/e310-arty.md) | [SiFive](../platforms/sifive.md) | On-board | FE310 | 450MHz | 16MB | 256MB |
