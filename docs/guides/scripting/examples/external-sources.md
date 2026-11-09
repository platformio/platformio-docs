# Build external sources

If your project depends on some arbitrary source files that are located outside of the usual source directory [src_dir](../../../reference/platformio-ini/platformio/src-dir.md) then you can use a preliminary extra script to add them to the build process. A typical situation when this approach may be useful is when a project depends on pregenerated files in a temporary folder. Here is a typical configuration with an extra_script that instructs PlatformIO to build all sources in an external folder:

`platformio.ini`:

```ini
[env:my_env]
platform = ...
extra_scripts = pre:extra_script.py
```

`extra_script.py` (place it near `platformio.ini`):

```python
import os

Import("env")

env.BuildSources(
    os.path.join("$BUILD_DIR", "external", "build"),
    os.path.join("$PROJECT_DIR", "external", "sources")
)
```
