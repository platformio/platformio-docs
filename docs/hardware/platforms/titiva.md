---
title: "TI TIVA"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "The TI TIVA development platform for PlatformIO: configuration, frameworks, packages, debugging and boards."
---

# TI TIVA

**Registry:** [https://registry.platformio.org/platforms/platformio/titiva](https://registry.platformio.org/platforms/platformio/titiva)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/titiva`

Texas Instruments TM4C12x MCUs offer the industrys most popular ARM Cortex-M4 core with scalable memory and package options, unparalleled connectivity peripherals, advanced application functions, industry-leading analog integration, and extensive software solutions.

Vendor website: [www.ti.com](http://www.ti.com/lsds/ti/microcontrollers_16-bit_32-bit/c2000_performance/control_automation/tm4c12x/overview.page?utm_source=platformio.org&utm_medium=docs).

## Examples

Example projects from the [TI TIVA platform repository](https://github.com/platformio/platform-titiva/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [libopencm3-blink](https://github.com/platformio/platform-titiva/tree/master/examples/libopencm3-blink?utm_source=platformio.org&utm_medium=docs)
- [libopencm3-usb-cdcacm](https://github.com/platformio/platform-titiva/tree/master/examples/libopencm3-usb-cdcacm?utm_source=platformio.org&utm_medium=docs)
- [arduino-blink](https://github.com/platformio/platform-titiva/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs)
- [native-blink](https://github.com/platformio/platform-titiva/tree/master/examples/native-blink?utm_source=platformio.org&utm_medium=docs)
- [arduino-internal-libs](https://github.com/platformio/platform-titiva/tree/master/examples/arduino-internal-libs?utm_source=platformio.org&utm_medium=docs)

## Debugging

[Debugging](../../guides/debugging/index.md) works with the boards below without extra configuration.

### Debug probes

Select a [debug probe](../../guides/debugging/index.md#debugging-tools) with the [debug_tool](../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../reference/platformio-ini/index.md). Each board's page lists its compatible probes.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

#### Boards with an on-board debug probe

These boards are ready for debugging; no external probe is needed.

| Name | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|
| [TI LaunchPad (Stellaris) w/ lm4f120 (80MHz)](../boards/titiva/lplm4f120h5qr.md) | LPLM4F120H5QR | 80MHz | 256KB | 32KB |
| [TI LaunchPad (Tiva C) w/ tm4c123 (80MHz)](../boards/titiva/lptm4c123gh6pm.md) | LPTM4C123GH6PM | 80MHz | 256KB | 32KB |
| [TI LaunchPad (Tiva C) w/ tm4c129 (120MHz)](../boards/titiva/lptm4c1294ncpdt.md) | LPTM4C1294NCPDT | 120MHz | 1MB | 256KB |

## Stable and upstream versions

Choose between the [stable releases](https://github.com/platformio/platform-titiva/releases) of the TI TIVA platform and its latest upstream version with the [platform](../../reference/platformio-ini/env/platform.md) option in [platformio.ini](../../reference/platformio-ini/index.md).

### Stable

```ini
; Latest stable version, NOT recommended
; Pin the version as shown below
[env:latest_stable]
platform = titiva
board = ...

; Specific version
[env:custom_stable]
platform = titiva@x.y.z
board = ...
```

### Upstream

```ini
[env:upstream_develop]
platform = https://github.com/platformio/platform-titiva.git
board = ...
```

## Packages

| Name | Description |
|---|---|
| [framework-energiativa](https://registry.platformio.org/tools/platformio/framework-energiativa) | Energia Wiring-based Framework for Texas Instruments TIVA C Series |
| [framework-libopencm3](https://registry.platformio.org/tools/platformio/framework-libopencm3) | The libopencm3 project aims to create an open-source firmware library for various ARM Cortex-M microcontrollers. |
| [tool-openocd](https://registry.platformio.org/tools/platformio/tool-openocd) | Open On-Chip Debugger. Free and Open On-Chip Debugging, In-System Programming and Boundary-Scan Testing |
| [toolchain-gccarmnoneeabi](https://registry.platformio.org/tools/platformio/toolchain-gccarmnoneeabi) | GNU toolchain for Arm Cortex-M and Cortex-R processors |

:::warning

**Linux:**

- Install the [udev rules](../../get-started/install/udev-rules.md).
- On a Raspberry Pi, [enable the serial port](https://hallard.me/enable-serial-port-on-raspberry-pi/).

**Windows:**

Install the USB driver from the board manufacturer, if needed.

:::

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [Energia](../frameworks/energia.md) | Energia Wiring-based Framework for Texas Instruments MSP430 microcontrollers |
| [LibOpenCM3](../frameworks/libopencm3.md) | The libopencm3 project aims to create an open-source firmware library for various ARM Cortex-M microcontrollers. |

## Boards

To list the boards from the command line, use [pio boards](../../reference/cli/pio-boards.md).

### TI

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [TI LaunchPad (Stellaris) w/ lm4f120 (80MHz)](../boards/titiva/lplm4f120h5qr.md) | On-board | LPLM4F120H5QR | 80MHz | 256KB | 32KB |
| [TI LaunchPad (Tiva C) w/ tm4c123 (80MHz)](../boards/titiva/lptm4c123gh6pm.md) | On-board | LPTM4C123GH6PM | 80MHz | 256KB | 32KB |
| [TI LaunchPad (Tiva C) w/ tm4c129 (120MHz)](../boards/titiva/lptm4c1294ncpdt.md) | On-board | LPTM4C1294NCPDT | 120MHz | 1MB | 256KB |
