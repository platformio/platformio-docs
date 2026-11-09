---
description: "An extra flags for `uploader` tool (platformio.ini option upload_flags)."
---

<a id="projectconf-upload-flags"></a>

# `upload_flags` {#upload-flags}

- **Type:** String
- **Multiple values:** Yes
- **Environment variable:** [`PLATFORMIO_UPLOAD_FLAGS`](../../environment-variables.md#envvar-PLATFORMIO_UPLOAD_FLAGS), appended to the values in `platformio.ini`

Extra flags for uploader. Will be added to the end of uploader command. If you need to override uploader command or base flags please use [extra_scripts](./extra-scripts.md).

## Example

Specify each flag/option in a new line starting with minimum 2 spaces.

```ini
[env:atmega328pb]
platform = atmelavr
board = atmega328pb
framework = arduino
upload_flags =
  -P$UPLOAD_PORT
  -b$UPLOAD_SPEED
  -u
  -Ulock:w:0xCF:m
  -Uhfuse:w:0xD7:m
  -Uefuse:w:0xF6:m
  -Ulfuse:w:0xE2:m
```
