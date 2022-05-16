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

.. _board_intel_mcs51_STC8F2K60S4:

Generic STC8F2K60S4
===================

.. contents::

Hardware
--------

Platform :ref:`platform_intel_mcs51`: The Intel MCS-51 (commonly termed 8051) is an internally Harvard architecture, complex instruction set computer (CISC) instruction set, single chip microcontroller (uC) series developed by Intel in 1980 for use in embedded systems.

.. list-table::

  * - **Microcontroller**
    - STC8F2K60S4
  * - **Frequency**
    - 11MHz
  * - **Flash**
    - 60KB
  * - **RAM**
    - 2.25KB
  * - **Vendor**
    - `STC <http://www.stcmicro.com/STC/STC8F2K64S4.html?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``STC8F2K60S4`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:STC8F2K60S4]
  platform = intel_mcs51
  board = STC8F2K60S4

You can override default Generic STC8F2K60S4 settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `STC8F2K60S4.json <https://github.com/platformio/platform-intel_mcs51/blob/master/boards/STC8F2K60S4.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:STC8F2K60S4]
  platform = intel_mcs51
  board = STC8F2K60S4

  ; change microcontroller
  board_build.mcu = stc8f2k60s4

  ; change MCU frequency
  board_build.f_cpu = 11059200L

Debugging
---------
:ref:`piodebug` currently does not support Generic STC8F2K60S4 board.