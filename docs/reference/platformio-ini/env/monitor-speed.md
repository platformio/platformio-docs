---
description: "A monitor speed (baud rate) (platformio.ini option monitor_speed)."
---

<a id="projectconf-monitor-speed"></a>

# `monitor_speed` {#monitor-speed}

- **Type:** Integer
- **Multiple values:** No
- **Default:** `9600`
- **Deprecated name:** `monitor_baud` (still accepted, with a warning)

A monitor speed ([baud rate](http://en.wikipedia.org/wiki/Baud)). See [`pio device monitor --baud`](../../cli/pio-device/monitor.md#cmdoption-pio-device-monitor-b).

## Example

```ini
[env:custom_monitor_speedrate]
...
monitor_speed = 115200
```
