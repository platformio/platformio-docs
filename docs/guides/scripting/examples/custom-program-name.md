# Custom firmware/program name

Sometimes it is useful to have a different firmware/program name in [build_dir](../../../reference/platformio-ini/platformio/build-dir.md). The following example uses [Custom options in platformio.ini](./platformio-ini-custom-options.md) and adds a project version suffix to the firmware name.

`platformio.ini`:

```ini
[env:env_custom_prog_name]
platform = platformio/espressif32
framework = arduino
board = esp32dev
build_flags =
    -DVERSION=${this.custom_prog_version}
extra_scripts = pre:extra_script.py
custom_prog_version = 1.2.3
```

`extra_script.py`:

```python
Import("env")

env.Replace(PROGNAME="firmware_%s" % env.GetProjectOption("custom_prog_version"))
```
