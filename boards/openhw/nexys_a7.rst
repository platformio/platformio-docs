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

.. _board_openhw_nexys_a7:

Digilent Nexys A7
=================

.. contents::

Hardware
--------

Platform :ref:`platform_openhw`: OpenHW Group is a not-for-profit, global organization that provides an infrastructure for hosting high quality open-source HW developments in line with industry best practices. The OpenHW CV32E40P RISC-V core is the first open-source core for high-volume chips verified with the state-of-the-art process required for high-integrity, commercial SoCs.

.. list-table::

  * - **Microcontroller**
    - 
  * - **Frequency**
    - 320MHz
  * - **Flash**
    - 16MB
  * - **RAM**
    - 1.16MB
  * - **Vendor**
    - `Digilent <https://reference.digilentinc.com/reference/programmable-logic/nexys-a7/start?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``nexys_a7`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:nexys_a7]
  platform = openhw
  board = nexys_a7

You can override default Digilent Nexys A7 settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `nexys_a7.json <https://github.com/platformio/platform-openhw/blob/master/boards/nexys_a7.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:nexys_a7]
  platform = openhw
  board = nexys_a7

  ; change microcontroller
  board_build.mcu = 

  ; change MCU frequency
  board_build.f_cpu = 320000000L

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further
    instructions and configuration information.

You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` option in :ref:`projectconf`.

Digilent Nexys A7 has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_digilent-hs1`
    - Yes
    - Yes
  * - :ref:`debugging_tool_digilent-hs2`
    - 
    - 
  * - :ref:`debugging_tool_olimex-arm-usb-ocd`
    - 
    - 
  * - :ref:`debugging_tool_olimex-arm-usb-ocd-h`
    - 
    - 
  * - :ref:`debugging_tool_olimex-arm-usb-tiny-h`
    - 
    - 
  * - :ref:`debugging_tool_olimex-jtag-tiny`
    - 
    - 
  * - :ref:`debugging_tool_ovpsim`
    - Yes
    - 
  * - :ref:`debugging_tool_renode`
    - Yes
    - 

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_pulp-runtime`
      - Runtime Environment for Parallel Ultra Low Power platform targeting high energy efficiencies

    * - :ref:`framework_pulp-sdk`
      - Software Development Kit for Parallel Ultra Low Power platform targeting high energy efficiencies