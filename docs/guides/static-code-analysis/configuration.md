# Configuration {#configuration}

**Static Code Analysis** can be configured from ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md) using the next options:

- [Check options](../../reference/platformio-ini/env/check-options.md)

  - [`check_tool`](../../reference/platformio-ini/env/check-tool.md)
  - [`check_flags`](../../reference/platformio-ini/env/check-flags.md)
  - [`check_severity`](../../reference/platformio-ini/env/check-severity.md)
  - [`check_skip_packages`](../../reference/platformio-ini/env/check-skip-packages.md)
  - [`check_src_filters`](../../reference/platformio-ini/env/check-src-filters.md)

You can also override some options using [pio check](../../reference/cli/pio-check.md) command.

Custom tool version can be configured using [platform_packages](../../reference/platformio-ini/env/platform-packages.md) option. Check [PlatformIO Registry](https://registry.platformio.org/) for the available versions.

**Example**

```ini
[env:myenv]
platform = ...
board = ...
check_tool = cppcheck
platform_packages = tool-cppcheck@1.260.0
```
