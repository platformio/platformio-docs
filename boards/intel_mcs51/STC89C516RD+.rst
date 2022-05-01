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

.. _board_intel_mcs51_STC89C516RD+:

Generic STC89C516RD+
====================

.. contents::

Hardware
--------

Platform :ref:`platform_intel_mcs51`: The Intel MCS-51 (commonly termed 8051) is an internally Harvard architecture, complex instruction set computer (CISC) instruction set, single chip microcontroller (uC) series developed by Intel in 1980 for use in embedded systems.

.. list-table::

  * - **Microcontroller**
    - STC89C516RD+
  * - **Frequency**
    - 11MHz
  * - **Flash**
    - 64KB
  * - **RAM**
    - 1.25KB
  * - **Vendor**
    - `STC <https://www.stcmicro.com/STC/STC89C52RC.html?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``STC89C516RD+`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:STC89C516RD+]
  platform = intel_mcs51
  board = STC89C516RD+

You can override default Generic STC89C516RD+ settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `STC89C516RD+.json <https://github.com/platformio/platform-intel_mcs51/blob/master/boards/STC89C516RD+.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:STC89C516RD+]
  platform = intel_mcs51
  board = STC89C516RD+

  ; change microcontroller
  board_build.mcu = stc89c516rd+

  ; change MCU frequency
  board_build.f_cpu = 11059200L

Debugging
---------
:ref:`piodebug` currently does not support Generic STC89C516RD+ board.