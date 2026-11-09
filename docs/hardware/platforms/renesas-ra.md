---
title: "Renesas RA"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
---

<a id="platform-renesas-ra"></a>

# Renesas RA

**Registry:** [https://registry.platformio.org/platforms/platformio/renesas-ra](https://registry.platformio.org/platforms/platformio/renesas-ra)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/renesas-ra`

Renesas Advanced (RA) 32-bit microcontrollers with the Arm Cortex-M33, -M23 and -M4 processor cores deliver key advantages compared to competitive Arm Cortex-M MCUs by providing stronger embedded security, superior CoreMark performance and ultra-low power operation.

For more detailed information please visit [vendor site](https://www.renesas.com/us/en/products/microcontrollers-microprocessors/ra-cortex-m-mcus?utm_source=platformio.org&utm_medium=docs).

## Examples

Examples are listed from [Renesas RA development platform repository](https://github.com/platformio/platform-renesas-ra/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [arduino-uno-r4-led-animation](https://github.com/platformio/platform-renesas-ra/tree/master/examples/arduino-uno-r4-led-animation?utm_source=platformio.org&utm_medium=docs)
- [fsp-button-isr](https://github.com/platformio/platform-renesas-ra/tree/master/examples/fsp-button-isr?utm_source=platformio.org&utm_medium=docs)
- [cmsis-blink](https://github.com/platformio/platform-renesas-ra/tree/master/examples/cmsis-blink?utm_source=platformio.org&utm_medium=docs)
- [arduino-blink](https://github.com/platformio/platform-renesas-ra/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs)
- [arduino-internal-libs](https://github.com/platformio/platform-renesas-ra/tree/master/examples/arduino-internal-libs?utm_source=platformio.org&utm_medium=docs)
- [fsp-blink](https://github.com/platformio/platform-renesas-ra/tree/master/examples/fsp-blink?utm_source=platformio.org&utm_medium=docs)
- [arduino-iot-cloud-basic](https://github.com/platformio/platform-renesas-ra/tree/master/examples/arduino-iot-cloud-basic?utm_source=platformio.org&utm_medium=docs)
- [arduino-wifiscan](https://github.com/platformio/platform-renesas-ra/tree/master/examples/arduino-wifiscan?utm_source=platformio.org&utm_medium=docs)

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
| [Arduino Uno R4 WiFi](../boards/renesas-ra/uno-r4-wifi.md) | RA4M1 | 48MHz | 256KB | 32KB |

#### External Debug Tools

Boards listed below are compatible with [Debugging](../../guides/debugging/index.md) but **DEPEND ON** external debug probe. They **ARE NOT READY** for debugging. Please click on board name for the further details.

| Name | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|
| [Arduino Nano R4](../boards/renesas-ra/nano-r4.md) | RA4M1 | 48MHz | 256KB | 32KB |
| [Arduino Portenta C33](../boards/renesas-ra/portenta-c33.md) | R7FA6M5BH2CBG | 200MHz | 2MB | 511.35KB |
| [Arduino Uno R4 Minima](../boards/renesas-ra/uno-r4-minima.md) | RA4M1 | 48MHz | 256KB | 32KB |

## Stable and upstream versions

You can switch between [stable releases](https://github.com/platformio/platform-renesas-ra/releases) of Renesas RA development platform and the latest upstream version using [platform](../../reference/platformio-ini/env/platform.md) option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md) as described below.

### Stable

```ini
; Latest stable version, NOT recommended
; Pin the version as shown below
[env:latest_stable]
platform = renesas-ra
board = ...

; Specific version
[env:custom_stable]
platform = renesas-ra@x.y.z
board = ...
```

### Upstream

```ini
[env:upstream_develop]
platform = https://github.com/platformio/platform-renesas-ra.git
board = ...
```

## Packages

| Name | Description |
|---|---|
| [framework-arduinorenesas-portenta](https://registry.platformio.org/tools/platformio/framework-arduinorenesas-portenta) | Arduino Wiring-based Framework for Renesas MCUs (Portenta core) |
| [framework-arduinorenesas-uno](https://registry.platformio.org/tools/platformio/framework-arduinorenesas-uno) | Arduino Wiring-based Framework for Renesas MCUs (UNOR4 core) |
| [framework-cmsis-renesas](https://registry.platformio.org/tools/platformio/framework-cmsis-renesas) | Renesas FSP CMSIS module for Renesas RA MCU family |
| [framework-renesas-fsp](https://registry.platformio.org/tools/platformio/framework-renesas-fsp) | The Renesas Flexible Software Package (FSP) is an enhanced software package designed to provide easy-to-use, scalable, high-quality software for embedded system designs using Renesas RA family of Arm Microcontrollers. |
| [tool-bossac](https://registry.platformio.org/tools/platformio/tool-bossac) | Basic Open Source SAM-BA Application (BOSSA) |
| [tool-dfuutil-arduino](https://registry.platformio.org/tools/platformio/tool-dfuutil-arduino) | Device Firmware Upgrade Utilities |
| [tool-jlink](https://registry.platformio.org/tools/platformio/tool-jlink) | Software and Documentation Pack for SEGGER J-Link debug probes |
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
| [CMSIS](../frameworks/cmsis.md) | Vendor-independent hardware abstraction layer for the Cortex-M processor series |
| [Renesas Flexible Software Package](../frameworks/fsp.md) | The Renesas Flexible Software Package (FSP) is an enhanced software package designed to provide easy-to-use, scalable, high-quality software for embedded system designs using Renesas RA family of Arm Microcontrollers. |

## Boards

:::note

- You can list pre-configured boards by [pio boards](../../reference/cli/pio-boards.md) command
- For more detailed `board` information please scroll the tables below by horizontally.

:::

### Arduino

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Arduino Nano R4](../boards/renesas-ra/nano-r4.md) | External | RA4M1 | 48MHz | 256KB | 32KB |
| [Arduino Portenta C33](../boards/renesas-ra/portenta-c33.md) | External | R7FA6M5BH2CBG | 200MHz | 2MB | 511.35KB |
| [Arduino Uno R4 Minima](../boards/renesas-ra/uno-r4-minima.md) | External | RA4M1 | 48MHz | 256KB | 32KB |
| [Arduino Uno R4 WiFi](../boards/renesas-ra/uno-r4-wifi.md) | On-board | RA4M1 | 48MHz | 256KB | 32KB |
