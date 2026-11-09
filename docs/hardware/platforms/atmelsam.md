---
title: "Atmel SAM"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "The Atmel SAM development platform for PlatformIO: configuration, frameworks, packages, debugging and boards."
---

# Atmel SAM

**Registry:** [https://registry.platformio.org/platforms/platformio/atmelsam](https://registry.platformio.org/platforms/platformio/atmelsam)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/atmelsam`

Atmel | SMART offers Flash- based ARM products based on the ARM Cortex-M0+, Cortex-M3 and Cortex-M4 architectures, ranging from 8KB to 2MB of Flash including a rich peripheral and feature mix.

Vendor website: [www.microchip.com](https://www.microchip.com/design-centers/32-bit?utm_source=platformio.org&utm_medium=docs).

## Examples

Example projects from the [Atmel SAM platform repository](https://github.com/platformio/platform-atmelsam/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [zephyr-blink](https://github.com/platformio/platform-atmelsam/tree/master/examples/zephyr-blink?utm_source=platformio.org&utm_medium=docs)
- [zephyr-subsys-logger](https://github.com/platformio/platform-atmelsam/tree/master/examples/zephyr-subsys-logger?utm_source=platformio.org&utm_medium=docs)
- [arduino-blink](https://github.com/platformio/platform-atmelsam/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs)
- [arduino-internal-libs](https://github.com/platformio/platform-atmelsam/tree/master/examples/arduino-internal-libs?utm_source=platformio.org&utm_medium=docs)
- [zephyr-drivers-lcd-hd44780](https://github.com/platformio/platform-atmelsam/tree/master/examples/zephyr-drivers-lcd-hd44780?utm_source=platformio.org&utm_medium=docs)
- [arduino-external-libs](https://github.com/platformio/platform-atmelsam/tree/master/examples/arduino-external-libs?utm_source=platformio.org&utm_medium=docs)
- [arduino-web-thing-led](https://github.com/platformio/platform-atmelsam/tree/master/examples/arduino-web-thing-led?utm_source=platformio.org&utm_medium=docs)

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
| [Arduino M0 Pro (Programming/Debug Port)](../boards/atmelsam/mzeropro.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Arduino Zero (Programming/Debug Port)](../boards/atmelsam/zero.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Atmel ATSAMR21-XPRO](../boards/atmelsam/samr21-xpro.md) | SAMR21G18A | 48MHz | 256KB | 32KB |
| [Atmel ATSAMW25-XPRO](../boards/atmelsam/samd21g18a.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Atmel SAMC21-XPRO](../boards/atmelsam/samc21-xpro.md) | SAMC21J18A | 48MHz | 256KB | 32KB |
| [Atmel SAMD21-XPRO](../boards/atmelsam/samd21-xpro.md) | SAMD21J18A | 48MHz | 256KB | 32KB |

#### Boards that need an external debug probe

These boards support [Debugging](../../guides/debugging/index.md) with an external debug probe. See each board's page for the compatible probes.

| Name | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|
| [Adafruit BLM Badge](../boards/atmelsam/adafruit-blm-badge.md) | SAMD21E18A | 48MHz | 256KB | 32KB |
| [Adafruit Circuit Playground Express](../boards/atmelsam/adafruit-circuitplayground-m0.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Adafruit Crickit M0](../boards/atmelsam/adafruit-crickit-m0.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Adafruit Feather M0](../boards/atmelsam/adafruit-feather-m0.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Adafruit Feather M0 Express](../boards/atmelsam/adafruit-feather-m0-express.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Adafruit Feather M4 CAN](../boards/atmelsam/adafruit-feather-m4-can.md) | SAME51J19A | 120MHz | 496KB | 192KB |
| [Adafruit Feather M4 Express](../boards/atmelsam/adafruit-feather-m4.md) | SAMD51J19A | 120MHz | 512KB | 192KB |
| [Adafruit Gemma M0](../boards/atmelsam/adafruit-gemma-m0.md) | SAMD21E18A | 48MHz | 256KB | 32KB |
| [Adafruit Grand Central M4](../boards/atmelsam/adafruit-grandcentral-m4.md) | SAMD51P20A | 120MHz | 1MB | 256KB |
| [Adafruit Hallowing M0](../boards/atmelsam/adafruit-hallowing.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Adafruit Hallowing M4](../boards/atmelsam/adafruit-hallowing-m4.md) | SAMD51J19A | 120MHz | 496KB | 192KB |
| [Adafruit ItsyBitsy M0](../boards/atmelsam/adafruit-itsybitsy-m0.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Adafruit ItsyBitsy M4](../boards/atmelsam/adafruit-itsybitsy-m4.md) | SAMD51G19A | 120MHz | 512KB | 192KB |
| [Adafruit MONSTER M4SK](../boards/atmelsam/adafruit-monster-m4sk.md) | SAMD51G19A | 120MHz | 496KB | 192KB |
| [Adafruit Matrix Portal M4](../boards/atmelsam/adafruit-matrix-portal-m4.md) | SAMD51J19A | 120MHz | 496KB | 192KB |
| [Adafruit Metro M0 Express](../boards/atmelsam/adafruit-metro-m0.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Adafruit Metro M4](../boards/atmelsam/adafruit-metro-m4.md) | SAMD51J19A | 120MHz | 512KB | 192KB |
| [Adafruit Metro M4 AirLift Lite](../boards/atmelsam/adafruit-metro-m4-airliftlite.md) | SAMD51J19A | 120MHz | 512KB | 192KB |
| [Adafruit NeoKey Trinkey](../boards/atmelsam/adafruit-neokeytrinkey-m0.md) | SAMD21E18A | 48MHz | 256KB | 32KB |
| [Adafruit NeoPixel Trinkey](../boards/atmelsam/adafruit-neotrinkey-m0.md) | SAMD21E18A | 48MHz | 256KB | 32KB |
| [Adafruit ProxLight Trinkey](../boards/atmelsam/adafruit-proxlighttrinkey-m0.md) | SAMD21E18A | 48MHz | 256KB | 32KB |
| [Adafruit PyGamer Advance M4](../boards/atmelsam/adafruit-pygamer-advance-m4.md) | SAMD51J20A | 120MHz | 1MB | 256KB |
| [Adafruit PyGamer M4 Express](../boards/atmelsam/adafruit-pygamer-m4.md) | SAMD51J19A | 120MHz | 512KB | 192KB |
| [Adafruit PyPortal M4](../boards/atmelsam/adafruit-pyportal-m4.md) | SAMD51J20A | 120MHz | 1MB | 256KB |
| [Adafruit PyPortal M4 Titano](../boards/atmelsam/adafruit-pyportal-m4-titano.md) | SAMD51J20A | 120MHz | 1MB | 256KB |
| [Adafruit QT Py M0](../boards/atmelsam/adafruit-qt-py-m0.md) | SAMD21E18A | 48MHz | 256KB | 32KB |
| [Adafruit Rotary Trinkey](../boards/atmelsam/adafruit-rotarytrinkey-m0.md) | SAMD21E18A | 48MHz | 256KB | 32KB |
| [Adafruit Slide Trinkey](../boards/atmelsam/adafruit-slidetrinkey-m0.md) | SAMD21E18A | 48MHz | 256KB | 32KB |
| [Adafruit Trellis M4](../boards/atmelsam/adafruit-trellis-m4.md) | SAMD51J19A | 120MHz | 512KB | 192KB |
| [Adafruit Trinket M0](../boards/atmelsam/adafruit-trinket-m0.md) | SAMD21E18A | 48MHz | 256KB | 32KB |
| [Adafruit pIRkey](../boards/atmelsam/adafruit-pirkey.md) | SAMD21E18A | 48MHz | 256KB | 32KB |
| [Adafruit pyBadge AirLift M4](../boards/atmelsam/adafruit-pybadge-airlift-m4.md) | SAMD51J20A | 120MHz | 1008KB | 192KB |
| [Adafruit pyBadge M4 Express](../boards/atmelsam/adafruit-pybadge-m4.md) | SAMD51J19A | 120MHz | 512KB | 192KB |
| [Arduino Due (Programming Port)](../boards/atmelsam/due.md) | AT91SAM3X8E | 84MHz | 512KB | 96KB |
| [Arduino Due (USB Native Port)](../boards/atmelsam/dueusb.md) | AT91SAM3X8E | 84MHz | 512KB | 96KB |
| [Arduino M0](../boards/atmelsam/mzerousb.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Arduino M0 Pro (Native USB Port)](../boards/atmelsam/mzeroprousb.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Arduino MKR FOX 1200](../boards/atmelsam/mkrfox1200.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Arduino MKR GSM 1400](../boards/atmelsam/mkrgsm1400.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Arduino MKR NB 1500](../boards/atmelsam/mkrnb1500.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Arduino MKR WAN 1300](../boards/atmelsam/mkrwan1300.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Arduino MKR WAN 1310](../boards/atmelsam/mkrwan1310.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Arduino MKR WiFi 1010](../boards/atmelsam/mkrwifi1010.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Arduino MKR1000](../boards/atmelsam/mkr1000usb.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Arduino MKRZERO](../boards/atmelsam/mkrzero.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Arduino Tian](../boards/atmelsam/tian.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Arduino Zero (USB Native Port)](../boards/atmelsam/zerousb.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Digistump DigiX](../boards/atmelsam/digix.md) | AT91SAM3X8E | 84MHz | 512KB | 96KB |
| [MKR Vidor 4000](../boards/atmelsam/mkrvidor4000.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Minitronics v2.0](../boards/atmelsam/minitronics20.md) | SAMD21J18A | 48MHz | 256KB | 32KB |
| [Moteino M0](../boards/atmelsam/moteino-zero.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [NANO 33 IoT](../boards/atmelsam/nano-33-iot.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [SODAQ Autonomo](../boards/atmelsam/sodaq-autonomo.md) | SAMD21J18A | 48MHz | 256KB | 32KB |
| [SODAQ ExpLoRer](../boards/atmelsam/sodaq-explorer.md) | SAMD21J18A | 48MHz | 256KB | 32KB |
| [SODAQ ONE](../boards/atmelsam/sodaq-one.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [SODAQ SARA](../boards/atmelsam/sodaq-sara.md) | SAMD21J18A | 48MHz | 256KB | 32KB |
| [SODAQ SFF](../boards/atmelsam/sodaq-sff.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [SainSmart Due (Programming Port)](../boards/atmelsam/sainsmartdue.md) | AT91SAM3X8E | 84MHz | 512KB | 96KB |
| [SainSmart Due (USB Native Port)](../boards/atmelsam/sainsmartdueusb.md) | AT91SAM3X8E | 84MHz | 512KB | 96KB |
| [Seeeduino Femto M0](../boards/atmelsam/seeed-femto.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Seeeduino LoRaWAN](../boards/atmelsam/seeeduino-lorawan.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Seeeduino Wio Lite MG126](../boards/atmelsam/seeed-wio-lite-mg126.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Seeeduino Wio Terminal](../boards/atmelsam/seeed-wio-terminal.md) | SAMD51P19A | 120MHz | 496KB | 192KB |
| [Seeeduino XIAO](../boards/atmelsam/seeed-xiao.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Seeeduino Zero](../boards/atmelsam/seeed-zero.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [SparkFun 9DoF Razor IMU M0](../boards/atmelsam/sparkfun-samd21-9dof.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [SparkFun Qwiic Micro](../boards/atmelsam/sparkfun-qwiic-micro-samd21e.md) | SAMD21E18A | 48MHz | 256KB | 32KB |
| [SparkFun RedBoard Turbo](../boards/atmelsam/sparkfun-redboard-turbo.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [SparkFun SAMD21 Dev Breakout](../boards/atmelsam/sparkfun-samd21-dev-usb.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [SparkFun SAMD21 Mini Breakout](../boards/atmelsam/sparkfun-samd21-mini-usb.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [SparkFun SAMD21 Pro RF](../boards/atmelsam/sparkfun-samd21-prorf.md) | SAMD21G18A | 48MHz | 256KB | 32KB |
| [SparkFun SAMD51 MicroMod](../boards/atmelsam/sparkfun-samd51-micromod.md) | SAMD51J20A | 120MHz | 496KB | 192KB |
| [SparkFun SAMD51 Thing Plus](../boards/atmelsam/sparkfun-samd51-thing-plus.md) | SAMD51J20A | 120MHz | 496KB | 192KB |
| [Tuino 096](../boards/atmelsam/tuinozero96.md) | SAMD21G18A | 48MHz | 256KB | 32KB |

## Stable and upstream versions

Choose between the [stable releases](https://github.com/platformio/platform-atmelsam/releases) of the Atmel SAM platform and its latest upstream version with the [platform](../../reference/platformio-ini/env/platform.md) option in [platformio.ini](../../reference/platformio-ini/index.md).

### Stable

```ini
; Latest stable version, NOT recommended
; Pin the version as shown below
[env:latest_stable]
platform = atmelsam
board = ...

; Specific version
[env:custom_stable]
platform = atmelsam@x.y.z
board = ...
```

### Upstream

```ini
[env:upstream_develop]
platform = https://github.com/platformio/platform-atmelsam.git
board = ...
```

## Packages

| Name | Description |
|---|---|
| [framework-arduino-sam](https://registry.platformio.org/tools/platformio/framework-arduino-sam) | The official Arduino Wiring-based Framework for ATSAM3 microcontrollers |
| [framework-arduino-samd](https://registry.platformio.org/tools/platformio/framework-arduino-samd) | The official Arduino Wiring-based Framework for Microchip SAM D microcontrollers |
| [framework-arduino-samd-adafruit](https://registry.platformio.org/tools/platformio/framework-arduino-samd-adafruit) | Arduino Wiring-based Framework for Microchip SAM D microcontrollers (Adafruit SAMD Core) |
| [framework-arduino-samd-moteino](https://registry.platformio.org/tools/platformio/framework-arduino-samd-moteino) | Arduino Wiring-based Framework for Microchip SAM D microcontrollers (Moteino SAMD Core) |
| [framework-arduino-samd-reprap](https://registry.platformio.org/tools/platformio/framework-arduino-samd-reprap) | Arduino Wiring-based Framework for Microchip SAM D microcontrollers (RepRap SAMD Core) |
| [framework-arduino-samd-seeed](https://registry.platformio.org/tools/platformio/framework-arduino-samd-seeed) | Arduino Wiring-based Framework for Microchip SAM D microcontrollers (Seeed SAMD Core) |
| [framework-arduino-samd-sodaq](https://registry.platformio.org/tools/platformio/framework-arduino-samd-sodaq) | Arduino Wiring-based Framework for Microchip SAM D microcontrollers (SODAQ SAMD Core) |
| [framework-arduino-samd-sparkfun](https://registry.platformio.org/tools/platformio/framework-arduino-samd-sparkfun) | Arduino Wiring-based Framework for Microchip SAM D microcontrollers (SparkFun SAMD Core) |
| [framework-arduino-samd-tuino0](https://registry.platformio.org/tools/platformio/framework-arduino-samd-tuino0) | Arduino Wiring-based Framework for Microchip SAM D microcontrollers (Tuino0 SAMD Core) |
| [framework-cmsis](https://registry.platformio.org/tools/platformio/framework-cmsis) | Vendor-independent hardware abstraction layer for the Cortex-M processor series |
| [framework-cmsis-atmel](https://registry.platformio.org/tools/platformio/framework-cmsis-atmel) | Atmel Smart ARM devices CMSIS module |
| [framework-zephyr](https://registry.platformio.org/tools/platformio/framework-zephyr) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
| [tool-avrdude](https://registry.platformio.org/tools/platformio/tool-avrdude) | AVRDUDE is a utility to download/upload/manipulate the ROM and EEPROM contents of AVR microcontrollers |
| [tool-bossac](https://registry.platformio.org/tools/platformio/tool-bossac) | Basic Open Source SAM-BA Application (BOSSA) |
| [tool-cmake](https://registry.platformio.org/tools/platformio/tool-cmake) | CMake is an open-source, cross-platform family of tools designed to build, test and package software |
| [tool-dtc](https://registry.platformio.org/tools/platformio/tool-dtc) | Device tree compiler |
| [tool-gperf](https://registry.platformio.org/tools/platformio/tool-gperf) | GNU gperf is a perfect hash function generator |
| [tool-jlink](https://registry.platformio.org/tools/platformio/tool-jlink) | Software and Documentation Pack for SEGGER J-Link debug probes |
| [tool-ninja](https://registry.platformio.org/tools/platformio/tool-ninja) | Ninja is a small build system with a focus on speed |
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
| [Zephyr](../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |

## Boards

To list the boards from the command line, use [pio boards](../../reference/cli/pio-boards.md).

### Adafruit

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Adafruit BLM Badge](../boards/atmelsam/adafruit-blm-badge.md) | External | SAMD21E18A | 48MHz | 256KB | 32KB |
| [Adafruit Circuit Playground Express](../boards/atmelsam/adafruit-circuitplayground-m0.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Adafruit Crickit M0](../boards/atmelsam/adafruit-crickit-m0.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Adafruit Feather M0](../boards/atmelsam/adafruit-feather-m0.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Adafruit Feather M0 Express](../boards/atmelsam/adafruit-feather-m0-express.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Adafruit Feather M4 CAN](../boards/atmelsam/adafruit-feather-m4-can.md) | External | SAME51J19A | 120MHz | 496KB | 192KB |
| [Adafruit Feather M4 Express](../boards/atmelsam/adafruit-feather-m4.md) | External | SAMD51J19A | 120MHz | 512KB | 192KB |
| [Adafruit Gemma M0](../boards/atmelsam/adafruit-gemma-m0.md) | External | SAMD21E18A | 48MHz | 256KB | 32KB |
| [Adafruit Grand Central M4](../boards/atmelsam/adafruit-grandcentral-m4.md) | External | SAMD51P20A | 120MHz | 1MB | 256KB |
| [Adafruit Hallowing M0](../boards/atmelsam/adafruit-hallowing.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Adafruit Hallowing M4](../boards/atmelsam/adafruit-hallowing-m4.md) | External | SAMD51J19A | 120MHz | 496KB | 192KB |
| [Adafruit ItsyBitsy M0](../boards/atmelsam/adafruit-itsybitsy-m0.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Adafruit ItsyBitsy M4](../boards/atmelsam/adafruit-itsybitsy-m4.md) | External | SAMD51G19A | 120MHz | 512KB | 192KB |
| [Adafruit MONSTER M4SK](../boards/atmelsam/adafruit-monster-m4sk.md) | External | SAMD51G19A | 120MHz | 496KB | 192KB |
| [Adafruit Matrix Portal M4](../boards/atmelsam/adafruit-matrix-portal-m4.md) | External | SAMD51J19A | 120MHz | 496KB | 192KB |
| [Adafruit Metro M0 Express](../boards/atmelsam/adafruit-metro-m0.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Adafruit Metro M4](../boards/atmelsam/adafruit-metro-m4.md) | External | SAMD51J19A | 120MHz | 512KB | 192KB |
| [Adafruit Metro M4 AirLift Lite](../boards/atmelsam/adafruit-metro-m4-airliftlite.md) | External | SAMD51J19A | 120MHz | 512KB | 192KB |
| [Adafruit NeoKey Trinkey](../boards/atmelsam/adafruit-neokeytrinkey-m0.md) | External | SAMD21E18A | 48MHz | 256KB | 32KB |
| [Adafruit NeoPixel Trinkey](../boards/atmelsam/adafruit-neotrinkey-m0.md) | External | SAMD21E18A | 48MHz | 256KB | 32KB |
| [Adafruit ProxLight Trinkey](../boards/atmelsam/adafruit-proxlighttrinkey-m0.md) | External | SAMD21E18A | 48MHz | 256KB | 32KB |
| [Adafruit PyGamer Advance M4](../boards/atmelsam/adafruit-pygamer-advance-m4.md) | External | SAMD51J20A | 120MHz | 1MB | 256KB |
| [Adafruit PyGamer M4 Express](../boards/atmelsam/adafruit-pygamer-m4.md) | External | SAMD51J19A | 120MHz | 512KB | 192KB |
| [Adafruit PyPortal M4](../boards/atmelsam/adafruit-pyportal-m4.md) | External | SAMD51J20A | 120MHz | 1MB | 256KB |
| [Adafruit PyPortal M4 Titano](../boards/atmelsam/adafruit-pyportal-m4-titano.md) | External | SAMD51J20A | 120MHz | 1MB | 256KB |
| [Adafruit QT Py M0](../boards/atmelsam/adafruit-qt-py-m0.md) | External | SAMD21E18A | 48MHz | 256KB | 32KB |
| [Adafruit Rotary Trinkey](../boards/atmelsam/adafruit-rotarytrinkey-m0.md) | External | SAMD21E18A | 48MHz | 256KB | 32KB |
| [Adafruit Slide Trinkey](../boards/atmelsam/adafruit-slidetrinkey-m0.md) | External | SAMD21E18A | 48MHz | 256KB | 32KB |
| [Adafruit Trellis M4](../boards/atmelsam/adafruit-trellis-m4.md) | External | SAMD51J19A | 120MHz | 512KB | 192KB |
| [Adafruit Trinket M0](../boards/atmelsam/adafruit-trinket-m0.md) | External | SAMD21E18A | 48MHz | 256KB | 32KB |
| [Adafruit pIRkey](../boards/atmelsam/adafruit-pirkey.md) | External | SAMD21E18A | 48MHz | 256KB | 32KB |
| [Adafruit pyBadge AirLift M4](../boards/atmelsam/adafruit-pybadge-airlift-m4.md) | External | SAMD51J20A | 120MHz | 1008KB | 192KB |
| [Adafruit pyBadge M4 Express](../boards/atmelsam/adafruit-pybadge-m4.md) | External | SAMD51J19A | 120MHz | 512KB | 192KB |

### Arduino

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Arduino Due (Programming Port)](../boards/atmelsam/due.md) | External | AT91SAM3X8E | 84MHz | 512KB | 96KB |
| [Arduino Due (USB Native Port)](../boards/atmelsam/dueusb.md) | External | AT91SAM3X8E | 84MHz | 512KB | 96KB |
| [Arduino M0](../boards/atmelsam/mzerousb.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Arduino M0 Pro (Native USB Port)](../boards/atmelsam/mzeroprousb.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Arduino M0 Pro (Programming/Debug Port)](../boards/atmelsam/mzeropro.md) | On-board | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Arduino MKR FOX 1200](../boards/atmelsam/mkrfox1200.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Arduino MKR GSM 1400](../boards/atmelsam/mkrgsm1400.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Arduino MKR NB 1500](../boards/atmelsam/mkrnb1500.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Arduino MKR WAN 1300](../boards/atmelsam/mkrwan1300.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Arduino MKR WAN 1310](../boards/atmelsam/mkrwan1310.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Arduino MKR WiFi 1010](../boards/atmelsam/mkrwifi1010.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Arduino MKR1000](../boards/atmelsam/mkr1000usb.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Arduino MKRZERO](../boards/atmelsam/mkrzero.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Arduino Tian](../boards/atmelsam/tian.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Arduino Zero (Programming/Debug Port)](../boards/atmelsam/zero.md) | On-board | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Arduino Zero (USB Native Port)](../boards/atmelsam/zerousb.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |
| [MKR Vidor 4000](../boards/atmelsam/mkrvidor4000.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |
| [NANO 33 IoT](../boards/atmelsam/nano-33-iot.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |

### Atmel

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Atmel ATSAMR21-XPRO](../boards/atmelsam/samr21-xpro.md) | On-board | SAMR21G18A | 48MHz | 256KB | 32KB |
| [Atmel ATSAMW25-XPRO](../boards/atmelsam/samd21g18a.md) | On-board | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Atmel SAMC21-XPRO](../boards/atmelsam/samc21-xpro.md) | On-board | SAMC21J18A | 48MHz | 256KB | 32KB |
| [Atmel SAMD21-XPRO](../boards/atmelsam/samd21-xpro.md) | On-board | SAMD21J18A | 48MHz | 256KB | 32KB |

### Digistump

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Digistump DigiX](../boards/atmelsam/digix.md) | External | AT91SAM3X8E | 84MHz | 512KB | 96KB |

### Gimasi

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Tuino 096](../boards/atmelsam/tuinozero96.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |

### LowPowerLab

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [LowPowerLab CurrentRanger](../boards/atmelsam/current-ranger.md) | No | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Moteino M0](../boards/atmelsam/moteino-zero.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |

### ReprapWorld

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Minitronics v2.0](../boards/atmelsam/minitronics20.md) | External | SAMD21J18A | 48MHz | 256KB | 32KB |

### SODAQ

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [SODAQ Autonomo](../boards/atmelsam/sodaq-autonomo.md) | External | SAMD21J18A | 48MHz | 256KB | 32KB |
| [SODAQ ExpLoRer](../boards/atmelsam/sodaq-explorer.md) | External | SAMD21J18A | 48MHz | 256KB | 32KB |
| [SODAQ ONE](../boards/atmelsam/sodaq-one.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |
| [SODAQ SARA](../boards/atmelsam/sodaq-sara.md) | External | SAMD21J18A | 48MHz | 256KB | 32KB |
| [SODAQ SFF](../boards/atmelsam/sodaq-sff.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |

### SainSmart

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [SainSmart Due (Programming Port)](../boards/atmelsam/sainsmartdue.md) | External | AT91SAM3X8E | 84MHz | 512KB | 96KB |
| [SainSmart Due (USB Native Port)](../boards/atmelsam/sainsmartdueusb.md) | External | AT91SAM3X8E | 84MHz | 512KB | 96KB |

### Seeed

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Seeeduino Femto M0](../boards/atmelsam/seeed-femto.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Seeeduino LoRaWAN](../boards/atmelsam/seeeduino-lorawan.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Seeeduino Wio Lite MG126](../boards/atmelsam/seeed-wio-lite-mg126.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Seeeduino Wio Terminal](../boards/atmelsam/seeed-wio-terminal.md) | External | SAMD51P19A | 120MHz | 496KB | 192KB |
| [Seeeduino XIAO](../boards/atmelsam/seeed-xiao.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |
| [Seeeduino Zero](../boards/atmelsam/seeed-zero.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |

### SparkFun

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [SparkFun 9DoF Razor IMU M0](../boards/atmelsam/sparkfun-samd21-9dof.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |
| [SparkFun Qwiic Micro](../boards/atmelsam/sparkfun-qwiic-micro-samd21e.md) | External | SAMD21E18A | 48MHz | 256KB | 32KB |
| [SparkFun RedBoard Turbo](../boards/atmelsam/sparkfun-redboard-turbo.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |
| [SparkFun SAMD21 Dev Breakout](../boards/atmelsam/sparkfun-samd21-dev-usb.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |
| [SparkFun SAMD21 Mini Breakout](../boards/atmelsam/sparkfun-samd21-mini-usb.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |
| [SparkFun SAMD21 Pro RF](../boards/atmelsam/sparkfun-samd21-prorf.md) | External | SAMD21G18A | 48MHz | 256KB | 32KB |
| [SparkFun SAMD51 MicroMod](../boards/atmelsam/sparkfun-samd51-micromod.md) | External | SAMD51J20A | 120MHz | 496KB | 192KB |
| [SparkFun SAMD51 Thing Plus](../boards/atmelsam/sparkfun-samd51-thing-plus.md) | External | SAMD51J20A | 120MHz | 496KB | 192KB |
