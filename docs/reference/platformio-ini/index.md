---
description: Reference of platformio.ini, the PlatformIO project configuration file - syntax, sections and options.
---

# platformio.ini

`platformio.ini` is the project configuration file. Every PlatformIO project
has one in its root directory. It declares the
[project environments](./env/index.md) (the boards, frameworks and build
settings the project targets) and the project-wide settings, so that the
project builds the same way on every machine.

## Syntax {#syntax}

`platformio.ini` is an [INI file](https://en.wikipedia.org/wiki/INI_file): it
consists of sections, each starting with a `[header]`, and `name = value`
options within them.

- Lines that start with `;` or `#` are comments. A `;` preceded by whitespace
  starts an inline comment.
- Options that accept multiple values take them either on one line separated
  by `, ` (a comma and a space), or one value per line, with each continuation
  line indented:

  ```ini
  lib_deps = bblanchon/ArduinoJson, knolleary/PubSubClient

  lib_deps =
      bblanchon/ArduinoJson
      knolleary/PubSubClient
  ```

- Values can reference other options and environment variables with
  `${section.option}` and `${sysenv.NAME}`. See
  [Interpolation of values](./interpolation.md).

## Sections {#sections}

| Section | Purpose |
| --- | --- |
| [`[platformio]`](./platformio/index.md) | Project-wide settings: [generic options](./platformio/generic-options.md) and [directories](./platformio/directory-options.md) |
| [`[env]`](./env/index.md#common-env) | Options shared by all environments |
| [`[env:NAME]`](./env/index.md#working-env-name) | A project environment |
| Any other name, such as `[common]` | Your own values, to reuse with `${common.option}` |

To check how PlatformIO reads your file, run
[`pio project config`](../cli/pio-project/config.md); add `--lint` to find
errors.

## Example {#example}

More examples: [platformio.ini examples](../../guides/projects/examples.md)
and the [tutorials](../../get-started/tutorials/index.md).

```ini
[platformio]
default_envs = nodemcuv2

; custom common options
[common]
build_flags =
    -D VERSION=1.2.3
    -D DEBUG=1
lib_deps_builtin =
    SPI
    Wire
lib_deps_external =
    bblanchon/ArduinoJson @ ~5.6,!=5.4
    https://github.com/gioblu/PJON.git#v2.0
    IRremoteESP8266=https://github.com/markszabo/IRremoteESP8266/archive/master.zip

[env:nodemcuv2]
platform = espressif8266
framework = arduino
board = nodemcuv2

; Build options
build_flags =
    ${common.build_flags}
    -DSSID_NAME=HELLO
    -DSSID_PASWORD=WORLD

; Library options
lib_deps =
    ${common.lib_deps_builtin}
    ${common.lib_deps_external}
    https://github.com/me-no-dev/ESPAsyncTCP.git
    knolleary/PubSubClient@^2.8
    paulstoffregen/OneWire

; Serial Monitor options
monitor_speed = 115200
monitor_filters = hexlify

; Unit Testing options
test_ignore = test_desktop

[env:bluepill_f103c8]
platform = ststm32
framework = arduino
board = bluepill_f103c8

; Library options
lib_deps = ${common.lib_deps_external}

; Debug options
debug_tool = custom
debug_server =
    ${platformio.packages_dir}/tool-jlink/JLinkGDBServer
    -singlerun
    -if
    SWD
    -select
    USB
    -port
    2331
    -device
    STM32F103C8

; Unit Testing options
test_ignore = test_desktop
```
