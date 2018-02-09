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

.. _platform_titiva:

TI TIVA
=======
:ref:`projectconf_env_platform` = ``titiva``

Texas Instruments TM4C12x MCUs offer the industrys most popular ARM Cortex-M4 core with scalable memory and package options, unparalleled connectivity peripherals, advanced application functions, industry-leading analog integration, and extensive software solutions.

For more detailed information please visit `vendor site <http://www.ti.com/lsds/ti/microcontrollers_16-bit_32-bit/c2000_performance/control_automation/tm4c12x/overview.page?utm_source=platformio&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `TI TIVA development platform repository <https://github.com/platformio/platform-titiva/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_:

* `energia-blink <https://github.com/platformio/platform-titiva/tree/develop/examples/energia-blink?utm_source=platformio&utm_medium=docs>`_
* `energia-internal-libs <https://github.com/platformio/platform-titiva/tree/develop/examples/energia-internal-libs?utm_source=platformio&utm_medium=docs>`_
* `libopencm3-blink <https://github.com/platformio/platform-titiva/tree/develop/examples/libopencm3-blink?utm_source=platformio&utm_medium=docs>`_
* `native-blink <https://github.com/platformio/platform-titiva/tree/develop/examples/native-blink?utm_source=platformio&utm_medium=docs>`_

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

Supported debugging tools are listed in "Debug" column. For more detailed
information, please scroll table by horizontal.
You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` options.


On-Board tools
~~~~~~~~~~~~~~

Boards listed below have on-board debugging tools and **ARE READY** for debugging!
You do not need to use/buy external debugger.


.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``lplm4f120h5qr``
      - `TI LaunchPad (Stellaris) w/ lm4f120 (80MHz) <http://www.ti.com/tool/ek-lm4f120xl?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_ti-icdi` (on-board)
      - LPLM4F120H5QR
      - 80MHz
      - 256KB
      - 32KB
    * - ``lptm4c1230c3pm``
      - `TI LaunchPad (Tiva C) w/ tm4c123 (80MHz) <http://www.ti.com/ww/en/launchpad/launchpads-connected-ek-tm4c123gxl.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_ti-icdi` (on-board)
      - LPTM4C1230C3PM
      - 80MHz
      - 256KB
      - 32KB
    * - ``lptm4c1294ncpdt``
      - `TI LaunchPad (Tiva C) w/ tm4c129 (120MHz) <http://www.ti.com/ww/en/launchpad/launchpads-connected-ek-tm4c1294xl.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_ti-icdi` (on-board)
      - LPTM4C1294NCPDT
      - 120MHz
      - 1MB
      - 256KB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-titiva/releases>`__
of TI TIVA development platform and the latest upstream version using
:ref:`projectconf_env_platform` option as described below:

.. code-block:: ini

    ; Custom stable version
    [env:stable]
    platform =titiva@x.y.z
    board = ...
    ...

    ; The latest upstream/development version
    [env:upstream]
    platform = https://github.com/platformio/platform-titiva.git
    board = ...
    ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-energiativa <http://energia.nu/reference/?utm_source=platformio&utm_medium=docs>`__
      - Energia Wiring-based Framework (LM4F Core)

    * - `framework-libopencm3 <http://www.libopencm3.org/?utm_source=platformio&utm_medium=docs>`__
      - libOpenCM3 Framework

    * - `tool-lm4flash <http://www.ti.com/tool/lmflashprogrammer?utm_source=platformio&utm_medium=docs>`__
      - Flash Programmer

    * - `tool-openocd <http://openocd.org?utm_source=platformio&utm_medium=docs>`__
      - OpenOCD

    * - `toolchain-gccarmnoneeabi <https://launchpad.net/gcc-arm-embedded?utm_source=platformio&utm_medium=docs>`__
      - gcc-arm-embedded

.. warning::
    **Linux Users**:

        * Install "udev" rules file `99-platformio-udev.rules <https://github.com/platformio/platformio-core/blob/develop/scripts/99-platformio-udev.rules>`_
          (an instruction is located inside a file).
        * Raspberry Pi users, please read this article
          `Enable serial port on Raspberry Pi <https://hallard.me/enable-serial-port-on-raspberry-pi/>`__.


    **Windows Users:**

        Please check that you have a correctly installed USB driver from board
        manufacturer


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
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <http://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by
      horizontal.

TI
~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``lplm4f120h5qr``
      - `TI LaunchPad (Stellaris) w/ lm4f120 (80MHz) <http://www.ti.com/tool/ek-lm4f120xl?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - LPLM4F120H5QR
      - 80MHz
      - 256KB
      - 32KB
    * - ``lptm4c1230c3pm``
      - `TI LaunchPad (Tiva C) w/ tm4c123 (80MHz) <http://www.ti.com/ww/en/launchpad/launchpads-connected-ek-tm4c123gxl.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - LPTM4C1230C3PM
      - 80MHz
      - 256KB
      - 32KB
    * - ``lptm4c1294ncpdt``
      - `TI LaunchPad (Tiva C) w/ tm4c129 (120MHz) <http://www.ti.com/ww/en/launchpad/launchpads-connected-ek-tm4c1294xl.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - LPTM4C1294NCPDT
      - 120MHz
      - 1MB
      - 256KB
