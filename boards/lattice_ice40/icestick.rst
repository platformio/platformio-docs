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

.. _board_lattice_ice40_icestick:

Lattice iCEstick FPGA Evaluation Kit
====================================

.. contents::

Hardware
--------

Platform :ref:`platform_lattice_ice40`: The iCE40 family of ultra-low power, non-volatile FPGAs has five devices with densities ranging from 384 to 7680 Look-Up Tables (LUTs). In addition to LUT-based,low-cost programmable logic, these devices feature Embedded Block RAM (EBR), Non-volatile Configuration Memory (NVCM) and Phase Locked Loops (PLLs). These features allow the devices to be used in low-cost, high-volume consumer and system applications.

.. list-table::

  * - **Microcontroller**
    - ICE40-HX1K-TQ144
  * - **Frequency**
    - 12MHz
  * - **Flash**
    - 32KB
  * - **RAM**
    - 32KB
  * - **Vendor**
    - `Lattice <http://www.latticesemi.com/icestick?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``icestick`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:icestick]
  platform = lattice_ice40
  board = icestick

You can override default Lattice iCEstick FPGA Evaluation Kit settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `icestick.json <https://github.com/platformio/platform-lattice_ice40/blob/master/boards/icestick.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:icestick]
  platform = lattice_ice40
  board = icestick

  ; change microcontroller
  board_build.mcu = iCE40-HX1K-TQ144

  ; change MCU frequency
  board_build.f_cpu = 12000000L

Debugging
---------
:ref:`piodebug` currently does not support Lattice iCEstick FPGA Evaluation Kit board.