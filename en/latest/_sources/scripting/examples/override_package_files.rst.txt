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

Override package files
~~~~~~~~~~~~~~~~~~~~~~

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