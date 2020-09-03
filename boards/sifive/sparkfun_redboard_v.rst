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

.. _board_sifive_sparkfun_redboard_v:

SparkFun RED-V RedBoard
=======================

.. contents::

Hardware
--------

Platform :ref:`platform_sifive`: SiFive brings the power of open source and software automation to the semiconductor industry, making it possible to develop new hardware faster and more affordably than ever before. 

.. list-table::

  * - **Microcontroller**
    - FE310
  * - **Frequency**
    - 320MHz
  * - **Flash**
    - 16MB
  * - **RAM**
    - 16KB
  * - **Vendor**
    - `SparkFun <https://www.sparkfun.com/products/15594?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``sparkfun_redboard_v`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:sparkfun_redboard_v]
  platform = sifive
  board = sparkfun_redboard_v

You can override default SparkFun RED-V RedBoard settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `sparkfun_redboard_v.json <https://github.com/platformio/platform-sifive/blob/master/boards/sparkfun_redboard_v.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:sparkfun_redboard_v]
  platform = sifive
  board = sparkfun_redboard_v

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

SparkFun RED-V RedBoard has on-board debug probe and **IS READY** for debugging. You don't need to use/buy external debug probe.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_jlink`
    - Yes
    - Yes
  * - :ref:`debugging_tool_renode`
    - Yes
    - 

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_freertos`
      - FreeRTOS is a real-time operating system kernel for embedded devices that has been ported to 40 microcontroller platforms

    * - :ref:`framework_freedom-e-sdk`
      - Open Source Software for Developing on the SiFive Freedom E Platform

    * - :ref:`framework_zephyr`
      - The Zephyr Project is a scalable real-time operating system (RTOS) supporting multiple hardware architectures, optimized for resource constrained devices, and built with safety and security in mind