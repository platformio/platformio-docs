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

.. _platform_nxplpc:

NXP LPC
=======

:Configuration:
  :ref:`projectconf_env_platform` = ``nxplpc``

The NXP LPC is a family of 32-bit microcontroller integrated circuits by NXP Semiconductors. The LPC chips are grouped into related series that are based around the same 32-bit ARM processor core, such as the Cortex-M4F, Cortex-M3, Cortex-M0+, or Cortex-M0. Internally, each microcontroller consists of the processor core, static RAM memory, flash memory, debugging interface, and various peripherals.

For more detailed information please visit `vendor site <http://www.nxp.com/products/microcontrollers/?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `NXP LPC development platform repository <https://github.com/platformio/platform-nxplpc/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `zephyr-blink <https://github.com/platformio/platform-nxplpc/tree/master/examples/zephyr-blink?utm_source=platformio.org&utm_medium=docs>`_
* `mbed-rtos-blockdevice <https://github.com/platformio/platform-nxplpc/tree/master/examples/mbed-rtos-blockdevice?utm_source=platformio.org&utm_medium=docs>`_
* `mbed-rtos-blink-baremetal <https://github.com/platformio/platform-nxplpc/tree/master/examples/mbed-rtos-blink-baremetal?utm_source=platformio.org&utm_medium=docs>`_
* `mbed-rtos-thread-statistics <https://github.com/platformio/platform-nxplpc/tree/master/examples/mbed-rtos-thread-statistics?utm_source=platformio.org&utm_medium=docs>`_
* `zephyr-custom-board <https://github.com/platformio/platform-nxplpc/tree/master/examples/zephyr-custom-board?utm_source=platformio.org&utm_medium=docs>`_
* `mbed-legacy-examples <https://github.com/platformio/platform-nxplpc/tree/master/examples/mbed-legacy-examples?utm_source=platformio.org&utm_medium=docs>`_
* `zephyr-synchronization <https://github.com/platformio/platform-nxplpc/tree/master/examples/zephyr-synchronization?utm_source=platformio.org&utm_medium=docs>`_

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
    * - :ref:`board_nxplpc_lpc11u24_301`
      - LPC11U24
      - 48MHz
      - 32KB
      - 8KB
    * - :ref:`board_nxplpc_lpc4330_m4`
      - LPC4330
      - 204MHz
      - 8MB
      - 264KB
    * - :ref:`board_nxplpc_elektor_cocorico`
      - LPC812
      - 30MHz
      - 16KB
      - 4KB
    * - :ref:`board_nxplpc_lpc4088_dm`
      - LPC4088
      - 120MHz
      - 512KB
      - 96KB
    * - :ref:`board_nxplpc_lpc4088`
      - LPC4088
      - 120MHz
      - 512KB
      - 96KB
    * - :ref:`board_nxplpc_lpc11u68`
      - LPC11U68
      - 50MHz
      - 256KB
      - 36KB
    * - :ref:`board_nxplpc_lpc824`
      - LPC824
      - 30MHz
      - 32KB
      - 8KB
    * - :ref:`board_nxplpc_lpc812`
      - LPC812
      - 30MHz
      - 16KB
      - 4KB
    * - :ref:`board_nxplpc_lpc54114`
      - LPC54114J256BD64
      - 100MHz
      - 256KB
      - 192KB
    * - :ref:`board_nxplpc_lpc546xx`
      - LPC54608ET512
      - 180MHz
      - 512KB
      - 200KB
    * - :ref:`board_nxplpc_lpcxpresso55s16`
      - LPC55S16
      - 150MHz
      - 256KB
      - 96KB
    * - :ref:`board_nxplpc_lpcxpresso55s69`
      - LPC55S69
      - 150MHz
      - 640KB
      - 320KB
    * - :ref:`board_nxplpc_lpc11u24`
      - LPC11U24
      - 48MHz
      - 32KB
      - 8KB
    * - :ref:`board_nxplpc_lpc1768`
      - LPC1768
      - 96MHz
      - 512KB
      - 64KB
    * - :ref:`board_nxplpc_seeedArchPro`
      - LPC1768
      - 96MHz
      - 512KB
      - 64KB
    * - :ref:`board_nxplpc_lpc1114fn28`
      - LPC1114FN28
      - 48MHz
      - 32KB
      - 4KB
    * - :ref:`board_nxplpc_ssci824`
      - LPC824
      - 30MHz
      - 32KB
      - 8KB
    * - :ref:`board_nxplpc_ubloxc027`
      - LPC1768
      - 96MHz
      - 512KB
      - 64KB


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
    * - :ref:`board_nxplpc_lpc11u35_501`
      - LPC11U35
      - 48MHz
      - 64KB
      - 10KB
    * - :ref:`board_nxplpc_lpc1347`
      - LPC1347
      - 72MHz
      - 64KB
      - 12KB
    * - :ref:`board_nxplpc_lpc11u35`
      - LPC11U35
      - 48MHz
      - 64KB
      - 10KB
    * - :ref:`board_nxplpc_blueboard_lpc11u24`
      - LPC11U24
      - 48MHz
      - 32KB
      - 8KB
    * - :ref:`board_nxplpc_lpc11c24`
      - LPC11C24
      - 48MHz
      - 32KB
      - 8KB
    * - :ref:`board_nxplpc_lpc11u34_421`
      - LPC11U34
      - 48MHz
      - 40KB
      - 8KB
    * - :ref:`board_nxplpc_lpc11u37_501`
      - LPC11U37
      - 48MHz
      - 128KB
      - 10KB
    * - :ref:`board_nxplpc_lpc1549`
      - LPC1549
      - 72MHz
      - 256KB
      - 36KB
    * - :ref:`board_nxplpc_dipcortexm0`
      - LPC11U24
      - 50MHz
      - 32KB
      - 8KB
    * - :ref:`board_nxplpc_lpc11u35_y5_mbug`
      - LPC11U35
      - 48MHz
      - 64KB
      - 10KB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-nxplpc/releases>`__
of NXP LPC development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = nxplpc
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = nxplpc@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-nxplpc.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-mbed <http://mbed.org?utm_source=platformio.org&utm_medium=docs>`__
      - Arm Mbed OS is a platform operating system designed for the internet of things

    * - `framework-zephyr <https://www.zephyrproject.org?utm_source=platformio.org&utm_medium=docs>`__
      - Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures

    * - `framework-zephyr-canopennode <https://github.com/zephyrproject-rtos/canopennode?utm_source=platformio.org&utm_medium=docs>`__
      - canopennode Zephyr module

    * - `framework-zephyr-civetweb <https://github.com/zephyrproject-rtos/civetweb.git?utm_source=platformio.org&utm_medium=docs>`__
      - Zephyr module for CivetWeb Embedded C/C++ web server

    * - `framework-zephyr-cmsis <https://github.com/zephyrproject-rtos/cmsis.git?utm_source=platformio.org&utm_medium=docs>`__
      - Software Interface Standard for Arm Cortex-based Microcontrollers and Zephyr framework

    * - `framework-zephyr-fatfs <https://github.com/zephyrproject-rtos/fatfs.git?utm_source=platformio.org&utm_medium=docs>`__
      - Zephyr module for FATFS filesystem

    * - `framework-zephyr-hal-nxp <https://github.com/zephyrproject-rtos/hal_nxp.git?utm_source=platformio.org&utm_medium=docs>`__
      - NXP HAL for Zephyr framework

    * - `framework-zephyr-hal-st <https://github.com/zephyrproject-rtos/hal_st.git?utm_source=platformio.org&utm_medium=docs>`__
      - Zephyr module for the official libraries provided by STMicroelectronics

    * - `framework-zephyr-libmetal <https://github.com/zephyrproject-rtos/libmetal.git?utm_source=platformio.org&utm_medium=docs>`__
      - Zephyr module for HAL abstraction layer used by open-amp

    * - `framework-zephyr-littlefs <https://github.com/zephyrproject-rtos/littlefs.git?utm_source=platformio.org&utm_medium=docs>`__
      - Zephyr module for littlefs filesystem

    * - `framework-zephyr-loramac-node <https://github.com/zephyrproject-rtos/loramac-node.git?utm_source=platformio.org&utm_medium=docs>`__
      - Zephyr module for LoRaWAN endpoint stack implementation

    * - `framework-zephyr-lvgl <https://github.com/zephyrproject-rtos/lvgl.git?utm_source=platformio.org&utm_medium=docs>`__
      - Zephyr module for LittlevGL - an Open-source Embedded GUI Library

    * - `framework-zephyr-mbedtls <https://github.com/zephyrproject-rtos/mbedtls.git?utm_source=platformio.org&utm_medium=docs>`__
      - mbedTLS module for Zephyr

    * - `framework-zephyr-mcuboot <https://github.com/zephyrproject-rtos/mcuboot.git?utm_source=platformio.org&utm_medium=docs>`__
      - Zephyr module for MCUboot - a secure bootloader for 32-bit MCUs

    * - `framework-zephyr-mcumgr <https://github.com/zephyrproject-rtos/mcumgr.git?utm_source=platformio.org&utm_medium=docs>`__
      - Zephyr module for mcumgr management library for 32-bit MCUs

    * - `framework-zephyr-mipi-sys-t <https://github.com/zephyrproject-rtos/mipi-sys-t.git?utm_source=platformio.org&utm_medium=docs>`__
      - Zephyr module for MIPI System Software Trace

    * - `framework-zephyr-open-amp <https://github.com/zephyrproject-rtos/open-amp.git?utm_source=platformio.org&utm_medium=docs>`__
      - Zephyr module for Open Asymmetric Multi Processing (OpenAMP) framework

    * - `framework-zephyr-openthread <https://github.com/zephyrproject-rtos/openthread.git?utm_source=platformio.org&utm_medium=docs>`__
      - OpenThread module for Zephyr

    * - `framework-zephyr-segger <https://github.com/zephyrproject-rtos/segger.git?utm_source=platformio.org&utm_medium=docs>`__
      - Zephyr module for Segger RTT

    * - `framework-zephyr-tinycbor <https://github.com/zephyrproject-rtos/tinycbor.git?utm_source=platformio.org&utm_medium=docs>`__
      - Zephyr module for Concise Binary Object Representation Library

    * - `framework-zephyr-tinycrypt <https://github.com/zephyrproject-rtos/tinycrypt.git?utm_source=platformio.org&utm_medium=docs>`__
      - The TinyCrypt Library provides an implementation for constrained devices of a minimal set of standard cryptography primitives for Zephyr framework

    * - `framework-zephyr-trusted-firmware-m <https://github.com/zephyrproject-rtos/trusted-firmware-m.git?utm_source=platformio.org&utm_medium=docs>`__
      - Trusted Firmware M provides a reference implementation of secure world software for ARMv8-M and Zephyr framework

    * - `tool-cmake <https://cmake.org?utm_source=platformio.org&utm_medium=docs>`__
      - CMake is an open-source, cross-platform family of tools designed to build, test and package software

    * - `tool-dtc <https://git.kernel.org/pub/scm/utils/dtc/dtc.git?utm_source=platformio.org&utm_medium=docs>`__
      - Device tree compiler

    * - `tool-gperf <https://www.gnu.org/software/gperf?utm_source=platformio.org&utm_medium=docs>`__
      - GNU gperf is a perfect hash function generator

    * - `tool-jlink <https://www.segger.com/downloads/jlink/?utm_source=platformio.org&utm_medium=docs>`__
      - Software and Documentation Pack for SEGGER J-Link debug probes

    * - `tool-ninja <https://ninja-build.org?utm_source=platformio.org&utm_medium=docs>`__
      - Ninja is a small build system with a focus on speed

    * - `tool-openocd <http://openocd.org?utm_source=platformio.org&utm_medium=docs>`__
      - Open On-Chip Debugger. Free and Open On-Chip Debugging, In-System Programming and Boundary-Scan Testing

    * - `tool-pyocd <https://github.com/pyocd/pyOCD.git?utm_source=platformio.org&utm_medium=docs>`__
      - Open source python library for programming and debugging ARM Cortex-M microcontrollers using CMSIS-DAP

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


Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_mbed`
      - Arm Mbed OS is an open source embedded operating system designed specifically for the 'things' in the Internet of Things. It includes all the features you need to develop a connected product based on an Arm Cortex-M microcontroller, including security, connectivity, an RTOS and drivers for sensors and I/O devices

    * - :ref:`framework_zephyr`
      - The Zephyr Project is a scalable real-time operating system (RTOS) supporting multiple hardware architectures, optimized for resource constrained devices, and built with safety and security in mind

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll the tables below by
      horizontally.

AppNearMe
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_micronfcboard`
      - No
      - LPC11U34
      - 48MHz
      - 48KB
      - 10KB

