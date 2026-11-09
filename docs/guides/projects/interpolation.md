<a id="projectconf-interpolation"></a>

# Interpolation of Values {#interpolation-of-values}

In addition to its core functionality, PlatformIO introduces support for interpolation, allowing values to incorporate format strings that reference other values from different sections.

The interpolation feature adheres to the following syntax:

- `${<variable>}`, where `<variable>` represents the name of a supported built-in variable (refer to the table below for details).
- `${<section>.<option>}`, with `<section>` denoting a value from the `[<section>]` group, and `<option>` representing the first item in the pair `<option> = value`.

<table>
<thead>
<tr>
<th>

Syntax

</th>
<th>

Meaning

</th>
<th>

Example

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

`${<variable>}`

</td>
<td>

Incorporate built-in variables using their designated names. The following variables are supported:

- `PROJECT_DIR` - represents the current project directory
- `PROJECT_HASH` - corresponds to the hash of the project path
- `UNIX_TIME` - indicates the current  [Unix time](https://en.wikipedia.org/wiki/Unix_time), represented by 10 digits

</td>
<td>

`/tmp/pio-workspaces/${PROJECT_HASH}` refers to the new directory `/tmp/pio-workspaces/project_name-8f66e9463d/`

</td>
</tr>
<tr>
<td>

`${sysenv.<name>}`

</td>
<td>

Embed operating system environment variable by a name

</td>
<td>

`${sysenv.HOME}` refers to the user home directory on Unix machine

</td>
</tr>
<tr>
<td>

`${platformio.<option>}`

</td>
<td>

Embed value from [Section \[platformio\]](../../reference/platformio-ini/platformio/index.md)

</td>
<td>

`${platformio.packages_dir}` refers to the path of [packages_dir](../../reference/platformio-ini/platformio/packages-dir.md)

</td>
</tr>
<tr>
<td>

`${env.<option>}`

</td>
<td>

Embed default value from [Section \[env\]](../../reference/platformio-ini/env/index.md)

</td>
<td>

`${env.debug_build_flags}` refers to the default debugging flags

</td>
</tr>
<tr>
<td>

`${<section>.<option>}`

</td>
<td>

Embed value from another section.

</td>
<td>

`${extra.lib_deps}` embeds library dependencies declared in the section named `extra`

</td>
</tr>
<tr>
<td>

`${this.<option>}`

</td>
<td>

Embed value from the current section without declaring a section name

</td>
<td>

`${this.board}` refers to the "board" value of the current section

</td>
</tr>
<tr>
<td>

`${this.__env__}`

</td>
<td>

Embed environment name of the current section. The section must start with `env:` prefix

</td>
<td>

`${this.__env__}` will embed "foo" value being declared in the "env:foo" section

</td>
</tr>
</tbody>
</table>

- Interpolation can span multiple levels
- Interpolation can be applied only for the option's value
- Multiple interpolations are allowed
- The [Section \[platformio\]](../../reference/platformio-ini/platformio/index.md) and [Section \[env\]](../../reference/platformio-ini/env/index.md) sections are reserved and could not be used as a custom section. Some good section names might be `extra` or `custom`.

:::note

If you need to **share common configuration options** between build environments, please take a look at **"Global scope"** in [Section \[env\]](../../reference/platformio-ini/env/index.md) or [extends](../../reference/platformio-ini/env/extends.md) option which allows extending of other sections.

:::

**Example:**

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
build_flags = ${env.build_flags} -Wall
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
