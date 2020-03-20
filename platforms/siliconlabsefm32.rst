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

.. _platform_siliconlabsefm32:

Silicon Labs EFM32
==================

:Configuration:
  :ref:`projectconf_env_platform` = ``siliconlabsefm32``

Silicon Labs EFM32 Gecko 32-bit microcontroller (MCU) family includes devices that offer flash memory configurations up to 256 kB, 32 kB of RAM and CPU speeds up to 48 MHz. Based on the powerful ARM Cortex-M core, the Gecko family features innovative low energy techniques, short wake-up time from energy saving modes and a wide selection of peripherals, making it ideal for battery operated applications and other systems requiring high performance and low-energy consumption.

For more detailed information please visit `vendor site <http://www.silabs.com/products/mcu/32-bit/efm32-gecko/Pages/efm32-gecko.aspx?utm_source=platformio&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `Silicon Labs EFM32 development platform repository <https://github.com/platformio/platform-siliconlabsefm32/tree/master/examples?utm_source=platformio&utm_medium=docs>`_:

* `mbed-blink <https://github.com/platformio/platform-siliconlabsefm32/tree/master/examples/mbed-blink?utm_source=platformio&utm_medium=docs>`_
* `zephyr-subsys-console-getline <https://github.com/platformio/platform-siliconlabsefm32/tree/master/examples/zephyr-subsys-console-getline?utm_source=platformio&utm_medium=docs>`_
* `mbed-serial <https://github.com/platformio/platform-siliconlabsefm32/tree/master/examples/mbed-serial?utm_source=platformio&utm_medium=docs>`_
* `zephyr-blink <https://github.com/platformio/platform-siliconlabsefm32/tree/master/examples/zephyr-blink?utm_source=platformio&utm_medium=docs>`_
* `mbed-events <https://github.com/platformio/platform-siliconlabsefm32/tree/master/examples/mbed-events?utm_source=platformio&utm_medium=docs>`_
* `mbed-dsp <https://github.com/platformio/platform-siliconlabsefm32/tree/master/examples/mbed-dsp?utm_source=platformio&utm_medium=docs>`_
* `zephyr-sensor-vl53l0x <https://github.com/platformio/platform-siliconlabsefm32/tree/master/examples/zephyr-sensor-vl53l0x?utm_source=platformio&utm_medium=docs>`_

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
    * - :ref:`board_siliconlabsefm32_efm32gg_stk3700`
      - EFM32GG990F1024
      - 48MHz
      - 1MB
      - 128KB
    * - :ref:`board_siliconlabsefm32_efm32lg_stk3600`
      - EFM32LG990F256
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_siliconlabsefm32_efm32wg_stk3800`
      - EFM32WG990F256
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_siliconlabsefm32_efm32zg_stk3200`
      - EFM32ZG222F32
      - 24MHz
      - 32KB
      - 4KB
    * - :ref:`board_siliconlabsefm32_efm32hg_stk3400`
      - EFM32HG322F64
      - 25MHz
      - 64KB
      - 8KB
    * - :ref:`board_siliconlabsefm32_efm32pg_stk3401`
      - EFM32PG1B200F256GM48
      - 40MHz
      - 256KB
      - 32KB
    * - :ref:`board_siliconlabsefm32_tb_sense_12`
      - EFR32MG12P432F1024
      - 40MHz
      - 1MB
      - 256KB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-siliconlabsefm32/releases>`__
of Silicon Labs EFM32 development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = siliconlabsefm32
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = siliconlabsefm32@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-siliconlabsefm32.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-mbed <http://mbed.org?utm_source=platformio&utm_medium=docs>`__
      - mbed Framework

    * - `framework-zephyr <https://github.com/zephyrproject-rtos/zephyr?utm_source=platformio&utm_medium=docs>`__
      - Primary Git Repository for the Zephyr Project. Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures.

    * - `framework-zephyr-civetweb <https://github.com/zephyrproject-rtos/civetweb?utm_source=platformio&utm_medium=docs>`__
      - Zephyr module CivetWeb Embedded C/C++ web server

    * - `framework-zephyr-fatfs <https://github.com/zephyrproject-rtos/fatfs?utm_source=platformio&utm_medium=docs>`__
      - Zephyr module for FATFS filesystem

    * - `framework-zephyr-hal-silabs <https://github.com/zephyrproject-rtos/hal_silabs?utm_source=platformio&utm_medium=docs>`__
      - SiliconLabs HAL for Zephyr framework

    * - `framework-zephyr-libmetal <https://github.com/zephyrproject-rtos/libmetal?utm_source=platformio&utm_medium=docs>`__
      - Zephyr module for HAL abstraction layer used by open-amp

    * - `framework-zephyr-littlefs <https://github.com/zephyrproject-rtos/littlefs?utm_source=platformio&utm_medium=docs>`__
      - Zephyr module for littlefs filesystem

    * - `framework-zephyr-lvgl <https://github.com/zephyrproject-rtos/lvgl?utm_source=platformio&utm_medium=docs>`__
      - Zephyr module for LittlevGL - an Open-source Embedded GUI Library

    * - `framework-zephyr-mbedtls <https://github.com/zephyrproject-rtos/mbedtls?utm_source=platformio&utm_medium=docs>`__
      - mbedTLS module for Zephyr

    * - `framework-zephyr-mcumgr <https://github.com/zephyrproject-rtos/mcumgr?utm_source=platformio&utm_medium=docs>`__
      - Zephyr module for mcumgr management library for 32-bit MCUs

    * - `framework-zephyr-mipi-sys-t <https://github.com/zephyrproject-rtos/mipi-sys-t?utm_source=platformio&utm_medium=docs>`__
      - Zephyr module for MIPI System Software Trace

    * - `framework-zephyr-nffs <https://github.com/zephyrproject-rtos/nffs?utm_source=platformio&utm_medium=docs>`__
      - Zephyr module for the Newtron Flash File System

    * - `framework-zephyr-open-amp <https://github.com/zephyrproject-rtos/open-amp?utm_source=platformio&utm_medium=docs>`__
      - Zephyr module for Open Asymmetric Multi Processing (OpenAMP) framework

    * - `framework-zephyr-openthread <https://github.com/zephyrproject-rtos/openthread?utm_source=platformio&utm_medium=docs>`__
      - OpenThread module for Zephyr

    * - `framework-zephyr-segger <https://github.com/zephyrproject-rtos/segger?utm_source=platformio&utm_medium=docs>`__
      - Zephyr module for Segger RTT

    * - `framework-zephyr-tinycbor <https://github.com/zephyrproject-rtos/tinycbor?utm_source=platformio&utm_medium=docs>`__
      - Zephyr module for Concise Binary Object Representation Library

    * - `tool-cmake <https://cmake.org?utm_source=platformio&utm_medium=docs>`__
      - CMake is an open-source, cross-platform family of tools designed to build, test and package software.

    * - `tool-dtc <https://git.kernel.org/pub/scm/utils/dtc/dtc.git/about/?utm_source=platformio&utm_medium=docs>`__
      - Device tree compiler

    * - `tool-gperf <https://www.gnu.org/software/gperf?utm_source=platformio&utm_medium=docs>`__
      - GNU gperf is a perfect hash function generator.

    * - `tool-jlink <https://www.segger.com/downloads/jlink/?utm_source=platformio&utm_medium=docs>`__
      - SEGGER J-Link Software and Documentation Pack

    * - `tool-ninja <https://ninja-build.org?utm_source=platformio&utm_medium=docs>`__
      - Ninja is a small build system with a focus on speed.

    * - `toolchain-gccarmnoneeabi <https://launchpad.net/gcc-arm-embedded?utm_source=platformio&utm_medium=docs>`__
      - gcc-arm-embedded

