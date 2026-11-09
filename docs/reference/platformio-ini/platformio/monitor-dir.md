---
description: "A storage for custom monitor filters (platformio.ini option monitor_dir)."
---

<a id="projectconf-pio-monitor-dir"></a>

# `monitor_dir` {#monitor-dir}

- **Type:** Path
- **Multiple values:** No
- **Default:** `${PROJECT_DIR}/monitor`
- **Environment variable:** [`PLATFORMIO_MONITOR_DIR`](../../environment-variables.md#envvar-PLATFORMIO_MONITOR_DIR), overrides the value in `platformio.ini`

The directory where [pio device monitor](../../cli/pio-device/monitor.md) will look for the [Custom Filters](../../cli/pio-device/monitor.md#cmd-device-monitor-custom-filters). The default value is `monitor`, meaning a `monitor` directory located in the root of the project.
