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

.. _board_intel_mcs51_MS51TC0AE:

Generic MS51TC0AE
=================

.. contents::

Hardware
--------

Platform :ref:`platform_intel_mcs51`: The Intel MCS-51 (commonly termed 8051) is an internally Harvard architecture, complex instruction set computer (CISC) instruction set, single chip microcontroller (uC) series developed by Intel in 1980 for use in embedded systems.

.. list-table::

  * - **Microcontroller**
    - MS51TC0AE
  * - **Frequency**
    - 16MHz
  * - **Flash**
    - 32KB
  * - **RAM**
    - 2.25KB
  * - **Vendor**
    - `Nuvoton <https://www.nuvoton.com/products/microcontrollers/8bit-8051-mcus/industrial-8051-series/ms51tc0ae/?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``MS51TC0AE`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:MS51TC0AE]
  platform = intel_mcs51
  board = MS51TC0AE

You can override default Generic MS51TC0AE settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `MS51TC0AE.json <https://github.com/platformio/platform-intel_mcs51/blob/master/boards/MS51TC0AE.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:MS51TC0AE]
  platform = intel_mcs51
  board = MS51TC0AE

  ; change microcontroller
  board_build.mcu = ms51tc0ae

  ; change MCU frequency
  board_build.f_cpu = 16000000L

Debugging
---------
:ref:`piodebug` currently does not support Generic MS51TC0AE board.