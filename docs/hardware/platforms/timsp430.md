---
title: "TI MSP430"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
---

<a id="platform-timsp430"></a>

# TI MSP430

**Registry:** [https://registry.platformio.org/platforms/platformio/timsp430](https://registry.platformio.org/platforms/platformio/timsp430)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/timsp430`

MSP430 microcontrollers (MCUs) from Texas Instruments (TI) are 16-bit, RISC-based, mixed-signal processors designed for ultra-low power. These MCUs offer the lowest power consumption and the perfect mix of integrated peripherals for thousands of applications.

For more detailed information please visit [vendor site](http://www.ti.com/lsds/ti/microcontrollers_16-bit_32-bit/msp/overview.page?utm_source=platformio.org&utm_medium=docs).

## Examples

Examples are listed from [TI MSP430 development platform repository](https://github.com/platformio/platform-timsp430/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [arduino-blink](https://github.com/platformio/platform-timsp430/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs)
- [native-blink](https://github.com/platformio/platform-timsp430/tree/master/examples/native-blink?utm_source=platformio.org&utm_medium=docs)
- [arduino-internal-libs](https://github.com/platformio/platform-timsp430/tree/master/examples/arduino-internal-libs?utm_source=platformio.org&utm_medium=docs)

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
| [TI FraunchPad MSP-EXP430FR5739LP](../boards/timsp430/lpmsp430fr5739.md) | MSP430FR5739 | 16MHz | 15.37KB | 1KB |
| [TI LaunchPad MSP-EXP430F5529LP](../boards/timsp430/lpmsp430f5529.md) | MSP430F5529 | 25MHz | 47KB | 8KB |
| [TI LaunchPad MSP-EXP430FR2311LP](../boards/timsp430/lpmsp430fr2311.md) | MSP430FR2311 | 16MHz | 3.75KB | 1KB |
| [TI LaunchPad MSP-EXP430FR2355LP](../boards/timsp430/lpmsp430fr2355.md) | MSP430FR2355 | 16MHz | 32KB | 4KB |
| [TI LaunchPad MSP-EXP430FR2433LP](../boards/timsp430/lpmsp430fr2433.md) | MSP430FR2433 | 8MHz | 15KB | 4KB |
| [TI LaunchPad MSP-EXP430FR2476LP](../boards/timsp430/lpmsp430fr2476.md) | MSP430FR2476 | 16MHz | 64KB | 8KB |
| [TI LaunchPad MSP-EXP430FR4133LP](../boards/timsp430/lpmsp430fr4133.md) | MSP430FR4133 | 8MHz | 15KB | 2KB |
| [TI LaunchPad MSP-EXP430FR5969LP](../boards/timsp430/lpmsp430fr5969.md) | MSP430FR5969 | 8MHz | 47KB | 2KB |
| [TI LaunchPad MSP-EXP430FR5994LP](../boards/timsp430/lpmsp430fr5994.md) | MSP430FR5994 | 16MHz | 256KB | 4KB |
| [TI LaunchPad MSP-EXP430FR6989LP](../boards/timsp430/lpmsp430fr6989.md) | MSP430FR6989 | 8MHz | 47KB | 2KB |
| [TI LaunchPad MSP-EXP430G2 w/ MSP430G2231](../boards/timsp430/lpmsp430g2231.md) | MSP430G2231 | 1MHz | 2KB | 256B |
| [TI LaunchPad MSP-EXP430G2 w/ MSP430G2452](../boards/timsp430/lpmsp430g2452.md) | MSP430G2452 | 16MHz | 8KB | 256B |
| [TI LaunchPad MSP-EXP430G2553LP](../boards/timsp430/lpmsp430g2553.md) | MSP430G2553 | 16MHz | 16KB | 512B |

## Stable and upstream versions

You can switch between [stable releases](https://github.com/platformio/platform-timsp430/releases) of TI MSP430 development platform and the latest upstream version using [platform](../../reference/platformio-ini/env/platform.md) option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md) as described below.

### Stable

```ini
; Latest stable version, NOT recommended
; Pin the version as shown below
[env:latest_stable]
platform = timsp430
board = ...

; Specific version
[env:custom_stable]
platform = timsp430@x.y.z
board = ...
```

### Upstream

```ini
[env:upstream_develop]
platform = https://github.com/platformio/platform-timsp430.git
board = ...
```

## Packages

| Name | Description |
|---|---|
| [framework-energiamsp430](https://registry.platformio.org/tools/platformio/framework-energiamsp430) | Energia Wiring-based Framework for Texas Instruments MSP430 microcontrollers |
| [tool-dslite](https://registry.platformio.org/tools/platformio/tool-dslite) | Uniflash Standalone Flash Tool for TI Microcontrollers, Sitara Processors & SimpleLink devices |
| [tool-mspdebug](https://registry.platformio.org/tools/platformio/tool-mspdebug) | MSPDebug is a free debugger for use with MSP430 MCUs |
| [toolchain-timsp430](https://registry.platformio.org/tools/platformio/toolchain-timsp430) | A port of the GNU C Compiler (GCC) and GNU Binutils (as, ld) for the embedded processor MSP430 |

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

## Boards

:::note

- You can list pre-configured boards by [pio boards](../../reference/cli/pio-boards.md) command
- For more detailed `board` information please scroll the tables below by horizontally.

:::

### TI

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [TI FraunchPad MSP-EXP430FR5739LP](../boards/timsp430/lpmsp430fr5739.md) | On-board | MSP430FR5739 | 16MHz | 15.37KB | 1KB |
| [TI LaunchPad MSP-EXP430F5529LP](../boards/timsp430/lpmsp430f5529.md) | On-board | MSP430F5529 | 25MHz | 47KB | 8KB |
| [TI LaunchPad MSP-EXP430FR2311LP](../boards/timsp430/lpmsp430fr2311.md) | On-board | MSP430FR2311 | 16MHz | 3.75KB | 1KB |
| [TI LaunchPad MSP-EXP430FR2355LP](../boards/timsp430/lpmsp430fr2355.md) | On-board | MSP430FR2355 | 16MHz | 32KB | 4KB |
| [TI LaunchPad MSP-EXP430FR2433LP](../boards/timsp430/lpmsp430fr2433.md) | On-board | MSP430FR2433 | 8MHz | 15KB | 4KB |
| [TI LaunchPad MSP-EXP430FR2476LP](../boards/timsp430/lpmsp430fr2476.md) | On-board | MSP430FR2476 | 16MHz | 64KB | 8KB |
| [TI LaunchPad MSP-EXP430FR4133LP](../boards/timsp430/lpmsp430fr4133.md) | On-board | MSP430FR4133 | 8MHz | 15KB | 2KB |
| [TI LaunchPad MSP-EXP430FR5969LP](../boards/timsp430/lpmsp430fr5969.md) | On-board | MSP430FR5969 | 8MHz | 47KB | 2KB |
| [TI LaunchPad MSP-EXP430FR5994LP](../boards/timsp430/lpmsp430fr5994.md) | On-board | MSP430FR5994 | 16MHz | 256KB | 4KB |
| [TI LaunchPad MSP-EXP430FR6989LP](../boards/timsp430/lpmsp430fr6989.md) | On-board | MSP430FR6989 | 8MHz | 47KB | 2KB |
| [TI LaunchPad MSP-EXP430G2 w/ MSP430G2231](../boards/timsp430/lpmsp430g2231.md) | On-board | MSP430G2231 | 1MHz | 2KB | 256B |
| [TI LaunchPad MSP-EXP430G2 w/ MSP430G2452](../boards/timsp430/lpmsp430g2452.md) | On-board | MSP430G2452 | 16MHz | 8KB | 256B |
| [TI LaunchPad MSP-EXP430G2553LP](../boards/timsp430/lpmsp430g2553.md) | On-board | MSP430G2553 | 16MHz | 16KB | 512B |
