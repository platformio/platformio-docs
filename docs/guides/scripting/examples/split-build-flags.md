# Split C/C++ build flags

`platformio.ini`:

```ini
[env:my_env]
platform = ...
extra_scripts = extra_script.py
```

`extra_script.py` (place it near `platformio.ini`):

```python
Import("env")

# General options that are passed to the C and C++ compilers
env.Append(CCFLAGS=["flag1", "flag2"])

# General options that are passed to the C compiler (C only; not C++).
env.Append(CFLAGS=["flag1", "flag2"])

# General options that are passed to the C++ compiler
env.Append(CXXFLAGS=["flag1", "flag2"])
```
