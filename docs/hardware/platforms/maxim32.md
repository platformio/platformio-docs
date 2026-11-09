---
title: "Maxim 32"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
---

<a id="platform-maxim32"></a>

# Maxim 32

**Registry:** [https://registry.platformio.org/platforms/platformio/maxim32](https://registry.platformio.org/platforms/platformio/maxim32)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/maxim32`

Maxim's microcontrollers provide low-power, efficient, and secure solutions for challenging embedded applications. Maxim's processors embed cutting-edge technologies to secure data and intellectual property, proven analog circuitry for real-world applications, and battery-conserving low power operation.

For more detailed information please visit [vendor site](https://www.maximintegrated.com/en/products/digital/microcontrollers.html?utm_source=platformio.org&utm_medium=docs).

## Examples

Examples are listed from [Maxim 32 development platform repository](https://github.com/platformio/platform-maxim32/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [mbed-rtos-mutex](https://github.com/platformio/platform-maxim32/tree/master/examples/mbed-rtos-mutex?utm_source=platformio.org&utm_medium=docs)
- [mbed-rtos-blink-baremetal](https://github.com/platformio/platform-maxim32/tree/master/examples/mbed-rtos-blink-baremetal?utm_source=platformio.org&utm_medium=docs)
- [mbed-rtos-sysinfo](https://github.com/platformio/platform-maxim32/tree/master/examples/mbed-rtos-sysinfo?utm_source=platformio.org&utm_medium=docs)

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
| [Maxim ARM mbed Enabled Development Platform for MAX32600](../boards/maxim32/max32600mbed.md) | MAX32600 | 24MHz | 256KB | 32KB |

#### External Debug Tools

Boards listed below are compatible with [Debugging](../../guides/debugging/index.md) but **DEPEND ON** external debug probe. They **ARE NOT READY** for debugging. Please click on board name for the further details.

| Name | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|
| [MAX32620FTHR](../boards/maxim32/max32620fthr.md) | MAX32620FTHR | 96MHz | 2MB | 256KB |
| [Maxim Health Sensor Platform](../boards/maxim32/max32620hsp.md) | MAX32620 | 96MHz | 2MB | 256KB |
| [Maxim Wireless Sensor Node Demonstrator](../boards/maxim32/maxwsnenv.md) | MAX32610 | 24MHz | 256KB | 32KB |

## Stable and upstream versions

You can switch between [stable releases](https://github.com/platformio/platform-maxim32/releases) of Maxim 32 development platform and the latest upstream version using [platform](../../reference/platformio-ini/env/platform.md) option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md) as described below.

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

**Linux Users**:

- Install "udev" rules [99-platformio-udev.rules](../../get-started/install/udev-rules.md)
- Raspberry Pi users, please read this article [Enable serial port on Raspberry Pi](https://hallard.me/enable-serial-port-on-raspberry-pi/).

**Windows Users:**

Please check that you have a correctly installed USB driver from board manufacturer

:::

## Frameworks

| Name | Description |
|---|---|
| [Mbed](../frameworks/mbed.mdx) | Arm Mbed OS is a platform operating system designed for the internet of things |

## Boards

:::note

- You can list pre-configured boards by [pio boards](../../reference/cli/pio-boards.md) command
- For more detailed `board` information please scroll the tables below by horizontally.

:::

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
