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

.. _platform_aceinna_imu:

Aceinna IMU
===========

:Configuration:
  :ref:`projectconf_env_platform` = ``aceinna_imu``

Open-source, embedded development platform for Aceinna IMU hardware. Run custom algorithms and navigation code on Aceinna IMU/INS hardware.

For more detailed information please visit `vendor site <https://www.aceinna.com?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `Aceinna IMU development platform repository <https://github.com/aceinna/platform-aceinna_imu/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `OpenIMU300RI <https://github.com/aceinna/platform-aceinna_imu/tree/master/examples/OpenIMU300RI?utm_source=platformio.org&utm_medium=docs>`_
* `OpenIMU330BI <https://github.com/aceinna/platform-aceinna_imu/tree/master/examples/OpenIMU330BI?utm_source=platformio.org&utm_medium=docs>`_
* `OpenRTK330LI <https://github.com/aceinna/platform-aceinna_imu/tree/master/examples/OpenRTK330LI?utm_source=platformio.org&utm_medium=docs>`_
* `OpenIMU300ZI <https://github.com/aceinna/platform-aceinna_imu/tree/master/examples/OpenIMU300ZI?utm_source=platformio.org&utm_medium=docs>`_

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. contents::
    :local:


Tools & Debug Probes
~~~~~~~~~~~~~~~~~~~~

Supported debugging tools are listed in "Debug" column. For more detailed
information, please scroll table by horizontal.
You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` option in :ref:`projectconf`.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further instructions.


On-Board Debug Tools
^^^^^^^^^^^^^^^^^^^^

Boards listed below have on-board debug probe and **ARE READY** for debugging!
You do not need to use/buy external debug probe.


.. list-table::
    :header-rows:  1

    * - Name
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_aceinna_imu_LowCostRTK`
      - STM32F469NIH6
      - 180MHz
      - 1MB
      - 384KB


External Debug Tools
^^^^^^^^^^^^^^^^^^^^

Boards listed below are compatible with :ref:`piodebug` but **DEPEND ON**
external debug probe. They **ARE NOT READY** for debugging.
Please click on board name for the further details.


.. list-table::
    :header-rows:  1

    * - Name
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_aceinna_imu_OpenIMU300`
      - STM32F405RG
      - 120MHz
      - 1MB
      - 128KB
    * - :ref:`board_aceinna_imu_OpenIMU300ZA`
      - STM32F405RG
      - 120MHz
      - 1MB
      - 128KB
    * - :ref:`board_aceinna_imu_OpenIMU330`
      - STM32L431CB
      - 80MHz
      - 128KB
      - 64KB
    * - :ref:`board_aceinna_imu_OpenRTK`
      - STM32F469IG
      - 180MHz
      - 1MB
      - 384KB
    * - :ref:`board_aceinna_imu_OpenRTK330L`
      - STM32F469IG
      - 180MHz
      - 1MB
      - 384KB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/aceinna/platform-aceinna_imu/releases>`__
of Aceinna IMU development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = aceinna_imu
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = aceinna_imu@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/aceinna/platform-aceinna_imu.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `tool-jlink <https://www.segger.com/downloads/jlink/?utm_source=platformio.org&utm_medium=docs>`__
      - Software and Documentation Pack for SEGGER J-Link debug probes

    * - `tool-openocd <http://openocd.org?utm_source=platformio.org&utm_medium=docs>`__
      - Open On-Chip Debugger. Free and Open On-Chip Debugging, In-System Programming and Boundary-Scan Testing

    * - `toolchain-gccarmnoneeabi <https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm?utm_source=platformio.org&utm_medium=docs>`__
      - GNU toolchain for Arm Cortex-M and Cortex-R processors

.. warning::
    **Linux Users**:

        * Install "udev" rules :ref:`faq_udev_rules`
        * Raspberry Pi users, please read this article
          `Enable serial port on Raspberry Pi <https://hallard.me/enable-serial-port-on-raspberry-pi/>`__.


    **Windows Users:**

        Please check that you have a correctly installed USB driver from board
        manufacturer


Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll the tables below by
      horizontally.

Aceinna
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_aceinna_imu_LowCostRTK`
      - On-board
      - STM32F469NIH6
      - 180MHz
      - 1MB
      - 384KB
    * - :ref:`board_aceinna_imu_OpenIMU300`
      - External
      - STM32F405RG
      - 120MHz
      - 1MB
      - 128KB
    * - :ref:`board_aceinna_imu_OpenIMU300ZA`
      - External
      - STM32F405RG
      - 120MHz
      - 1MB
      - 128KB
    * - :ref:`board_aceinna_imu_OpenIMU330`
      - External
      - STM32L431CB
      - 80MHz
      - 128KB
      - 64KB
    * - :ref:`board_aceinna_imu_OpenRTK`
      - External
      - STM32F469IG
      - 180MHz
      - 1MB
      - 384KB
    * - :ref:`board_aceinna_imu_OpenRTK330L`
      - External
      - STM32F469IG
      - 180MHz
      - 1MB
      - 384KB
