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

.. _board_nxplpc_mbuino:

Outrageous Circuits mBuino
==========================

.. contents::
    :local:

Platform :ref:`platform_nxplpc`: The NXP LPC is a family of 32-bit microcontroller integrated circuits by NXP Semiconductors. The LPC chips are grouped into related series that are based around the same 32-bit ARM processor core, such as the Cortex-M4F, Cortex-M3, Cortex-M0+, or Cortex-M0. Internally, each microcontroller consists of the processor core, static RAM memory, flash memory, debugging interface, and various peripherals.

System
------

.. list-table::

  * - **Microcontroller**
    - LPC11U24
  * - **Frequency**
    - 48Mhz
  * - **Flash**
    - 32KB
  * - **RAM**
    - 8KB
  * - **Vendor**
    - `Outrageous Circuits <https://developer.mbed.org/platforms/Outrageous-Circuits-mBuino/?utm_source=platformio&utm_medium=docs>`__


Configuration
-------------

Please use ``mbuino`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:mbuino]
  platform = nxplpc
  board = mbuino

You can override default Outrageous Circuits mBuino settings per build environment using
``board_{JSON.PATH}`` option, where ``{JSON.PATH}`` is a path from
board manifest `mbuino.json <https://github.com/platformio/platform-nxplpc/blob/master/boards/mbuino.json>`_. For example,

.. code-block:: ini

  [env:mbuino]
  platform = nxplpc
  board = mbuino

  ; change microcontroller
  board_build.mcu = lpc11u24

  ; change MCU frequency
  board_build.f_cpu = 48000000L

Debugging
---------
:ref:`piodebug` currently does not support Outrageous Circuits mBuino board.

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_mbed`
      - The mbed framework The mbed SDK has been designed to provide enough hardware abstraction to be intuitive and concise, yet powerful enough to build complex projects. It is built on the low-level ARM CMSIS APIs, allowing you to code down to the metal if needed. In addition to RTOS, USB and Networking libraries, a cookbook of hundreds of reusable peripheral and module libraries have been built on top of the SDK by the mbed Developer Community.