.. warning::
    **Linux Users**:

        * Install "udev" rules :ref:`faq_udev_rules`
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
      - The mbed framework The mbed SDK has been designed to provide enough hardware abstraction to be intuitive and concise, yet powerful enough to build complex projects. It is built on the low-level ARM CMSIS APIs, allowing you to code down to the metal if needed. In addition to RTOS, USB and Networking libraries, a cookbook of hundreds of reusable peripheral and module libraries have been built on top of the SDK by the mbed Developer Community.

    * - :ref:`framework_zephyr`
      - The Zephyr Project is a scalable real-time operating system (RTOS) supporting multiple hardware architectures, optimized for resource constrained devices, and built with safety and security in mind.

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll the tables below by
      horizontally.

Silicon Labs
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_siliconlabsefm32_efm32gg_stk3700`
      - On-board
      - EFM32GG990F1024
      - 48MHz
      - 1MB
      - 128KB
    * - :ref:`board_siliconlabsefm32_efm32lg_stk3600`
      - On-board
      - EFM32LG990F256
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_siliconlabsefm32_efm32wg_stk3800`
      - On-board
      - EFM32WG990F256
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_siliconlabsefm32_efm32zg_stk3200`
      - On-board
      - EFM32ZG222F32
      - 24MHz
      - 32KB
      - 4KB
    * - :ref:`board_siliconlabsefm32_efm32hg_stk3400`
      - On-board
      - EFM32HG322F64
      - 25MHz
      - 64KB
      - 8KB
    * - :ref:`board_siliconlabsefm32_efm32pg_stk3401`
      - On-board
      - EFM32PG1B200F256GM48
      - 40MHz
      - 256KB
      - 32KB
    * - :ref:`board_siliconlabsefm32_tb_sense_12`
      - On-board
      - EFR32MG12P432F1024
      - 40MHz
      - 1MB
      - 256KB
