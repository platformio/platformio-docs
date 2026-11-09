<a id="library-json-buid-extra-script"></a>

# `extraScript` {#extrascript}

*Optional* | Type: `String`

:::info[See also]

Please make sure to read [Advanced Scripting](../../../guides/scripting/index.md) and [Construction Environments](../../scripting-api/construction-environments.md) guides first.

:::

Launch extra script before a build process.

:::warning

The [Pre & Post Actions](../../scripting-api/actions.md) can only be applied to the global construction environment (see [Construction Environments](../../scripting-api/construction-environments.md)).

:::

**Example** (HAL-based library)

This example demonstrates how to build HAL-dependent source files and exclude other source files from a build process.

Project structure

```text
├── lib
│   ├── README
│   └── SomeLib
│       ├── extra_script.py
│       ├── hal
│       │   ├── bar
│       │   │   ├── hal.c
│       │   │   └── hal.h
│       │   ├── foo
│       │       ├── hal.c
│       │       └── hal.h
│       ├── library.json
│       ├── SomeLib.c
│       └── SomeLib.h
├── platformio.ini
└── src
    └── test.c
```

`platformio.ini`

```ini
[env:foo]
platform = native
build_flags = -DHAL=foo

[env:bar]
platform = native
build_flags = -DHAL=bar
```

`library.json`

```ini
{
    "name": "SomeLib",
    "version": "0.0.0",
    "build": {
        "extraScript": "extra_script.py"
    }
}
```

`extra_script.py`

```py
Import('env')
from os.path import join, realpath

#
# Private flags (only for the current "SomeLib" source files)
#
for item in env.get("CPPDEFINES", []):
    if isinstance(item, tuple) and item[0] == "HAL":
        env.Append(CPPPATH=[realpath(join("hal", item[1]))])
        env.Replace(SRC_FILTER=["+<*>", "-<hal*>", "+<hal/%s>" % item[1]])
        break

#
# Pass flags to the other Project Dependencies (libraries)
#
for lb in env.GetLibBuilders():
    lb.env.Append(CPPDEFINES=[("TEST_LIBDEPS", 1)])
    if lb.name == "OneWire":
        lb.env.Append(CPPDEFINES=[("OW_PIN", 13)])


# Operate with the project environment (files located in the `src` folder)
Import("projenv")
# add (prepend) to the beginning of list
projenv.Prepend(CPPPATH=["some/path"])
# remove specified flags
projenv.ProcessUnFlags("-fno-rtti")

# Pass flags to the Global environment (project `src` files, frameworks)
global_env = DefaultEnvironment()
global_env.Append(CPPDEFINES=[("TEST_GLOBAL", 1)])

# Attach post action to the global environment

def post_program_action(source, target, env):
    print("Program has been built!")
    program_path = target[0].get_abspath()
    print("Program path", program_path)
    # Use case: sign a firmware, do any manipulations with ELF, etc
    # env.Execute(f"sign --elf {program_path}")

global_env.AddPostAction("$PROGPATH", post_program_action)
```
