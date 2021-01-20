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

.. _platform_nordicnrf52:

Nordic nRF52
============

:Configuration:
  :ref:`projectconf_env_platform` = ``nordicnrf52``

The nRF52 Series are built for speed to carry out increasingly complex tasks in the shortest possible time and return to sleep, conserving precious battery power. They have a Cortex-M4F processor and are the most capable Bluetooth Smart SoCs on the market.

For more detailed information please visit `vendor site <https://www.nordicsemi.com/Products/nRF52-Series-SoC?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1

.. include:: nordicnrf52_extra.rst

Examples
--------

Examples are listed from `Nordic nRF52 development platform repository <https://github.com/platformio/platform-nordicnrf52/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `zephyr-blink <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/zephyr-blink?utm_source=platformio.org&utm_medium=docs>`_
* `zephyr-net-echo-client <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/zephyr-net-echo-client?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-blink <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-ble-led <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/arduino-ble-led?utm_source=platformio.org&utm_medium=docs>`_
* `mbed-rtos-blink-baremetal <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/mbed-rtos-blink-baremetal?utm_source=platformio.org&utm_medium=docs>`_
* `zephyr-ble-beacon <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/zephyr-ble-beacon?utm_source=platformio.org&utm_medium=docs>`_
* `zephyr-subsys-nvs <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/zephyr-subsys-nvs?utm_source=platformio.org&utm_medium=docs>`_
* `mbed-rtos-nfc <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/mbed-rtos-nfc?utm_source=platformio.org&utm_medium=docs>`_
* `mbed-legacy-examples <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/mbed-legacy-examples?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-nina-b1-generic-example <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/arduino-nina-b1-generic-example?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-bluefruit-bleuart <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/arduino-bluefruit-bleuart?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-serial-plotter <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/arduino-serial-plotter?utm_source=platformio.org&utm_medium=docs>`_
* `mbed-rtos-ble-thermometer <https://github.com/platformio/platform-nordicnrf52/tree/master/examples/mbed-rtos-ble-thermometer?utm_source=platformio.org&utm_medium=docs>`_

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
    * - :ref:`board_nordicnrf52_bbcmicrobit_v2`
      - NRF52833
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_laird_bl652_dvk`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_laird_bl654_dvk`
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf52_delta_dfbm_nq620`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_electronut_blip`
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf52_electronut_papyr`
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf52_nrf52832_mdk`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_nrf52840_mdk`
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf52_nrf52_dk`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_nrf52840_dk`
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf52_nrf52840_dk_adafruit`
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_reel_board`
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf52_reel_board_v2`
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf52_redbear_blenano2`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_redbear_blend2`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_vbluno52`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_dwm1001_dev`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_ublox_evk_nina_b1`
      - NRF52832
      - 64MHz
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
    * - :ref:`board_nordicnrf52_96b_nitrogen`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_adafruit_feather_nrf52832`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_adafruit_clue_nrf52840`
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_adafruit_feather_nrf52840_sense`
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_adafruit_feather_nrf52840`
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_nano33ble`
      - NRF52840
      - 64MHz
      - 960KB
      - 256KB
    * - :ref:`board_nordicnrf52_bluey`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_adafruit_cplaynrf52840`
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_holyiot_yj16019`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_adafruit_itsybitsy_nrf52840`
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_laird_pinnacle_100_dvk`
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf52_adafruit_metro_nrf52840`
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_thingy_52`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_particle_argon`
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_particle_boron`
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_particle_xenon`
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_raytac_mdbt50q_rx`
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_ruuvitag`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_sdt52832b`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_stct_nrf52_minidev`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_hackaBLE`
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-nordicnrf52/releases>`__
of Nordic nRF52 development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = nordicnrf52
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = nordicnrf52@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-nordicnrf52.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-arduino-nrf52-mbedos <https://www.arduino.cc/reference/en?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino framework supporting mbed-enabled boards

    * - `framework-arduinoadafruitnrf52 <https://github.com/adafruit/Adafruit_nRF52_Arduino.git?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for Nordic Semiconductor nRF52 BLE SoC

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

    * - `tool-bossac-nordicnrf52 <https://github.com/shumatech/BOSSA.git?utm_source=platformio.org&utm_medium=docs>`__
      - Basic Open Source SAM-BA Application (BOSSA) for Nordic nRF52 microcontrollers

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

96Boards
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_96b_nitrogen`
      - External
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

Adafruit
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_adafruit_feather_nrf52832`
      - External
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_adafruit_clue_nrf52840`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_adafruit_feather_nrf52840_sense`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_adafruit_feather_nrf52840`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_adafruit_cplaynrf52840`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_adafruit_itsybitsy_nrf52840`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_adafruit_metro_nrf52840`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB

Arduino
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_nano33ble`
      - External
      - NRF52840
      - 64MHz
      - 960KB
      - 256KB

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
    * - :ref:`board_nordicnrf52_bbcmicrobit_v2`
      - On-board
      - NRF52833
      - 64MHz
      - 512KB
      - 64KB

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
    * - :ref:`board_nordicnrf52_delta_dfbm_nq620`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

Electronut Labs
~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_bluey`
      - External
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_hackaBLE`
      - External
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

ElectronutLabs
~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_electronut_blip`
      - On-board
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf52_electronut_papyr`
      - On-board
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB

Holyiot
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_holyiot_yj16019`
      - External
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

Laird Connectivity
~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_laird_bl652_dvk`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_laird_bl654_dvk`
      - On-board
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf52_laird_pinnacle_100_dvk`
      - External
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB

Makerdiary
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_nrf52832_mdk`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_nrf52840_mdk`
      - On-board
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB

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
    * - :ref:`board_nordicnrf52_thingy_52`
      - External
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_nrf52_dk`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_nrf52840_dk`
      - On-board
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf52_nrf52840_dk_adafruit`
      - On-board
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB

PHYTEC
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_reel_board`
      - On-board
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB
    * - :ref:`board_nordicnrf52_reel_board_v2`
      - On-board
      - NRF52840
      - 64MHz
      - 1MB
      - 256KB

Particle
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_particle_argon`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_particle_boron`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB
    * - :ref:`board_nordicnrf52_particle_xenon`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB

Raytac
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_raytac_mdbt50q_rx`
      - External
      - NRF52840
      - 64MHz
      - 796KB
      - 243KB

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
    * - :ref:`board_nordicnrf52_redbear_blenano2`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
    * - :ref:`board_nordicnrf52_redbear_blend2`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

Ruuvi
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_ruuvitag`
      - External
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

Sigma Delta Technologies
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_sdt52832b`
      - External
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

Taida Century
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_stct_nrf52_minidev`
      - External
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

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
    * - :ref:`board_nordicnrf52_vbluno52`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

decaWave
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_nordicnrf52_dwm1001_dev`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB

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
    * - :ref:`board_nordicnrf52_ublox_evk_nina_b1`
      - On-board
      - NRF52832
      - 64MHz
      - 512KB
      - 64KB
