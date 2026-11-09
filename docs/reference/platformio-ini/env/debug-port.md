---
description: "A debugging port of a remote target (a serial device or network address) (platformio.ini option debug_port)."
---

<a id="projectconf-debug-port"></a>

# `debug_port` {#debug-port}

- **Type:** String
- **Multiple values:** No

A debugging port of a remote target. Could be a serial device or network address. PlatformIO detects it automatically if is not specified.

For example:

- `/dev/ttyUSB0` - Unix-based OS
- `COM3` - Windows OS
- `localhost:3333`
