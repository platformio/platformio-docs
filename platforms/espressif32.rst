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

.. _platform_espressif32:

Espressif 32
============

:Configuration:
  :ref:`projectconf_env_platform` = ``espressif32``

Espressif Systems is a privately held fabless semiconductor company. They provide wireless communications and Wi-Fi chips which are widely used in mobile devices and the Internet of Things applications.

For more detailed information please visit `vendor site <https://espressif.com/?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1

.. include:: espressif32_extra.rst

Examples
--------

Examples are listed from `Espressif 32 development platform repository <https://github.com/platformio/platform-espressif32/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `espidf-storage-sdcard <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-storage-sdcard?utm_source=platformio.org&utm_medium=docs>`_
* `espidf-blink <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-blink?utm_source=platformio.org&utm_medium=docs>`_
* `espidf-coap-server <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-coap-server?utm_source=platformio.org&utm_medium=docs>`_
* `espidf-exceptions <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-exceptions?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-blink <https://github.com/platformio/platform-espressif32/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs>`_
* `simba-blink <https://github.com/platformio/platform-espressif32/tree/master/examples/simba-blink?utm_source=platformio.org&utm_medium=docs>`_
* `espidf-ble-eddystone <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-ble-eddystone?utm_source=platformio.org&utm_medium=docs>`_
* `espidf-ulp-adc <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-ulp-adc?utm_source=platformio.org&utm_medium=docs>`_
* `espidf-ulp-pulse <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-ulp-pulse?utm_source=platformio.org&utm_medium=docs>`_
* `espidf-arduino-wifiscan <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-arduino-wifiscan?utm_source=platformio.org&utm_medium=docs>`_
* `espidf-http-request <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-http-request?utm_source=platformio.org&utm_medium=docs>`_
* `espidf-arduino-blink <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-arduino-blink?utm_source=platformio.org&utm_medium=docs>`_
* `pumbaa-blink <https://github.com/platformio/platform-espressif32/tree/master/examples/pumbaa-blink?utm_source=platformio.org&utm_medium=docs>`_
* `espidf-hello-world <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-hello-world?utm_source=platformio.org&utm_medium=docs>`_
* `espidf-aws-iot <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-aws-iot?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-briki-internal-libs <https://github.com/platformio/platform-espressif32/tree/master/examples/arduino-briki-internal-libs?utm_source=platformio.org&utm_medium=docs>`_
* `espidf-peripherals-uart <https://github.com/platformio/platform-espressif32/tree/master/examples/espidf-peripherals-uart?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-wifiscan <https://github.com/platformio/platform-espressif32/tree/master/examples/arduino-wifiscan?utm_source=platformio.org&utm_medium=docs>`_

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. contents::
    :local:

