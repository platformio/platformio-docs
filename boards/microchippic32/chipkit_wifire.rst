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

.. _board_microchippic32_chipkit_wifire:

Digilent chipKIT WiFire
=======================

.. contents::

Hardware
--------

Platform :ref:`platform_microchippic32`: Microchip's 32-bit portfolio with the MIPS microAptiv or M4K core offer high performance microcontrollers, and all the tools needed to develop your embedded projects. PIC32 MCUs gives your application the processing power, memory and peripherals your design needs!

.. list-table::

  * - **Microcontroller**
    - 32MZ2048ECG100
  * - **Frequency**
    - 200MHz
  * - **Flash**
    - 1.98MB
  * - **RAM**
    - 512KB
  * - **Vendor**
    - `Digilent <http://store.digilentinc.com/chipkit-wi-fire-wifi-enabled-mz-microcontroller-board/?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``chipkit_wifire`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:chipkit_wifire]
  platform = microchippic32
  board = chipkit_wifire

You can override default Digilent chipKIT WiFire settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `chipkit_wifire.json <https://github.com/platformio/platform-microchippic32/blob/master/boards/chipkit_wifire.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:chipkit_wifire]
  platform = microchippic32
  board = chipkit_wifire

  ; change microcontroller
  board_build.mcu = 32MZ2048ECG100

  ; change MCU frequency
  board_build.f_cpu = 200000000L

Debugging
---------
:ref:`piodebug` currently does not support Digilent chipKIT WiFire board.

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences