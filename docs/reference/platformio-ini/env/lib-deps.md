---
description: "A list of project library dependencies which should be installed automatically before a build process (platformio.ini option lib_deps)."
---

# `lib_deps`

- **Type:** String
- **Multiple values:** Yes
- **Deprecated name:** `lib_use`, `lib_force`, `lib_install` (still accepted, with a warning)

:::info[See also]

Read [Dependency Management](../../../guides/libraries/dependencies.md) guide first.

:::

Specify project dependencies using [Package Specifications](../../cli/pio-pkg/install.md#cmd-pkg-install-specifications) that should be installed automatically to the [libdeps_dir](../platformio/libdeps-dir.md) before environment processing.

If you have multiple build environments that depend on the same libraries, you can use [Section \[env\]](./index.md) or [Interpolation of Values](../../../guides/projects/interpolation.md) to use the common configuration.

Check the [PlatformIO Registry](https://registry.platformio.org) for the available libraries and the installation instructions.

## Example

```ini
[env:myenv]
lib_deps =
  ; name-based (built-in library in framework)
  SPI

  ; owner-based declaration
  knolleary/PubSubClient

  ; SemVer specification
  bblanchon/ArduinoJson @ ~5.6,!=5.4

  ; external Git resource
  https://github.com/gioblu/PJON.git#v2.0

  ; custom name
  IRremoteESP8266=https://github.com/markszabo/IRremoteESP8266/archive/master.zip
```