.. include:: espressif32_debug.rst

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
    * - :ref:`board_espressif32_esp-wrover-kit`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB


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
    * - :ref:`board_espressif32_esp32cam`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_alksesp32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_az-delivery-devkit-v4`
      - ESP32
      - 240MHz
      - 16MB
      - 520KB
    * - :ref:`board_espressif32_featheresp32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_briki_abc_esp32`
      - ESP32
      - 240MHz
      - 3.25MB
      - 320KB
    * - :ref:`board_espressif32_briki_mbc-wb_esp32`
      - ESP32
      - 240MHz
      - 3.25MB
      - 320KB
    * - :ref:`board_espressif32_d-duino-32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32doit-devkit-v1`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_pocket_32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_fm-devkit`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_pico32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32vn-iot-uno`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_espectro32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_espino32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32dev`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_firebeetle32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_frogboard`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_heltec_wifi_lora_32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_heltec_wifi_lora_32_V2`
      - ESP32
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_heltec_wireless_stick`
      - ESP32
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_hornbill32dev`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_hornbill32minima`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_iotaap_magnolia`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_mhetesp32devkit`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_mhetesp32minikit`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_node32s`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_nodemcu-32s`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-devkitlipo`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-evb`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-gateway`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lopy`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lopy4`
      - ESP32
      - 240MHz
      - 4MB
      - 1.25MB
    * - :ref:`board_espressif32_sg-o_airMon`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_wesp32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32thing`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_sparkfun_lora_gateway_1-channel`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_ttgo-lora32-v1`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_ttgo-lora32-v2`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_ttgo-t-beam`
      - ESP32
      - 240MHz
      - 4MB
      - 1.25MB
    * - :ref:`board_espressif32_ttgo-t1`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_vintlabs-devkit-v1`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lolin_d32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lolin_d32_pro`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lolin32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_wemos_d1_mini32`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_wemosbat`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_xinabox_cw02`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_iotbusio`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_iotbusproteus`
      - ESP32
      - 240MHz
      - 4MB
      - 320KB


Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-espressif32/releases>`__
of Espressif 32 development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = espressif32
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = espressif32@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-espressif32.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-arduino-mbcwb <https://briki.org?utm_source=platformio.org&utm_medium=docs>`__
      - Fork of Arduino Framework for briki MBC-WB boards

    * - `framework-arduinoespressif32 <https://github.com/espressif/arduino-esp32.git?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for Espressif ESP32 microcontrollers

    * - `framework-espidf <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/?utm_source=platformio.org&utm_medium=docs>`__
      - Espressif IoT Development Framework. Official development framework for ESP32 chip

    * - `framework-pumbaa <https://github.com/eerimoq/pumbaa.git?utm_source=platformio.org&utm_medium=docs>`__
      - Pumbaa Framework - a port of MicroPython, designed for embedded devices with limited amount of RAM and code memory

    * - `framework-simba <https://github.com/eerimoq/simba.git?utm_source=platformio.org&utm_medium=docs>`__
      - Simba is an Embedded Programming Platform. It aims to make embedded programming easy and portable

    * - `tool-cmake <https://cmake.org?utm_source=platformio.org&utm_medium=docs>`__
      - CMake is an open-source, cross-platform family of tools designed to build, test and package software

    * - `tool-esptoolpy <https://github.com/espressif/esptool.git?utm_source=platformio.org&utm_medium=docs>`__
      - Espressif ESP8266 and ESP32 serial bootloader utility

    * - `tool-idf <https://github.com/espressif/esp-idf/tree/master/tools.git?utm_source=platformio.org&utm_medium=docs>`__
      - idf is a top-level config/build command line tool for ESP-IDF

    * - `tool-mbctool <https://briki.org?utm_source=platformio.org&utm_medium=docs>`__
      - MBC-WB Uploader Application

    * - `tool-mconf <https://github.com/espressif/kconfig-frontends.git?utm_source=platformio.org&utm_medium=docs>`__
      - Fork of kconfig-frontends project with some modifications for use with ESP-IDF

    * - `tool-mkspiffs <https://github.com/igrr/mkspiffs.git?utm_source=platformio.org&utm_medium=docs>`__
      - Tool to build and unpack SPIFFS images

    * - `tool-ninja <https://ninja-build.org?utm_source=platformio.org&utm_medium=docs>`__
      - Ninja is a small build system with a focus on speed

    * - `tool-openocd-esp32 <http://openocd.org?utm_source=platformio.org&utm_medium=docs>`__
      - Open On-Chip Debugger for Espressif ESP32

    * - `toolchain-esp32s2ulp <https://github.com/espressif/esp-idf.git?utm_source=platformio.org&utm_medium=docs>`__
      - Binutils fork with support for the ESP32-S2 ULP co-processor

    * - `toolchain-esp32ulp <https://github.com/espressif/binutils-esp32ulp.git?utm_source=platformio.org&utm_medium=docs>`__
      - Binutils fork with support for the Espressif ESP32 ULP co-processor

    * - `toolchain-xtensa32 <https://github.com/espressif/crosstool-NG.git?utm_source=platformio.org&utm_medium=docs>`__
      - GCC Toolchain for Xtensa32 processor

    * - `toolchain-xtensa32s2 <https://github.com/espressif/crosstool-NG.git?utm_source=platformio.org&utm_medium=docs>`__
      - GCC Toolchain for Xtensa32-S2 processor

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

    * - :ref:`framework_espidf`
      - ESP-IDF is the official development framework for the ESP32 and ESP32-S Series SoCs.

    * - :ref:`framework_pumbaa`
      - Pumbaa is Python on top of Simba. The implementation is a port of MicroPython, designed for embedded devices with limited amount of RAM and code memory

    * - :ref:`framework_simba`
      - Simba is an RTOS and build framework with aims to make embedded programming easy and portable

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll the tables below by
      horizontally.

AI Thinker
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_esp32cam`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

AZ-Delivery
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_az-delivery-devkit-v4`
      - External
      - ESP32
      - 240MHz
      - 16MB
      - 520KB

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
    * - :ref:`board_espressif32_featheresp32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Aiyarafun
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_node32s`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

