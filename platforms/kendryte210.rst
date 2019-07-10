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

.. _platform_kendryte210:

Kendryte K210
=============

:Configuration:
  :ref:`projectconf_env_platform` = ``kendryte210``

Kendryte K210 is an AI capable RISCV64 dual core SoC, this platform is ported by Sipeed.

For more detailed information please visit `vendor site <http://www.sipeed.com?utm_source=platformio&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `Kendryte K210 development platform repository <https://github.com/sipeed/platform-kendryte210/tree/master/examples?utm_source=platformio&utm_medium=docs>`_:

* `arduino-blink <https://github.com/sipeed/platform-kendryte210/tree/master/examples/arduino-blink?utm_source=platformio&utm_medium=docs>`_
* `kendryte-standalone-sdk_hello <https://github.com/sipeed/platform-kendryte210/tree/master/examples/kendryte-standalone-sdk_hello?utm_source=platformio&utm_medium=docs>`_

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
    * - :ref:`board_kendryte210_sipeed-maix-bit`
      - K210
      - 400MHz
      - 16MB
      - 6MB
    * - :ref:`board_kendryte210_sipeed-maix-go`
      - K210
      - 400MHz
      - 16MB
      - 6MB
    * - :ref:`board_kendryte210_sipeed-maix-one`
      - K210
      - 400MHz
      - 16MB
      - 6MB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/sipeed/platform-kendryte210/releases>`__
of Kendryte K210 development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = kendryte210
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = kendryte210@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/sipeed/platform-kendryte210.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-kendryte-standalone-sdk <https://github.com/kendryte/kendryte-standalone-sdk?utm_source=platformio&utm_medium=docs>`__
      - This SDK is for Kendryte K210 without OS support

    * - `framework-maixduino <https://github.com/sipeed/Maixduino?utm_source=platformio&utm_medium=docs>`__
      - Arduino Wiring-based Framework (K210 Core)

    * - `tool-kflash-kendryte210 <https://github.com/kendryte/kflash.py?utm_source=platformio&utm_medium=docs>`__
      - kflash, A Python-based Kendryte K210 UART ISP Utility

    * - `tool-openocd-kendryte210 <https://github.com/kendryte/openocd-kendryte?utm_source=platformio&utm_medium=docs>`__
      - OpenOCD for RISC-V kendryte 210

    * - `toolchain-kendryte210 <https://github.com/kendryte/kendryte-gnu-toolchain?utm_source=platformio&utm_medium=docs>`__
      - RISC-V GCC toolchain for Kendryte 210

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
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences.

    * - :ref:`framework_kendryte-standalone-sdk`
      - Kendryte Standalone SDK without OS support

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by
      horizontal.

Sipeed
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_kendryte210_sipeed-maix-bit`
      - On-board
      - K210
      - 400MHz
      - 16MB
      - 6MB
    * - :ref:`board_kendryte210_sipeed-maix-go`
      - On-board
      - K210
      - 400MHz
      - 16MB
      - 6MB
    * - :ref:`board_kendryte210_sipeed-maix-one`
      - On-board
      - K210
      - 400MHz
      - 16MB
      - 6MB
