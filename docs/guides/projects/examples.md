---
description: Practical platformio.ini patterns - several boards, release and debug builds, shared settings and secrets.
---

# platformio.ini examples

Common patterns for [`platformio.ini`](../../reference/platformio-ini/index.md).
For complete projects, see the
[PlatformIO examples](https://github.com/platformio/platformio-examples) and
the [tutorials](../../get-started/tutorials/index.md).

## One project, several boards {#several-boards}

Shared options go in `[env]`; each board gets its own environment. Build one
with `pio run -e esp32dev`, or all of them with `pio run`.

```ini
[env]
framework = arduino
lib_deps = bblanchon/ArduinoJson @ ^7.0.0

[env:uno]
platform = atmelavr
board = uno

[env:esp32dev]
platform = espressif32
board = esp32dev
monitor_speed = 115200
```

## Release and debug builds {#release-and-debug}

See [Build configurations](./build-configurations.md).

```ini
[env]
platform = ststm32
board = nucleo_f401re
framework = stm32cube

[env:release]
build_flags = -D NDEBUG

[env:debug]
build_type = debug
build_flags = -D DEBUG=1
```

## Reuse an environment with `extends` {#extends}

[`extends`](../../reference/platformio-ini/env/extends.md) copies the options
of other sections; options set in the environment take precedence.

```ini
[common]
build_flags = -D VERSION=1.2.3

[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino
extends = common

[env:esp32dev_ota]
extends = env:esp32dev
upload_protocol = espota
upload_port = 192.168.1.20
```

## Keep secrets out of the file {#secrets}

Read values from environment variables with
[interpolation](../../reference/platformio-ini/interpolation.md):

```ini
[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino
build_flags =
  -D WIFI_SSID=\"${sysenv.WIFI_SSID}\"
  -D WIFI_PASS=\"${sysenv.WIFI_PASS}\"
```

## Run only some environments by default {#default-envs}

```ini
[platformio]
default_envs = esp32dev

[env:uno]
...

[env:esp32dev]
...
```
