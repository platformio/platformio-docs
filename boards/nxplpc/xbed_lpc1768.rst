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

.. _board_nxplpc_xbed_lpc1768:

Smeshlink xbed LPC1768
======================

.. contents::

Hardware
--------

Platform :ref:`platform_nxplpc`: The NXP LPC is a family of 32-bit microcontroller integrated circuits by NXP Semiconductors. The LPC chips are grouped into related series that are based around the same 32-bit ARM processor core, such as the Cortex-M4F, Cortex-M3, Cortex-M0+, or Cortex-M0. Internally, each microcontroller consists of the processor core, static RAM memory, flash memory, debugging interface, and various peripherals.

.. list-table::

  * - **Microcontroller**
    - LPC1768
  * - **Frequency**
    - 96MHz
  * - **Flash**
    - 512KB
  * - **RAM**
    - 32KB
  * - **Vendor**
    - `Smeshlink <https://developer.mbed.org/platforms/xbed-LPC1768/?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``xbed_lpc1768`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:xbed_lpc1768]
  platform = nxplpc
  board = xbed_lpc1768

You can override default Smeshlink xbed LPC1768 settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `xbed_lpc1768.json <https://github.com/platformio/platform-nxplpc/blob/master/boards/xbed_lpc1768.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:xbed_lpc1768]
  platform = nxplpc
  board = xbed_lpc1768

  ; change microcontroller
  board_build.mcu = lpc1768

  ; change MCU frequency
  board_build.f_cpu = 96000000L

Debugging
---------
:ref:`piodebug` currently does not support Smeshlink xbed LPC1768 board.

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_mbed`
      - Arm Mbed OS is an open source embedded operating system designed specifically for the 'things' in the Internet of Things. It includes all the features you need to develop a connected product based on an Arm Cortex-M microcontroller, including security, connectivity, an RTOS and drivers for sensors and I/O devices