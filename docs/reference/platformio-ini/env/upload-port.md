<a id="projectconf-upload-port"></a>

# `upload_port` {#upload-port}

Type: `String (Pattern)` | Multiple: `No`

This option is used by "uploader" tool when sending firmware to board via `upload_port`. For example,

- `/dev/ttyUSB0` - Serial port (Unix-based OS)
- `COM3` - Serial port (Windows OS)
- `192.168.0.13` - IP address when using OTA
- `/media/disk` - physical path to media disk/flash drive ([Mbed](/hardware/frameworks/mbed) enabled boards)
- `D:` - physical path to media disk/flash drive (Windows OS).

If `upload_port` isn't specified, then *PlatformIO* will try to detect it automatically.

To print all available serial ports please use [pio device list](../../cli/pio-device/list.md) command.

This option can also be set by global environment variable [`PLATFORMIO_UPLOAD_PORT`](../../environment-variables.md#envvar-PLATFORMIO_UPLOAD_PORT).

Please note that you can use patterns:

| Pattern | Meaning |
|---|---|
| `*` | matches everything |
| `?` | matches any single character |
| `[seq]` | matches any character in seq |
| `[!seq]` | matches any character not in seq |

**Example**

```ini
[env:uno]
platform = atmelavr
framework = arduino
; any port that starts with /dev/ttyUSB
upload_port = /dev/ttyUSB*

; COM1 or COM3
upload_port = COM[13]
```
