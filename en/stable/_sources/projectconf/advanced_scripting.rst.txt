..  Copyright (c) 2014-present PlatformIO <contact@platformio.org>
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

.. _projectconf_advanced_scripting:

Advanced Scripting
------------------

.. warning::

  Advanced Scripting is recommended for Advanced Users and requires
  knowledge of the Python language.

.. warning::

  :ref:`projectconf_dynamic_build_flags` is a highly recommended
  alternative to advanced scripting, where you can use any programming
  language. Also, that option is useful if you need to apply changes
  to the project before the building/uploading process, such as:

  * Macro with the latest VCS revision/tag "on-the-fly"
  * Generate dynamic headers (``*.h``)
  * Process media content before generating SPIFFS image
  * Make some changes to source code or related libraries

.. contents::

The PlatformIO Build System allows the user to extend the build process with
custom scripts using the Python interpreter and
the `SCons <http://www.scons.org>`_ construction tool.
Build flags, upload flags, targets, toolchains data and other information are
available for modification as `SCons Construction Environments <http://www.scons.org/doc/production/HTML/scons-user.html#chap-environments>`_.
Custom scripts are included with :ref:`projectconf_extra_scripts`

.. warning::
  You can not run or debug these scripts manually with a Python
  interpreter. They will be loaded automatically when the
  :ref:`cmd_run` command processes the project environment.

Launch types
~~~~~~~~~~~~

There are two execution orders for extra scripts:

1. **PRE** - executes before the main script of :ref:`platforms`
2. **POST** - executes after the main script of :ref:`platforms`

Multiple extra scripts are allowed. Please split them via  ", "
(comma + space) in the same line or use multi-line values.

For example, in :ref:`projectconf`:

.. code-block:: ini

  [env:my_env_1]
  platform = ...
  ; Defaults to POST script since no prefix is used
  extra_scripts = post_extra_script.py

  [env:my_env_2]
  platform = ...
  extra_scripts =
    pre:pre_extra_script.py
    post:post_extra_script1.py
    post_extra_script2.py

This option can also be set by the global environment variable :envvar:`PLATFORMIO_EXTRA_SCRIPTS`.

Construction Environments
~~~~~~~~~~~~~~~~~~~~~~~~~

The PlatformIO Build System uses two built-in construction environments
to process each project:

* ``env``, ``Import("env")`` - the global construction environment used
  for the :ref:`platforms` and :ref:`frameworks` build scripts, upload tools,
  :ref:`ldf`, and other internal operations
* ``projenv``, ``Import("projenv")`` - the isolated construction environment
  used for processing the project source code in :ref:`projectconf_pio_src_dir`.
  Please note that any :ref:`projectconf_src_build_flags` specified in
  :ref:`projectconf` will be passed to ``projenv`` and not to ``env``.


.. warning::
  1. ``projenv`` is available only for POST-type scripts
  2. Flags passed to ``env`` using PRE-type script will affect ``projenv`` too.

``my_pre_extra_script.py``:

.. code-block:: python

    Import("env")

    # access to global construction environment
    print(env)

    # Dump construction environment (for debug purpose)
    print(env.Dump())

    # append extra flags to global build environment
    # which later will be used to build:
    # - project source code
    # - frameworks
    # - dependent libraries
    env.Append(CPPDEFINES=[
      "MACRO_1_NAME",
      ("MACRO_2_NAME", "MACRO_2_VALUE")
    ])


``my_post_extra_script.py``:

.. code-block:: python

    Import("env", "projenv")

    # access to global construction environment
    print(env)

    # access to project construction environment
    print(projenv)

    # Dump construction environments (for debug purpose)
    print(env.Dump())
    print(projenv.Dump())

    # append extra flags to global build environment
    # which later will be used to build:
    # - frameworks
    # - dependent libraries
    env.Append(CPPDEFINES=[
      "MACRO_1_NAME",
      ("MACRO_2_NAME", "MACRO_2_VALUE")
    ])

    # append extra flags to only project build environment
    projenv.Append(CPPDEFINES=[
      "PROJECT_EXTRA_MACRO_1_NAME",
      ("ROJECT_EXTRA_MACRO_2_NAME", "ROJECT_EXTRA_MACRO_2_VALUE")
    ])


See examples below how to import construction environments and modify existing
data or add new.

