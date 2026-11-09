---
title: "Lattice iCE40"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "The Lattice iCE40 development platform for PlatformIO: configuration, frameworks, packages, debugging and boards."
---

<a id="platform-lattice-ice40"></a>

# Lattice iCE40

**Registry:** [https://registry.platformio.org/platforms/platformio/lattice_ice40](https://registry.platformio.org/platforms/platformio/lattice_ice40)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/lattice_ice40`

The iCE40 family of ultra-low power, non-volatile FPGAs has five devices with densities ranging from 384 to 7680 Look-Up Tables (LUTs). In addition to LUT-based,low-cost programmable logic, these devices feature Embedded Block RAM (EBR), Non-volatile Configuration Memory (NVCM) and Phase Locked Loops (PLLs). These features allow the devices to be used in low-cost, high-volume consumer and system applications.

Vendor website: [www.latticesemi.com](http://www.latticesemi.com/Products/FPGAandCPLD/iCE40.aspx?utm_source=platformio.org&utm_medium=docs).

## Examples

Example projects from the [Lattice iCE40 platform repository](https://github.com/platformio/platform-lattice_ice40/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [leds](https://github.com/platformio/platform-lattice_ice40/tree/master/examples/leds?utm_source=platformio.org&utm_medium=docs)
- [counter](https://github.com/platformio/platform-lattice_ice40/tree/master/examples/counter?utm_source=platformio.org&utm_medium=docs)

## Stable and upstream versions

Choose between the [stable releases](https://github.com/platformio/platform-lattice_ice40/releases) of the Lattice iCE40 platform and its latest upstream version with the [platform](../../reference/platformio-ini/env/platform.md) option in [platformio.ini](../../reference/platformio-ini/index.md).

### Stable

```ini
; Latest stable version, NOT recommended
; Pin the version as shown below
[env:latest_stable]
platform = lattice_ice40
board = ...

; Specific version
[env:custom_stable]
platform = lattice_ice40@x.y.z
board = ...
```

### Upstream

```ini
[env:upstream_develop]
platform = https://github.com/platformio/platform-lattice_ice40.git
board = ...
```

## Packages

| Name | Description |
|---|---|
| [toolchain-icestorm](https://registry.platformio.org/tools/platformio/toolchain-icestorm) | Tools for analyzing and creating bitstream files for FPGA IceStorm |
| [toolchain-iverilog](https://registry.platformio.org/tools/platformio/toolchain-iverilog) | Verilog simulation and synthesis tool |

:::warning

**Linux:**

- Install the [udev rules](../../get-started/install/udev-rules.md).
- On a Raspberry Pi, [enable the serial port](https://hallard.me/enable-serial-port-on-raspberry-pi/).

**Windows:**

Install the USB driver from the board manufacturer, if needed.

:::

## Boards

To list the boards from the command line, use [pio boards](../../reference/cli/pio-boards.md).

### FPGAwars

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [IceZUM Alhambra FPGA](../boards/lattice-ice40/icezum.md) | No | ICE40-HX1K-TQ144 | 12MHz | 32KB | 32KB |

### Lattice

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Lattice iCEstick FPGA Evaluation Kit](../boards/lattice-ice40/icestick.md) | No | ICE40-HX1K-TQ144 | 12MHz | 32KB | 32KB |
