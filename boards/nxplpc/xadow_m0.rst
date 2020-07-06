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

.. _board_nxplpc_xadow_m0:

Seeed Xadow M0
==============

.. contents::

Hardware
--------

Platform :ref:`platform_nxplpc`: The NXP LPC is a family of 32-bit microcontroller integrated circuits by NXP Semiconductors. The LPC chips are grouped into related series that are based around the same 32-bit ARM processor core, such as the Cortex-M4F, Cortex-M3, Cortex-M0+, or Cortex-M0. Internally, each microcontroller consists of the processor core, static RAM memory, flash memory, debugging interface, and various peripherals.

.. list-table::

  * - **Microcontroller**
    - LPC11U35
  * - **Frequency**
    - 48MHz
  * - **Flash**
    - 64KB
  * - **RAM**
    - 10KB
  * - **Vendor**
    - `SeeedStudio <https://developer.mbed.org/platforms/Seeed-Xadow-M0/?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``xadow_m0`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:xadow_m0]
  platform = nxplpc
  board = xadow_m0

You can override default Seeed Xadow M0 settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `xadow_m0.json <https://github.com/platformio/platform-nxplpc/blob/master/boards/xadow_m0.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:xadow_m0]
  platform = nxplpc
  board = xadow_m0

  ; change microcontroller
  board_build.mcu = lpc11u35

  ; change MCU frequency
  board_build.f_cpu = 48000000L

Debugging
---------
:ref:`piodebug` currently does not support Seeed Xadow M0 board.

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_mbed`
      - Arm Mbed OS is an open source embedded operating system designed specifically for the 'things' in the Internet of Things. It includes all the features you need to develop a connected product based on an Arm Cortex-M microcontroller, including security, connectivity, an RTOS and drivers for sensors and I/O devices