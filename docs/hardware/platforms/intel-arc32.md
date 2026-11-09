---
title: "Intel ARC32"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
---

<a id="platform-intel-arc32"></a>

# Intel ARC32

**Registry:** [https://registry.platformio.org/platforms/platformio/intel_arc32](https://registry.platformio.org/platforms/platformio/intel_arc32)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/intel_arc32`

ARC embedded processors are a family of 32-bit CPUs that are widely used in SoC devices for storage, home, mobile, automotive, and Internet of Things applications.

For more detailed information please visit [vendor site](http://www.intel.com/content/www/us/en/wearables/wearable-soc.html?utm_source=platformio.org&utm_medium=docs).

## Examples

Examples are listed from [Intel ARC32 development platform repository](https://github.com/platformio/platform-intel_arc32/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [arduino-curie-imu](https://github.com/platformio/platform-intel_arc32/tree/master/examples/arduino-curie-imu?utm_source=platformio.org&utm_medium=docs)
- [arduino-blink](https://github.com/platformio/platform-intel_arc32/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs)
- [arduino-internal-libs](https://github.com/platformio/platform-intel_arc32/tree/master/examples/arduino-internal-libs?utm_source=platformio.org&utm_medium=docs)

## Stable and upstream versions

You can switch between [stable releases](https://github.com/platformio/platform-intel_arc32/releases) of Intel ARC32 development platform and the latest upstream version using [platform](../../reference/platformio-ini/env/platform.md) option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md) as described below.

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

### Intel

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Arduino/Genuino 101](../boards/intel-arc32/genuino101.md) | No | ARCV2EM | 32MHz | 152KB | 80KB |
