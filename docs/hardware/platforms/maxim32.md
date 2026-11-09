---
title: "Maxim 32"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "The Maxim 32 development platform for PlatformIO: configuration, frameworks, packages, debugging and boards."
---

# Maxim 32

**Registry:** [https://registry.platformio.org/platforms/platformio/maxim32](https://registry.platformio.org/platforms/platformio/maxim32)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/maxim32`

Maxim's microcontrollers provide low-power, efficient, and secure solutions for challenging embedded applications. Maxim's processors embed cutting-edge technologies to secure data and intellectual property, proven analog circuitry for real-world applications, and battery-conserving low power operation.

Vendor website: [www.maximintegrated.com](https://www.maximintegrated.com/en/products/digital/microcontrollers.html?utm_source=platformio.org&utm_medium=docs).

## Examples

Example projects from the [Maxim 32 platform repository](https://github.com/platformio/platform-maxim32/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [mbed-rtos-mutex](https://github.com/platformio/platform-maxim32/tree/master/examples/mbed-rtos-mutex?utm_source=platformio.org&utm_medium=docs)
- [mbed-rtos-blink-baremetal](https://github.com/platformio/platform-maxim32/tree/master/examples/mbed-rtos-blink-baremetal?utm_source=platformio.org&utm_medium=docs)
- [mbed-rtos-sysinfo](https://github.com/platformio/platform-maxim32/tree/master/examples/mbed-rtos-sysinfo?utm_source=platformio.org&utm_medium=docs)

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
| [Maxim ARM mbed Enabled Development Platform for MAX32600](../boards/maxim32/max32600mbed.md) | MAX32600 | 24MHz | 256KB | 32KB |

#### Boards that need an external debug probe

These boards support [Debugging](../../guides/debugging/index.md) with an external debug probe. See each board's page for the compatible probes.

| Name | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|
| [MAX32620FTHR](../boards/maxim32/max32620fthr.md) | MAX32620FTHR | 96MHz | 2MB | 256KB |
| [Maxim Health Sensor Platform](../boards/maxim32/max32620hsp.md) | MAX32620 | 96MHz | 2MB | 256KB |
| [Maxim Wireless Sensor Node Demonstrator](../boards/maxim32/maxwsnenv.md) | MAX32610 | 24MHz | 256KB | 32KB |

## Stable and upstream versions

Choose between the [stable releases](https://github.com/platformio/platform-maxim32/releases) of the Maxim 32 platform and its latest upstream version with the [platform](../../reference/platformio-ini/env/platform.md) option in [platformio.ini](../../reference/platformio-ini/index.md).

### Stable

```ini
; Latest stable version, NOT recommended
; Pin the version as shown below
[env:latest_stable]
platform = maxim32
board = ...

; Specific version
[env:custom_stable]
platform = maxim32@x.y.z
board = ...
```

### Upstream

```ini
[env:upstream_develop]
platform = https://github.com/platformio/platform-maxim32.git
board = ...
```

## Packages

| Name | Description |
|---|---|
| [framework-mbed](https://registry.platformio.org/tools/platformio/framework-mbed) | Arm Mbed OS is a platform operating system designed for the internet of things |
| [tool-jlink](https://registry.platformio.org/tools/platformio/tool-jlink) | Software and Documentation Pack for SEGGER J-Link debug probes |
| [tool-pyocd](https://registry.platformio.org/tools/platformio/tool-pyocd) | Open source python library for programming and debugging ARM Cortex-M microcontrollers using CMSIS-DAP |
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
| [Mbed](../frameworks/mbed.mdx) | Arm Mbed OS is a platform operating system designed for the internet of things |

## Boards

To list the boards from the command line, use [pio boards](../../reference/cli/pio-boards.md).

### Maxim

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [MAX32620FTHR](../boards/maxim32/max32620fthr.md) | External | MAX32620FTHR | 96MHz | 2MB | 256KB |
| [MAX32625MBED](../boards/maxim32/max32625mbed.md) | No | MAX32625 | 96MHz | 512KB | 160KB |
| [MAX32625PICO](../boards/maxim32/max32625pico.md) | No | MAX32625 | 96MHz | 512KB | 160KB |
| [Maxim ARM mbed Enabled Development Platform for MAX32600](../boards/maxim32/max32600mbed.md) | On-board | MAX32600 | 24MHz | 256KB | 32KB |
| [Maxim Health Sensor Platform](../boards/maxim32/max32620hsp.md) | External | MAX32620 | 96MHz | 2MB | 256KB |
| [Maxim MAX32630FTHR Application Platform](../boards/maxim32/max32630fthr.md) | No | MAX32630 | 96MHz | 2MB | 512KB |
| [Maxim Wireless Sensor Node Demonstrator](../boards/maxim32/maxwsnenv.md) | External | MAX32610 | 24MHz | 256KB | 32KB |

### Sigma Delta Technologies

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [SDT32620B](../boards/maxim32/sdt32620b.md) | No | MAX32620IWG | 96MHz | 2MB | 256KB |
| [SDT32625B](../boards/maxim32/sdt32625b.md) | No | MAX32625ITK | 96MHz | 512KB | 160KB |
