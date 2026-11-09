---
description: "Configure a list with environments which PlatformIO should process by default (platformio.ini option default_envs)."
---

<a id="projectconf-pio-default-envs"></a>

# `default_envs` {#default-envs}

- **Type:** String
- **Multiple values:** Yes
- **Environment variable:** [`PLATFORMIO_DEFAULT_ENVS`](../../environment-variables.md#envvar-PLATFORMIO_DEFAULT_ENVS), appended to the values in `platformio.ini`
- **Deprecated name:** `env_default` (still accepted, with a warning)

The [pio run](../../cli/pio-run.md) command processes all environments `[env:***]` by default if the [`pio run --environment`](../../cli/pio-run.md#cmdoption-pio-run-e) option is not specified. [default_envs](#projectconf-pio-default-envs) allows one to define which environments that should be processed by default.

Also, [Debugging](../../../guides/debugging/index.md) checks this option when looking for debug environment.

## Example

```ini
[platformio]
default_envs = uno, nodemcu

[env:uno]
platform = atmelavr
framework = arduino
board = uno

[env:nodemcu]
platform = espressif8266
framework = arduino
board = nodemcu

[env:teensy31]
platform = teensy
framework = arduino
board = teensy31

[env:lpmsp430g2553]
platform = timsp430
framework = arduino
board = lpmsp430g2553
build_flags = -D LED_BUILTIN=RED_LED
```
