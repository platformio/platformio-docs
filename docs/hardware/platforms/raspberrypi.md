---
title: "Raspberry Pi RP2040"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "The Raspberry Pi RP2040 development platform for PlatformIO: configuration, frameworks, packages, debugging and boards."
---

# Raspberry Pi RP2040

**Registry:** [https://registry.platformio.org/platforms/platformio/raspberrypi](https://registry.platformio.org/platforms/platformio/raspberrypi)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/raspberrypi`

RP2040 is a low-cost, high-performance microcontroller device with a large on-chip memory, symmetric dual-core processor complex, and rich peripheral.

Vendor website: [www.raspberrypi.org](https://www.raspberrypi.org/documentation/rp2040/getting-started/?utm_source=platformio.org&utm_medium=docs).

## Examples

Example projects from the [Raspberry Pi RP2040 platform repository](https://github.com/platformio/platform-raspberrypi/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [arduino-blink](https://github.com/platformio/platform-raspberrypi/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs)
- [arduino-external-libs](https://github.com/platformio/platform-raspberrypi/tree/master/examples/arduino-external-libs?utm_source=platformio.org&utm_medium=docs)

## Debugging

[Debugging](../../guides/debugging/index.md) works with the boards below without extra configuration.

### Debug probes

Select a [debug probe](../../guides/debugging/index.md#debugging-tools) with the [debug_tool](../../reference/platformio-ini/env/debug-tool.md) option in [platformio.ini](../../reference/platformio-ini/index.md). Each board's page lists its compatible probes.

:::warning

Most debug probes need a driver or udev rules. See the probe's page for instructions.

:::

#### Boards that need an external debug probe

These boards support [Debugging](../../guides/debugging/index.md) with an external debug probe. See each board's page for the compatible probes.

| Name | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|
| [Arduino Nano RP2040 Connect](../boards/raspberrypi/nanorp2040connect.md) | RP2040 | 133MHz | 2MB | 264KB |
| [Raspberry Pi Pico](../boards/raspberrypi/pico.md) | RP2040 | 133MHz | 2MB | 264KB |

## Stable and upstream versions

Choose between the [stable releases](https://github.com/platformio/platform-raspberrypi/releases) of the Raspberry Pi RP2040 platform and its latest upstream version with the [platform](../../reference/platformio-ini/env/platform.md) option in [platformio.ini](../../reference/platformio-ini/index.md).

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

### Arduino

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Arduino Nano RP2040 Connect](../boards/raspberrypi/nanorp2040connect.md) | External | RP2040 | 133MHz | 2MB | 264KB |

### Raspberry Pi

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Raspberry Pi Pico](../boards/raspberrypi/pico.md) | External | RP2040 | 133MHz | 2MB | 264KB |
