---
description: "A port, a number or a device name (platformio.ini option monitor_port)."
---

<a id="projectconf-monitor-port"></a>

# `monitor_port` {#monitor-port}

- **Type:** String
- **Multiple values:** No

Port, a number or a device name, or valid [URL Handlers](https://pyserial.readthedocs.io/en/latest/url_handlers.html).

To print all available serial ports please use [pio device list](../../cli/pio-device/list.md) command.

Note that you can use patterns for serial ports:

| Pattern | Meaning |
|---|---|
| `*` | matches everything |
| `?` | matches any single character |
| `[seq]` | matches any character in seq |
| `[!seq]` | matches any character not in seq |

## Example

```ini
[env:custom_monitor_port]
...
; Unix
monitor_port = /dev/ttyUSB1

; Windows, COM1 or COM3
monitor_port = COM[13]

; Socket
monitor_port = socket://localhost:4444
```
