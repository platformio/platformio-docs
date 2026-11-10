---
description: Show the computed project configuration or check platformio.ini for errors.
---

# pio project config

Show the project configuration as PlatformIO computes it from [`platformio.ini`](../../platformio-ini/index.md), or check
the file for errors.

## Usage {#usage}

```bash
pio project config [OPTIONS]
```

## Description {#description}

The computed configuration includes the files listed in
[`extra_configs`](../../platformio-ini/platformio/extra-configs.md) and has
[interpolated values](../../platformio-ini/interpolation.md) expanded. Use
it to see which value an option ends up with.

## Options {#options}

<a id="cmdoption-pio-project-config-project-dir"></a>

### `-d, --project-dir` {#cmdoption-pio-project-config-d}

The project directory. Default: the current working directory.

### `--lint` {#cmdoption-pio-project-config-lint}

Check `platformio.ini` for errors and warnings instead of showing the
configuration. Added in PlatformIO Core 6.1.8.

### `--json-output` {#cmdoption-pio-project-config-json-output}

Print the result in [JSON](https://en.wikipedia.org/wiki/JSON) format.

## Examples {#examples}

```bash
pio project config
```

```text
Computed project configuration for Tasmota Project

platformio
----------
src_dir          =  tasmota
build_dir        =  .pioenvs
build_cache_dir  =  .cache
extra_configs    =  platformio_tasmota_env.ini
                    platformio_override.ini
default_envs     =  tasmota

common
------
framework               =  arduino
board                   =  esp01_1m
board_build.flash_mode  =  dout
platform                =  espressif8266
build_flags             =  -D NDEBUG
                           -mtarget-align
                           -Wl,-Map,firmware.map
                           -Wl,-Teagle.flash.1m.ld
                           -DBEARSSL_SSL_BASIC
                           -DPIO_FRAMEWORK_ARDUINO_ESPRESSIF_SDK22x_190703
                           -DPIO_FRAMEWORK_ARDUINO_LWIP2_HIGHER_BANDWIDTH_LOW_FLASH
                           -DVTABLES_IN_FLASH
                           -fno-exceptions
                           -lstdc++
build_unflags           =  -Wall
board_build.f_cpu       =  80000000L
monitor_speed           =  115200
upload_speed            =  115200
upload_resetmethod      =  nodemcu
upload_port             =  COM5
extra_scripts           =  pio/strip-floats.py
                           pio/name-firmware.py

scripts_defaults
----------------
extra_scripts  =  pio/strip-floats.py
                  pio/name-firmware.py

...
```

Check the configuration for errors:

```bash
pio project config --lint
```

```text
The "platformio.ini" configuration file is free from linting errors.
```
