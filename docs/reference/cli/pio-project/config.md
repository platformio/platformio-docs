<a id="cmd-project-config"></a>

# pio project config {#pio-project-config}

## Usage {#usage}

```bash
pio project config [OPTIONS]
```

## Description {#description}

Show project computed configuration based on ["platformio.ini" (Project Configuration File)](../../platformio-ini/index.md). The extra configuration files and dynamic variables will be expanded.

This command is useful for developers to check how PlatformIO computes configuration from ["platformio.ini" (Project Configuration File)](../../platformio-ini/index.md).

### Options {#options}

<a id="cmdoption-pio-project-config-project-dir"></a>

#### `-d, --project-dir` {#cmdoption-pio-project-config-d}

Specify the path to project directory. By default, `--project-dir` is equal to current working directory (`CWD`).

#### `--lint` {#cmdoption-pio-project-config-lint}

:::info

Added in version 6.1.8.

:::

Perform linting on ["platformio.ini" (Project Configuration File)](../../platformio-ini/index.md).

#### `--json-output` {#cmdoption-pio-project-config-json-output}

Return the output in [JSON](http://en.wikipedia.org/wiki/JSON) format.

## Examples {#examples}

```text
> pio project config
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
