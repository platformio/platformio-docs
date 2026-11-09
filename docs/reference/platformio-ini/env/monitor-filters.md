<a id="projectconf-monitor-filters"></a>

# `monitor_filters` {#monitor-filters}

Type: `String` | Multiple: `Yes`

Apply filters and text transformation for device output. See available filters at [Filters](../../cli/pio-device/monitor.md#cmd-device-monitor-filters).

Example:

```ini
[env:log_output_to_file_with_timestamp]
...
platform = ...
monitor_filters =
  default   ; Remove typical terminal control codes from input
  time      ; Add timestamp with milliseconds for each new line
  log2file  ; Log data to a file “platformio-device-monitor-*.log” located in the current working directory
```
