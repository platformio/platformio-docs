---
title: "ST STM8"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "The ST STM8 development platform for PlatformIO: configuration, frameworks, packages, debugging and boards."
---

<a id="platform-ststm8"></a>

# ST STM8

**Registry:** [https://registry.platformio.org/platforms/platformio/ststm8](https://registry.platformio.org/platforms/platformio/ststm8)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/ststm8`

The STM8 is an 8-bit microcontroller family by STMicroelectronics an extended variant of the ST7 microcontroller architecture. STM8 microcontrollers are particularly low cost for a full-featured 8-bit microcontroller.

Vendor website: [www.st.com](https://www.st.com/en/microcontrollers/stm8-8-bit-mcus.html?utm_source=platformio.org&utm_medium=docs).

## Examples

Example projects from the [ST STM8 platform repository](https://github.com/platformio/platform-ststm8/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [spl-uart-loopback](https://github.com/platformio/platform-ststm8/tree/master/examples/spl-uart-loopback?utm_source=platformio.org&utm_medium=docs)
- [spl-blink](https://github.com/platformio/platform-ststm8/tree/master/examples/spl-blink?utm_source=platformio.org&utm_medium=docs)
- [arduino-fade-all-pins](https://github.com/platformio/platform-ststm8/tree/master/examples/arduino-fade-all-pins?utm_source=platformio.org&utm_medium=docs)
- [native-blink](https://github.com/platformio/platform-ststm8/tree/master/examples/native-blink?utm_source=platformio.org&utm_medium=docs)
- [spl-uart-simple-printf](https://github.com/platformio/platform-ststm8/tree/master/examples/spl-uart-simple-printf?utm_source=platformio.org&utm_medium=docs)
- [spl-flash](https://github.com/platformio/platform-ststm8/tree/master/examples/spl-flash?utm_source=platformio.org&utm_medium=docs)
- [arduino-internal-lib](https://github.com/platformio/platform-ststm8/tree/master/examples/arduino-internal-lib?utm_source=platformio.org&utm_medium=docs)
- [arduino-ping-hc04](https://github.com/platformio/platform-ststm8/tree/master/examples/arduino-ping-hc04?utm_source=platformio.org&utm_medium=docs)

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
| [NUCLEO-8S207K8](../boards/ststm8/nucleo-8s207k8.md) | STM8S207K8T6 | 16MHz | 64KB | 6KB |
| [NUCLEO-8S208RB](../boards/ststm8/nucleo-8s208rb.md) | STM8S208RBT6 | 16MHz | 128KB | 6KB |
| [ST STM8S-DISCOVERY](../boards/ststm8/stm8sdisco.md) | STM8S105C6T6 | 16MHz | 32KB | 2KB |

#### Boards that need an external debug probe

These boards support [Debugging](../../guides/debugging/index.md) with an external debug probe. See each board's page for the compatible probes.

| Name | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|
| [ST STM8S003F3 chip](../boards/ststm8/stm8s003f3.md) | STM8S003F3P6 | 16MHz | 8KB | 1KB |
| [ST STM8S103F3 Breakout Board](../boards/ststm8/stm8sblue.md) | STM8S103F3P6 | 16MHz | 8KB | 1KB |
| [ST STM8S105K4T6 Breakout Board](../boards/ststm8/stm8sblack.md) | STM8S105K4T6 | 16MHz | 16KB | 2KB |
| [sduino MB (STM8S208MBT6B)](../boards/ststm8/mb208.md) | STM8S208MBT6 | 16MHz | 128KB | 6KB |
| [sduino UNO (STM8S105K6)](../boards/ststm8/s8uno.md) | STM8S105K6T6 | 16MHz | 32KB | 2KB |

## Stable and upstream versions

Choose between the [stable releases](https://github.com/platformio/platform-ststm8/releases) of the ST STM8 platform and its latest upstream version with the [platform](../../reference/platformio-ini/env/platform.md) option in [platformio.ini](../../reference/platformio-ini/index.md).

### Stable

```ini
; Latest stable version, NOT recommended
; Pin the version as shown below
[env:latest_stable]
platform = ststm8
board = ...

; Specific version
[env:custom_stable]
platform = ststm8@x.y.z
board = ...
```

### Upstream

```ini
[env:upstream_develop]
platform = https://github.com/platformio/platform-ststm8.git
board = ...
```

## Packages

| Name | Description |
|---|---|
| [framework-arduinoststm8](https://registry.platformio.org/tools/platformio/framework-arduinoststm8) | An Arduino-like programming API for the STM8 microcontrollers |
| [framework-ststm8spl](https://registry.platformio.org/tools/platformio/framework-ststm8spl) | Standard peripheral library for ST STM8S/A microcontrollers |
| [tool-openocd](https://registry.platformio.org/tools/platformio/tool-openocd) | Open On-Chip Debugger. Free and Open On-Chip Debugging, In-System Programming and Boundary-Scan Testing |
| [tool-stm8binutils](https://registry.platformio.org/tools/platformio/tool-stm8binutils) | STM8 toolchain with GDB debugger |
| [tool-stm8flash](https://registry.platformio.org/tools/platformio/tool-stm8flash) | stm8flash is an application for programing stm8 devices with SWIM/stlinkv(1,2). |
| [tool-stm8gal](https://registry.platformio.org/tools/platformio/tool-stm8gal) | stm8gal is an application for programming or reading out STM8 memory using the built-in ROM bootloader (BSL) via UART or SPI interface |
| [toolchain-sdcc](https://registry.platformio.org/tools/platformio/toolchain-sdcc) | Small Device C compiler suite |

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
| [Standard Peripheral Library](../frameworks/spl.mdx) | Standard Peripheral Library for ST STM32 microcontrollers |

## Boards

To list the boards from the command line, use [pio boards](../../reference/cli/pio-boards.md).

### ST

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [ST STM8S-DISCOVERY](../boards/ststm8/stm8sdisco.md) | On-board | STM8S105C6T6 | 16MHz | 32KB | 2KB |
| [ST STM8S003F3 chip](../boards/ststm8/stm8s003f3.md) | External | STM8S003F3P6 | 16MHz | 8KB | 1KB |
| [ST STM8S103F3 Breakout Board](../boards/ststm8/stm8sblue.md) | External | STM8S103F3P6 | 16MHz | 8KB | 1KB |
| [ST STM8S105K4T6 Breakout Board](../boards/ststm8/stm8sblack.md) | External | STM8S105K4T6 | 16MHz | 16KB | 2KB |

### STMicroelectronics

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [NUCLEO-8S207K8](../boards/ststm8/nucleo-8s207k8.md) | On-board | STM8S207K8T6 | 16MHz | 64KB | 6KB |
| [NUCLEO-8S208RB](../boards/ststm8/nucleo-8s208rb.md) | On-board | STM8S208RBT6 | 16MHz | 128KB | 6KB |

### sduino

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [sduino MB (STM8S208MBT6B)](../boards/ststm8/mb208.md) | External | STM8S208MBT6 | 16MHz | 128KB | 6KB |
| [sduino UNO (STM8S105K6)](../boards/ststm8/s8uno.md) | External | STM8S105K6T6 | 16MHz | 32KB | 2KB |
