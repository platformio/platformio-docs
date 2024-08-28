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

.. _platform_heltec-cubecell:

Heltec CubeCell
===============

:Registry:
  `https://registry.platformio.org/platforms/heltecautomation/heltec-cubecell <https://registry.platformio.org/platforms/heltecautomation/heltec-cubecell>`__
:Configuration:
  :ref:`projectconf_env_platform` = ``heltecautomation/heltec-cubecell``

Heltec CubeCell is an easy-to-use LoRa Node series brand based on a highly integrated and ultra low power SoC and the LoRa SX1262 transceiver.

For more detailed information please visit `vendor site <https://heltec.org/?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1

.. include:: heltec-cubecell_extra.rst

Examples
--------

Examples are listed from `Heltec CubeCell development platform repository <https://github.com/HelTecAutomation/platform-heltec-cubecell/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `arduino-blink <https://github.com/HelTecAutomation/platform-heltec-cubecell/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-rgb <https://github.com/HelTecAutomation/platform-heltec-cubecell/tree/master/examples/arduino-rgb?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-adc <https://github.com/HelTecAutomation/platform-heltec-cubecell/tree/master/examples/arduino-adc?utm_source=platformio.org&utm_medium=docs>`_
* `LoRa <https://github.com/HelTecAutomation/platform-heltec-cubecell/tree/master/examples/LoRa?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-lowpower <https://github.com/HelTecAutomation/platform-heltec-cubecell/tree/master/examples/arduino-lowpower?utm_source=platformio.org&utm_medium=docs>`_

Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/HelTecAutomation/platform-heltec-cubecell/releases>`__
of Heltec CubeCell development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version, NOT recommended
    ; Pin the version as shown below
    [env:latest_stable]
    platform = heltec-cubecell
    board = ...

    ; Specific version
    [env:custom_stable]
    platform = heltec-cubecell@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/HelTecAutomation/platform-heltec-cubecell.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-arduinocubecell <https://registry.platformio.org/tools/heltecautomation/framework-arduinocubecell>`__
      - Arduino Wiring-based Framework for Heltec CubeCell

    * - `tool-cubecellelftool <https://registry.platformio.org/tools/heltecautomation/tool-cubecellelftool>`__
      - CubeCell ELF tool

    * - `tool-cubecellflash <https://registry.platformio.org/tools/heltecautomation/tool-cubecellflash>`__
      - CubeCell Flash tool

    * - `tool-cubecellflash6601 <https://registry.platformio.org/tools/heltecautomation/tool-cubecellflash6601>`__
      - CubeCell Flash tool for ASR6601

    * - `toolchain-gccarmnoneeabi <https://registry.platformio.org/tools/platformio/toolchain-gccarmnoneeabi>`__
      - GNU toolchain for Arm Cortex-M and Cortex-R processors

.. warning::
    **Linux Users**:

        * Install "udev" rules :ref:`platformio_udev_rules`
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

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command
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
    * - :ref:`board_heltec-cubecell_cubecell_capsule_solar_sensor`
      - No
      - ASR6051
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_heltec-cubecell_cubecell_node`
      - No
      - ASR6502
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_heltec-cubecell_cubecell_board`
      - No
      - ASR6501
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_heltec-cubecell_cubecell_board_pro`
      - No
      - ASR6601
      - 48MHz
      - 224KB
      - 224KB
    * - :ref:`board_heltec-cubecell_cubecell_board_plus`
      - No
      - ASR6502
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_heltec-cubecell_cubecell_board_v2`
      - No
      - ASR6501
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_heltec-cubecell_cubecell_capsule`
      - No
      - ASR6501
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_heltec-cubecell_cubecell_gps`
      - No
      - ASR6502
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_heltec-cubecell_cubecell_module`
      - No
      - ASR6501
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_heltec-cubecell_cubecell_module_plus`
      - No
      - ASR6502
      - 48MHz
      - 128KB
      - 16KB
    * - :ref:`board_heltec-cubecell_cubecell_module_v2`
      - No
      - ASR6501
      - 48MHz
      - 128KB
      - 16KB
