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

.. _board_aceinna_imu_OpenIMU300:

Aceinna OpenIMU 300
===================

.. contents::

Hardware
--------

Platform :ref:`platform_aceinna_imu`: Open-source, embedded development platform for Aceinna IMU hardware. Run custom algorithms and navigation code on Aceinna IMU/INS hardware.

.. list-table::

  * - **Microcontroller**
    - STM32F405RG
  * - **Frequency**
    - 120MHz
  * - **Flash**
    - 1MB
  * - **RAM**
    - 128KB
  * - **Vendor**
    - `Aceinna <https://www.aceinna.com/inertial-systems/?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``OpenIMU300`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:OpenIMU300]
  platform = aceinna_imu
  board = OpenIMU300

You can override default Aceinna OpenIMU 300 settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `OpenIMU300.json <https://github.com/aceinna/platform-aceinna_imu/blob/master/boards/OpenIMU300.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:OpenIMU300]
  platform = aceinna_imu
  board = OpenIMU300

  ; change microcontroller
  board_build.mcu = stm32f405rg

  ; change MCU frequency
  board_build.f_cpu = 120000000L


Uploading
---------
Aceinna OpenIMU 300 supports the next uploading protocols:

* ``blackmagic``
* ``jlink``
* ``stlink``

Default protocol is ``stlink``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:OpenIMU300]
  platform = aceinna_imu
  board = OpenIMU300

  upload_protocol = stlink

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further
    instructions and configuration information.

You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` option in :ref:`projectconf`.

Aceinna OpenIMU 300 does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_blackmagic`
    - 
    - 
  * - :ref:`debugging_tool_jlink`
    - 
    - 
  * - :ref:`debugging_tool_stlink`
    - 
    - Yes