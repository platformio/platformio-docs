---
title: "Renesas Flexible Software Package"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
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
| [Arduino Uno R4 WiFi](../boards/renesas-ra/uno-r4-wifi.md) | [Renesas RA](../platforms/renesas-ra.md) | RA4M1 | 48MHz | 256KB | 32KB |

#### External Debug Tools

Boards listed below are compatible with [Debugging](../../guides/debugging/index.md) but **DEPEND ON** external debug probe. They **ARE NOT READY** for debugging. Please click on board name for the further details.

| Name | Platform | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Arduino Nano R4](../boards/renesas-ra/nano-r4.md) | [Renesas RA](../platforms/renesas-ra.md) | RA4M1 | 48MHz | 256KB | 32KB |
| [Arduino Portenta C33](../boards/renesas-ra/portenta-c33.md) | [Renesas RA](../platforms/renesas-ra.md) | R7FA6M5BH2CBG | 200MHz | 2MB | 511.35KB |
| [Arduino Uno R4 Minima](../boards/renesas-ra/uno-r4-minima.md) | [Renesas RA](../platforms/renesas-ra.md) | RA4M1 | 48MHz | 256KB | 32KB |

## Boards

:::note

- You can list pre-configured boards by [pio boards](../../reference/cli/pio-boards.md) command
- For more detailed `board` information please scroll the tables below by horizontally.

:::

### Arduino

| Name | Platform | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|---|
| [Arduino Nano R4](../boards/renesas-ra/nano-r4.md) | [Renesas RA](../platforms/renesas-ra.md) | External | RA4M1 | 48MHz | 256KB | 32KB |
| [Arduino Portenta C33](../boards/renesas-ra/portenta-c33.md) | [Renesas RA](../platforms/renesas-ra.md) | External | R7FA6M5BH2CBG | 200MHz | 2MB | 511.35KB |
| [Arduino Uno R4 Minima](../boards/renesas-ra/uno-r4-minima.md) | [Renesas RA](../platforms/renesas-ra.md) | External | RA4M1 | 48MHz | 256KB | 32KB |
| [Arduino Uno R4 WiFi](../boards/renesas-ra/uno-r4-wifi.md) | [Renesas RA](../platforms/renesas-ra.md) | On-board | RA4M1 | 48MHz | 256KB | 32KB |
