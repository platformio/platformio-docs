---
title: "Intel ARC32"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
description: "The Intel ARC32 development platform for PlatformIO: configuration, frameworks, packages, debugging and boards."
---

# Intel ARC32

**Registry:** [https://registry.platformio.org/platforms/platformio/intel_arc32](https://registry.platformio.org/platforms/platformio/intel_arc32)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/intel_arc32`

ARC embedded processors are a family of 32-bit CPUs that are widely used in SoC devices for storage, home, mobile, automotive, and Internet of Things applications.

Vendor website: [www.intel.com](http://www.intel.com/content/www/us/en/wearables/wearable-soc.html?utm_source=platformio.org&utm_medium=docs).

## Examples

Example projects from the [Intel ARC32 platform repository](https://github.com/platformio/platform-intel_arc32/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [arduino-curie-imu](https://github.com/platformio/platform-intel_arc32/tree/master/examples/arduino-curie-imu?utm_source=platformio.org&utm_medium=docs)
- [arduino-blink](https://github.com/platformio/platform-intel_arc32/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs)
- [arduino-internal-libs](https://github.com/platformio/platform-intel_arc32/tree/master/examples/arduino-internal-libs?utm_source=platformio.org&utm_medium=docs)

## Stable and upstream versions

Choose between the [stable releases](https://github.com/platformio/platform-intel_arc32/releases) of the Intel ARC32 platform and its latest upstream version with the [platform](../../reference/platformio-ini/env/platform.md) option in [platformio.ini](../../reference/platformio-ini/index.md).

### Stable

```ini
; Latest stable version, NOT recommended
; Pin the version as shown below
[env:latest_stable]
platform = intel_arc32
board = ...

; Specific version
[env:custom_stable]
platform = intel_arc32@x.y.z
board = ...
```

### Upstream

```ini
[env:upstream_develop]
platform = https://github.com/platformio/platform-intel_arc32.git
board = ...
```

## Packages

| Name | Description |
|---|---|
| [framework-arduinointel](https://registry.platformio.org/tools/platformio/framework-arduinointel) | Arduino Wiring-based Framework Intel ARC32 processor |
| [tool-arduino101load](https://registry.platformio.org/tools/platformio/tool-arduino101load) | Genuino101 uploader tool |
| [toolchain-intelarc32](https://registry.platformio.org/tools/platformio/toolchain-intelarc32) | GCC for Intel ARC processor |

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

### Intel

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Arduino/Genuino 101](../boards/intel-arc32/genuino101.md) | No | ARCV2EM | 32MHz | 152KB | 80KB |
