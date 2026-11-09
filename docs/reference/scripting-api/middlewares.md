---
description: "PlatformIO Build System allows you to add middleware functions that can be used for Build Node(Object) construction."
---

<a id="scripting-middlewares"></a>

# Build middlewares {#build-middlewares}

PlatformIO Build System allows you to add middleware functions that can be used for Build Node(Object) construction. This is very useful if you need to add custom flags for the specific file nodes or exclude them from a build process.

There is `env.AddBuildMiddleware(callback, pattern)` helper which instructs PlatformIO Build System to call `callback` for each [SCons File System Node](https://scons.org/doc/latest/HTML/scons-api/SCons.Node/#SCons.Node.FS.Dir) whose path matches with [Unix shell-style "pattern" (wildcards)](https://docs.python.org/3.9/library/fnmatch.html).

If a `pattern` is omitted, the `callback` will be called for each File System Node which is added for the build process.

You can add an unlimited number of build middlewares. They will be called in order of registration. Please note, if a middleware ignores a node (returns `None`), the next middlewares in a chain will be ignored automatically.

A middleware can be only added to a `PRE` kind of [Launch Types](./launch-types.md).

## Examples

`platformio.ini`:

```ini
[env:build_middleware]
extra_scripts = pre:extra_script.py
```

`extra_script.py`:

```python
Import("env")


# --- Add custom macros for the ALL files which name contains "http"
def extra_http_configuration(env, node):
    """
    `node.name` - a name of File System Node
    `node.get_path()` - a relative path
    `node.get_abspath()` - an absolute path
    """

    # do not modify node if file name does not contain "http"
    if "http" not in node.name:
        return node

    # now, we can override ANY SCons variables (CPPDEFINES, CCFLAGS, etc.,) for the specific file
    # pass SCons variables as extra keyword arguments to `env.Object()` function
    # p.s: run `pio run -t envdump` to see a list with SCons variables

    return env.Object(
        node,
        CPPDEFINES=env["CPPDEFINES"]
        + [("HTTP_HOST", "device.local"), ("HTTP_PORT", 8080)],
        CCFLAGS=env["CCFLAGS"] + ["-fno-builtin-printf"]
    )

env.AddBuildMiddleware(extra_http_configuration)


# --- Replace some file from a build process with another

def replace_node_with_another(env, node):
    return env.File("path/to/patched/RtosTimer.cpp")

env.AddBuildMiddleware(
    replace_node_with_another,
    "framework-mbed/rtos/RtosTimer.cpp"
)


# --- Skip assembly *.S files from build process

def skip_asm_from_build(env, node):
    # to ignore file from a build process, just return None
    return None

env.AddBuildMiddleware(skip_asm_from_build, "*.S")
```
