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

.. _board_atmelavr_attiny88:

Generic ATTiny88
================

.. contents::

Platform :ref:`platform_atmelavr`: Atmel AVR 8- and 32-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industrys most code-efficient architecture for C and assembly programming.

System
------

.. list-table::

  * - **Microcontroller**
    - ATTINY88
  * - **Frequency**
    - 8Mhz
  * - **Flash**
    - 8KB
  * - **RAM**
    - 512B
  * - **Vendor**
    - `Atmel <http://www.atmel.com/devices/ATTINY88.aspx?utm_source=platformio&utm_medium=docs>`__


Configuration
-------------

Please use ``attiny88`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:attiny88]
  platform = atmelavr
  board = attiny88

You can override default Generic ATTiny88 settings per build environment using
``board_{JSON.PATH}`` option, where ``{JSON.PATH}`` is a path from
board manifest `attiny88.json <https://github.com/platformio/platform-atmelavr/blob/master/boards/attiny88.json>`_. For example,

.. code-block:: ini

  [env:attiny88]
  platform = atmelavr
  board = attiny88

  ; change microcontroller
  board_build.mcu = attiny88

  ; change MCU frequency
  board_build.f_cpu = 8000000L

Debugging
---------
:ref:`piodebug` currently does not support Generic ATTiny88 board.

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences.