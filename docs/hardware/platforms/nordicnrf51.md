---
title: "Nordic nRF51"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
---

<a id="platform-nordicnrf51"></a>

# Nordic nRF51

**Registry:** [https://registry.platformio.org/platforms/platformio/nordicnrf51](https://registry.platformio.org/platforms/platformio/nordicnrf51)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/nordicnrf51`

The Nordic nRF51 Series is a family of highly flexible, multi-protocol, system-on-chip (SoC) devices for ultra-low power wireless applications. nRF51 Series devices support a range of protocol stacks including Bluetooth Smart (previously called Bluetooth low energy), ANT and proprietary 2.4GHz protocols such as Gazell.

For more detailed information please visit [vendor site](https://www.nordicsemi.com/eng/Products/nRF51-Series-SoC?utm_source=platformio.org&utm_medium=docs).

## Examples

Examples are listed from [Nordic nRF51 development platform repository](https://github.com/platformio/platform-nordicnrf51/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [zephyr-blink](https://github.com/platformio/platform-nordicnrf51/tree/master/examples/zephyr-blink?utm_source=platformio.org&utm_medium=docs)
- [arduino-blink](https://github.com/platformio/platform-nordicnrf51/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs)
- [arduino-ble-led](https://github.com/platformio/platform-nordicnrf51/tree/master/examples/arduino-ble-led?utm_source=platformio.org&utm_medium=docs)
- [zephyr-ble-eddystone](https://github.com/platformio/platform-nordicnrf51/tree/master/examples/zephyr-ble-eddystone?utm_source=platformio.org&utm_medium=docs)
- [arduino-internal-libs](https://github.com/platformio/platform-nordicnrf51/tree/master/examples/arduino-internal-libs?utm_source=platformio.org&utm_medium=docs)

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
| [BBC micro:bit](../boards/nordicnrf51/bbcmicrobit.md) | NRF51822 | 16MHz | 256KB | 16KB |
| [Calliope mini](../boards/nordicnrf51/calliope-mini.md) | NRF51822 | 16MHz | 256KB | 16KB |
| [Nordic Beacon Kit (PCA20006)](../boards/nordicnrf51/nrf51-beacon.md) | NRF51822 | 32MHz | 256KB | 32KB |
| [Nordic nRF51 Dongle (PCA10031)](../boards/nordicnrf51/nrf51-dongle.md) | NRF51822 | 32MHz | 256KB | 32KB |
| [Nordic nRF51X22 Development Kit(PCA1000X)](../boards/nordicnrf51/nrf51-dk.md) | NRF51822 | 32MHz | 256KB | 32KB |
| [RedBearLab BLE Nano 1.5](../boards/nordicnrf51/redbearlabblenano.md) | NRF51822 | 16MHz | 256KB | 32KB |
| [RedBearLab nRF51822](../boards/nordicnrf51/redbearlab.md) | NRF51822 | 16MHz | 256KB | 16KB |
| [Seeed Tiny BLE](../boards/nordicnrf51/seeedtinyble.md) | NRF51822 | 16MHz | 256KB | 16KB |
| [VNG VBLUNO51](../boards/nordicnrf51/vbluno51.md) | NRF51822 | 16MHz | 128KB | 32KB |

#### External Debug Tools

Boards listed below are compatible with [Debugging](../../guides/debugging/index.md) but **DEPEND ON** external debug probe. They **ARE NOT READY** for debugging. Please click on board name for the further details.

| Name | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|
| [BluzDK](../boards/nordicnrf51/bluz-dk.md) | NRF51822 | 32MHz | 256KB | 32KB |
| [OSHChip](../boards/nordicnrf51/oshchip.md) | NRF51822 | 32MHz | 256KB | 32KB |
| [Sino:Bit](../boards/nordicnrf51/sinobit.md) | NRF51822 | 32MHz | 256KB | 32KB |
| [Waveshare BLE400](../boards/nordicnrf51/waveshare-ble400.md) | NRF51822 | 32MHz | 256KB | 32KB |
| [ng-beacon](../boards/nordicnrf51/ng-beacon.md) | NRF51822 | 16MHz | 256KB | 32KB |

## Stable and upstream versions

You can switch between [stable releases](https://github.com/platformio/platform-nordicnrf51/releases) of Nordic nRF51 development platform and the latest upstream version using [platform](../../reference/platformio-ini/env/platform.md) option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md) as described below.

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
| [Zephyr](../frameworks/zephyr.mdx) | Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures |

## Boards

:::note

- You can list pre-configured boards by [pio boards](../../reference/cli/pio-boards.md) command
- For more detailed `board` information please scroll the tables below by horizontally.

:::

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