CQ Publishing
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_lpc11u35_501`
      - External
      - LPC11U35
      - 48MHz
      - 64KB
      - 10KB

Elektor Labs
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_elektor_cocorico`
      - On-board
      - LPC812
      - 30MHz
      - 16KB
      - 4KB

Embedded Artists
~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_lpc11u35`
      - External
      - LPC11U35
      - 48MHz
      - 64KB
      - 10KB
    * - :ref:`board_nxplpc_lpc4088_dm`
      - On-board
      - LPC4088
      - 120MHz
      - 512KB
      - 96KB
    * - :ref:`board_nxplpc_lpc4088`
      - On-board
      - LPC4088
      - 120MHz
      - 512KB
      - 96KB

GHI Electronics
~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_oc_mbuino`
      - No
      - LPC11U24
      - 50MHz
      - 32KB
      - 10KB

Micromint
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_lpc4330_m4`
      - On-board
      - LPC4330
      - 204MHz
      - 8MB
      - 264KB

NGX Technologies
~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_blueboard_lpc11u24`
      - External
      - LPC11U24
      - 48MHz
      - 32KB
      - 8KB

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
    * - :ref:`board_nxplpc_lpc11u24_301`
      - On-board
      - LPC11U24
      - 48MHz
      - 32KB
      - 8KB
    * - :ref:`board_nxplpc_lpc11u68`
      - On-board
      - LPC11U68
      - 50MHz
      - 256KB
      - 36KB
    * - :ref:`board_nxplpc_lpc824`
      - On-board
      - LPC824
      - 30MHz
      - 32KB
      - 8KB
    * - :ref:`board_nxplpc_lpc11c24`
      - External
      - LPC11C24
      - 48MHz
      - 32KB
      - 8KB
    * - :ref:`board_nxplpc_lpc11u34_421`
      - External
      - LPC11U34
      - 48MHz
      - 40KB
      - 8KB
    * - :ref:`board_nxplpc_lpc11u37_501`
      - External
      - LPC11U37
      - 48MHz
      - 128KB
      - 10KB
    * - :ref:`board_nxplpc_lpc812`
      - On-board
      - LPC812
      - 30MHz
      - 16KB
      - 4KB
    * - :ref:`board_nxplpc_lpc1549`
      - External
      - LPC1549
      - 72MHz
      - 256KB
      - 36KB
    * - :ref:`board_nxplpc_lpc54114`
      - On-board
      - LPC54114J256BD64
      - 100MHz
      - 256KB
      - 192KB
    * - :ref:`board_nxplpc_lpc546xx`
      - On-board
      - LPC54608ET512
      - 180MHz
      - 512KB
      - 200KB
    * - :ref:`board_nxplpc_lpcxpresso55s16`
      - On-board
      - LPC55S16
      - 150MHz
      - 256KB
      - 96KB
    * - :ref:`board_nxplpc_lpcxpresso55s69`
      - On-board
      - LPC55S69
      - 150MHz
      - 640KB
      - 320KB
    * - :ref:`board_nxplpc_lpc11u24`
      - On-board
      - LPC11U24
      - 48MHz
      - 32KB
      - 8KB
    * - :ref:`board_nxplpc_lpc1768`
      - On-board
      - LPC1768
      - 96MHz
      - 512KB
      - 64KB

