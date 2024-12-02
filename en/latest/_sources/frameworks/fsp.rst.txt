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

.. _framework_fsp:

Renesas Flexible Software Package
=================================

:Configuration:
  :ref:`projectconf_env_framework` = ``fsp``

The Renesas Flexible Software Package (FSP) is an enhanced software package designed to provide easy-to-use, scalable, high-quality software for embedded system designs using Renesas RA family of Arm Microcontrollers.

.. contents:: Contents
    :local:
    :depth: 1

Platforms
---------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`platform_renesas-ra`
      - Renesas Advanced (RA) 32-bit microcontrollers with the Arm Cortex-M33, -M23 and -M4 processor cores deliver key advantages compared to competitive Arm Cortex-M MCUs by providing stronger embedded security, superior CoreMark performance and ultra-low power operation.

Examples
--------

* `Renesas Flexible Software Package for Renesas RA <https://github.com/platformio/platform-renesas-ra/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_

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
      - Platform
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_renesas-ra_uno_r4_wifi`
      - :ref:`platform_renesas-ra`
      - RA4M1
      - 48MHz
      - 256KB
      - 32KB


External Debug Tools
^^^^^^^^^^^^^^^^^^^^

Boards listed below are compatible with :ref:`piodebug` but **DEPEND ON**
external debug probe. They **ARE NOT READY** for debugging.
Please click on board name for the further details.


.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_renesas-ra_portenta_c33`
      - :ref:`platform_renesas-ra`
      - R7FA6M5BH2CBG
      - 200MHz
      - 2MB
      - 511.35KB
    * - :ref:`board_renesas-ra_uno_r4_minima`
      - :ref:`platform_renesas-ra`
      - RA4M1
      - 48MHz
      - 256KB
      - 32KB


Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command
    * For more detailed ``board`` information please scroll the tables below by horizontally.

Arduino
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_renesas-ra_portenta_c33`
      - :ref:`platform_renesas-ra`
      - External
      - R7FA6M5BH2CBG
      - 200MHz
      - 2MB
      - 511.35KB
    * - :ref:`board_renesas-ra_uno_r4_minima`
      - :ref:`platform_renesas-ra`
      - External
      - RA4M1
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_renesas-ra_uno_r4_wifi`
      - :ref:`platform_renesas-ra`
      - On-board
      - RA4M1
      - 48MHz
      - 256KB
      - 32KB
