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

.. _platform_asrmicro650x:

ASR Microelectronics ASR650x
============================

:Configuration:
  :ref:`projectconf_env_platform` = ``asrmicro650x``

ASR Microelectronics ASR650x series is highly intergrated and ultra low power SoC based on the PSoC 4000 series MCU (ARM Cortex M0+ Core) and Semtech SX1262 transceiver.

For more detailed information please visit `vendor site <http://www.asrmicro.com?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1

.. include:: asrmicro650x_extra.rst

Examples
--------

Examples are listed from `ASR Microelectronics ASR650x development platform repository <https://github.com/HelTecAutomation/platform-asrmicro650x/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `arduino-blink <https://github.com/HelTecAutomation/platform-asrmicro650x/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-rgb <https://github.com/HelTecAutomation/platform-asrmicro650x/tree/master/examples/arduino-rgb?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-adc <https://github.com/HelTecAutomation/platform-asrmicro650x/tree/master/examples/arduino-adc?utm_source=platformio.org&utm_medium=docs>`_
* `LoRa <https://github.com/HelTecAutomation/platform-asrmicro650x/tree/master/examples/LoRa?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-lowpower <https://github.com/HelTecAutomation/platform-asrmicro650x/tree/master/examples/arduino-lowpower?utm_source=platformio.org&utm_medium=docs>`_

Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/HelTecAutomation/platform-asrmicro650x/releases>`__
of ASR Microelectronics ASR650x development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = asrmicro650x
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = asrmicro650x@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/HelTecAutomation/platform-asrmicro650x.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-arduinoasrmicro650x <https://github.com/HelTecAutomation/ASR650x-Arduino.git?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for ASR Microelectronics ASR650x (Heltec core)

    * - `tool-cubecellelftool <https://github.com/HelTecAutomation/ASR650x-Arduino.git?utm_source=platformio.org&utm_medium=docs>`__
      - CubeCell ELF tool

    * - `tool-cubecellflash <https://github.com/HelTecAutomation/ASR650x-Arduino.git?utm_source=platformio.org&utm_medium=docs>`__
      - CubeCell Flash tool

    * - `toolchain-gccarmnoneeabi <https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm?utm_source=platformio.org&utm_medium=docs>`__
      - GNU toolchain for Arm Cortex-M and Cortex-R processors

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

Heltec
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_asrmicro650x_cubecell_capsule_solar_sensor`
      - No
      - ASR6502
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_asrmicro650x_cubecell_node`
      - No
      - ASR6502
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_asrmicro650x_cubecell_board`
      - No
      - ASR6501
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_asrmicro650x_cubecell_board_plus`
      - No
      - ASR6502
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_asrmicro650x_cubecell_capsule`
      - No
      - ASR6501
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_asrmicro650x_cubecell_gps`
      - No
      - ASR6502
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_asrmicro650x_cubecell_module`
      - No
      - ASR6501
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_asrmicro650x_cubecell_module_plus`
      - No
      - ASR6502
      - 48MHz
      - 128KB
      - 16KB
