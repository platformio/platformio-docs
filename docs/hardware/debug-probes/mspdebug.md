---
description: "Use the MSP debug debug probe with PlatformIO: configuration, drivers, wiring and supported boards."
---

# MSP debug

The MSP debug stack (MSPDS) for all MSP430™ microcontrollers (MCUs) and SimpleLink™ MSP432™ devices consists of a static library on the host system side as well as an embedded firmware that runs on debug tools including the MSP-FET, MSP-FET430UIF or on-board eZ debuggers. It is the bridging element between all PC software and all MSP430 and SimpleLink MSP432 microcontroller derivatives and handles tasks such as code download, stepping through code or break points. See the [official documentation](http://www.ti.com/tool/mspds?utm_source=platformio&utm_medium=docs).

## Configuration {#configuration}

Select this probe with the [`debug_tool`](../../reference/platformio-ini/env/debug-tool.md) option in [`platformio.ini`](../../reference/platformio-ini/index.md):

```ini
[env:myenv]
platform = ...
board = ...
debug_tool = mspdebug
```

To also upload firmware with this probe, set [`upload_protocol`](../../reference/platformio-ini/env/upload-protocol.md):

```ini
[env:myenv]
platform = ...
board = ...
debug_tool = mspdebug
upload_protocol = mspdebug
```

See also:

- [Debugging options](../../reference/platformio-ini/env/debug-options.md)
- [Upload options](../../reference/platformio-ini/env/upload-options.md)

## Drivers {#drivers}

| Operating system | Driver |
| --- | --- |
| Windows | Please "USB Driver Installation" guide for your board. |
| macOS | Not required. |
| Linux | Install the [udev rules](../../get-started/install/udev-rules.md). If you installed them before, update them to the latest version. |

<!-- begin_platforms -->

## Platforms

| Name | Description |
|---|---|
| [TI MSP430](../platforms/timsp430.md) | MSP430 microcontrollers (MCUs) from Texas Instruments (TI) are 16-bit, RISC-based, mixed-signal processors designed for ultra-low power. These MCUs offer the lowest power consumption and the perfect mix of integrated peripherals for thousands of applications. |

## Frameworks

| Name | Description |
|---|---|
| [Arduino](../frameworks/arduino.mdx) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences. |

## Boards

| Name | Platform | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|---|
| [TI FraunchPad MSP-EXP430FR5739LP](../boards/timsp430/lpmsp430fr5739.md) | [TI MSP430](../platforms/timsp430.md) | On-board | MSP430FR5739 | 16MHz | 15.37KB | 1KB |
| [TI LaunchPad MSP-EXP430F5529LP](../boards/timsp430/lpmsp430f5529.md) | [TI MSP430](../platforms/timsp430.md) | On-board | MSP430F5529 | 25MHz | 47KB | 8KB |
| [TI LaunchPad MSP-EXP430FR2311LP](../boards/timsp430/lpmsp430fr2311.md) | [TI MSP430](../platforms/timsp430.md) | On-board | MSP430FR2311 | 16MHz | 3.75KB | 1KB |
| [TI LaunchPad MSP-EXP430FR2355LP](../boards/timsp430/lpmsp430fr2355.md) | [TI MSP430](../platforms/timsp430.md) | On-board | MSP430FR2355 | 16MHz | 32KB | 4KB |
| [TI LaunchPad MSP-EXP430FR2433LP](../boards/timsp430/lpmsp430fr2433.md) | [TI MSP430](../platforms/timsp430.md) | On-board | MSP430FR2433 | 8MHz | 15KB | 4KB |
| [TI LaunchPad MSP-EXP430FR2476LP](../boards/timsp430/lpmsp430fr2476.md) | [TI MSP430](../platforms/timsp430.md) | On-board | MSP430FR2476 | 16MHz | 64KB | 8KB |
| [TI LaunchPad MSP-EXP430FR4133LP](../boards/timsp430/lpmsp430fr4133.md) | [TI MSP430](../platforms/timsp430.md) | On-board | MSP430FR4133 | 8MHz | 15KB | 2KB |
| [TI LaunchPad MSP-EXP430FR5969LP](../boards/timsp430/lpmsp430fr5969.md) | [TI MSP430](../platforms/timsp430.md) | On-board | MSP430FR5969 | 8MHz | 47KB | 2KB |
| [TI LaunchPad MSP-EXP430FR5994LP](../boards/timsp430/lpmsp430fr5994.md) | [TI MSP430](../platforms/timsp430.md) | On-board | MSP430FR5994 | 16MHz | 256KB | 4KB |
| [TI LaunchPad MSP-EXP430FR6989LP](../boards/timsp430/lpmsp430fr6989.md) | [TI MSP430](../platforms/timsp430.md) | On-board | MSP430FR6989 | 8MHz | 47KB | 2KB |
| [TI LaunchPad MSP-EXP430G2 w/ MSP430G2231](../boards/timsp430/lpmsp430g2231.md) | [TI MSP430](../platforms/timsp430.md) | On-board | MSP430G2231 | 1MHz | 2KB | 256B |
| [TI LaunchPad MSP-EXP430G2 w/ MSP430G2452](../boards/timsp430/lpmsp430g2452.md) | [TI MSP430](../platforms/timsp430.md) | On-board | MSP430G2452 | 16MHz | 8KB | 256B |
| [TI LaunchPad MSP-EXP430G2553LP](../boards/timsp430/lpmsp430g2553.md) | [TI MSP430](../platforms/timsp430.md) | On-board | MSP430G2553 | 16MHz | 16KB | 512B |
