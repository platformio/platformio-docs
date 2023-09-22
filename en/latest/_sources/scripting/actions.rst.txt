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

.. _scripting_actions:

Pre & Post Actions
------------------

The PlatformIO Build System has a rich API that allows one to attach different pre-/post
actions (hooks) using ``env.AddPreAction(target, callback)`` or
``env.AddPreAction(target, [callback1, callback2, ...])`` function. The first
argument ``target`` can be the name of a target that is passed using the
:option:`pio run --target` command, the name of a built-in target
(buildprog, size, upload, program, buildfs, uploadfs, uploadfsota) or the path
to a file which PlatformIO processes (ELF, HEX, BIN, OBJ, etc.).

.. warning::
    The actions can only be applied to the global construction environment
    (see :ref:`scripting_envs`).

**Examples**

The ``extra_script.py`` file is located in the same directory as
:ref:`projectconf`.

``platformio.ini``:

.. code-block:: ini

    [env:pre_and_post_hooks]
    extra_scripts = post:extra_script.py

``extra_script.py``:

.. code-block:: python

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
