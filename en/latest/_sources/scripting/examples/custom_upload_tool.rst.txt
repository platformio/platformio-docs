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

Custom upload tool
~~~~~~~~~~~~~~~~~~

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