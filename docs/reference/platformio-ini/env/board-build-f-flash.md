---
description: Override the flash memory frequency of a board in platformio.ini.
---

# `board_build.f_flash`

- **Type:** String
- **Multiple values:** No
- **Deprecated name:** `board_f_flash` (still accepted, with a warning)

Override the frequency, in hertz, of the board's external flash memory. Use
the C long integer format with an `L` suffix, for example `80000000L` for
80 MHz. By default, the value comes from the board's manifest.

The option is used by development platforms whose chips read the program from
external flash, such as [Espressif 32](/hardware/platforms/espressif32) and
[Espressif 8266](/hardware/platforms/espressif8266). See the platform's page
for the supported values.

## Example {#example}

```ini
[env:esp32dev]
platform = espressif32
board = esp32dev
board_build.f_flash = 80000000L
```
