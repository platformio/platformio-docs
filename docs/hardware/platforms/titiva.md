---
title: "TI TIVA"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
---

<a id="platform-titiva"></a>

# TI TIVA

**Registry:** [https://registry.platformio.org/platforms/platformio/titiva](https://registry.platformio.org/platforms/platformio/titiva)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/titiva`

Texas Instruments TM4C12x MCUs offer the industrys most popular ARM Cortex-M4 core with scalable memory and package options, unparalleled connectivity peripherals, advanced application functions, industry-leading analog integration, and extensive software solutions.

For more detailed information please visit [vendor site](http://www.ti.com/lsds/ti/microcontrollers_16-bit_32-bit/c2000_performance/control_automation/tm4c12x/overview.page?utm_source=platformio.org&utm_medium=docs).

## Examples

Examples are listed from [TI TIVA development platform repository](https://github.com/platformio/platform-titiva/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [libopencm3-blink](https://github.com/platformio/platform-titiva/tree/master/examples/libopencm3-blink?utm_source=platformio.org&utm_medium=docs)
- [libopencm3-usb-cdcacm](https://github.com/platformio/platform-titiva/tree/master/examples/libopencm3-usb-cdcacm?utm_source=platformio.org&utm_medium=docs)
- [arduino-blink](https://github.com/platformio/platform-titiva/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs)
- [native-blink](https://github.com/platformio/platform-titiva/tree/master/examples/native-blink?utm_source=platformio.org&utm_medium=docs)
- [arduino-internal-libs](https://github.com/platformio/platform-titiva/tree/master/examples/arduino-internal-libs?utm_source=platformio.org&utm_medium=docs)

## Debugging

[Debugging](../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

### Tools & Debug Probes

Supported debugging tools are listed in "Debug" column. For more detailed information, please scroll table by horizontal. You can switch between debugging [Tools & Debug Probes](../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md).

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions.

:::

#### On-Board Debug Tools

Boards listed below have on-board debug probe and **ARE READY** for debugging! You do not need to use/buy external debug probe.

| Name | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|
| [TI LaunchPad (Stellaris) w/ lm4f120 (80MHz)](../boards/titiva/lplm4f120h5qr.md) | LPLM4F120H5QR | 80MHz | 256KB | 32KB |
| [TI LaunchPad (Tiva C) w/ tm4c123 (80MHz)](../boards/titiva/lptm4c123gh6pm.md) | LPTM4C123GH6PM | 80MHz | 256KB | 32KB |
| [TI LaunchPad (Tiva C) w/ tm4c129 (120MHz)](../boards/titiva/lptm4c1294ncpdt.md) | LPTM4C1294NCPDT | 120MHz | 1MB | 256KB |

## Stable and upstream versions

You can switch between [stable releases](https://github.com/platformio/platform-titiva/releases) of TI TIVA development platform and the latest upstream version using [platform](../../reference/platformio-ini/env/platform.md) option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md) as described below.

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

**Linux Users**:

- Install "udev" rules [99-platformio-udev.rules](../../get-started/install/udev-rules.md)
- Raspberry Pi users, please read this article [Enable serial port on Raspberry Pi](https://hallard.me/enable-serial-port-on-raspberry-pi/).

**Windows Users:**

Please check that you have a correctly installed USB driver from board manufacturer

:::

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |
| [Energia](../frameworks/energia.md) | Energia Wiring-based Framework for Texas Instruments MSP430 microcontrollers |
| [LibOpenCM3](../frameworks/libopencm3.md) | The libopencm3 project aims to create an open-source firmware library for various ARM Cortex-M microcontrollers. |

## Boards

:::note

- You can list pre-configured boards by [pio boards](../../reference/cli/pio-boards.md) command
- For more detailed `board` information please scroll the tables below by horizontally.

:::

### TI

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [TI LaunchPad (Stellaris) w/ lm4f120 (80MHz)](../boards/titiva/lplm4f120h5qr.md) | On-board | LPLM4F120H5QR | 80MHz | 256KB | 32KB |
| [TI LaunchPad (Tiva C) w/ tm4c123 (80MHz)](../boards/titiva/lptm4c123gh6pm.md) | On-board | LPTM4C123GH6PM | 80MHz | 256KB | 32KB |
| [TI LaunchPad (Tiva C) w/ tm4c129 (120MHz)](../boards/titiva/lptm4c1294ncpdt.md) | On-board | LPTM4C1294NCPDT | 120MHz | 1MB | 256KB |
