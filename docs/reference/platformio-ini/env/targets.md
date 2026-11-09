---
description: "A custom list of targets for PlatformIO Build System (platformio.ini option targets)."
---

# `targets`

- **Type:** String
- **Multiple values:** Yes

A list of targets which will be processed by the [pio run](../../cli/pio-run.md) command by default. You can enter more than one target, if separated by comma+space **", "**.

See [`pio run --list-targets`](../../cli/pio-run.md#cmdoption-pio-run-list-targets) documentation for the other targets.

## Examples

1. Build a project using [Release Configuration](../../../guides/projects/build-configurations.md), upload the firmware, and start [Serial Monitor](../../cli/pio-device/monitor.md) automatically:

   ```ini
   [env:upload_and_monitor]
   targets = upload, monitor
   ```

2. Build a project using [Debug Configuration](../../../guides/projects/build-configurations.md).

**Tip!** You can use these targets like an option to [`pio run --target`](../../cli/pio-run.md#cmdoption-pio-run-t) command. For example:

```bash
# clean project
pio run -t clean

# dump current build environment
pio run --target envdump
```

When no targets are defined, *PlatformIO* will build only sources by default.
