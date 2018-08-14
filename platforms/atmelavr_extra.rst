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

Configuration
-------------

.. contents::
    :local:

.. _atmelavr_upload_via_programmer:

Upload using Programmer
~~~~~~~~~~~~~~~~~~~~~~~

To upload firmware using programmer you need to use ``program`` target instead
of ``upload`` for :option:`platformio run --target` command. For example,
``platformio run -t program``.

.. warning::
    Upload options like ``upload_port`` don't work as expected with ``platformio run -t program``. You need to use ``upload_flags`` if you want to specify custom port or speed (see examples below).

.. note::
    List of avrdude supported programmers are accessible with ``avrdude -c ?``

Configuration for the programmers:

*   AVR ISP

    .. code-block:: ini

        [env:myenv]
        platform = atmelavr
        framework = arduino
        upload_protocol = stk500v1
        ; each flag in a new line
        upload_flags =
            -P$UPLOAD_PORT

        ; edit this line with valid upload port
        upload_port = SERIAL_PORT_HERE

*   AVRISP mkII

    .. code-block:: ini

        [env:myenv]
        platform = atmelavr
        framework = arduino
        upload_protocol = stk500v2
        ; each flag in a new line
        upload_flags =
            -Pusb

*   USBtinyISP

    .. code-block:: ini

        [env:myenv]
        platform = atmelavr
        framework = arduino
        upload_protocol = usbtiny

*   ArduinoISP

    .. code-block:: ini

        [env:myenv]
        platform = atmelavr
        framework = arduino
        upload_protocol = arduinoisp

*   USBasp

    .. code-block:: ini

        [env:myenv]
        platform = atmelavr
        framework = arduino
        upload_protocol = usbasp
        ; each flag in a new line
        upload_flags =
            -Pusb

*   Parallel Programmer

    .. code-block:: ini

        [env:myenv]
        platform = atmelavr
        framework = arduino
        upload_protocol = dapa
        ; each flag in a new line
        upload_flags =
            -F

*   Arduino as ISP

    .. code-block:: ini

        [env:myenv]
        platform = atmelavr
        framework = arduino
        upload_protocol = stk500v1
        ; each flag in a new line
        upload_flags =
            -P$UPLOAD_PORT
            -b$UPLOAD_SPEED

        ; edit these lines
        upload_port = SERIAL_PORT_HERE
        upload_speed = 19200

*   Bus Pirate as ISP

    .. code-block:: ini

        [env:myenv]
        platform = atmelavr
        framework = arduino
        upload_protocol = buspirate
        ; each flag in a new line
        upload_flags =
            -P$UPLOAD_PORT
            -b$UPLOAD_SPEED

        ; edit these lines
        upload_port = SERIAL_PORT_HERE
        upload_speed = 115200

Upload EEPROM data
~~~~~~~~~~~~~~~~~~

To upload EEPROM data (from EEMEM directive) you need to use ``uploadeep``
target instead ``upload`` for :option:`platformio run --target` command.
For example, ``platformio run -t uploadeep``.

Fuses
~~~~~

PlatformIO has built-in target named ``fuses`` for setting fuse bits. The
default fuse bits are predefined in board manifest file in ``fuses`` section.
For example, `Arduino Uno Fuses <https://github.com/platformio/platform-atmelavr/blob/develop/boards/uno.json#L31>`_.

To set fuse bits you need to use  target ``fuses`` for
:option:`platformio run --target` command.

Custom Fuses
^^^^^^^^^^^^

You can specify custom fuse bits. Please create custom
:ref:`projectconf_extra_scripts` and override default "fuses" command:

``platformio.ini``:

.. code-block:: ini

    [env:custom_fuses]
    platform = atmelavr
    extra_scripts = extra_script.py


``extra_script.py``:

.. code-block:: py

    Import('env')
    env.Replace(FUSESCMD="avrdude $UPLOADERFLAGS -e -Ulock:w:0x3F:m -Uhfuse:w:0xDE:m -Uefuse:w:0x05:m -Ulfuse:w:0xFF:m")
