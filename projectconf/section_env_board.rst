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

.. _projectconf_section_env_board:

Board options
~~~~~~~~~~~~~

.. contents::
    :local:

``board_build.mcu``
^^^^^^^^^^^^^^^^^^^

``board_build.mcu`` is a microcontroller(MCU) type that is used by compiler to
recognize MCU architecture. The correct type of ``board_build.mcu`` depends on
platform library. For example, the list of ``board_build.mcu`` for "megaAVR Devices"
is described `here <http://www.nongnu.org/avr-libc/user-manual/>`_.

The full list of ``board_build.mcu`` for the popular embedded platforms you can find
in *Boards* section of :ref:`platforms`. See "Microcontroller" column.

.. _projectconf_board_build.f_cpu:

``board_build.f_cpu``
^^^^^^^^^^^^^^^^^^^^^

An option ``board_build.f_cpu`` is used to define MCU frequency (Hertz, Clock). A
format of this option is ``C-like long integer`` value with ``L`` suffix. The
1 Hertz is equal to ``1L``, then 16 MHz (Mega Hertz) is equal to ``16000000L``.

The full list of ``board_build.f_cpu`` for the popular embedded platforms you can
find in *Boards* section of :ref:`platforms`. See "Frequency" column. You can
overclock a board by specifying a ``board_build.f_cpu`` value other than the default.

More options
^^^^^^^^^^^^

You can override any board option declared in manifest file using the next
format ``board_{OBJECT.PATH}``, where ``{OBJECT.PATH}`` is an object path in
JSON manifest. Please navigate to "boards" folder of `PlatfomIO development platforms <https://github.com/topics/platformio-platform>`_
and open JSON file to list all available options.

For example, `Manifest: Espressif ESP32 Dev Module <https://github.com/platformio/platform-espressif32/blob/develop/boards/esp32dev.json>`_:

.. code-block:: ini

    [env:custom_board_options]
    ; Custom CPU Frequency
    board_build.f_cpu = 160000000L

    ; Custom FLASH Frequency
    board_build.f_flash = 80000000L

    ; Custom FLASH Mode
    board_build.flash_mode = qio

    ; Custom maximum program size
    board_upload.maximum_size = 1310720
