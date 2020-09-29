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

.. _board_microchippic32_flipnclickmz:

MikroElektronika Flip N Click MZ
================================

.. contents::

Hardware
--------

Platform :ref:`platform_microchippic32`: Microchip's 32-bit portfolio with the MIPS microAptiv or M4K core offer high performance microcontrollers, and all the tools needed to develop your embedded projects. PIC32 MCUs gives your application the processing power, memory and peripherals your design needs!

.. list-table::

  * - **Microcontroller**
    - 32MZ2048EFH100
  * - **Frequency**
    - 252MHz
  * - **Flash**
    - 1.98MB
  * - **RAM**
    - 512KB
  * - **Vendor**
    - `MikroElektronika <https://shop.mikroe.com/flipclick-pic32mz?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``flipnclickmz`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:flipnclickmz]
  platform = microchippic32
  board = flipnclickmz

You can override default MikroElektronika Flip N Click MZ settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `flipnclickmz.json <https://github.com/platformio/platform-microchippic32/blob/master/boards/flipnclickmz.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:flipnclickmz]
  platform = microchippic32
  board = flipnclickmz

  ; change microcontroller
  board_build.mcu = 32MZ2048EFH100

  ; change MCU frequency
  board_build.f_cpu = 252000000L

Debugging
---------
:ref:`piodebug` currently does not support MikroElektronika Flip N Click MZ board.

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences