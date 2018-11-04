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

.. _board_atmelavr_reprap_rambo:

RepRap RAMBo
============

.. contents::

Hardware
--------

Platform :ref:`platform_atmelavr`: Atmel AVR 8- and 32-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industrys most code-efficient architecture for C and assembly programming.

.. list-table::

  * - **Microcontroller**
    - ATMEGA2560
  * - **Frequency**
    - 16MHz
  * - **Flash**
    - 252KB
  * - **RAM**
    - 8KB
  * - **Vendor**
    - `RepRap <http://reprap.org/wiki/Rambo?utm_source=platformio&utm_medium=docs>`__


Configuration
-------------

Please use ``reprap_rambo`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:reprap_rambo]
  platform = atmelavr
  board = reprap_rambo

You can override default RepRap RAMBo settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `reprap_rambo.json <https://github.com/platformio/platform-atmelavr/blob/master/boards/reprap_rambo.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:reprap_rambo]
  platform = atmelavr
  board = reprap_rambo

  ; change microcontroller
  board_build.mcu = atmega2560

  ; change MCU frequency
  board_build.f_cpu = 16000000L

Debugging
---------
:ref:`piodebug` currently does not support RepRap RAMBo board.

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences.