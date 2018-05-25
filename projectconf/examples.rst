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

.. _projectconf_examples:

Examples
--------

.. note::
    A full list with project examples can be found in
    `PlatformIO Repository <https://github.com/platformio/platformio-examples/tree/develop>`_.

1. :ref:`platform_atmelavr`: Arduino UNO board with auto pre-configured
   ``board_*`` and ``upload_*`` options (use only ``board`` option) and Arduino
   Wiring-based Framework

.. code-block:: ini

    [env:atmelavr_arduino_uno_board]
    platform = atmelavr
    framework = arduino
    board = uno

    ; enable auto-uploading
    targets = upload


2. :ref:`platform_atmelavr`: Embedded board that is based on ATmega168 MCU with
   "arduino" bootloader

.. code-block:: ini

    [env:atmelavr_atmega168_board]
    platform = atmelavr
    board_build.mcu = atmega168
    board_build.f_cpu = 16000000L

    upload_port = /dev/ttyUSB0
    ; for Windows OS
    ; upload_port = COM3
    upload_protocol = arduino
    upload_speed = 19200

    ; enable auto-uploading
    targets = upload


3. Upload firmware via USB programmer (USBasp) to :ref:`platform_atmelavr`
   microcontrollers

.. code-block:: ini

    [env:atmelavr_usbasp]
    platform = atmelavr
    framework = arduino
    board = pro8MHzatmega328
    upload_protocol = usbasp
    upload_flags = -Pusb -B5

Then upload firmware using target ``program`` for :option:`platformio run --target`.
command. To use other programmers see :ref:`atmelavr_upload_via_programmer`.


4. :ref:`platform_ststm32`: Upload firmware using GDB script ``upload.gdb``,
   `issue #175 <https://github.com/platformio/platformio-core/issues/175>`_

.. code-block:: ini

    [env:st_via_gdb]
    platform = ststm32
    board = armstrap_eagle512
    upload_protocol = gdb

Also, take a look at this article `Armstrap Eagle and PlatformIO <https://www.isobit.io/blog/2015-08-08-armstrap/>`_.

5. :ref:`platform_ststm32`: Upload firmware using ST-Link instead mbed's media
   disk

.. code-block:: ini

    [env:stlink_for_mbed]
    platform = ststm32
    board = disco_f100rb
    upload_protocol = stlink