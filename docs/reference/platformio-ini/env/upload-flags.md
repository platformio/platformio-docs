<a id="projectconf-upload-flags"></a>

# `upload_flags` {#upload-flags}

Type: `String` | Multiple: `Yes`

Extra flags for uploader. Will be added to the end of uploader command. If you need to override uploader command or base flags please use [extra_scripts](./extra-scripts.md).

This option can also be set by global environment variable [`PLATFORMIO_UPLOAD_FLAGS`](../../environment-variables.md#envvar-PLATFORMIO_UPLOAD_FLAGS).

**Example**

Please specify each flag/option in a new line starting with minimum 2 spaces.

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
