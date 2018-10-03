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

Platform :ref:`platform_titiva`: Texas Instruments TM4C12x MCUs offer the industrys most popular ARM Cortex-M4 core with scalable memory and package options, unparalleled connectivity peripherals, advanced application functions, industry-leading analog integration, and extensive software solutions.

System
------

.. list-table::

  * - **Microcontroller**
    - LPLM4F120H5QR
  * - **Frequency**
    - 80Mhz
  * - **Flash**
    - 256KB
  * - **RAM**
    - 32KB
  * - **Vendor**
    - `TI <http://www.ti.com/tool/ek-lm4f120xl?utm_source=platformio&utm_medium=docs>`__


Configuration
-------------

Please use ``lplm4f120h5qr`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:lplm4f120h5qr]
  platform = titiva
  board = lplm4f120h5qr

You can override default TI LaunchPad (Stellaris) w/ lm4f120 (80MHz) settings per build environment using
``board_{JSON.PATH}`` option, where ``{JSON.PATH}`` is a path from
board manifest `lplm4f120h5qr.json <https://github.com/platformio/platform-titiva/blob/master/boards/lplm4f120h5qr.json>`_. For example,

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

    * - :ref:`framework_energia`
      - Energia Wiring-based framework enables pretty much anyone to start easily creating microcontroller-based projects and applications. Its easy-to-use libraries and functions provide developers of all experience levels to start blinking LEDs, buzzing buzzers and sensing sensors more quickly than ever before.

    * - :ref:`framework_libopencm3`
      - The libOpenCM3 framework aims to create a free/libre/open-source firmware library for various ARM Cortex-M0(+)/M3/M4 microcontrollers, including ST STM32, Ti Tiva and Stellaris, NXP LPC 11xx, 13xx, 15xx, 17xx parts, Atmel SAM3, Energy Micro EFM32 and others.