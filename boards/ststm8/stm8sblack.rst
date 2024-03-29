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

.. _board_ststm8_stm8sblack:

ST STM8S105K4T6 Breakout Board
==============================

.. contents::

Hardware
--------

Platform :ref:`platform_ststm8`: The STM8 is an 8-bit microcontroller family by STMicroelectronics an extended variant of the ST7 microcontroller architecture. STM8 microcontrollers are particularly low cost for a full-featured 8-bit microcontroller.

.. list-table::

  * - **Microcontroller**
    - STM8S105K4T6
  * - **Frequency**
    - 16MHz
  * - **Flash**
    - 16KB
  * - **RAM**
    - 2KB
  * - **Vendor**
    - `ST <https://github.com/TG9541/stm8ef/wiki/Breakout-Boards?utm_source=platformio.org&utm_medium=docs#stm8s105k4t6-breakout-board>`__


Configuration
-------------

Please use ``stm8sblack`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:stm8sblack]
  platform = ststm8
  board = stm8sblack

You can override default ST STM8S105K4T6 Breakout Board settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `stm8sblack.json <https://github.com/platformio/platform-ststm8/blob/master/boards/stm8sblack.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:stm8sblack]
  platform = ststm8
  board = stm8sblack

  ; change microcontroller
  board_build.mcu = stm8s105k4t6

  ; change MCU frequency
  board_build.f_cpu = 16000000L


Uploading
---------
ST STM8S105K4T6 Breakout Board supports the following uploading protocols:

* ``serial``
* ``stlinkv2``

Default protocol is ``serial``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:stm8sblack]
  platform = ststm8
  board = stm8sblack

  upload_protocol = serial

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further
    instructions and configuration information.

You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` option in :ref:`projectconf`.

ST STM8S105K4T6 Breakout Board does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_stlink`
    - 
    - Yes

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences.

    * - :ref:`framework_spl`
      - Standard Peripheral Library for ST STM32 microcontrollers