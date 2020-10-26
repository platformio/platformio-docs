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

.. _projectconf_section_env_upload:

Upload options
--------------

.. contents::
    :local:

.. _projectconf_upload_port:

``upload_port``
^^^^^^^^^^^^^^^

Type: ``String (Pattern)`` | Multiple: ``No``

This option is used by "uploader" tool when sending firmware to board via
``upload_port``. For example,

* ``/dev/ttyUSB0`` - Serial port (Unix-based OS)
* ``COM3`` - Serial port (Windows OS)
* ``192.168.0.13`` - IP address when using OTA
* ``/media/disk`` - physical path to media disk/flash drive
  (:ref:`framework_mbed` enabled boards)
* ``D:`` - physical path to media disk/flash drive (Windows OS).

If ``upload_port`` isn't specified, then *PlatformIO* will try to detect it
automatically.

To print all available serial ports please use :ref:`cmd_device_list` command.

This option can also be set by global environment variable
:envvar:`PLATFORMIO_UPLOAD_PORT`.

Please note that you can use Unix shell-style wildcards:

.. list-table::
    :header-rows:  1

    * - Pattern
      - Meaning

    * - ``*``
      - matches everything

    * - ``?``
      - matches any single character

    * - ``[seq]``
      - matches any character in seq

    * - ``[!seq]``
      - matches any character not in seq

**Example**

.. code-block:: ini

    [env:uno]
    platform = atmelavr
    framework = arduino
    ; any port that starts with /dev/ttyUSB
    upload_port = /dev/ttyUSB*

    ; COM1 or COM3
    upload_port = COM[13]

.. _projectconf_upload_protocol:

``upload_protocol``
^^^^^^^^^^^^^^^^^^^

Type: ``String`` | Multiple: ``No``

A protocol that "uploader" tool uses to talk to a board. Please check
:ref:`boards` for supported uploading protocols by your board.

.. note::
    ``upload_protocol = custom`` allows one to use a custom ``upload_command`` - see below.



.. _projectconf_upload_speed:

``upload_speed``
^^^^^^^^^^^^^^^^

Type: ``Integer`` | Multiple: ``No``

A connection speed (`baud rate <http://en.wikipedia.org/wiki/Baud>`_)
which "uploader" tool uses when sending firmware to board.

.. _projectconf_upload_flags:

``upload_flags``
^^^^^^^^^^^^^^^^

Type: ``String`` | Multiple: ``Yes``

Extra flags for uploader. Will be added to the end of uploader command. If you
need to override uploader command or base flags please use
:ref:`projectconf_extra_scripts`.

This option can also be set by global environment variable
:envvar:`PLATFORMIO_UPLOAD_FLAGS`.

**Example**

Please specify each flag/option in a new line starting with minimum 2 spaces.

.. code-block:: ini

    [env:atmega328pb]
    platform = atmelavr
    board = atmega328pb
    framework = arduino
    upload_flags =
      -P$UPLOAD_PORT
      -b$UPLOAD_SPEED
      -u
      -Ulock:w:0xCF:m
      -Uhfuse:w:0xD7:m
      -Uefuse:w:0xF6:m
      -Ulfuse:w:0xE2:m

.. _projectconf_upload_resetmethod:

``upload_resetmethod``
^^^^^^^^^^^^^^^^^^^^^^

Type: ``String`` | Multiple: ``No``

Specify reset method for "uploader" tool. This option isn't available for all
development platforms. The only :ref:`platform_espressif8266` supports it.

.. _projectconf_upload_command:

``upload_command``
^^^^^^^^^^^^^^^^^^

Type: ``String`` | Multiple: ``No``

Override default :ref:`platforms` upload command with a custom command. You can pass a full
upload command with arguments and options or mix with :ref:`projectconf_upload_flags`.

In order to use ``upload_command``, ``upload_protocol = custom`` must be specified.

Default upload commands are declared in ``build/main.py`` script file of
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

    ``$PROJECT_PACKAGES_DIR`` build variable points to :ref:`projectconf_pio_packages_dir`.

    .. code-block:: ini

        [env:program_via_AVR_ISP]
        platform = atmelavr
        framework = arduino
        board = uno
        upload_protocol = custom
        upload_flags =
            -C
            $PROJECT_PACKAGES_DIR/tool-avrdude/avrdude.conf
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
            $PROJECT_PACKAGES_DIR/tool-avrdude/avrdude.conf
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
        upload_command = $PROJECT_PACKAGES_DIR/tool-stlink/st-flash write $SOURCE 0x8000000
