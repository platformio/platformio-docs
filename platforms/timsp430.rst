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

.. _platform_timsp430:

TI MSP430
=========
:ref:`projectconf_env_platform` = ``timsp430``

MSP430 microcontrollers (MCUs) from Texas Instruments (TI) are 16-bit, RISC-based, mixed-signal processors designed for ultra-low power. These MCUs offer the lowest power consumption and the perfect mix of integrated peripherals for thousands of applications.

For more detailed information please visit `vendor site <http://www.ti.com/lsds/ti/microcontrollers_16-bit_32-bit/msp/overview.page?utm_source=platformio&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are located in `TI MSP430 development platform repository <https://github.com/platformio/platform-timsp430/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_.


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
    * - ``lpmsp430f5529``
      - `TI LaunchPad MSP-EXP430F5529LP <http://www.ti.com/ww/en/launchpad/launchpads-msp430-msp-exp430f5529lp.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_mspdebug` (on-board)
      - MSP430F5529
      - 16 MHz
      - 128K
      - 8K
    * - ``lpmsp430fr4133``
      - `TI LaunchPad MSP-EXP430FR4133LP <http://www.ti.com/tool/msp-exp430fr4133?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_mspdebug` (on-board)
      - MSP430FR4133
      - 8 MHz
      - 15K
      - 2K
    * - ``lpmsp430fr5739``
      - `TI FraunchPad MSP-EXP430FR5739LP <http://www.ti.com/tool/msp-exp430fr5739?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_mspdebug` (on-board)
      - MSP430FR5739
      - 16 MHz
      - 16K
      - 512B
    * - ``lpmsp430fr5969``
      - `TI LaunchPad MSP-EXP430FR5969LP <http://www.ti.com/ww/en/launchpad/launchpads-msp430-msp-exp430fr5969.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_mspdebug` (on-board)
      - MSP430FR5969
      - 8 MHz
      - 64K
      - 2K
    * - ``lpmsp430fr6989``
      - `TI LaunchPad MSP-EXP430FR6989LP <http://www.ti.com/tool/msp-exp430fr6989?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_mspdebug` (on-board)
      - MSP430FR6989
      - 8 MHz
      - 127K
      - 2K
    * - ``lpmsp430g2553``
      - `TI LaunchPad MSP-EXP430G2553LP <http://www.ti.com/ww/en/launchpad/launchpads-msp430-msp-exp430g2.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`debugging_tool_mspdebug` (on-board)
      - MSP430G2553
      - 16 MHz
      - 16K
      - 512B


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-arduinomsp430 <http://arduino.cc/en/Reference/HomePage?utm_source=platformio&utm_medium=docs>`__
      - Arduino Wiring-based Framework (MSP430 Core)

    * - `framework-energiamsp430 <http://energia.nu/reference/?utm_source=platformio&utm_medium=docs>`__
      - Energia Wiring-based Framework (MSP430 Core)

    * - `tool-mspdebug <http://mspdebug.sourceforge.net/?utm_source=platformio&utm_medium=docs>`__
      - MSPDebug

    * - `toolchain-timsp430 <http://sourceforge.net/projects/mspgcc/?utm_source=platformio&utm_medium=docs>`__
      - msp-gcc

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

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences.

    * - :ref:`framework_energia`
      - Energia Wiring-based framework enables pretty much anyone to start easily creating microcontroller-based projects and applications. Its easy-to-use libraries and functions provide developers of all experience levels to start blinking LEDs, buzzing buzzers and sensing sensors more quickly than ever before.

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <http://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by
      horizontal.

PanStamp
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``panStampNRG``
      - `PanStamp NRG 1.1 <http://www.panstamp.com/product/197/?utm_source=platformio&utm_medium=docs>`_
      - No
      - CC430F5137
      - 12 MHz
      - 31.88K
      - 4K

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
    * - ``lpmsp430f5529``
      - `TI LaunchPad MSP-EXP430F5529LP <http://www.ti.com/ww/en/launchpad/launchpads-msp430-msp-exp430f5529lp.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - MSP430F5529
      - 16 MHz
      - 128K
      - 8K
    * - ``lpmsp430fr4133``
      - `TI LaunchPad MSP-EXP430FR4133LP <http://www.ti.com/tool/msp-exp430fr4133?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - MSP430FR4133
      - 8 MHz
      - 15K
      - 2K
    * - ``lpmsp430fr5739``
      - `TI FraunchPad MSP-EXP430FR5739LP <http://www.ti.com/tool/msp-exp430fr5739?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - MSP430FR5739
      - 16 MHz
      - 16K
      - 512B
    * - ``lpmsp430fr5969``
      - `TI LaunchPad MSP-EXP430FR5969LP <http://www.ti.com/ww/en/launchpad/launchpads-msp430-msp-exp430fr5969.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - MSP430FR5969
      - 8 MHz
      - 64K
      - 2K
    * - ``lpmsp430fr6989``
      - `TI LaunchPad MSP-EXP430FR6989LP <http://www.ti.com/tool/msp-exp430fr6989?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - MSP430FR6989
      - 8 MHz
      - 127K
      - 2K
    * - ``lpmsp430g2553``
      - `TI LaunchPad MSP-EXP430G2553LP <http://www.ti.com/ww/en/launchpad/launchpads-msp430-msp-exp430g2.html?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Yes <piodebug>`
      - MSP430G2553
      - 16 MHz
      - 16K
      - 512B
