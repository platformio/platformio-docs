---
description: "Inherit configuration from other sections or build environments (platformio.ini option extends)."
---

# `extends`

- **Type:** String
- **Multiple values:** Yes

This option allows one to inherit configuration from other sections or build environments in [`platformio.ini`](../index.md). Multiple items are allowed, split them with `,` or with a new line.

If you need to extend only a few options from some section, please take a look at [Interpolation of Values](../interpolation.md).

## Example

```ini
[strict_ldf]
lib_ldf_mode = chain+
lib_compat_mode = strict

[espressi32_base]
platform = platformio/espressif32
framework = arduino

[env:release]
extends = espressi32_base, strict_ldf
board = esp32dev
build_flags = -D RELEASE

[env:debug]
extends = env:release
build_type = debug
build_flags = -D DEBUG
```

:::warning

Note that the `extends` option doesn't merge values from multiple sections or environments. If multiple items specified in the extends field then only values from the latter one will be used in the final configuration. For example:

```ini
[base]
platform = teensy
framework = arduino
board = teensy31

[lib_deps1]
lib_deps =
    monstrenyatko/ArduinoMqtt @ ^1.5.1
    bblanchon/ArduinoJson @ ^6.18.3
    knolleary/PubSubClient @ ^2.8

[lib_deps2]
lib_deps =
    sstaub/Ticker @ ^4.3.0
    thijse/ArduinoLog @ ^1.1.1
    adafruit/RTClib @ ^1.14.0

[env:final]
extends = base, lib_deps1, lib_deps2
; The values from `lib_deps2` will override the values from lib_deps1, so
; the final `lib_deps` option will be equivalent to the following:
; lib_deps =
;    sstaub/Ticker @ ^4.3.0
;    thijse/ArduinoLog @ ^1.1.1
;    adafruit/RTClib @ ^1.14.0
```

:::
