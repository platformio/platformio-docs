---
title: "Nordic nRF51"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "The Nordic nRF51 development platform for PlatformIO: configuration, frameworks, packages, debugging and boards."
---

# Nordic nRF51

**Registry:** [https://registry.platformio.org/platforms/platformio/nordicnrf51](https://registry.platformio.org/platforms/platformio/nordicnrf51)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/nordicnrf51`

The Nordic nRF51 Series is a family of highly flexible, multi-protocol, system-on-chip (SoC) devices for ultra-low power wireless applications. nRF51 Series devices support a range of protocol stacks including Bluetooth Smart (previously called Bluetooth low energy), ANT and proprietary 2.4GHz protocols such as Gazell.

Vendor website: [www.nordicsemi.com](https://www.nordicsemi.com/eng/Products/nRF51-Series-SoC?utm_source=platformio.org&utm_medium=docs).

## Examples

Example projects from the [Nordic nRF51 platform repository](https://github.com/platformio/platform-nordicnrf51/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [zephyr-blink](https://github.com/platformio/platform-nordicnrf51/tree/master/examples/zephyr-blink?utm_source=platformio.org&utm_medium=docs)
- [arduino-blink](https://github.com/platformio/platform-nordicnrf51/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs)
- [arduino-ble-led](https://github.com/platformio/platform-nordicnrf51/tree/master/examples/arduino-ble-led?utm_source=platformio.org&utm_medium=docs)
- [zephyr-ble-eddystone](https://github.com/platformio/platform-nordicnrf51/tree/master/examples/zephyr-ble-eddystone?utm_source=platformio.org&utm_medium=docs)
- [arduino-internal-libs](https://github.com/platformio/platform-nordicnrf51/tree/master/examples/arduino-internal-libs?utm_source=platformio.org&utm_medium=docs)

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
| [BBC micro:bit](../boards/nordicnrf51/bbcmicrobit.md) | NRF51822 | 16MHz | 256KB | 16KB |
| [Calliope mini](../boards/nordicnrf51/calliope-mini.md) | NRF51822 | 16MHz | 256KB | 16KB |
| [Nordic Beacon Kit (PCA20006)](../boards/nordicnrf51/nrf51-beacon.md) | NRF51822 | 32MHz | 256KB | 32KB |
| [Nordic nRF51 Dongle (PCA10031)](../boards/nordicnrf51/nrf51-dongle.md) | NRF51822 | 32MHz | 256KB | 32KB |
| [Nordic nRF51X22 Development Kit(PCA1000X)](../boards/nordicnrf51/nrf51-dk.md) | NRF51822 | 32MHz | 256KB | 32KB |
| [RedBearLab BLE Nano 1.5](../boards/nordicnrf51/redbearlabblenano.md) | NRF51822 | 16MHz | 256KB | 32KB |
| [RedBearLab nRF51822](../boards/nordicnrf51/redbearlab.md) | NRF51822 | 16MHz | 256KB | 16KB |
| [Seeed Tiny BLE](../boards/nordicnrf51/seeedtinyble.md) | NRF51822 | 16MHz | 256KB | 16KB |
| [VNG VBLUNO51](../boards/nordicnrf51/vbluno51.md) | NRF51822 | 16MHz | 128KB | 32KB |

#### Boards that need an external debug probe

These boards support [Debugging](../../guides/debugging/index.md) with an external debug probe. See each board's page for the compatible probes.

| Name | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|
| [BluzDK](../boards/nordicnrf51/bluz-dk.md) | NRF51822 | 32MHz | 256KB | 32KB |
| [OSHChip](../boards/nordicnrf51/oshchip.md) | NRF51822 | 32MHz | 256KB | 32KB |
| [Sino:Bit](../boards/nordicnrf51/sinobit.md) | NRF51822 | 32MHz | 256KB | 32KB |
| [Waveshare BLE400](../boards/nordicnrf51/waveshare-ble400.md) | NRF51822 | 32MHz | 256KB | 32KB |
| [ng-beacon](../boards/nordicnrf51/ng-beacon.md) | NRF51822 | 16MHz | 256KB | 32KB |

## Stable and upstream versions

Choose between the [stable releases](https://github.com/platformio/platform-nordicnrf51/releases) of the Nordic nRF51 platform and its latest upstream version with the [platform](../../reference/platformio-ini/env/platform.md) option in [platformio.ini](../../reference/platformio-ini/index.md).

### Stable

```ini
; Latest stable version, NOT recommended
; Pin the version as shown below
[env:latest_stable]
platform = nordicnrf51
board = ...

; Specific version
[env:custom_stable]
platform = nordicnrf51@x.y.z
board = ...
```

### Upstream

```ini
[env:upstream_develop]
platform = https://github.com/platformio/platform-nordicnrf51.git
board = ...
```

## Packages

| Name | Description |
|---|---|
| [framework-arduinonordicnrf5](https://registry.platformio.org/tools/platformio/framework-arduinonordicnrf5) | Arduino Wiring-based Framework for Nordic Semiconductor nRF5 based boards |
| [framework-zephyr](https://registry.platformio.org/tools/platformio/framework-zephyr) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |
| [tool-cmake](https://registry.platformio.org/tools/platformio/tool-cmake) | CMake is an open-source, cross-platform family of tools designed to build, test and package software |
| [tool-dtc](https://registry.platformio.org/tools/platformio/tool-dtc) | Device tree compiler |
| [tool-gperf](https://registry.platformio.org/tools/platformio/tool-gperf) | GNU gperf is a perfect hash function generator |
| [tool-jlink](https://registry.platformio.org/tools/platformio/tool-jlink) | Software and Documentation Pack for SEGGER J-Link debug probes |
| [tool-ninja](https://registry.platformio.org/tools/platformio/tool-ninja) | Ninja is a small build system with a focus on speed |
| [tool-nrfjprog](https://registry.platformio.org/tools/platformio/tool-nrfjprog) | nRFx command line tools |
| [tool-openocd](https://registry.platformio.org/tools/platformio/tool-openocd) | Open On-Chip Debugger. Free and Open On-Chip Debugging, In-System Programming and Boundary-Scan Testing |
| [tool-sreccat](https://registry.platformio.org/tools/platformio/tool-sreccat) | Collection of powerful tools for manipulating EPROM load files |
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

### BBC

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [BBC micro:bit](../boards/nordicnrf51/bbcmicrobit.md) | On-board | NRF51822 | 16MHz | 256KB | 16KB |

### BluzDK

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [BluzDK](../boards/nordicnrf51/bluz-dk.md) | External | NRF51822 | 32MHz | 256KB | 32KB |

### Calliope

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Calliope mini](../boards/nordicnrf51/calliope-mini.md) | On-board | NRF51822 | 16MHz | 256KB | 16KB |

### Nordic

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Nordic Beacon Kit (PCA20006)](../boards/nordicnrf51/nrf51-beacon.md) | On-board | NRF51822 | 32MHz | 256KB | 32KB |
| [Nordic nRF51 Dongle (PCA10031)](../boards/nordicnrf51/nrf51-dongle.md) | On-board | NRF51822 | 32MHz | 256KB | 32KB |
| [Nordic nRF51X22 Development Kit(PCA1000X)](../boards/nordicnrf51/nrf51-dk.md) | On-board | NRF51822 | 32MHz | 256KB | 32KB |

### OSHChip

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [OSHChip](../boards/nordicnrf51/oshchip.md) | External | NRF51822 | 32MHz | 256KB | 32KB |

### RedBearLab

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [RedBearLab BLE Nano 1.5](../boards/nordicnrf51/redbearlabblenano.md) | On-board | NRF51822 | 16MHz | 256KB | 32KB |
| [RedBearLab nRF51822](../boards/nordicnrf51/redbearlab.md) | On-board | NRF51822 | 16MHz | 256KB | 16KB |

### SeeedStudio

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Seeed Tiny BLE](../boards/nordicnrf51/seeedtinyble.md) | On-board | NRF51822 | 16MHz | 256KB | 16KB |

### VNG

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [VNG VBLUNO51](../boards/nordicnrf51/vbluno51.md) | On-board | NRF51822 | 16MHz | 128KB | 32KB |

### Waveshare

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Waveshare BLE400](../boards/nordicnrf51/waveshare-ble400.md) | External | NRF51822 | 32MHz | 256KB | 32KB |

### ng-beacon

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [ng-beacon](../boards/nordicnrf51/ng-beacon.md) | External | NRF51822 | 16MHz | 256KB | 32KB |

### sino:bit

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Sino:Bit](../boards/nordicnrf51/sinobit.md) | External | NRF51822 | 32MHz | 256KB | 32KB |
