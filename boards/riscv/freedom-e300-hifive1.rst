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

.. _board_riscv_freedom-e300-hifive1:

HiFive1
=======

.. contents::

Platform :ref:`platform_riscv`: RISC-V is an open, free ISA enabling a new era of processor innovation through open standard collaboration. Born in academia and research, RISC-V ISA delivers a new level of free, extensible software and hardware freedom on architecture, paving the way for the next 50 years of computing design and innovation.

System
------

.. list-table::

  * - **Microcontroller**
    - FE310
  * - **Frequency**
    - 320Mhz
  * - **Flash**
    - 16MB
  * - **RAM**
    - 16KB
  * - **Vendor**
    - `SiFive <https://www.sifive.com/products/hifive1/?utm_source=platformio&utm_medium=docs>`__


Configuration
-------------

Please use ``freedom-e300-hifive1`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:freedom-e300-hifive1]
  platform = riscv
  board = freedom-e300-hifive1

You can override default HiFive1 settings per build environment using
``board_{JSON.PATH}`` option, where ``{JSON.PATH}`` is a path from
board manifest `freedom-e300-hifive1.json <https://github.com/platformio/platform-riscv/blob/master/boards/freedom-e300-hifive1.json>`_. For example,

.. code-block:: ini

  [env:freedom-e300-hifive1]
  platform = riscv
  board = freedom-e300-hifive1

  ; change microcontroller
  board_build.mcu = fe310

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

HiFive1 has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

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

    * - :ref:`framework_freedom-e-sdk`
      - Open Source Software for Developing on the SiFive Freedom E Platform