April Brother
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_espea32`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

BPI Tech
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_bpi-bit`
      - No
      - ESP32
      - 160MHz
      - 4MB
      - 320KB

DFRobot
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_firebeetle32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

DOIT
~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_esp32doit-devkit-v1`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

DSTIKE
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_d-duino-32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Dongsen Technology
~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_pocket_32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

DycodeX
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_espectro32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

ESP32vn
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_esp32vn-iot-uno`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Electronic SweetPeas
~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_esp320`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Espressif
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_pico32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp-wrover-kit`
      - On-board
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32dev`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Fred
~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_frogboard`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Hardkernel
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_odroid_esp32`
      - No
      - ESP32
      - 240MHz
      - 16MB
      - 320KB

Heltec Automation
~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_heltec_wifi_kit_32`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_heltec_wifi_lora_32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_heltec_wifi_lora_32_V2`
      - External
      - ESP32
      - 240MHz
      - 8MB
      - 320KB
    * - :ref:`board_espressif32_heltec_wireless_stick`
      - External
      - ESP32
      - 240MHz
      - 8MB
      - 320KB

Hornbill
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_hornbill32dev`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_hornbill32minima`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

IntoRobot
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_intorobot`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

IoTaaP
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_iotaap_magnolia`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

M5Stack
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_m5stack-core-esp32`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_m5stack-fire`
      - No
      - ESP32
      - 240MHz
      - 16MB
      - 6.25MB
    * - :ref:`board_espressif32_m5stack-grey`
      - No
      - ESP32
      - 240MHz
      - 16MB
      - 520KB
    * - :ref:`board_espressif32_m5stick-c`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

MH-ET Live
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_mhetesp32devkit`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_mhetesp32minikit`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Magicblocks.io
~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_magicbit`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

MakerAsia
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_nano32`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Microduino
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_microduino-core-esp32`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

NodeMCU
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_nodemcu-32s`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Noduino
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_quantum`
      - No
      - ESP32
      - 240MHz
      - 16MB
      - 320KB

OLIMEX
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_esp32-devkitlipo`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-evb`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-gateway`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-pro`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-poe`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_esp32-poe-iso`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

OROCA
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_oroca_edubot`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Onehorse
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_onehorse32dev`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Pycom Ltd.
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_pycom_gpy`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lopy`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lopy4`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 1.25MB

Qmobot LLP
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_qchip`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

RoboticsBrno
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_alksesp32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

SG-O
~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_sg-o_airMon`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Silicognition
~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_wesp32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

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
    * - :ref:`board_espressif32_sparkfun_lora_gateway_1-channel`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

SparkFun Electronics
~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_esp32thing`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

TTGO
~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_ttgo-lora32-v1`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_ttgo-lora32-v2`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_ttgo-t-beam`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 1.25MB
    * - :ref:`board_espressif32_ttgo-t-watch`
      - No
      - ESP32
      - 240MHz
      - 16MB
      - 320KB
    * - :ref:`board_espressif32_ttgo-t1`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

ThaiEasyElec
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_espino32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

TinyPICO
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_tinypico`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Turta
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_turta_iot_node`
      - No
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Unknown
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_fm-devkit`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

VintLabs
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_vintlabs-devkit-v1`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

WEMOS
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_lolin_d32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lolin_d32_pro`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_lolin32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_wemos_d1_mini32`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_wemosbat`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

Widora
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_widora-air`
      - No
      - ESP32
      - 240MHz
      - 16MB
      - 320KB

XinaBox
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_xinabox_cw02`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

YeaCreate
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_nscreen-32`
      - No
      - ESP32
      - 240MHz
      - 16MB
      - 320KB

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
    * - :ref:`board_espressif32_briki_abc_esp32`
      - External
      - ESP32
      - 240MHz
      - 3.25MB
      - 320KB
    * - :ref:`board_espressif32_briki_mbc-wb_esp32`
      - External
      - ESP32
      - 240MHz
      - 3.25MB
      - 320KB

oddWires
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_iotbusio`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB
    * - :ref:`board_espressif32_iotbusproteus`
      - External
      - ESP32
      - 240MHz
      - 4MB
      - 320KB

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
    * - :ref:`board_espressif32_nina_w10`
      - No
      - ESP32
      - 240MHz
      - 2MB
      - 320KB
