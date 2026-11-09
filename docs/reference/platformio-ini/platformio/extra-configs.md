---
description: "Extend main configuration with the extra configuration files (platformio.ini option extra_configs)."
---

# `extra_configs`

- **Type:** String
- **Multiple values:** Yes

This option allows extending a base [`platformio.ini`](../index.md) with extra configuration files. The format and rules are the same as for the [`platformio.ini`](../index.md). A name of the configuration file can be any.

`extra_configs` can be a single path to an extra configuration file or a list of them. Note that you can use Unix shell-style wildcards:

| Pattern | Meaning |
|---|---|
| `*` | matches everything |
| `?` | matches any single character |
| `[seq]` | matches any character in seq |
| `[!seq]` | matches any character not in seq |

:::note

If you declare the same pair of "group" + "option" in an extra configuration file which was previously declared in a base [`platformio.ini`](../index.md), it will be overwritten with a value from extra configuration.

:::

## Example

*Base "platformio.ini"*

```ini
[platformio]
extra_configs =
  extra_envs.ini
  extra_debug.ini

; Global data for all [env:***]
[env]
platform = platformio/espressif32
framework = espidf

; Custom data group
; can be use in [env:***] via ${common.***}
[common]
debug_flags = -D RELEASE
lib_flags = -lc -lm

[env:esp-wrover-kit]
board = esp-wrover-kit
build_flags = ${common.debug_flags}
```

*"extra_envs.ini"*

```ini
[env:esp32dev]
board = esp32dev
build_flags = ${common.lib_flags} ${common.debug_flags}

[env:lolin32]
platform = platformio/espressif32
framework = espidf
board = lolin32
build_flags = ${common.debug_flags}
```

*"extra_debug.ini"*

```ini
# Override base "common.debug_flags"
[common]
debug_flags = -D DEBUG=1

[env:lolin32]
build_flags = -Og
```

After a parsing process, configuration state will be the next:

```ini
[common]
debug_flags = -D DEBUG=1
lib_flags = -lc -lm

[env:esp-wrover-kit]
platform = platformio/espressif32
framework = espidf
board = esp-wrover-kit
build_flags = ${common.debug_flags}

[env:esp32dev]
platform = platformio/espressif32
framework = espidf
board = esp32dev
build_flags = ${common.lib_flags} ${common.debug_flags}

[env:lolin32]
platform = platformio/espressif32
framework = espidf
board = lolin32
build_flags = -Og
```
