<a id="scripting-actions"></a>

# Pre & Post Actions {#pre-post-actions}

The PlatformIO Build System has a rich API that allows one to attach different pre-/post actions (hooks) using `env.AddPreAction(target, callback)` or `env.AddPreAction(target, [callback1, callback2, ...])` function. The first argument `target` can be the name of a target that is passed using the [`pio run --target`](../cli/pio-run.md#cmdoption-pio-run-t) command, the name of a built-in target (buildprog, size, upload, program, buildfs, uploadfs, uploadfsota) or the path to a file which PlatformIO processes (ELF, HEX, BIN, OBJ, etc.).

:::warning

The actions can only be applied to the global construction environment (see [Construction Environments](./construction-environments.md)).

:::

**Examples**

The `extra_script.py` file is located in the same directory as ["platformio.ini" (Project Configuration File)](../platformio-ini/index.md).

`platformio.ini`:

```ini
[env:pre_and_post_hooks]
extra_scripts = post:extra_script.py
```

`extra_script.py`:

```python
Import("env")

print("Current CLI targets", COMMAND_LINE_TARGETS)
print("Current Build targets", BUILD_TARGETS)

def post_program_action(source, target, env):
    print("Program has been built!")
    program_path = target[0].get_abspath()
    print("Program path", program_path)
    # Use case: sign a firmware, do any manipulations with ELF, etc
    # env.Execute(f"sign --elf {program_path}")

env.AddPostAction("$PROGPATH", post_program_action)

#
# Upload actions
#

def before_upload(source, target, env):
    print("before_upload")
    # do some actions

    # call Node.JS or other script
    env.Execute("node --version")


def after_upload(source, target, env):
    print("after_upload")
    # do some actions

env.AddPreAction("upload", before_upload)
env.AddPostAction("upload", after_upload)

#
# Custom actions when building program/firmware
#

env.AddPreAction("buildprog", callback...)
env.AddPostAction("buildprog", callback...)

#
# Custom actions for specific files/objects
#

env.AddPreAction("$PROGPATH", callback...)
env.AddPreAction("$BUILD_DIR/${PROGNAME}.elf", [callback1, callback2,...])
env.AddPostAction("$BUILD_DIR/${PROGNAME}.hex", callback...)

# custom action before building SPIFFS image. For example, compress HTML, etc.
env.AddPreAction("$BUILD_DIR/spiffs.bin", callback...)

# custom action for project's main.cpp
env.AddPostAction("$BUILD_DIR/src/main.cpp.o", callback...)

# Custom HEX from ELF
env.AddPostAction(
    "$BUILD_DIR/${PROGNAME}.elf",
    env.VerboseAction(" ".join([
        "$OBJCOPY", "-O", "ihex", "-R", ".eeprom",
        "$BUILD_DIR/${PROGNAME}.elf", "$BUILD_DIR/${PROGNAME}.hex"
    ]), "Building $BUILD_DIR/${PROGNAME}.hex")
)
```
