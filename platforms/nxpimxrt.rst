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

.. _platform_nxpimxrt:

NXP i.MX RT
===========

:Registry:
  `https://registry.platformio.org/platforms/platformio/nxpimxrt <https://registry.platformio.org/platforms/platformio/nxpimxrt>`__
:Configuration:
  :ref:`projectconf_env_platform` = ``platformio/nxpimxrt``

The i.MX RT series of crossover processors features the Arm Cortex-M core, real-time functionality and MCU usability at a cost-effective price.

For more detailed information please visit `vendor site <https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i.mx-rt-crossover-mcus:IMX-RT-SERIES?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `NXP i.MX RT development platform repository <https://github.com/platformio/platform-nxpimxrt/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `zephyr-blink <https://github.com/platformio/platform-nxpimxrt/tree/master/examples/zephyr-blink?utm_source=platformio.org&utm_medium=docs>`_
* `mbed-rtos-blink-baremetal <https://github.com/platformio/platform-nxpimxrt/tree/master/examples/mbed-rtos-blink-baremetal?utm_source=platformio.org&utm_medium=docs>`_
* `mbed-rtos-cellular <https://github.com/platformio/platform-nxpimxrt/tree/master/examples/mbed-rtos-cellular?utm_source=platformio.org&utm_medium=docs>`_
* `mbed-rtos-ethernet-tls <https://github.com/platformio/platform-nxpimxrt/tree/master/examples/mbed-rtos-ethernet-tls?utm_source=platformio.org&utm_medium=docs>`_
* `zephyr-synchronization <https://github.com/platformio/platform-nxpimxrt/tree/master/examples/zephyr-synchronization?utm_source=platformio.org&utm_medium=docs>`_

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
    * - :ref:`board_nxpimxrt_mimxrt1010_evk`
      - MIMXRT1011DAE5A
      - 500MHz
      - 64KB
      - 128KB
    * - :ref:`board_nxpimxrt_mimxrt1015_evk`
      - MIMXRT1015DAF5A
      - 500MHz
      - 96KB
      - 128KB
    * - :ref:`board_nxpimxrt_mimxrt1020_evk`
      - MIMXRT1021DAG5A
      - 500MHz
      - 8MB
      - 32MB
    * - :ref:`board_nxpimxrt_mimxrt1050_evk`
      - MIMXRT1052DVL6B
      - 600MHz
      - 8MB
      - 32MB
    * - :ref:`board_nxpimxrt_mimxrt1060_evk`
      - MIMXRT1062DVL6A
      - 600MHz
      - 8MB
      - 32MB
    * - :ref:`board_nxpimxrt_mimxrt1064_evk`
      - MIMXRT1064DVL6A
      - 600MHz
      - 8MB
      - 32MB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-nxpimxrt/releases>`__
of NXP i.MX RT development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version, NOT recommended
    ; Pin the version as shown below
    [env:latest_stable]
    platform = nxpimxrt
    board = ...

    ; Specific version
    [env:custom_stable]
    platform = nxpimxrt@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-nxpimxrt.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-mbed <https://registry.platformio.org/tools/platformio/framework-mbed>`__
      - Arm Mbed OS is a platform operating system designed for the internet of things

    * - `framework-zephyr <https://registry.platformio.org/tools/platformio/framework-zephyr>`__
      - Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures

    * - `tool-cmake <https://registry.platformio.org/tools/platformio/tool-cmake>`__
      - CMake is an open-source, cross-platform family of tools designed to build, test and package software

    * - `tool-dtc <https://registry.platformio.org/tools/platformio/tool-dtc>`__
      - Device tree compiler

    * - `tool-gperf <https://registry.platformio.org/tools/platformio/tool-gperf>`__
      - GNU gperf is a perfect hash function generator

    * - `tool-jlink <https://registry.platformio.org/tools/platformio/tool-jlink>`__
      - Software and Documentation Pack for SEGGER J-Link debug probes

    * - `tool-ninja <https://registry.platformio.org/tools/platformio/tool-ninja>`__
      - Ninja is a small build system with a focus on speed

    * - `tool-openocd <https://registry.platformio.org/tools/platformio/tool-openocd>`__
      - Open On-Chip Debugger. Free and Open On-Chip Debugging, In-System Programming and Boundary-Scan Testing

    * - `tool-pyocd <https://registry.platformio.org/tools/platformio/tool-pyocd>`__
      - Open source python library for programming and debugging ARM Cortex-M microcontrollers using CMSIS-DAP

    * - `toolchain-gccarmnoneeabi <https://registry.platformio.org/tools/platformio/toolchain-gccarmnoneeabi>`__
      - GNU toolchain for Arm Cortex-M and Cortex-R processors

.. warning::
    **Linux Users**:

        * Install "udev" rules :ref:`platformio_udev_rules`
        * Raspberry Pi users, please read this article
          `Enable serial port on Raspberry Pi <https://hallard.me/enable-serial-port-on-raspberry-pi/>`__.


    **Windows Users:**

        Please check that you have a correctly installed USB driver from board
        manufacturer


Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_mbed`
      - Arm Mbed OS is a platform operating system designed for the internet of things

    * - :ref:`framework_zephyr`
      - Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command
    * For more detailed ``board`` information please scroll the tables below by
      horizontally.

NXP
~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxpimxrt_mimxrt1010_evk`
      - On-board
      - MIMXRT1011DAE5A
      - 500MHz
      - 64KB
      - 128KB
    * - :ref:`board_nxpimxrt_mimxrt1015_evk`
      - On-board
      - MIMXRT1015DAF5A
      - 500MHz
      - 96KB
      - 128KB
    * - :ref:`board_nxpimxrt_mimxrt1020_evk`
      - On-board
      - MIMXRT1021DAG5A
      - 500MHz
      - 8MB
      - 32MB
    * - :ref:`board_nxpimxrt_mimxrt1050_evk`
      - On-board
      - MIMXRT1052DVL6B
      - 600MHz
      - 8MB
      - 32MB
    * - :ref:`board_nxpimxrt_mimxrt1060_evk`
      - On-board
      - MIMXRT1062DVL6A
      - 600MHz
      - 8MB
      - 32MB
    * - :ref:`board_nxpimxrt_mimxrt1064_evk`
      - On-board
      - MIMXRT1064DVL6A
      - 600MHz
      - 8MB
      - 32MB