Before/Pre and After/Post actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The PlatformIO Build System has a rich API that allows one to attach different pre-/post
actions (hooks) using ``env.AddPreAction(target, callback)`` or
``env.AddPreAction(target, [callback1, callback2, ...])`` function. The first
argument ``target`` can be the name of a target that is passed using the
:option:`pio run --target` command, the name of a built-in target
(buildprog, size, upload, program, buildfs, uploadfs, uploadfsota) or the path
to a file which PlatformIO processes (ELF, HEX, BIN, OBJ, etc.).

**Examples**

The ``extra_script.py`` file is located in the same directory as ``platformio.ini``.

``platformio.ini``:

.. code-block:: ini

    [env:pre_and_post_hooks]
    extra_scripts = post:extra_script.py

``extra_script.py``:

.. code-block:: python

    Import("env", "projenv")

    # access to global build environment
    print(env)

    # access to project build environment (is used source files in "src" folder)
    print(projenv)

    #
    # Dump build environment (for debug purpose)
    # print(env.Dump())
    #

    #
    # Change build flags in runtime
    #
    env.ProcessUnFlags("-DVECT_TAB_ADDR")
    env.Append(CPPDEFINES=("VECT_TAB_ADDR", 0x123456789))

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

    print("Current build targets", map(str, BUILD_TARGETS))

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


Build Middlewares
~~~~~~~~~~~~~~~~~

PlatformIO Build System allows you to add middleware functions that can be used for
Build Node(Object) construction. This is very useful if you need to add custom flags
for the specific file nodes or exclude them from a build process.

There is ``env.AddBuildMiddleware(callback, pattern)`` helper which instructs
PlatformIO Build System to call ``callback`` for each `SCons File System Node <https://scons.org/doc/latest/HTML/scons-api/SCons.Node.FS.Dir-class.html>`_
whose path matches with `Unix shell-style "pattern" (wildcards) <https://docs.python.org/3.8/library/fnmatch.html>`_.

If a ``pattern`` is omitted, the ``callback`` will be called for each File System Node
which is added for the build process.

You can add an unlimited number of build middlewares. They will be called in order of
registration. Please note, if the first middleware ignores some File Nodes, they will
not be passed to the next middleware in chain.

**Examples**

``platformio.ini``:

.. code-block:: ini

    [env:build_middleware]
    extra_scripts = pre:extra_script.py

``extra_script.py``:

.. code-block:: python

    Import("env")


    # --- Add custom macros for the ALL files which name contains "http"
    def extra_http_configuration(node):
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

    def replace_node_with_another(node):
        return env.File("path/to/patched/RtosTimer.cpp")

    env.AddBuildMiddleware(
        replace_node_with_another,
        "framework-mbed/rtos/RtosTimer.cpp"
    )


    # --- Skip assembly *.S files from build process

    def skip_asm_from_build(node):
        # to ignore file from a build process, just return None
        return None

    env.AddBuildMiddleware(skip_asm_from_build, "*.S")


.. _projectconf_advanced_scripting_custom_targets:

Custom Targets
~~~~~~~~~~~~~~

.. versionadded:: 5.0

PlatformIO allows you to declare unlimited number of the custom targets. There are a
lot of use cases for them:

- Pre/Post processing based on a dependent sources (other target, source file, etc.)
- Command launcher with own arguments
- Launch command with custom options declared in :ref:`projectconf`
- Python callback as a target (use the power of Python interpreter and PlatformIO Build API).

A custom target can be processed using :option:`pio run --target` option and
you can list them via :option:`pio run --list-targets` command.

Build System API
^^^^^^^^^^^^^^^^

.. code-block:: python

    Import("env")

    env.AddCustomTarget(
        name,
        dependencies,
        actions,
        title=None,
        description=None,
        always_build=True
    )


``AddCustomTarget`` arguments:

:name:
    A name of target. ASCII chars (a-z, 0-9, _, -) are recommended. Good names are
    "gen_headers", "program_bitstream", etc.

:dependencies:
    A list of dependencies that should be built BEFORE target will be launched. It is
    possible pass multiple dependencies as a Python list ``["dep1", dep_target_2]``.
    If a target does not have dependencies, ``None`` should be passed.

:actions:
    A list of actions to call on a target. It is possible to pass multiple actions as
    a Python list ``["python --version", my_calback]``.

:title:
    A title of a target. It will be printed when using :ref:`piocore` or :ref:`pioide`.
    We recommend to keep a title very short, 1-2 words.

:description:
    The same as a ``title`` argument but allows you to provide detailed explanation
    what target does.

:always_build:
    If there are declared ``dependencies`` and they are already built, this target
    will not be called if ``always_build=False``. A default value is
    ``always_build=True`` and means always building/calling target.


Examples
^^^^^^^^

