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

.. _projectconf_upload_command:

``upload_command``
------------------

Type: ``String`` | Singleline: ``Yes``

Override default :ref:`platforms` upload command with a custom command. You can pass a full
upload command with arguments and options or mix with :ref:`projectconf_upload_flags`.

In order to use ``upload_command``, ``upload_protocol = custom`` must be specified.

Default upload commands are declared in ``builder/main.py`` script file of
:ref:`platforms`. See a list with open source
:ref:`platforms` => https://github.com/topics/platformio-platform

.. note::
  Please note that you can use build variables in ``upload_command``, such as
  PlatformIO project folders and other runtime configuration. A list with
  build variables are available by running
  ``pio run --target envdump`` command.

**Examples**

1.  Override default upload command but handle pre-uploading actions (looking
    for serial port, extra image preparation, etc.). Normally, the
    pre-configured upload options will be stored in ``$UPLOADERFLAGS`` build
    variable. A classic default upload command for :ref:`platforms` may look as
    ``some-flash-bin-tool $UPLOADERFLAGS $SOURCE``, where
    ``$SOURCE`` will be replaced by a real program/firmware binary.

    ``${platformio.packages_dir}`` template points to :ref:`projectconf_pio_packages_dir`.

    .. code-block:: ini

        [env:program_via_AVR_ISP]
        platform = atmelavr
        framework = arduino
        board = uno
        upload_protocol = custom
        upload_flags =
            -C
            ${platformio.packages_dir}/tool-avrdude/avrdude.conf
            -p
            atmega328p
            -P
            $UPLOAD_PORT
            -b
            115200
            -c
            stk500v1
        upload_command = avrdude $UPLOAD_FLAGS -U flash:w:$SOURCE:i

2.  Override default upload command and skip pre-uploading actions.

    .. code-block:: ini

        [env:program_via_usbasp]
        platform = atmelavr
        framework = arduino
        board = uno
        upload_protocol = custom
        upload_flags =
            -C
            ${platformio.packages_dir}/tool-avrdude/avrdude.conf
            -p
            atmega328p
            -Pusb
            -c
            stk500v1
        upload_command = avrdude $UPLOAD_FLAGS -U flash:w:$SOURCE:i


        ; Use ST-util for flashing
        ; https://github.com/texane/stlink

        [env:custom_st_flash]
        platform = ststm32
        framework = stm32cube
        board = bluepill_f103c6
        upload_protocol = custom
        upload_command = ${platformio.packages_dir}/tool-stlink/st-flash write $SOURCE 0x8000000
