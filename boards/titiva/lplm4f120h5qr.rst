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

.. _board_titiva_lplm4f120h5qr:

TI LaunchPad (Stellaris) w/ lm4f120 (80MHz)
===========================================

.. contents::

Hardware
--------

Platform :ref:`platform_titiva`: Texas Instruments TM4C12x MCUs offer the industrys most popular ARM Cortex-M4 core with scalable memory and package options, unparalleled connectivity peripherals, advanced application functions, industry-leading analog integration, and extensive software solutions.

.. list-table::

  * - **Microcontroller**
    - LPLM4F120H5QR
  * - **Frequency**
    - 80MHz
  * - **Flash**
    - 256KB
  * - **RAM**
    - 32KB
  * - **Vendor**
    - `TI <http://www.ti.com/tool/ek-lm4f120xl?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``lplm4f120h5qr`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:lplm4f120h5qr]
  platform = titiva
  board = lplm4f120h5qr

You can override default TI LaunchPad (Stellaris) w/ lm4f120 (80MHz) settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `lplm4f120h5qr.json <https://github.com/platformio/platform-titiva/blob/master/boards/lplm4f120h5qr.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:lplm4f120h5qr]
  platform = titiva
  board = lplm4f120h5qr

  ; change microcontroller
  board_build.mcu = lplm4f120h5qr

  ; change MCU frequency
  board_build.f_cpu = 80000000L

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further
    instructions and configuration information.

You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` option in :ref:`projectconf`.

TI LaunchPad (Stellaris) w/ lm4f120 (80MHz) has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_ti-icdi`
    - Yes
    - Yes

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences

    * - :ref:`framework_libopencm3`
      - The libOpenCM3 framework aims to create a free and open-source firmware library for various ARM Cortex-M0(+)/M3/M4 microcontrollers, including ST STM32, Ti Tiva and Stellaris, NXP LPC, Atmel SAM3, Energy Micro EFM32 and others