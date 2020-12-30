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

For more detailed information please visit `vendor site <https://www.microchip.com/design-centers/32-bit?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `Atmel SAM development platform repository <https://github.com/platformio/platform-atmelsam/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `mbed-blink <https://github.com/platformio/platform-atmelsam/tree/master/examples/mbed-blink?utm_source=platformio.org&utm_medium=docs>`_
* `mbed-serial <https://github.com/platformio/platform-atmelsam/tree/master/examples/mbed-serial?utm_source=platformio.org&utm_medium=docs>`_
* `zephyr-blink <https://github.com/platformio/platform-atmelsam/tree/master/examples/zephyr-blink?utm_source=platformio.org&utm_medium=docs>`_
* `zephyr-subsys-logger <https://github.com/platformio/platform-atmelsam/tree/master/examples/zephyr-subsys-logger?utm_source=platformio.org&utm_medium=docs>`_
* `mbed-events <https://github.com/platformio/platform-atmelsam/tree/master/examples/mbed-events?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-blink <https://github.com/platformio/platform-atmelsam/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs>`_
* `simba-blink <https://github.com/platformio/platform-atmelsam/tree/master/examples/simba-blink?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-internal-libs <https://github.com/platformio/platform-atmelsam/tree/master/examples/arduino-internal-libs?utm_source=platformio.org&utm_medium=docs>`_
* `zephyr-drivers-lcd-hd44780 <https://github.com/platformio/platform-atmelsam/tree/master/examples/zephyr-drivers-lcd-hd44780?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-external-libs <https://github.com/platformio/platform-atmelsam/tree/master/examples/arduino-external-libs?utm_source=platformio.org&utm_medium=docs>`_
* `mbed-dsp <https://github.com/platformio/platform-atmelsam/tree/master/examples/mbed-dsp?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-web-thing-led <https://github.com/platformio/platform-atmelsam/tree/master/examples/arduino-web-thing-led?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-briki-internal-libs <https://github.com/platformio/platform-atmelsam/tree/master/examples/arduino-briki-internal-libs?utm_source=platformio.org&utm_medium=docs>`_

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
    * - :ref:`board_atmelsam_samc21_xpro`
      - SAMC21J18A
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
    * - :ref:`board_atmelsam_adafruit_blm_badge`
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
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
    * - :ref:`board_atmelsam_adafruit_feather_m4_can`
      - SAME51J19A
      - 120MHz
      - 496KB
      - 192KB
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
      - SAMD51G19A
      - 120MHz
      - 496KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_matrix_portal_m4`
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
    * - :ref:`board_atmelsam_adafruit_pyportal_m4_titano`
      - SAMD51J20A
      - 120MHz
      - 1MB
      - 256KB
    * - :ref:`board_atmelsam_adafruit_qt_py_m0`
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
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
    * - :ref:`board_atmelsam_mkrwan1310`
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
    * - :ref:`board_atmelsam_briki_abc_samd21`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_briki_mbcwb_samd21`
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
    * - :ref:`board_atmelsam_seeed_femto`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_seeeduino_lorawan`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_seeed_wio_lite_mg126`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_seeed_wio_terminal`
      - SAMD51P19A
      - 120MHz
      - 496KB
      - 192KB
    * - :ref:`board_atmelsam_seeed_xiao`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_seeed_zero`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sparkfun_samd21_9dof`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sparkfun_qwiic_micro_samd21e`
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sparkfun_redboard_turbo`
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
    * - :ref:`board_atmelsam_sparkfun_samd21_proRF`
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sparkfun_samd51_thing_plus`
      - SAMD51J20A
      - 120MHz
      - 496KB
      - 192KB
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

    * - `framework-arduino-mbcwb <https://briki.org?utm_source=platformio.org&utm_medium=docs>`__
      - Fork of Arduino Framework for briki MBC-WB boards

    * - `framework-arduino-sam <https://www.arduino.cc/reference/en?utm_source=platformio.org&utm_medium=docs>`__
      - The official Arduino Wiring-based Framework for ATSAM3 microcontrollers

    * - `framework-arduino-samd <https://www.arduino.cc/reference/en?utm_source=platformio.org&utm_medium=docs>`__
      - The official Arduino Wiring-based Framework for Microchip SAM D microcontrollers

    * - `framework-arduino-samd-adafruit <https://github.com/adafruit/ArduinoCore-samd.git?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for Microchip SAM D microcontrollers (Adafruit SAMD Core)

    * - `framework-arduino-samd-moteino <https://github.com/LowPowerLab/Arduino.git?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for Microchip SAM D microcontrollers (Moteino SAMD Core)

    * - `framework-arduino-samd-reprap <https://github.com/brupje/ArduinoCore-samd.git?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for Microchip SAM D microcontrollers (RepRap SAMD Core)

    * - `framework-arduino-samd-seeed <https://github.com/Seeed-Studio/ArduinoCore-samd.git?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for Microchip SAM D microcontrollers (Seeed SAMD Core)

    * - `framework-arduino-samd-sodaq <https://github.com/SodaqMoja/SodaqCore-samd.git?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for Microchip SAM D microcontrollers (SODAQ SAMD Core)

    * - `framework-arduino-samd-sparkfun <https://github.com/sparkfun/Arduino_Boards/tree/master/sparkfun/samd.git?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for Microchip SAM D microcontrollers (SparkFun SAMD Core)

    * - `framework-arduino-samd-tuino0 <https://github.com/gimasi/TUINO_ZERO_96/tree/master/arduino_ide.git?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for Microchip SAM D microcontrollers (Tuino0 SAMD Core)

    * - `framework-cmsis <http://www.arm.com/products/processors/cortex-m/cortex-microcontroller-software-interface-standard.php?utm_source=platformio.org&utm_medium=docs>`__
      - Vendor-independent hardware abstraction layer for the Cortex-M processor series

    * - `framework-cmsis-atmel <https://github.com/arduino/ArduinoModule-CMSIS-Atmel.git?utm_source=platformio.org&utm_medium=docs>`__
      - Atmel Smart ARM devices CMSIS module

    * - `framework-mbed <http://mbed.org?utm_source=platformio.org&utm_medium=docs>`__
      - Arm Mbed OS is a platform operating system designed for the internet of things

    * - `framework-simba <https://github.com/eerimoq/simba.git?utm_source=platformio.org&utm_medium=docs>`__
      - Simba is an Embedded Programming Platform. It aims to make embedded programming easy and portable

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

    * - `framework-zephyr-hal-atmel <https://github.com/zephyrproject-rtos/hal_atmel.git?utm_source=platformio.org&utm_medium=docs>`__
      - Atmel SAM HAL for Zephyr framework

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

    * - `tool-avrdude <http://savannah.nongnu.org/projects/avrdude?utm_source=platformio.org&utm_medium=docs>`__
      - AVRDUDE is a utility to download/upload/manipulate the ROM and EEPROM contents of AVR microcontrollers

    * - `tool-bossac <https://github.com/shumatech/BOSSA.git?utm_source=platformio.org&utm_medium=docs>`__
      - Basic Open Source SAM-BA Application (BOSSA)

    * - `tool-cmake <https://cmake.org?utm_source=platformio.org&utm_medium=docs>`__
      - CMake is an open-source, cross-platform family of tools designed to build, test and package software

    * - `tool-dtc <https://git.kernel.org/pub/scm/utils/dtc/dtc.git?utm_source=platformio.org&utm_medium=docs>`__
      - Device tree compiler

    * - `tool-gperf <https://www.gnu.org/software/gperf?utm_source=platformio.org&utm_medium=docs>`__
      - GNU gperf is a perfect hash function generator

    * - `tool-jlink <https://www.segger.com/downloads/jlink/?utm_source=platformio.org&utm_medium=docs>`__
      - Software and Documentation Pack for SEGGER J-Link debug probes

    * - `tool-mbctool <https://briki.org?utm_source=platformio.org&utm_medium=docs>`__
      - MBC-WB Uploader Application

    * - `tool-ninja <https://ninja-build.org?utm_source=platformio.org&utm_medium=docs>`__
      - Ninja is a small build system with a focus on speed

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

    * - :ref:`framework_simba`
      - Simba is an RTOS and build framework with aims to make embedded programming easy and portable

    * - :ref:`framework_zephyr`
      - The Zephyr Project is a scalable real-time operating system (RTOS) supporting multiple hardware architectures, optimized for resource constrained devices, and built with safety and security in mind

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll the tables below by
      horizontally.

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
    * - :ref:`board_atmelsam_adafruit_blm_badge`
      - External
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
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
    * - :ref:`board_atmelsam_adafruit_feather_m4_can`
      - External
      - SAME51J19A
      - 120MHz
      - 496KB
      - 192KB
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
      - SAMD51G19A
      - 120MHz
      - 496KB
      - 192KB
    * - :ref:`board_atmelsam_adafruit_matrix_portal_m4`
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
    * - :ref:`board_atmelsam_adafruit_pyportal_m4_titano`
      - External
      - SAMD51J20A
      - 120MHz
      - 1MB
      - 256KB
    * - :ref:`board_atmelsam_adafruit_qt_py_m0`
      - External
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
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
    * - :ref:`board_atmelsam_mkrwan1310`
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
    * - :ref:`board_atmelsam_samc21_xpro`
      - On-board
      - SAMC21J18A
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
    * - :ref:`board_atmelsam_seeed_femto`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_seeeduino_lorawan`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_seeed_wio_lite_mg126`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_seeed_wio_terminal`
      - External
      - SAMD51P19A
      - 120MHz
      - 496KB
      - 192KB
    * - :ref:`board_atmelsam_seeed_xiao`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_seeed_zero`
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
    * - :ref:`board_atmelsam_sparkfun_samd21_9dof`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sparkfun_qwiic_micro_samd21e`
      - External
      - SAMD21E18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sparkfun_redboard_turbo`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
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
    * - :ref:`board_atmelsam_sparkfun_samd21_proRF`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_sparkfun_samd51_thing_plus`
      - External
      - SAMD51J20A
      - 120MHz
      - 496KB
      - 192KB

meteca
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelsam_briki_abc_samd21`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
    * - :ref:`board_atmelsam_briki_mbcwb_samd21`
      - External
      - SAMD21G18A
      - 48MHz
      - 256KB
      - 32KB
