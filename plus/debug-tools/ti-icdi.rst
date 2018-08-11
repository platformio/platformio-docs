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

.. _debugging_tool_ti-icdi:

TI-ICDI
=======

:Configuration:
  :ref:`projectconf_debug_tool` = ``ti-icdi``

Tiva™ C Series evaluation and reference design kits provide an integrated
In-Circuit Debug Interface (ICDI) which allows programming and debugging of
the onboard C Series microcontroller.
`Vendor information... <http://www.ti.com/tool/stellaris_icdi_drivers?utm_source=platformio&utm_medium=docs>`__

.. contents:: Contents
    :local:
    :depth: 1

Drivers
-------

:Windows:
  Please "USB Driver Installation" guide for your board.

:Mac:
  Not required.

:Linux:
  Please install "udev" rules :ref:`faq_udev_rules`. If you already installed
  them before, please check that your rules are up-to-date or repeat steps.

.. begin_platforms

Platforms
---------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`platform_titiva`
      - Texas Instruments TM4C12x MCUs offer the industrys most popular ARM Cortex-M4 core with scalable memory and package options, unparalleled connectivity peripherals, advanced application functions, industry-leading analog integration, and extensive software solutions.

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

Boards
------

.. note::
    For more detailed ``board`` information please scroll tables below by horizontal.


.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``lplm4f120h5qr``
      - `TI LaunchPad (Stellaris) w/ lm4f120 (80MHz) <http://www.ti.com/tool/ek-lm4f120xl?utm_source=platformio&utm_medium=docs>`_
      - :ref:`TI TIVA <platform_titiva>`
      - :ref:`debugging_tool_ti-icdi` (on-board)
      - LPLM4F120H5QR
      - 80MHz
      - 256KB
      - 32KB
    * - ``lptm4c1230c3pm``
      - `TI LaunchPad (Tiva C) w/ tm4c123 (80MHz) <http://www.ti.com/ww/en/launchpad/launchpads-connected-ek-tm4c123gxl.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`TI TIVA <platform_titiva>`
      - :ref:`debugging_tool_ti-icdi` (on-board)
      - LPTM4C1230C3PM
      - 80MHz
      - 256KB
      - 32KB
    * - ``lptm4c1294ncpdt``
      - `TI LaunchPad (Tiva C) w/ tm4c129 (120MHz) <http://www.ti.com/ww/en/launchpad/launchpads-connected-ek-tm4c1294xl.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`TI TIVA <platform_titiva>`
      - :ref:`debugging_tool_ti-icdi` (on-board)
      - LPTM4C1294NCPDT
      - 120MHz
      - 1MB
      - 256KB
