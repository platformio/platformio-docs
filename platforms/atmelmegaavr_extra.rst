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

.. _atmelmegaavr_upload_via_programmer:

Upload using Programmer
~~~~~~~~~~~~~~~~~~~~~~~

In the case of external programmers, it's easy to brick a board simply by specifying
incorrect upload flags. It's highly recommended to use the
:ref:`projectconf_upload_command` option that gives the full control over flags used
for uploading. Please read :ref:`atmelavr_upload_via_programmer` for more information.

Upload using pyupdi
^^^^^^^^^^^^^^^^^^^

``pyupdi`` is a Python-based tool for programming tinyAVR and megaAVR devices with UPDI
interface via a standard serial port. It can be installed directly in the PlatformIO
virtual environment using the following command:

.. code-block:: bash

    pip install https://github.com/mraardvark/pyupdi/archive/master.zip


Once ``pyupdi`` is installed it can be used as the uploader via a custom
:ref:`projectconf_upload_command` option, for example:

.. code-block:: ini

    [env:ATmega3209_pyupdi_upload]
    platform = atmelmegaavr
    framework = arduino
    board = ATmega3209
    upload_speed = 115200
    upload_flags =
        -d
        mega3209
        -c
        $UPLOAD_PORT
        -b
        $UPLOAD_SPEED
    upload_command = pyupdi $UPLOAD_FLAGS -f $SOURCE

.. warning::

    Device names used in in ``pyupdi`` differ from MCU names used in the ``atmelmegaavr``
    platform. Run ``pyupdi --help`` to see the list of supported devices.

More information and a typical circuit diagram can be found in the official
`pyupdi repository <https://github.com/mraardvark/pyupdi>`_ repository.

Fuses programming
~~~~~~~~~~~~~~~~~

PlatformIO has a built-in target called ``fuses`` for setting fuse bits. The default fuse
bits are predefined in the board manifest file in the ``fuses`` section. For example,
`fuses section for Arduino Nano Every board <https://github.com/platformio/platform-atmelmegaavr/blob/develop/boards/nano_every.json>`_.
To set fuse bits you need to use target ``fuses`` with :option:`pio run --target` command.

Custom fuses
^^^^^^^^^^^^

Custom fuse values and upload flags (based on upload protocol) should be specified in
:ref:`projectconf`. An example of setting custom fuses for ``ATmega3209`` board:

.. code-block:: ini

    [env:custom_fuses]
    platform = atmelmegaavr
    framework = arduino
    board = ATmega3209
    upload_protocol = xplainedmini_updi
    board_fuses.bootend = 0xAA
    board_fuses.syscfg0 = 0xBB
    board_fuses.osccfg = 0xCC

Overriding default fuses command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For more detailed information read :ref:`atmelavr_overriding_fuses_command`.

Bootloader programming
~~~~~~~~~~~~~~~~~~~~~~

PlatformIO has a built-in target called ``bootloader`` for flashing bootloaders. The
default bootloader image and corresponding fuse bits are predefined in the board manifest
file in the ``bootloader`` section, for example, `Arduino Uno WiFi Rev2 <https://github.com/platformio/platform-atmelmegaavr/blob/develop/boards/uno_wifi_rev2.json>`_.
To upload a bootloader image you need to use target ``bootloader`` with
:option:`pio run --target` command.

Custom bootloader
^^^^^^^^^^^^^^^^^

Custom bootloader and accompanying fuses should be specified in :ref:`projectconf`.
An example of setting custom bootloader for ``ATmega4808`` board:

.. code-block:: ini

    [env:ATmega4808]
    platform = atmelmegaavr
    framework = arduino
    board = ATmega4808

    board_bootloader.file = /path/to/custom/bootloader.hex
    board_bootloader.bootend = 0xFF
    board_bootloader.syscfg0 = 0xDE
    board_bootloader.osccfg = 0xFD
    board_bootloader.lock_bits = 0x0F

Overriding default bootloader command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For more detailed information read :ref:`atmelavr_overriding_bootloader_command`.
