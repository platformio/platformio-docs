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

.. _board_asrmicro650x_cubecell_module:

Heltec CubeCell-Module (HTCC-AM01)
==================================

.. contents::

Hardware
--------

Platform :ref:`platform_asrmicro650x`: ASR Microelectronics ASR650x series is highly intergrated and ultra low power SoC based on the PSoC 4000 series MCU (ARM Cortex M0+ Core) and Semtech SX1262 transceiver.

.. list-table::

  * - **Microcontroller**
    - ASR6501
  * - **Frequency**
    - 48MHz
  * - **Flash**
    - 128KB
  * - **RAM**
    - 16KB
  * - **Vendor**
    - `Heltec <https://heltec.org/project/htcc-am01/?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``cubecell_module`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:cubecell_module]
  platform = asrmicro650x
  board = cubecell_module

You can override default Heltec CubeCell-Module (HTCC-AM01) settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `cubecell_module.json <https://github.com/HelTecAutomation/platform-asrmicro650x/blob/master/boards/cubecell_module.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:cubecell_module]
  platform = asrmicro650x
  board = cubecell_module

  ; change microcontroller
  board_build.mcu = asr6501

  ; change MCU frequency
  board_build.f_cpu = 48000000L

Debugging
---------
:ref:`piodebug` currently does not support Heltec CubeCell-Module (HTCC-AM01) board.

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences