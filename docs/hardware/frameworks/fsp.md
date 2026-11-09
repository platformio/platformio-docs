---
title: "Renesas Flexible Software Package"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "The Renesas Flexible Software Package framework in PlatformIO: configuration, platforms, debugging and boards."
---

<a id="framework-fsp"></a>

# Renesas Flexible Software Package

**Configuration:** [framework](../../reference/platformio-ini/env/framework.md) = `fsp`

The Renesas Flexible Software Package (FSP) is an enhanced software package designed to provide easy-to-use, scalable, high-quality software for embedded system designs using Renesas RA family of Arm Microcontrollers.

## Platforms

| Name | Description |
|---|---|
| [Renesas RA](../platforms/renesas-ra.md) | Renesas Advanced (RA) 32-bit microcontrollers with the Arm Cortex-M33, -M23 and -M4 processor cores deliver key advantages compared to competitive Arm Cortex-M MCUs by providing stronger embedded security, superior CoreMark performance and ultra-low power operation. |

## Examples

- [Renesas Flexible Software Package for Renesas RA](https://github.com/platformio/platform-renesas-ra/tree/master/examples?utm_source=platformio.org&utm_medium=docs)

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
| [Arduino Uno R4 WiFi](../boards/renesas-ra/uno-r4-wifi.md) | [Renesas RA](../platforms/renesas-ra.md) | RA4M1 | 48MHz | 256KB | 32KB |

#### Boards that need an external debug probe

These boards support [Debugging](../../guides/debugging/index.md) with an external debug probe. See each board's page for the compatible probes.

| Name | Platform | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Arduino Nano R4](../boards/renesas-ra/nano-r4.md) | [Renesas RA](../platforms/renesas-ra.md) | RA4M1 | 48MHz | 256KB | 32KB |
| [Arduino Portenta C33](../boards/renesas-ra/portenta-c33.md) | [Renesas RA](../platforms/renesas-ra.md) | R7FA6M5BH2CBG | 200MHz | 2MB | 511.35KB |
| [Arduino Uno R4 Minima](../boards/renesas-ra/uno-r4-minima.md) | [Renesas RA](../platforms/renesas-ra.md) | RA4M1 | 48MHz | 256KB | 32KB |

## Boards

To list the boards from the command line, use [pio boards](../../reference/cli/pio-boards.md).

### Arduino

| Name | Platform | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|---|
| [Arduino Nano R4](../boards/renesas-ra/nano-r4.md) | [Renesas RA](../platforms/renesas-ra.md) | External | RA4M1 | 48MHz | 256KB | 32KB |
| [Arduino Portenta C33](../boards/renesas-ra/portenta-c33.md) | [Renesas RA](../platforms/renesas-ra.md) | External | R7FA6M5BH2CBG | 200MHz | 2MB | 511.35KB |
| [Arduino Uno R4 Minima](../boards/renesas-ra/uno-r4-minima.md) | [Renesas RA](../platforms/renesas-ra.md) | External | RA4M1 | 48MHz | 256KB | 32KB |
| [Arduino Uno R4 WiFi](../boards/renesas-ra/uno-r4-wifi.md) | [Renesas RA](../platforms/renesas-ra.md) | On-board | RA4M1 | 48MHz | 256KB | 32KB |
