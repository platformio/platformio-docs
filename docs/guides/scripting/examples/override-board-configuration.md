# Override board configuration {#override-board-configuration}

PlatformIO allows one to override some basic options (integer or string values) using [More options](../../../reference/platformio-ini/env/platform-options.md#projectconf-board-more-options) in ["platformio.ini" (Project Configuration File)](../../../reference/platformio-ini/index.md). Sometimes you need to do complex changes to default board manifest and extra PRE scripting work well here. See example below how to override default hardware VID/PIDs.

:::warning

Due to a technical limitation these board changes will not work for [pio device monitor](../../../reference/cli/pio-device/monitor.md) command.

:::

`platformio.ini`:

```ini
[env:uno]
platform = atmelavr
board = uno
framework = arduino
extra_scripts = pre:custon_hwids.py
```

`custon_hwids.py`:

```python
Import("env")

board_config = env.BoardConfig()
# should be array of VID:PID pairs
board_config.update("build.hwids", [
  ["0x2341", "0x0243"],  # 1st pair
  ["0x2A03", "0x0043"],  # 2nd pair, etc.
])
```