Outrageous Circuits
~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_mbuino`
      - No
      - LPC11U24
      - 48MHz
      - 32KB
      - 8KB

SeeedStudio
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_seeedArchGPRS`
      - No
      - LPC11U37
      - 48MHz
      - 128KB
      - 10KB
    * - :ref:`board_nxplpc_seeedArchPro`
      - On-board
      - LPC1768
      - 96MHz
      - 512KB
      - 64KB
    * - :ref:`board_nxplpc_xadow_m0`
      - No
      - LPC11U35
      - 48MHz
      - 64KB
      - 10KB

Smeshlink
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_xbed_lpc1768`
      - No
      - LPC1768
      - 96MHz
      - 512KB
      - 32KB

Solder Splash Labs
~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_lpc1347`
      - External
      - LPC1347
      - 72MHz
      - 64KB
      - 12KB
    * - :ref:`board_nxplpc_dipcortexm0`
      - External
      - LPC11U24
      - 50MHz
      - 32KB
      - 8KB

Switch Science
~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_lpc1114fn28`
      - On-board
      - LPC1114FN28
      - 48MHz
      - 32KB
      - 4KB
    * - :ref:`board_nxplpc_ssci824`
      - On-board
      - LPC824
      - 30MHz
      - 32KB
      - 8KB

u-blox
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_ubloxc027`
      - On-board
      - LPC1768
      - 96MHz
      - 512KB
      - 64KB

y5 design
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nxplpc_lpc11u35_y5_mbug`
      - External
      - LPC11U35
      - 48MHz
      - 64KB
      - 10KB