Command shortcut
''''''''''''''''

Create a custom ``node`` target (alias) which will print a NodeJS version

``platformio.ini``:

.. code-block:: ini

    [env:myenv]
    platform = ...
    ...
    extra_scripts = extra_script.py

``extra_script.py``:

.. code-block:: python

    Import("env")

    # Single action/command per 1 target
    env.AddCustomTarget("sysenv", None, 'python -c "import os; print(os.environ)"'))

    # Multiple actions
    env.AddCustomTarget(
        name="pioenv",
        dependencies=None,
        actions=[
            "pio --version",
            "python --version"
        ],
        title="Core Env",
        description="Show PlatformIO Core and Python versions"
    )


Now, run ``pio run --target sysenv`` or ``pio run -t pioenv`` (short version).

Dependent target
''''''''''''''''

Sometimes you need to run a command which depends on another target (file,
firmware, etc). Let's create an ``ota`` target and declare command which will
depend on a project firmware. If a build process successes, declared command
will be run.

``platformio.ini``:

.. code-block:: ini

    [env:myenv]
    platform = ...
    ...
    extra_scripts = extra_script.py


``extra_script.py``:

.. code-block:: python

    Import("env")

    env.AddCustomTarget(
        "ota",
        "$BUILD_DIR/${PROGNAME}.elf",
        "ota_script --firmware-path $SOURCE"
    )


Now, run ``pio run -t ota``.

Target with options
'''''''''''''''''''

Let's create a simple ``ping`` target and process it with
``pio run --target ping`` command:

``platformio.ini``:

.. code-block:: ini

    [env:env_custom_target]
    platform = ...
    ...
    extra_scripts = extra_script.py
    custom_ping_host = google.com

``extra_script.py``:

.. code-block:: python

    Import("env")

    host = env.GetProjectOption("custom_ping_host")

    def mytarget_callback(*args, **kwargs):
        print("Hello PlatformIO!")
        env.Execute("ping " + host)


    env.AddCustomTarget("ping", None, mytarget_callback)

Other Use Cases
~~~~~~~~~~~~~~~

The best examples are `PlatformIO development platforms <https://github.com/topics/platformio-platform>`__.
Please check ``builder`` folder for the main and framework scripts.

Custom options in ``platformio.ini``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

PlatformIO allows you extending project configuration with own data. You can read
these values later using `ProjectConfig API <https://github.com/platformio/platformio-core/blob/develop/platformio/project/config.py>`__:

:``ProjectConfig::get(section, option, default=None)``:
    Get an option value for the named section

:``ProjectConfig::options(section)``:
    Returns a list of the sections available

:``ProjectConfig::items(section, as_dict=False)``:
    Returns a list of "name", "value" pairs for the options in the given section or a dictionary when ``as_dict=True`` is passed

:``ProjectConfig::has_section(section)``:
    Indicates whether the named section is present in the configuration

:``ProjectConfig::has_option(section, option)``:
    If the given section exists, and contains the given option, returns ``True``; otherwise returns ``False``.

PlatformIO's "ProjectConfig" is compatible with a native Python's `ConfigParser <https://docs.python.org/3/library/configparser.html>`__ API.

**Example**

``platformio.ini``:

.. code-block:: ini

    [universe]
    hello = world

    [env:my_env]
    platform = ...
    extra_scripts = extra_script.py

    custom_option1 = value1
    custom_option2 = value2

``extra_script.py``:

.. code-block:: python

    # "env.GetProjectOption" shortcut for the active environment
    value1 = env.GetProjectOption("custom_option1")
    value2 = env.GetProjectOption("custom_option2")

    # Read value from other environments
    config = env.GetProjectConfig()
    world = config.get("universe", "hello")

Split C/C++ build flags
^^^^^^^^^^^^^^^^^^^^^^^

``platformio.ini``:

.. code-block:: ini

    [env:my_env]
    platform = ...
    extra_scripts = extra_script.py

``extra_script.py`` (place it near ``platformio.ini``):

.. code-block:: python

    Import("env")

    # General options that are passed to the C and C++ compilers
    env.Append(CCFLAGS=["flag1", "flag2"])

    # General options that are passed to the C compiler (C only; not C++).
    env.Append(CFLAGS=["flag1", "flag2"])

    # General options that are passed to the C++ compiler
    env.Append(CXXFLAGS=["flag1", "flag2"])

Extra Linker Flags without ``-Wl,`` prefix
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sometimes you need to pass extra flags to GCC linker without ``Wl,``. You could
use :ref:`projectconf_build_flags` option but it will not work. PlatformIO
will not parse these flags to ``LINKFLAGS`` scope. In this case, simple
extra script will help:

``platformio.ini``:

.. code-block:: ini

    [env:env_extra_link_flags]
    platform = windows_x86
    extra_scripts = extra_script.py

``extra_script.py`` (place it near ``platformio.ini``):

.. code-block:: python

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

Custom upload tool
^^^^^^^^^^^^^^^^^^

You can override default upload command of development platform using extra
script. There is the common environment variable ``UPLOADCMD`` which PlatformIO
Build System will handle when you :ref:`pio run -t upload <cmd_run>`.

Please note that some development platforms can have more than 1 upload command.
For example, :ref:`platform_atmelavr` has ``UPLOADHEXCMD``
(firmware) and ``UPLOADEEPCMD`` (EEPROM data).

See examples below:

**Template**

``platformio.ini``:

.. code-block:: ini

    [env:my_custom_upload_tool]
    platform = ...
    ; place it into the root of project or use full path
    extra_scripts = extra_script.py
    upload_protocol = custom
    ; each flag in a new line
    upload_flags =
      -arg1
      -arg2
      -argN

``extra_script.py`` (place it near ``platformio.ini``):

.. code-block:: python

    Import("env")

    # please keep $SOURCE variable, it will be replaced with a path to firmware

    # Generic
    env.Replace(
        UPLOADER="executable or path to executable",
        UPLOADCMD="$UPLOADER $UPLOADERFLAGS $SOURCE"
    )

    # In-line command with arguments
    env.Replace(
        UPLOADCMD="executable -arg1 -arg2 $SOURCE"
    )

    # Python callback
    def on_upload(source, target, env):
        print(source, target)
        firmware_path = str(source[0])
        # do something
        env.Execute("executable arg1 arg2")

    env.Replace(UPLOADCMD=on_upload)


**Custom openOCD command**

``platformio.ini``:

.. code-block:: ini

    [env:disco_f407vg]
    platform = ststm32
    board = disco_f407vg
    framework = mbed

    extra_scripts = extra_script.py
    upload_protocol = custom
    ; each flag in a new line
    upload_flags =
        -f
        scripts/interface/stlink.cfg
        -f
        scripts/target/stm32f4x.cfg

``extra_script.py`` (place it near ``platformio.ini``):

.. code-block:: python

    Import("env")

    platform = env.PioPlatform()

    env.Prepend(
        UPLOADERFLAGS=["-s", platform.get_package_dir("tool-openocd") or ""]
    )
    env.Append(
        UPLOADERFLAGS=["-c", "program {{$SOURCE}} verify reset; shutdown"]
    )
    env.Replace(
        UPLOADER="openocd",
        UPLOADCMD="$UPLOADER $UPLOADERFLAGS"
    )


Upload to Cloud (OTA)
^^^^^^^^^^^^^^^^^^^^^

See project example https://github.com/platformio/bintray-secure-ota

Custom firmware/program name
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sometimes is useful to have a different firmware/program name in
:ref:`projectconf_pio_build_dir`.

``platformio.ini``:

.. code-block:: ini

    [env:env_custom_prog_name]
    platform = espressif8266
    board = nodemcuv2
    framework = arduino
    build_flags = -D VERSION=13
    extra_scripts = pre:extra_script.py

``extra_script.py``:

.. code-block:: python

    Import("env")

    my_flags = env.ParseFlags(env['BUILD_FLAGS'])
    defines = {k: v for (k, v) in my_flags.get("CPPDEFINES")}
    # print(defines)

    env.Replace(PROGNAME="firmware_%s" % defines.get("VERSION"))

Override package files
^^^^^^^^^^^^^^^^^^^^^^

PlatformIO Package Manager automatically installs pre-built packages
(:ref:`frameworks`, toolchains, libraries) required by development
:ref:`platforms` and build process. Sometimes you need to override original
files with own versions: configure custom GPIO, do changes to built-in LD
scripts, or some patching to installed library dependency.

The simplest way is using `Diff and Patch technique <https://linuxacademy.com/blog/linux/introduction-using-diff-and-patch/>`_. How does it work?

1. Modify original source files
2. Generate patches
3. Apply patches via PlatformIO extra script before build process.

**Example**

We need to patch the original ``standard/pins_arduino.h`` variant from
:ref:`framework_arduino` framework and add extra macro ``#define PIN_A8   (99)``.
Let's duplicate ``standard/pins_arduino.h`` and apply changes. Generate a
patch file and place it into ``patches`` folder located in the root of a project:

.. code-block:: shell

    diff ~/.platformio/packages/framework-arduinoavr/variants/standard/pins_arduino.h /tmp/pins_arduino_modified.h > /path/to/platformio/project/patches/1-framework-arduinoavr-add-pin-a8.patch

The result of ``1-framework-arduinoavr-add-pin-a8.patch``:

.. code-block:: diff

    63a64
    > #define PIN_A8   (99)
    112c113
    < // 14-21 PA0-PA7 works
    ---
    > // 14-21 PA0-PA7 works

Using extra scripting we can apply patching before a build process. The final
result of :ref:`projectconf` and "PRE" extra script named ``apply_patches.py``:


``platformio.ini``:

.. code-block:: ini

    [env:uno]
    platform = atmelavr
    board = uno
    framework = arduino
    extra_scripts = pre:apply_patches.py

``apply_patches.py``:

.. code-block:: python

    from os.path import join, isfile

    Import("env")

    FRAMEWORK_DIR = env.PioPlatform().get_package_dir("framework-arduinoavr")
    patchflag_path = join(FRAMEWORK_DIR, ".patching-done")

    # patch file only if we didn't do it before
    if not isfile(join(FRAMEWORK_DIR, ".patching-done")):
        original_file = join(FRAMEWORK_DIR, "variants", "standard", "pins_arduino.h")
        patched_file = join("patches", "1-framework-arduinoavr-add-pin-a8.patch")

        assert isfile(original_file) and isfile(patched_file)

        env.Execute("patch %s %s" % (original_file, patched_file))
        # env.Execute("touch " + patchflag_path)


        def _touch(path):
            with open(path, "w") as fp:
                fp.write("")

        env.Execute(lambda *args, **kwargs: _touch(patchflag_path))


Please note that this example will work on a system where a ``patch`` tool
is available. For Windows OS, you can use ``patch`` and ``diff`` tools
provided by `Git client utility <https://git-scm.com/>`__
(located inside installation directory).

If you need to make it more independent to the operating system,
please replace the ``patch`` with a multi-platform
`python-patch <https://github.com/techtonik/python-patch>`_ script.

Override Board Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

PlatformIO allows one to override some basic options (integer or string values)
using :ref:`projectconf_board_more_options` in :ref:`projectconf`.
Sometimes you need to do complex changes to default board manifest and
extra PRE scripting work well here. See example below how to override default
hardware VID/PIDs.

.. warning::
    Due to a technical limitation these board changes will not work for
    :ref:`cmd_device_monitor` command.

``platformio.ini``:

.. code-block:: ini

    [env:uno]
    platform = atmelavr
    board = uno
    framework = arduino
    extra_scripts = pre:custon_hwids.py

``custon_hwids.py``:

.. code-block:: python

    Import("env")

    board_config = env.BoardConfig()
    # should be array of VID:PID pairs
    board_config.update("build.hwids", [
      ["0x2341", "0x0243"],  # 1st pair
      ["0x2A03", "0x0043"].  # 2nd pair, etc.
    ])

Custom debug flags
^^^^^^^^^^^^^^^^^^

PlatformIO removes all debug/optimization flags before a debug session or when
:ref:`build_configurations` is set to ``debug`` and overrides them with
``-0g -g2 -ggdb2`` for ``ASFLAGS``, ``CCFLAGS``, and ``LINKFLAGS`` build
scopes.

An extra script allows us to override PlatformIO's default behavior and declare
custom flags. See example below where we override ``-Og`` with ``-O0``:

``platformio.ini``:

.. code-block:: ini

    [env:teensy31]
    platform = teensy
    board = teensy31
    framework = arduino
    extra_scripts = custom_debug_flags.py

``custom_debug_flags.py``:

.. code-block:: python

    Import("env")

    if env.GetBuildType() == "debug":
       for scope in ("ASFLAGS", "CCFLAGS", "LINKFLAGS"):
          for i, flag in enumerate(env[scope]):
             if flag == "-Og":
                env[scope][i] = "-O0"

Extra Python packages
^^^^^^^^^^^^^^^^^^^^^

If your project depends on the extra Python packages, you can use extra script to
install them into the same virtual environment where :ref:`piocore` is installed.

``platformio.ini``:

.. code-block:: ini

    [env:my_env]
    platform = ...
    extra_scripts = extra_script.py

``extra_script.py`` (place it near ``platformio.ini``):

.. code-block:: python

    Import("env")

    # List installed packages
    env.Execute("$PYTHONEXE -m pip list")

    # Install custom packages from the PyPi registry
    env.Execute("$PYTHONEXE -m pip install pkg1 pkg2")
