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

.. _platform_ststm8:

ST STM8
=======

:Configuration:
  :ref:`projectconf_env_platform` = ``ststm8``

The STM8 is an 8-bit microcontroller family by STMicroelectronics an extended variant of the ST7 microcontroller architecture. STM8 microcontrollers are particularly low cost for a full-featured 8-bit microcontroller.

For more detailed information please visit `vendor site <https://www.st.com/en/microcontrollers/stm8-8-bit-mcus.html?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `ST STM8 development platform repository <https://github.com/platformio/platform-ststm8/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `spl-blink <https://github.com/platformio/platform-ststm8/tree/master/examples/spl-blink?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-fade-all-pins <https://github.com/platformio/platform-ststm8/tree/master/examples/arduino-fade-all-pins?utm_source=platformio.org&utm_medium=docs>`_
* `spl-uart <https://github.com/platformio/platform-ststm8/tree/master/examples/spl-uart?utm_source=platformio.org&utm_medium=docs>`_
* `spl-flash <https://github.com/platformio/platform-ststm8/tree/master/examples/spl-flash?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-internal-lib <https://github.com/platformio/platform-ststm8/tree/master/examples/arduino-internal-lib?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-ping-hc04 <https://github.com/platformio/platform-ststm8/tree/master/examples/arduino-ping-hc04?utm_source=platformio.org&utm_medium=docs>`_

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
    * - :ref:`board_ststm8_stm8sdisco`
      - STM8S105C6T6
      - 16MHz
      - 32KB
      - 2KB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-ststm8/releases>`__
of ST STM8 development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = ststm8
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = ststm8@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-ststm8.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-arduinoststm8 <https://tenbaht.github.io/sduino/?utm_source=platformio.org&utm_medium=docs>`__
      - An Arduino-like programming API for the STM8 microcontrollers

    * - `framework-ststm8spl <https://www.st.com/en/embedded-software/stsw-stm8069.html?utm_source=platformio.org&utm_medium=docs>`__
      - Standard peripheral library for ST STM8S/A microcontrollers

    * - `tool-openocd <http://openocd.org?utm_source=platformio.org&utm_medium=docs>`__
      - Open On-Chip Debugger. Free and Open On-Chip Debugging, In-System Programming and Boundary-Scan Testing

    * - `tool-stm8binutils <https://stm8-binutils-gdb.sourceforge.io/?utm_source=platformio.org&utm_medium=docs>`__
      - STM8 toolchain with GDB debugger

    * - `tool-stm8tools <https://github.com/vdudouyt/stm8flash.git?utm_source=platformio.org&utm_medium=docs>`__
      - Upload tools for ST STM8 microcontrollers

    * - `toolchain-sdcc <http://sdcc.sourceforge.net?utm_source=platformio.org&utm_medium=docs>`__
      - Small Device C compiler suite

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

    * - :ref:`framework_spl`
      - The ST Standard Peripheral Library provides a set of functions for handling the peripherals on the STM32 family of microcontrollers.

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll the tables below by
      horizontally.

ST
~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm8_stm8sdisco`
      - On-board
      - STM8S105C6T6
      - 16MHz
      - 32KB
      - 2KB
    * - :ref:`board_ststm8_stm8sblue`
      - No
      - STM8S103F3P6
      - 16MHz
      - 8KB
      - 1KB
    * - :ref:`board_ststm8_stm8sblack`
      - No
      - STM8S105K4T6
      - 16MHz
      - 16KB
      - 2KB

sduino
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_ststm8_mb208`
      - No
      - STM8S208MBT6
      - 16MHz
      - 128KB
      - 6KB
    * - :ref:`board_ststm8_s8uno`
      - No
      - STM8S105K6T6
      - 16MHz
      - 32KB
      - 2KB
