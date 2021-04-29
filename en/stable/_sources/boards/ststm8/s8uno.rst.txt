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

.. _board_ststm8_s8uno:

sduino UNO (STM8S105K6)
=======================

.. contents::

Hardware
--------

Platform :ref:`platform_ststm8`: The STM8 is an 8-bit microcontroller family by STMicroelectronics an extended variant of the ST7 microcontroller architecture. STM8 microcontrollers are particularly low cost for a full-featured 8-bit microcontroller.

.. list-table::

  * - **Microcontroller**
    - STM8S105K6T6
  * - **Frequency**
    - 16MHz
  * - **Flash**
    - 32KB
  * - **RAM**
    - 2KB
  * - **Vendor**
    - `sduino <https://github.com/roybaer/sduino_uno?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``s8uno`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:s8uno]
  platform = ststm8
  board = s8uno

You can override default sduino UNO (STM8S105K6) settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `s8uno.json <https://github.com/platformio/platform-ststm8/blob/master/boards/s8uno.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:s8uno]
  platform = ststm8
  board = s8uno

  ; change microcontroller
  board_build.mcu = stm8s105k6t6

  ; change MCU frequency
  board_build.f_cpu = 16000000L


Uploading
---------
sduino UNO (STM8S105K6) supports the next uploading protocols:

* ``serial``
* ``stlinkv2``

Default protocol is ``serial``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:s8uno]
  platform = ststm8
  board = s8uno

  upload_protocol = serial

Debugging
---------
:ref:`piodebug` currently does not support sduino UNO (STM8S105K6) board.

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences

    * - :ref:`framework_spl`
      - The ST Standard Peripheral Library provides a set of functions for handling the peripherals on the STM32 family of microcontrollers.