<a id="projectconf-pio-monitor-dir"></a>

# `monitor_dir` {#monitor-dir}

Type: `DirPath` | Multiple: `No` | Default: "\<Project>/`monitor`"

The directory where [pio device monitor](../../cli/pio-device/monitor.md) will look for the [Custom Filters](../../cli/pio-device/monitor.md#cmd-device-monitor-custom-filters). The default value is `monitor`, meaning a `monitor` directory located in the root of the project.

This option can also be configured by the global environment variable [`PLATFORMIO_MONITOR_DIR`](../../environment-variables.md#envvar-PLATFORMIO_MONITOR_DIR).
