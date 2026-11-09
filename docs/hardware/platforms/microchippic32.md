---
title: "Microchip PIC32"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "The Microchip PIC32 development platform for PlatformIO: configuration, frameworks, packages, debugging and boards."
---

<a id="platform-microchippic32"></a>

# Microchip PIC32

**Registry:** [https://registry.platformio.org/platforms/platformio/microchippic32](https://registry.platformio.org/platforms/platformio/microchippic32)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/microchippic32`

Microchip's 32-bit portfolio with the MIPS microAptiv or M4K core offer high performance microcontrollers, and all the tools needed to develop your embedded projects. PIC32 MCUs gives your application the processing power, memory and peripherals your design needs!

Vendor website: [www.microchip.com](http://www.microchip.com/design-centers/32-bit?utm_source=platformio.org&utm_medium=docs).

## Examples

Example projects from the [Microchip PIC32 platform repository](https://github.com/platformio/platform-microchippic32/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [arduino-blink](https://github.com/platformio/platform-microchippic32/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs)
- [arduino-internal-libs](https://github.com/platformio/platform-microchippic32/tree/master/examples/arduino-internal-libs?utm_source=platformio.org&utm_medium=docs)

## Stable and upstream versions

Choose between the [stable releases](https://github.com/platformio/platform-microchippic32/releases) of the Microchip PIC32 platform and its latest upstream version with the [platform](../../reference/platformio-ini/env/platform.md) option in [platformio.ini](../../reference/platformio-ini/index.md).

### Stable

```ini
; Latest stable version, NOT recommended
; Pin the version as shown below
[env:latest_stable]
platform = microchippic32
board = ...

; Specific version
[env:custom_stable]
platform = microchippic32@x.y.z
board = ...
```

### Upstream

```ini
[env:upstream_develop]
platform = https://github.com/platformio/platform-microchippic32.git
board = ...
```

## Packages

| Name | Description |
|---|---|
| [framework-arduinomicrochippic32](https://registry.platformio.org/tools/platformio/framework-arduinomicrochippic32) | Arduino Wiring-based Framework for Microchip PIC32 microcontrollers |
| [tool-pic32prog](https://registry.platformio.org/tools/platformio/tool-pic32prog) | Flash programming utility for Microchip PIC32 microcontrollers |
| [toolchain-microchippic32](https://registry.platformio.org/tools/platformio/toolchain-microchippic32) | GCC Toolchain for Microchip PIC32 |

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

## Boards

To list the boards from the command line, use [pio boards](../../reference/cli/pio-boards.md).

### 4D Systems

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [4D Systems PICadillo 35T](../boards/microchippic32/picadillo-35t.md) | No | 32MX795F512L | 80MHz | 508KB | 128KB |

### BOXTEC

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [HelvePic32](../boards/microchippic32/helvepic32.md) | No | 32MX250F128B | 48MHz | 120KB | 32KB |
| [HelvePic32](../boards/microchippic32/helvepic32-breadboardside.md) | No | 32MX250F128B | 48MHz | 120KB | 32KB |
| [HelvePic32](../boards/microchippic32/helvepic32-smd.md) | No | 32MX250F128D | 48MHz | 120KB | 32KB |
| [HelvePic32 MX270](../boards/microchippic32/helvepic32-mx270.md) | No | 32MX270F256B | 48MHz | 244KB | 62KB |
| [HelvePic32 Robot](../boards/microchippic32/helvepic32-robot.md) | No | 32MX270F256D | 48MHz | 244KB | 62KB |
| [HelvePic32 SMD MX270](../boards/microchippic32/helvepic32-smd-mx270.md) | No | 32MX270F256D | 48MHz | 244KB | 62KB |

### ChipKIT

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [RGB Station](../boards/microchippic32/rgb-station.md) | No | 32MX270F256D | 48MHz | 240KB | 62KB |

### Digilent

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Digilent Cerebot 32MX4](../boards/microchippic32/cerebot32mx4.md) | No | 32MX460F512L | 80MHz | 508KB | 32KB |
| [Digilent Cerebot 32MX7](../boards/microchippic32/cerebot32mx7.md) | No | 32MX795F512L | 80MHz | 508KB | 128KB |
| [Digilent OpenScope](../boards/microchippic32/openscope.md) | No | 32MZ2048EFG124 | 200MHz | 1.98MB | 512KB |
| [Digilent chipKIT Cmod](../boards/microchippic32/chipkit-cmod.md) | No | 32MX150F128D | 40MHz | 124KB | 32KB |
| [Digilent chipKIT DP32](../boards/microchippic32/chipkit-dp32.md) | No | 32MX250F128B | 40MHz | 120KB | 32KB |
| [Digilent chipKIT MAX32](../boards/microchippic32/mega-pic32.md) | No | 32MX795F512L | 80MHz | 508KB | 128KB |
| [Digilent chipKIT MX3](../boards/microchippic32/chipkit-mx3.md) | No | 32MX320F128H | 80MHz | 124KB | 16KB |
| [Digilent chipKIT Pro MX4](../boards/microchippic32/chipkit-pro-mx4.md) | No | 32MX460F512L | 80MHz | 508KB | 32KB |
| [Digilent chipKIT Pro MX7](../boards/microchippic32/chipkit-pro-mx7.md) | No | 32MX795F512L | 80MHz | 508KB | 128KB |
| [Digilent chipKIT UNO32](../boards/microchippic32/uno-pic32.md) | No | 32MX320F128H | 80MHz | 124KB | 16KB |
| [Digilent chipKIT WF32](../boards/microchippic32/chipkit-wf32.md) | No | 32MX695F512L | 80MHz | 508KB | 128KB |
| [Digilent chipKIT WiFire](../boards/microchippic32/chipkit-wifire.md) | No | 32MZ2048ECG100 | 200MHz | 1.98MB | 512KB |
| [Digilent chipKIT uC32](../boards/microchippic32/chipkit-uc32.md) | No | 32MX340F512H | 80MHz | 508KB | 32KB |
| [chipKIT WiFire rev. C](../boards/microchippic32/chipkit-wifire-revc.md) | No | 32MZ2048EFG100 | 200MHz | 1.98MB | 512KB |

### Fubarino

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Fubarino Mini](../boards/microchippic32/fubarino-mini.md) | No | 32MX250F128D | 48MHz | 120KB | 32KB |
| [Fubarino SD (1.5)](../boards/microchippic32/fubarino-sd.md) | No | 32MX795F512H | 80MHz | 508KB | 128KB |
| [Mini 2.0](../boards/microchippic32/fubarino-mini-20.md) | No | 32MX270F256D | 48MHz | 240KB | 62KB |

### Makerology

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [DataStation Mini](../boards/microchippic32/dsmini.md) | No | 32MX150F128C | 40MHz | 120KB | 32KB |

### MikroElektronika

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [MikroElektronika Clicker 2](../boards/microchippic32/clicker2.md) | No | 32MX460F512L | 80MHz | 508KB | 32KB |
| [MikroElektronika Flip N Click MZ](../boards/microchippic32/flipnclickmz.md) | No | 32MZ2048EFH100 | 252MHz | 1.98MB | 512KB |

### Olimex

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Olimex PIC32-PINGUINO](../boards/microchippic32/pinguino32.md) | No | 32MX440F256H | 80MHz | 252KB | 32KB |

### OpenBCI

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [OpenBCI 32bit](../boards/microchippic32/openbci.md) | No | 32MX250F128B | 40MHz | 120KB | 32KB |

### PONTECH

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [PONTECH UAV100](../boards/microchippic32/usbono-pic32.md) | No | 32MX440F512H | 80MHz | 508KB | 32KB |

### Pontech

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Pontech NoFire](../boards/microchippic32/nofire.md) | No | 32MZ2048EFG100 | 200MHz | 1.98MB | 512KB |
| [Pontech Quick240](../boards/microchippic32/quick240-usb.md) | No | 32MX795F512L | 80MHz | 508KB | 128KB |

### SeeedStudio

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [SeeedStudio CUI32stem](../boards/microchippic32/cui32stem.md) | No | 32MX795F512H | 80MHz | 508KB | 128KB |

### SparkFun

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Pic32 CUI32-Development Stick](../boards/microchippic32/cui32.md) | No | 32MX440F512H | 80MHz | 508KB | 32KB |

### UBW32

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [UBW32 MX460](../boards/microchippic32/ubw32-mx460.md) | No | 32MX460F512L | 80MHz | 508KB | 32KB |
| [UBW32 MX795](../boards/microchippic32/ubw32-mx795.md) | No | 32MX795F512L | 80MHz | 508KB | 128KB |

### chipKIT

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [chipKIT Lenny](../boards/microchippic32/lenny.md) | No | 32MX270F256D | 40MHz | 120KB | 32KB |

### element14

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Element14 chipKIT Pi](../boards/microchippic32/chipkit-pi.md) | No | 32MX250F128B | 40MHz | 120KB | 32KB |
