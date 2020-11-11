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

.. _platform_nordicnrf51:

Nordic nRF51
============

:Configuration:
  :ref:`projectconf_env_platform` = ``nordicnrf51``

The Nordic nRF51 Series is a family of highly flexible, multi-protocol, system-on-chip (SoC) devices for ultra-low power wireless applications. nRF51 Series devices support a range of protocol stacks including Bluetooth Smart (previously called Bluetooth low energy), ANT and proprietary 2.4GHz protocols such as Gazell.

For more detailed information please visit `vendor site <https://www.nordicsemi.com/eng/Products/nRF51-Series-SoC?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `Nordic nRF51 development platform repository <https://github.com/platformio/platform-nordicnrf51/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `mbed-blink <https://github.com/platformio/platform-nordicnrf51/tree/master/examples/mbed-blink?utm_source=platformio.org&utm_medium=docs>`_
* `mbed-serial <https://github.com/platformio/platform-nordicnrf51/tree/master/examples/mbed-serial?utm_source=platformio.org&utm_medium=docs>`_
* `zephyr-blink <https://github.com/platformio/platform-nordicnrf51/tree/master/examples/zephyr-blink?utm_source=platformio.org&utm_medium=docs>`_
* `mbed-events <https://github.com/platformio/platform-nordicnrf51/tree/master/examples/mbed-events?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-blink <https://github.com/platformio/platform-nordicnrf51/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-ble-led <https://github.com/platformio/platform-nordicnrf51/tree/master/examples/arduino-ble-led?utm_source=platformio.org&utm_medium=docs>`_
* `zephyr-ble-eddystone <https://github.com/platformio/platform-nordicnrf51/tree/master/examples/zephyr-ble-eddystone?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-internal-libs <https://github.com/platformio/platform-nordicnrf51/tree/master/examples/arduino-internal-libs?utm_source=platformio.org&utm_medium=docs>`_
* `zephyr-drivers-entropy <https://github.com/platformio/platform-nordicnrf51/tree/master/examples/zephyr-drivers-entropy?utm_source=platformio.org&utm_medium=docs>`_
* `mbed-ble-thermometer <https://github.com/platformio/platform-nordicnrf51/tree/master/examples/mbed-ble-thermometer?utm_source=platformio.org&utm_medium=docs>`_

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
    * - :ref:`board_nordicnrf51_bbcmicrobit`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - :ref:`board_nordicnrf51_calliope_mini`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - :ref:`board_nordicnrf51_dfcm_nnn40`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf51_delta_dfcm_nnn50`
      - NRF51822
      - 32MHz
      - 256KB
      - 16KB
    * - :ref:`board_nordicnrf51_wallbot_ble`
      - NRF51822
      - 16MHz
      - 128KB
      - 16KB
    * - :ref:`board_nordicnrf51_nrf51_beacon`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf51_nrf51_dongle`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf51_nrf51_mkit`
      - NRF51822
      - 16MHz
      - 128KB
      - 16KB
    * - :ref:`board_nordicnrf51_nrf51_dk`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf51_redBearLabBLENano`
      - NRF51822
      - 16MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf51_redBearLab`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - :ref:`board_nordicnrf51_seeedArchBLE`
      - NRF51822
      - 16MHz
      - 128KB
      - 16KB
    * - :ref:`board_nordicnrf51_seeedArchLink`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - :ref:`board_nordicnrf51_seeedTinyBLE`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - :ref:`board_nordicnrf51_hrm1017`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - :ref:`board_nordicnrf51_ty51822r3`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf51_vbluno51`
      - NRF51822
      - 16MHz
      - 128KB
      - 32KB
    * - :ref:`board_nordicnrf51_nrf51822_y5_mbug`
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB


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
    * - :ref:`board_nordicnrf51_bluz_dk`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf51_oshchip`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf51_Sinobit`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf51_waveshare_ble400`
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf51_ng_beacon`
      - NRF51822
      - 16MHz
      - 256KB
      - 32KB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-nordicnrf51/releases>`__
of Nordic nRF51 development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = nordicnrf51
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = nordicnrf51@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-nordicnrf51.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-arduinonordicnrf5 <https://github.com/sandeepmistry/arduino-nRF5.git?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for Nordic Semiconductor nRF5 based boards

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

    * - `framework-zephyr-hal-nordic <https://github.com/zephyrproject-rtos/hal_nordic.git?utm_source=platformio.org&utm_medium=docs>`__
      - Nordic nRF5x HAL for Zephyr framework

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

    * - `tool-nrfjprog <https://www.nordicsemi.com/Software-and-tools/Development-Tools/nRF-Command-Line-Tools?utm_source=platformio.org&utm_medium=docs>`__
      - nRFx command line tools

    * - `tool-openocd <http://openocd.org?utm_source=platformio.org&utm_medium=docs>`__
      - Open On-Chip Debugger. Free and Open On-Chip Debugging, In-System Programming and Boundary-Scan Testing

    * - `tool-sreccat <http://srecord.sourceforge.net?utm_source=platformio.org&utm_medium=docs>`__
      - Collection of powerful tools for manipulating EPROM load files

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

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences

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

BBC
~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_bbcmicrobit`
      - On-board
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB

BluzDK
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_bluz_dk`
      - External
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB

Calliope
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_calliope_mini`
      - On-board
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB

Delta
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_dfcm_nnn40`
      - On-board
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf51_delta_dfcm_nnn50`
      - On-board
      - NRF51822
      - 32MHz
      - 256KB
      - 16KB

JKSoft
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_wallbot_ble`
      - On-board
      - NRF51822
      - 16MHz
      - 128KB
      - 16KB

Nordic
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_nrf51_beacon`
      - On-board
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf51_nrf51_dongle`
      - On-board
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf51_nrf51_mkit`
      - On-board
      - NRF51822
      - 16MHz
      - 128KB
      - 16KB
    * - :ref:`board_nordicnrf51_nrf51_dk`
      - On-board
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB

OSHChip
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_oshchip`
      - External
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB

RedBearLab
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_redBearLabBLENano`
      - On-board
      - NRF51822
      - 16MHz
      - 256KB
      - 32KB
    * - :ref:`board_nordicnrf51_redBearLab`
      - On-board
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB

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
    * - :ref:`board_nordicnrf51_seeedArchBLE`
      - On-board
      - NRF51822
      - 16MHz
      - 128KB
      - 16KB
    * - :ref:`board_nordicnrf51_seeedArchLink`
      - On-board
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - :ref:`board_nordicnrf51_seeedTinyBLE`
      - On-board
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB

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
    * - :ref:`board_nordicnrf51_hrm1017`
      - On-board
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
    * - :ref:`board_nordicnrf51_ty51822r3`
      - On-board
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB

VNG
~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_vbluno51`
      - On-board
      - NRF51822
      - 16MHz
      - 128KB
      - 32KB

Waveshare
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_waveshare_ble400`
      - External
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB

ng-beacon
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_ng_beacon`
      - External
      - NRF51822
      - 16MHz
      - 256KB
      - 32KB

sino:bit
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf51_Sinobit`
      - External
      - NRF51822
      - 32MHz
      - 256KB
      - 32KB

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
    * - :ref:`board_nordicnrf51_nrf51822_y5_mbug`
      - On-board
      - NRF51822
      - 16MHz
      - 256KB
      - 16KB
