---
description: Reuse values across platformio.ini with ${section.option}, built-in variables and system environment variables.
---

<a id="projectconf-interpolation"></a>

# Interpolation of values {#interpolation-of-values}

A value in `platformio.ini` can include other values with `${...}`: options
from any section, built-in variables, and system environment variables. Use it
to avoid repeating settings and to keep secrets out of the file.

## Syntax {#syntax}

| Syntax | Inserts | Example |
| --- | --- | --- |
| `${<section>.<option>}` | The value of an option in another section | `${extra.lib_deps}`: the `lib_deps` option of the `[extra]` section |
| `${env.<option>}` | The value of an option in the shared [`[env]`](../../reference/platformio-ini/env/index.md#common-env) section | `${env.build_flags}` |
| `${platformio.<option>}` | The value of an option in the [`[platformio]`](../../reference/platformio-ini/platformio/index.md) section | `${platformio.packages_dir}`: the [`packages_dir`](../../reference/platformio-ini/platformio/packages-dir.md) path |
| `${this.<option>}` | The value of another option in the current section | `${this.board}` |
| `${this.__env__}` | The name of the current environment (only in `[env:NAME]` sections) | `foo` in `[env:foo]` |
| `${sysenv.<name>}` | A system environment variable | `${sysenv.HOME}`: the home directory on macOS and Linux |
| `${PROJECT_DIR}` | The project directory | |
| `${PROJECT_HASH}` | The project folder name and a short hash of its path | `myproject-8f66e9463d` |
| `${UNIX_TIME}` | The current [Unix time](https://en.wikipedia.org/wiki/Unix_time) | `1699999999` |

Any other `${NAME}` is passed unchanged to the build system as an
[SCons construction variable](../../reference/scripting-api/construction-environments.md),
for example `${BUILD_DIR}`.

Rules:

- Interpolation works only in values, not in option or section names.
- A value can contain several references, and referenced values can contain
  references themselves. Circular references are reported as an error.
- `[platformio]` and `[env]` are reserved names. For your own shared values,
  use another section name, such as `[extra]` or `[common]`.

:::tip

To share options between environments, the shared [`[env]`](../../reference/platformio-ini/env/index.md#common-env)
section and the [`extends`](../../reference/platformio-ini/env/extends.md)
option are often simpler than interpolation.

:::

## Example {#example}

```ini
; COMMON options
; Each "[env:***]" extends this "[env]" by default
[env]
framework = arduino
build_flags = -D VERSION=1.2.3

; CUSTOM options
; You need manually inject these options into a section
; using ${extra.<name_of_option>} (see below)
[extra]
lib_deps_builtin =
  SPI
  Wire
lib_deps_external =
  bblanchon/ArduinoJson@>5.6.0

[env:uno]
platform = atmelavr
board = uno
lib_deps =
  ${extra.lib_deps_builtin}
  ${extra.lib_deps_external}
platform_packages =
  platformio/tool-simavr
test_speed = 9600
test_testing_command =
  ${platformio.packages_dir}/tool-simavr/bin/simavr
  -m
  atmega328p
  -f
  16000000L
  ${platformio.build_dir}/${this.__env__}/firmware.elf

[env:esp32dev]
platform = platformio/espressif32
board = esp32dev
build_flags =
  ${env.build_flags}
  -Wall
  -DWIFI_SSID=${sysenv.WIFI_SSID}
  -DWIFI_PASS=${sysenv.WIFI_PASS}
lib_deps =
  ${extra.lib_deps_builtin}
  ${extra.lib_deps_external}
  knolleary/PubSubClient @ ~2.6
  paulstoffregen/OneWire @ ^2.3.5

; Keep sensitive data in environment variables
;
; Unix
; export WIFI_SSID='\"my\ ssid\ name\"'
; export WIFI_PASS='\"my\ password\"'
;
; Windows
; set WIFI_SSID='"my ssid name"'
; set WIFI_PASS='"my password"'
```

:::warning

Be careful with special characters in system environment variables on Unix systems, especially when they are used as the value for preprocessor directives. Symbols like `$`, `&`, `~`, etc must be explicitly escaped, for example:

```bash
export WIFI_PASS='\"my\~p\&a\\\$\$\$\$word\"'
```

:::
