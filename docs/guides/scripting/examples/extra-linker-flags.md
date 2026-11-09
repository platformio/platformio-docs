# Extra linker flags without `-Wl,` prefix {#extra-linker-flags-without-wl-prefix}

Sometimes you need to pass extra flags to GCC linker without `Wl,`. You could use [build_flags](../../../reference/platformio-ini/env/build-flags.md) option but it will not work. PlatformIO will not parse these flags to `LINKFLAGS` scope. In this case, simple extra script will help:

`platformio.ini`:

```ini
[env:env_extra_link_flags]
platform = windows_x86
extra_scripts = extra_script.py
```

`extra_script.py` (place it near `platformio.ini`):

```python
Import("env")

#
# Dump build environment (for debug)
# print(env.Dump())
#

env.Append(
  LINKFLAGS=[
      "-static",
      "-static-libgcc",
      "-static-libstdc++"
  ]
)
```
