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

.. _platform_atmelsam:

Atmel SAM
=========

:Configuration:
  :ref:`projectconf_env_platform` = ``atmelsam``

Atmel | SMART offers Flash- based ARM products based on the ARM Cortex-M0+, Cortex-M3 and Cortex-M4 architectures, ranging from 8KB to 2MB of Flash including a rich peripheral and feature mix.

For more detailed information please visit `vendor site <http://www.atmel.com/products/microcontrollers/arm/default.aspx?utm_source=platformio&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `Atmel SAM development platform repository <https://github.com/platformio/platform-atmelsam/tree/master/examples?utm_source=platformio&utm_medium=docs>`_:

* `mbed-blink <https://github.com/platformio/platform-atmelsam/tree/master/examples/mbed-blink?utm_source=platformio&utm_medium=docs>`_
* `mbed-serial <https://github.com/platformio/platform-atmelsam/tree/master/examples/mbed-serial?utm_source=platformio&utm_medium=docs>`_
* `zephyr-blink <https://github.com/platformio/platform-atmelsam/tree/master/examples/zephyr-blink?utm_source=platformio&utm_medium=docs>`_
* `zephyr-drivers-i2c-scanner <https://github.com/platformio/platform-atmelsam/tree/master/examples/zephyr-drivers-i2c-scanner?utm_source=platformio&utm_medium=docs>`_
* `zephyr-subsys-logger <https://github.com/platformio/platform-atmelsam/tree/master/examples/zephyr-subsys-logger?utm_source=platformio&utm_medium=docs>`_
* `mbed-events <https://github.com/platformio/platform-atmelsam/tree/master/examples/mbed-events?utm_source=platformio&utm_medium=docs>`_
* `arduino-blink <https://github.com/platformio/platform-atmelsam/tree/master/examples/arduino-blink?utm_source=platformio&utm_medium=docs>`_
* `simba-blink <https://github.com/platformio/platform-atmelsam/tree/master/examples/simba-blink?utm_source=platformio&utm_medium=docs>`_
* `arduino-internal-libs <https://github.com/platformio/platform-atmelsam/tree/master/examples/arduino-internal-libs?utm_source=platformio&utm_medium=docs>`_
* `arduino-external-libs <https://github.com/platformio/platform-atmelsam/tree/master/examples/arduino-external-libs?utm_source=platformio&utm_medium=docs>`_
* `mbed-dsp <https://github.com/platformio/platform-atmelsam/tree/master/examples/mbed-dsp?utm_source=platformio&utm_medium=docs>`_
* `arduino-web-thing-led <https://github.com/platformio/platform-atmelsam/tree/master/examples/arduino-web-thing-led?utm_source=platformio&utm_medium=docs>`_

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
    * - :ref:`board_atmelsam_mzeropro`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_zero`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_samr21_xpro`
      - SAMR21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_samd21g18a`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_samd21_xpro`
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_saml21_xpro_b`
      - SAML21J18B
      - 48MHz
      - 256KB
      - 32KB


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
    * - :ref:`board_atmelsam_adafruit_circuitplayground_m0`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_crickit_m0`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_feather_m0`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_feather_m0_express`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_feather_m4`
      - SAMD51J19A
      - 120MHz
      - 512KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_gemma_m0`
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_grandcentral_m4`
      - SAMD51P20A
      - 120MHz
      - 1MB
      - 256KB
    * - :ref:`board_atmelsam_adafruit_hallowing`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_hallowing_m4`
      - SAMD51J19A
      - 120MHz
      - 496KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_itsybitsy_m0`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_itsybitsy_m4`
      - SAMD51G19A
      - 120MHz
      - 512KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_monster_m4sk`
      - SAMD51J19A
      - 120MHz
      - 496KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_metro_m0`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_metro_m4`
      - SAMD51J19A
      - 120MHz
      - 512KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_metro_m4_airliftlite`
      - SAMD51J19A
      - 120MHz
      - 512KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_pygamer_advance_m4`
      - SAMD51J20A
      - 120MHz
      - 1MB
      - 256KB
    * - :ref:`board_atmelsam_adafruit_pygamer_m4`
      - SAMD51J19A
      - 120MHz
      - 512KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_pyportal_m4`
      - SAMD51J20A
      - 120MHz
      - 1MB
      - 256KB
    * - :ref:`board_atmelsam_adafruit_trellis_m4`
      - SAMD51J19A
      - 120MHz
      - 512KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_trinket_m0`
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_pirkey`
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_pybadge_airlift_m4`
      - SAMD51J20A
      - 120MHz
      - 1008KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_pybadge_m4`
      - SAMD51J19A
      - 120MHz
      - 512KB
      - 192KB
    * - :ref:`board_atmelsam_due`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_atmelsam_dueUSB`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_atmelsam_mzeroUSB`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mzeroproUSB`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrfox1200`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrgsm1400`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrnb1500`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrwan1300`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrwifi1010`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkr1000USB`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrzero`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_tian`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_zeroUSB`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_digix`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_atmelsam_mkrvidor4000`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_macchina2`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_atmelsam_minitronics20`
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_moteino_zero`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_nano_33_iot`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sodaq_autonomo`
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sodaq_explorer`
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sodaq_one`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sodaq_sara`
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sodaq_sff`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sainSmartDue`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_atmelsam_sainSmartDueUSB`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_atmelsam_seeeduino_lorawan`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sparkfun_samd21_dev_usb`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sparkfun_samd21_mini_usb`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_tuinozero96`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-atmelsam/releases>`__
of Atmel SAM development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = atmelsam
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = atmelsam@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-atmelsam.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-arduinosam <http://arduino.cc/en/Reference/HomePage?utm_source=platformio&utm_medium=docs>`__
      - Arduino Wiring-based Framework (SAM Core)

    * - `framework-mbed <http://mbed.org?utm_source=platformio&utm_medium=docs>`__
      - mbed Framework

    * - `framework-simba <https://github.com/eerimoq/simba?utm_source=platformio&utm_medium=docs>`__
      - Simba Framework

    * - `framework-zephyr <https://github.com/zephyrproject-rtos/zephyr?utm_source=platformio&utm_medium=docs>`__
      - Primary Git Repository for the Zephyr Project. Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures.

    * - `framework-zephyr-civetweb <https://github.com/zephyrproject-rtos/civetweb?utm_source=platformio&utm_medium=docs>`__
      - Zephyr module CivetWeb Embedded C/C++ web server

    * - `framework-zephyr-fatfs <https://github.com/zephyrproject-rtos/fatfs?utm_source=platformio&utm_medium=docs>`__
      - Zephyr module for FATFS filesystem

    * - `framework-zephyr-hal-atmel <https://github.com/zephyrproject-rtos/hal_atmel?utm_source=platformio&utm_medium=docs>`__
      - Atmel SAM HAL for Zephyr framework

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

    * - `tool-avrdude <http://www.nongnu.org/avrdude/?utm_source=platformio&utm_medium=docs>`__
      - AVRDUDE

    * - `tool-bossac <https://sourceforge.net/projects/b-o-s-s-a/?utm_source=platformio&utm_medium=docs>`__
      - BOSSA CLI

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

    * - `tool-openocd <http://openocd.org?utm_source=platformio&utm_medium=docs>`__
      - OpenOCD

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

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences.

    * - :ref:`framework_mbed`
      - The mbed framework The mbed SDK has been designed to provide enough hardware abstraction to be intuitive and concise, yet powerful enough to build complex projects. It is built on the low-level ARM CMSIS APIs, allowing you to code down to the metal if needed. In addition to RTOS, USB and Networking libraries, a cookbook of hundreds of reusable peripheral and module libraries have been built on top of the SDK by the mbed Developer Community.

    * - :ref:`framework_simba`
      - Simba is an RTOS and build framework. It aims to make embedded programming easy and portable.

    * - :ref:`framework_zephyr`
      - The Zephyr Project is a scalable real-time operating system (RTOS) supporting multiple hardware architectures, optimized for resource constrained devices, and built with safety and security in mind.

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by
      horizontal.

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
    * - :ref:`board_atmelsam_adafruit_circuitplayground_m0`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_crickit_m0`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_feather_m0`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_feather_m0_express`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_feather_m4`
      - External
      - SAMD51J19A
      - 120MHz
      - 512KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_gemma_m0`
      - External
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_grandcentral_m4`
      - External
      - SAMD51P20A
      - 120MHz
      - 1MB
      - 256KB
    * - :ref:`board_atmelsam_adafruit_hallowing`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_hallowing_m4`
      - External
      - SAMD51J19A
      - 120MHz
      - 496KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_itsybitsy_m0`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_itsybitsy_m4`
      - External
      - SAMD51G19A
      - 120MHz
      - 512KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_monster_m4sk`
      - External
      - SAMD51J19A
      - 120MHz
      - 496KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_metro_m0`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_metro_m4`
      - External
      - SAMD51J19A
      - 120MHz
      - 512KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_metro_m4_airliftlite`
      - External
      - SAMD51J19A
      - 120MHz
      - 512KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_pygamer_advance_m4`
      - External
      - SAMD51J20A
      - 120MHz
      - 1MB
      - 256KB
    * - :ref:`board_atmelsam_adafruit_pygamer_m4`
      - External
      - SAMD51J19A
      - 120MHz
      - 512KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_pyportal_m4`
      - External
      - SAMD51J20A
      - 120MHz
      - 1MB
      - 256KB
    * - :ref:`board_atmelsam_adafruit_trellis_m4`
      - External
      - SAMD51J19A
      - 120MHz
      - 512KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_trinket_m0`
      - External
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_pirkey`
      - External
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_adafruit_pybadge_airlift_m4`
      - External
      - SAMD51J20A
      - 120MHz
      - 1008KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_pybadge_m4`
      - External
      - SAMD51J19A
      - 120MHz
      - 512KB
      - 192KB

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
    * - :ref:`board_atmelsam_due`
      - External
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_atmelsam_dueUSB`
      - External
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_atmelsam_mzeroUSB`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mzeroproUSB`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mzeropro`
      - On-board
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrfox1200`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrgsm1400`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrnb1500`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrwan1300`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrwifi1010`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkr1000USB`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrzero`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_tian`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_zero`
      - On-board
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_zeroUSB`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_mkrvidor4000`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_nano_33_iot`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB

Atmel
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelsam_samr21_xpro`
      - On-board
      - SAMR21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_samd21g18a`
      - On-board
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_samd21_xpro`
      - On-board
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_saml21_xpro_b`
      - On-board
      - SAML21J18B
      - 48MHz
      - 256KB
      - 32KB

Digistump
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelsam_digix`
      - External
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB

Gimasi
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelsam_tuinozero96`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB

LowPowerLab
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelsam_current_ranger`
      - No
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_moteino_zero`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB

Macchina
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelsam_macchina2`
      - External
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB

ReprapWorld
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelsam_minitronics20`
      - External
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB

SODAQ
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelsam_sodaq_autonomo`
      - External
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sodaq_explorer`
      - External
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sodaq_one`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sodaq_sara`
      - External
      - SAMD21J18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sodaq_sff`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB

SainSmart
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelsam_sainSmartDue`
      - External
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_atmelsam_sainSmartDueUSB`
      - External
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB

Seeed
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelsam_seeeduino_lorawan`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB

SparkFun
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelsam_sparkfun_samd21_dev_usb`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sparkfun_samd21_mini_usb`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
