# Extra Python packages

If your project or library depends on the extra Python packages, you can use extra script to install them into the same virtual environment where [PlatformIO Core (CLI)](../../../get-started/platformio-core.md) is installed.

`platformio.ini`:

```ini
[env:my_env]
platform = ...
extra_scripts = extra_script.py
```

`extra_script.py` (place it near `platformio.ini`):

```python
Import("env")

# List installed packages
env.Execute("$PYTHONEXE -m pip list")

# Install custom packages from the PyPi registry
env.Execute("$PYTHONEXE -m pip install pkg1 pkg2")

# Install missed package
try:
    import some_package
except ImportError:
    env.Execute("$PYTHONEXE -m pip install some_package")
```
