<a id="projectconf-env-platform-packages"></a>

# `platform_packages` {#platform-packages}

Type: `Package Specification` | Multiple: `Yes`

Configure custom packages per a build environment. You can also override default packages by [Development Platforms](../../../hardware/platforms/index.md) using the same name. See [Package Specifications](../../cli/pio-pkg/install.md#cmd-pkg-install-specifications) for details.

Check the [PlatformIO Registry](https://registry.platformio.org) for the available toolchains, frameworks, SDKs, etc.

Examples:

```ini
[env:override_default_toolchain]
platform = atmelavr
platform_packages =
  ; use GCC AVR 5.0+
  toolchain-gccarmnoneeabi@>1.50000.0

[env:override_framework]
platform = espressif8266
platform_packages =
  ; use upstream Git version
  framework-arduinoespressif8266 @ https://github.com/esp8266/Arduino.git

[env:external_package]
platform = ststm32
platform_packages =
  ; latest openOCD from PlatformIO Package Registry
  tool-openocd

  ; source code of ST-Link
  tool-stlink-source @ https://github.com/texane/stlink.git
```
