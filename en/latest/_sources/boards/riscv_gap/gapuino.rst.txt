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

.. _board_riscv_gap_gapuino:

GAPuino GAP8
============

.. contents::

Hardware
--------

Platform :ref:`platform_riscv_gap`: GreenWaves GAP8 IoT application processor enables the cost-effective development, deployment and autonomous operation of intelligent sensing devices that capture, analyze, classify and act on the fusion of rich data sources such as images, sounds or vibrations.

.. list-table::

  * - **Microcontroller**
    - GAP8
  * - **Frequency**
    - 250MHz
  * - **Flash**
    - 64MB
  * - **RAM**
    - 8MB
  * - **Vendor**
    - `GreenWaves Technologies <https://greenwaves-technologies.com/product/gapduino/?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``gapuino`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:gapuino]
  platform = riscv_gap
  board = gapuino

You can override default GAPuino GAP8 settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `gapuino.json <https://github.com/platformio/platform-riscv_gap/blob/master/boards/gapuino.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:gapuino]
  platform = riscv_gap
  board = gapuino

  ; change microcontroller
  board_build.mcu = gap8

  ; change MCU frequency
  board_build.f_cpu = 250000000L

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further
    instructions and configuration information.

You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` option in :ref:`projectconf`.

GAPuino GAP8 has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_ftdi`
    - Yes
    - Yes

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_mbed`
      - Arm Mbed OS is an open source embedded operating system designed specifically for the 'things' in the Internet of Things. It includes all the features you need to develop a connected product based on an Arm Cortex-M microcontroller, including security, connectivity, an RTOS and drivers for sensors and I/O devices

    * - :ref:`framework_pulp-os`
      - PULP is a silicon-proven Parallel Ultra Low Power platform targeting high energy efficiencies. The platform is organized in clusters of RISC-V cores that share a tightly-coupled data memory