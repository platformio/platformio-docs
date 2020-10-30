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

:Configuration:
  :ref:`projectconf_env_platform` = ``timsp430``

MSP430 microcontrollers (MCUs) from Texas Instruments (TI) are 16-bit, RISC-based, mixed-signal processors designed for ultra-low power. These MCUs offer the lowest power consumption and the perfect mix of integrated peripherals for thousands of applications.

For more detailed information please visit `vendor site <http://www.ti.com/lsds/ti/microcontrollers_16-bit_32-bit/msp/overview.page?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `TI MSP430 development platform repository <https://github.com/platformio/platform-timsp430/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `arduino-blink <https://github.com/platformio/platform-timsp430/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs>`_
* `native-blink <https://github.com/platformio/platform-timsp430/tree/master/examples/native-blink?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-internal-libs <https://github.com/platformio/platform-timsp430/tree/master/examples/arduino-internal-libs?utm_source=platformio.org&utm_medium=docs>`_

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. contents::
    :local:


Tools & Debug Probes
~~~~~~~~~~~~~~~~~~~~

Supported debugging tools are listed in "Debug" column. For more detailed
information, please scroll table by horizontal.
You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` option in :ref:`projectconf`.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further instructions.


On-Board Debug Tools
^^^^^^^^^^^^^^^^^^^^

Boards listed below have on-board debug probe and **ARE READY** for debugging!
You do not need to use/buy external debug probe.


.. list-table::
    :header-rows:  1

    * - Name
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_timsp430_lpmsp430fr5739`
      - MSP430FR5739
      - 16MHz
      - 15.37KB
      - 1KB
    * - :ref:`board_timsp430_lpmsp430f5529`
      - MSP430F5529
      - 25MHz
      - 47KB
      - 8KB
    * - :ref:`board_timsp430_lpmsp430fr2311`
      - MSP430FR2311
      - 16MHz
      - 3.75KB
      - 1KB
    * - :ref:`board_timsp430_lpmsp430fr2433`
      - MSP430FR2433
      - 8MHz
      - 15KB
      - 4KB
    * - :ref:`board_timsp430_lpmsp430fr4133`
      - MSP430FR4133
      - 8MHz
      - 15KB
      - 2KB
    * - :ref:`board_timsp430_lpmsp430fr5969`
      - MSP430FR5969
      - 8MHz
      - 47KB
      - 2KB
    * - :ref:`board_timsp430_lpmsp430fr5994`
      - MSP430FR5994
      - 16MHz
      - 256KB
      - 4KB
    * - :ref:`board_timsp430_lpmsp430fr6989`
      - MSP430FR6989
      - 8MHz
      - 47KB
      - 2KB
    * - :ref:`board_timsp430_lpmsp430g2231`
      - MSP430G2231
      - 1MHz
      - 2KB
      - 256B
    * - :ref:`board_timsp430_lpmsp430g2452`
      - MSP430G2452
      - 16MHz
      - 8KB
      - 256B
    * - :ref:`board_timsp430_lpmsp430g2553`
      - MSP430G2553
      - 16MHz
      - 16KB
      - 512B


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-timsp430/releases>`__
of TI MSP430 development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = timsp430
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = timsp430@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-timsp430.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-energiamsp430 <http://energia.nu/reference/?utm_source=platformio.org&utm_medium=docs>`__
      - Energia Wiring-based Framework for Texas Instruments MSP430 microcontrollers

    * - `tool-dslite <http://www.ti.com/tool/UNIFLASH?utm_source=platformio.org&utm_medium=docs>`__
      - Texas Instruments DSLite (UniFlash)

    * - `tool-mspdebug <https://dlbeer.co.nz/mspdebug/?utm_source=platformio.org&utm_medium=docs>`__
      - MSPDebug is a free debugger for use with MSP430 MCUs

    * - `toolchain-timsp430 <https://sourceforge.net/projects/mspgcc/?utm_source=platformio.org&utm_medium=docs>`__
      - A port of the GNU C Compiler (GCC) and GNU Binutils (as, ld) for the embedded processor MSP430

.. warning::
    **Linux Users**:

        * Install "udev" rules :ref:`faq_udev_rules`
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
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll the tables below by
      horizontally.

TI
~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_timsp430_lpmsp430fr5739`
      - On-board
      - MSP430FR5739
      - 16MHz
      - 15.37KB
      - 1KB
    * - :ref:`board_timsp430_lpmsp430f5529`
      - On-board
      - MSP430F5529
      - 25MHz
      - 47KB
      - 8KB
    * - :ref:`board_timsp430_lpmsp430fr2311`
      - On-board
      - MSP430FR2311
      - 16MHz
      - 3.75KB
      - 1KB
    * - :ref:`board_timsp430_lpmsp430fr2433`
      - On-board
      - MSP430FR2433
      - 8MHz
      - 15KB
      - 4KB
    * - :ref:`board_timsp430_lpmsp430fr4133`
      - On-board
      - MSP430FR4133
      - 8MHz
      - 15KB
      - 2KB
    * - :ref:`board_timsp430_lpmsp430fr5969`
      - On-board
      - MSP430FR5969
      - 8MHz
      - 47KB
      - 2KB
    * - :ref:`board_timsp430_lpmsp430fr5994`
      - On-board
      - MSP430FR5994
      - 16MHz
      - 256KB
      - 4KB
    * - :ref:`board_timsp430_lpmsp430fr6989`
      - On-board
      - MSP430FR6989
      - 8MHz
      - 47KB
      - 2KB
    * - :ref:`board_timsp430_lpmsp430g2231`
      - On-board
      - MSP430G2231
      - 1MHz
      - 2KB
      - 256B
    * - :ref:`board_timsp430_lpmsp430g2452`
      - On-board
      - MSP430G2452
      - 16MHz
      - 8KB
      - 256B
    * - :ref:`board_timsp430_lpmsp430g2553`
      - On-board
      - MSP430G2553
      - 16MHz
      - 16KB
      - 512B
