---
title: "Raspberry Pi RP2040"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
---

<a id="platform-raspberrypi"></a>

# Raspberry Pi RP2040

**Registry:** [https://registry.platformio.org/platforms/platformio/raspberrypi](https://registry.platformio.org/platforms/platformio/raspberrypi)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/raspberrypi`

RP2040 is a low-cost, high-performance microcontroller device with a large on-chip memory, symmetric dual-core processor complex, and rich peripheral.

For more detailed information please visit [vendor site](https://www.raspberrypi.org/documentation/rp2040/getting-started/?utm_source=platformio.org&utm_medium=docs).

## Examples

Examples are listed from [Raspberry Pi RP2040 development platform repository](https://github.com/platformio/platform-raspberrypi/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [arduino-blink](https://github.com/platformio/platform-raspberrypi/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs)
- [arduino-external-libs](https://github.com/platformio/platform-raspberrypi/tree/master/examples/arduino-external-libs?utm_source=platformio.org&utm_medium=docs)

## Debugging

[Debugging](../../guides/debugging/index.md) - "1-click" solution for debugging with a zero configuration.

### Tools & Debug Probes

Supported debugging tools are listed in "Debug" column. For more detailed information, please scroll table by horizontal. You can switch between debugging [Tools & Debug Probes](../../guides/debugging/index.md#debugging-tools) using [debug_tool](../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md).

:::warning

You will need to install debug tool drivers depending on your system. Please click on compatible debug tool below for the further instructions.

:::

#### External Debug Tools

Boards listed below are compatible with [Debugging](../../guides/debugging/index.md) but **DEPEND ON** external debug probe. They **ARE NOT READY** for debugging. Please click on board name for the further details.

| Name | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|
| [Arduino Nano RP2040 Connect](../boards/raspberrypi/nanorp2040connect.md) | RP2040 | 133MHz | 2MB | 264KB |
| [Raspberry Pi Pico](../boards/raspberrypi/pico.md) | RP2040 | 133MHz | 2MB | 264KB |

## Stable and upstream versions

You can switch between [stable releases](https://github.com/platformio/platform-raspberrypi/releases) of Raspberry Pi RP2040 development platform and the latest upstream version using [platform](../../reference/platformio-ini/env/platform.md) option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md) as described below.

### Stable

```ini
; Latest stable version, NOT recommended
; Pin the version as shown below
[env:latest_stable]
platform = raspberrypi
board = ...

; Specific version
[env:custom_stable]
platform = raspberrypi@x.y.z
board = ...
```

### Upstream

```ini
[env:upstream_develop]
platform = https://github.com/platformio/platform-raspberrypi.git
board = ...
```

## Packages

| Name | Description |
|---|---|
| [framework-arduino-mbed](https://registry.platformio.org/tools/platformio/framework-arduino-mbed) | Arduino framework supporting mbed-enabled boards |
| [tool-jlink](https://registry.platformio.org/tools/platformio/tool-jlink) | Software and Documentation Pack for SEGGER J-Link debug probes |
| [tool-openocd-raspberrypi](https://registry.platformio.org/tools/platformio/tool-openocd-raspberrypi) | Open On-Chip Debugger for Raspberry Pi MCUs |
| [tool-rp2040tools](https://registry.platformio.org/tools/platformio/tool-rp2040tools) | Tools for interacting with a RP2040 device in BOOTSEL mode or with a RP2040 binary |
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

## Boards

:::note

- You can list pre-configured boards by [pio boards](../../reference/cli/pio-boards.md) command
- For more detailed `board` information please scroll the tables below by horizontally.

:::

### Arduino

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Arduino Nano RP2040 Connect](../boards/raspberrypi/nanorp2040connect.md) | External | RP2040 | 133MHz | 2MB | 264KB |

### Raspberry Pi

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Raspberry Pi Pico](../boards/raspberrypi/pico.md) | External | RP2040 | 133MHz | 2MB | 264KB |
