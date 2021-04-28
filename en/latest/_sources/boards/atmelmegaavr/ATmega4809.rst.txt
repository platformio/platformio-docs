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

.. _board_atmelmegaavr_ATmega4809:

ATmega4809
==========

.. contents::

Hardware
--------

Platform :ref:`platform_atmelmegaavr`: 8-bit MCUs Built for Real-time Control with Core Independent Peripherals combining intelligent hardware peripherals along with the low-power capability of an AVR core, megaAVR microcontrollers (MCUs) broaden the effectiveness of your real-time control systems.

.. list-table::

  * - **Microcontroller**
    - ATMEGA4809
  * - **Frequency**
    - 16MHz
  * - **Flash**
    - 48KB
  * - **RAM**
    - 6KB
  * - **Vendor**
    - `Microchip <https://www.microchip.com/wwwproducts/en/ATMEGA4809?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``ATmega4809`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:ATmega4809]
  platform = atmelmegaavr
  board = ATmega4809

You can override default ATmega4809 settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `ATmega4809.json <https://github.com/platformio/platform-atmelmegaavr/blob/master/boards/ATmega4809.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:ATmega4809]
  platform = atmelmegaavr
  board = ATmega4809

  ; change microcontroller
  board_build.mcu = atmega4809

  ; change MCU frequency
  board_build.f_cpu = 16000000L

Debugging
---------
:ref:`piodebug` currently does not support ATmega4809 board.

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences