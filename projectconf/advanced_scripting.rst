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

.. versionadded:: 3.4.1

.. warning::

  Advanced Scripting is recommended for Advanced Users and requires Python
  language knowledge.

  We highly recommend to take a look at :ref:`projectconf_dynamic_build_flags`
  option where you can use any programming language. Also, this option is
  useful if you need to apply changes to the project before building/uploading
  process:

  * Macro with the latest VCS revision/tag "on-the-fly"
  * Generate dynamic headers (``*.h``)
  * Process media content before generating SPIFFS image
  * Make some changes to source code or related libraries

  More details :ref:`projectconf_dynamic_build_flags`.

.. contents::

PlatformIO Build System allows one to extend build process with the custom
:ref:`projectconf_extra_scripts` using Python interpreter and
`SCons <http://www.scons.org>`_ construction tool.
Build and upload flags, targets, toolchains data, and other information are
stored in `SCons Construction Environments <http://www.scons.org/doc/production/HTML/scons-user.html#chap-environments>`_.

.. warning::
  You can not run/debug these scripts directly with Python interpreter. They
  will be loaded automatically when you processing project environment using
  :ref:`cmd_run` command.

Launch types
~~~~~~~~~~~~

There are 2 launch type of extra scripts:

1. **PRE** - executes before a main script of :ref:`platforms`
2. **POST** - executes after a main script of :ref:`platforms`


Multiple extra scripts are allowed. Please split them via  ", "
(comma + space) in the same line or use multi-line values.

For example, :ref:`projectconf`

.. code-block:: ini

  [env:my_env_1]
  platform = ...
  ; without prefix, POST script
  extra_scripts = post_extra_script.py

  [env:my_env_2]
  platform = ...
  extra_scripts =
    pre:pre_extra_script.py
    post:post_extra_script1.py
    post_extra_script2.py

This option can be set by global environment variable :envvar:`PLATFORMIO_EXTRA_SCRIPTS`.

Construction Environments
~~~~~~~~~~~~~~~~~~~~~~~~~

There are 2 built-in construction environments which PlatformIO Build System
uses to process a project:

* ``env``, ``Import("env")`` - global construction environment which is used
  for :ref:`platforms` and :ref:`frameworks` build scripts, upload tools,
  :ref:`ldf`, and other internal operations
* ``projenv``, ``Import("projenv")`` - isolated construction environment which
  is used for processing of a project source code located in :ref:`projectconf_pio_src_dir`.
  Please note that :ref:`projectconf_src_build_flags` specified in
  :ref:`projectconf` will be passed to ``projenv`` and not to ``env``.


.. warning::
  1. ``projenv`` is available only for POST-type scripts
  2. Flags passed to ``env`` using PRE-type script will affect ``projenv`` too.

``my_pre_extra_script.py``:

.. code-block:: python

    Import("env")

    # access to global construction environment
    print env

    # Dump construction environment (for debug purpose)
    print env.Dump()

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
    print env

    # access to project construction environment
    print projenv

    # Dump construction environments (for debug purpose)
    print env.Dump()
    print projenv.Dump()

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

PlatformIO Build System has rich API that allows one to attach different pre-/post
actions (hooks) using ``env.AddPreAction(target, callback)`` or
``env.AddPreAction(target, [callback1, callback2, ...])`` function. A first
argument ``target`` can be a name of target that is passed using
:option:`platformio run --target` command, a name of built-in targets
(buildprog, size, upload, program, buildfs, uploadfs, uploadfsota) or path
to file which PlatformIO processes (ELF, HEX, BIN, OBJ, etc.).


**Examples**

``extra_script.py`` file is located on the same level as ``platformio.ini``.

``platformio.ini``:

.. code-block:: ini

    [env:pre_and_post_hooks]
    extra_scripts = post:extra_script.py

``extra_script.py``:

.. code-block:: python

    Import("env", "projenv")

    # access to global build environment
    print env

    # access to project build environment (is used source files in "src" folder)
    print projenv

    #
    # Dump build environment (for debug purpose)
    # print env.Dump()
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
        print "before_upload"
        # do some actions

        # call Node.JS or other script
        env.Execute("node --version")


    def after_upload(source, target, env):
        print "after_upload"
        # do some actions

    print "Current build targets", map(str, BUILD_TARGETS)

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


Custom target
~~~~~~~~~~~~~

There is a list with built-in targets which could be processed using
:option:`platformio run --target` option. You can create unlimited number of
the own targets and declare custom handlers for them.

We will use SCons's `Alias(alias, [targets, [action]]) , env.Alias(alias, [targets, [action]]) <https://scons.org/doc/production/HTML/scons-user/apd.html>`__
function to declare a custom target/alias.

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
    env.AlwaysBuild(env.Alias("node", None, ["node --version"]))


Now, run ``pio run -t node``.

Dependent target
''''''''''''''''

Sometime you need to run a command which depends on another target (file,
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
    env.AlwaysBuild(env.Alias("ota",
        "$BUILD_DIR/${PROGNAME}.elf",
        ["ota_script --firmware-path $SOURCE"]))


Now, run ``pio run -t ota``.

Target with options
'''''''''''''''''''

Let's create a simple ``ping`` target and process it with
``platformio run --target ping`` command:

``platformio.ini``:

.. code-block:: ini

    [env:env_custom_target]
    platform = ...
    ...
    extra_scripts = extra_script.py
    custom_ping_host = google.com

``extra_script.py``:

.. code-block:: python

    from platformio import util
    Import("env")

    config = util.load_project_config()
    host = config.get("env_custom_target", "custom_ping_host")

    def mytarget_callback(*args, **kwargs):
        print "Hello PlatformIO!"
        env.Execute("ping " + host)


    env.AlwaysBuild(env.Alias("ping", None, mytarget_callback))

Examples
~~~~~~~~

The beast examples are `PlatformIO development platforms <https://github.com/topics/platformio-platform>`__.
Please check ``builder`` folder for the main and framework scripts.

Custom options in ``platformio.ini``
''''''''''''''''''''''''''''''''''''

``platformio.ini``:

.. code-block:: ini

    [env:my_env]
    platform = ...
    extra_scripts = extra_script.py

    custom_option1 = value1
    custom_option2 = value2

``extra_script.py``:

.. code-block:: python

    from platformio import util

    config = util.load_project_config()

    value1 = config.get("my_env", "custom_option1")
    value2 = config.get("my_env", "custom_option2")

Split C/C++ build flags
'''''''''''''''''''''''

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
''''''''''''''''''''''''''''''''''''''''''

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
    # print env.Dump()
    #

    env.Append(
      LINKFLAGS=[
          "-static",
          "-static-libgcc",
          "-static-libstdc++"
      ]
    )

Custom upload tool
''''''''''''''''''

You can override default upload command of development platform using extra
script. There is the common environment variable ``UPLOADCMD`` which PlatformIO
Build System will handle when you :ref:`platformio run -t upload <cmd_run>`.

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
        UPLOADER="executable or path to executable"
        UPLOADCMD="$UPLOADER $UPLOADERFLAGS $SOURCE"
    )

    # In-line command with arguments
    env.Replace(
        UPLOADCMD="executable -arg1 -arg2 $SOURCE"
    )

    # Python callback
    def on_upload(source, target, env):
        print source, target
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
'''''''''''''''''''''

See project example https://github.com/platformio/bintray-secure-ota

Custom firmware/program name
''''''''''''''''''''''''''''

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
    # print defines

    env.Replace(PROGNAME="firmware_%s" % defines.get("VERSION"))
