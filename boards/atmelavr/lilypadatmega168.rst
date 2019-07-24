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

.. _board_atmelavr_lilypadatmega168:

Arduino LilyPad ATmega168
=========================

.. contents::

Hardware
--------

Platform :ref:`platform_atmelavr`: Atmel AVR 8- and 32-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industrys most code-efficient architecture for C and assembly programming.

.. list-table::

  * - **Microcontroller**
    - ATMEGA168
  * - **Frequency**
    - 8MHz
  * - **Flash**
    - 14KB
  * - **RAM**
    - 1KB
  * - **Vendor**
    - `Arduino <http://arduino.cc/en/Main/ArduinoBoardLilyPad?utm_source=platformio&utm_medium=docs>`__


Configuration
-------------

Please use ``lilypadatmega168`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:lilypadatmega168]
  platform = atmelavr
  board = lilypadatmega168

You can override default Arduino LilyPad ATmega168 settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `lilypadatmega168.json <https://github.com/platformio/platform-atmelavr/blob/master/boards/lilypadatmega168.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:lilypadatmega168]
  platform = atmelavr
  board = lilypadatmega168

  ; change microcontroller
  board_build.mcu = atmega168

  ; change MCU frequency
  board_build.f_cpu = 8000000L

Debugging
---------
:ref:`piodebug` currently does not support Arduino LilyPad ATmega168 board.

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences.