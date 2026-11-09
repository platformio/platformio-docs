---
description: Override the flash memory interface mode of a board in platformio.ini.
---

<a id="projectconf-board-build-flash-mode"></a>

# `board_build.flash_mode` {#board-build-flash-mode}

- **Type:** String
- **Multiple values:** No
- **Deprecated name:** `board_flash_mode` (still accepted, with a warning)

Override the interface mode of the board's external flash memory, for example
`qio`, `qout`, `dio` or `dout`. By default, the value comes from the board's
manifest.

The option is used by development platforms whose chips read the program from
external flash, such as [Espressif 32](/hardware/platforms/espressif32) and
[Espressif 8266](/hardware/platforms/espressif8266). See the platform's page
for the supported modes.

## Example {#example}

```ini
[env:esp32dev]
platform = espressif32
board = esp32dev
board_build.flash_mode = qio
```
