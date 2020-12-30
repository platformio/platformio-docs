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

.. _platform_espressif8266:

Espressif 8266
==============

:Configuration:
  :ref:`projectconf_env_platform` = ``espressif8266``

Espressif Systems is a privately held fabless semiconductor company. They provide wireless communications and Wi-Fi chips which are widely used in mobile devices and the Internet of Things applications.

For more detailed information please visit `vendor site <https://espressif.com/?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1

.. include:: espressif8266_extra.rst

Examples
--------

Examples are listed from `Espressif 8266 development platform repository <https://github.com/platformio/platform-espressif8266/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `arduino-webserver <https://github.com/platformio/platform-espressif8266/tree/master/examples/arduino-webserver?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-asyncudp <https://github.com/platformio/platform-espressif8266/tree/master/examples/arduino-asyncudp?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-blink <https://github.com/platformio/platform-espressif8266/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs>`_
* `simba-blink <https://github.com/platformio/platform-espressif8266/tree/master/examples/simba-blink?utm_source=platformio.org&utm_medium=docs>`_
* `esp8266-rtos-sdk-blink <https://github.com/platformio/platform-espressif8266/tree/master/examples/esp8266-rtos-sdk-blink?utm_source=platformio.org&utm_medium=docs>`_
* `esp8266-nonos-sdk-blink <https://github.com/platformio/platform-espressif8266/tree/master/examples/esp8266-nonos-sdk-blink?utm_source=platformio.org&utm_medium=docs>`_
* `arduino-wifiscan <https://github.com/platformio/platform-espressif8266/tree/master/examples/arduino-wifiscan?utm_source=platformio.org&utm_medium=docs>`_

Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-espressif8266/releases>`__
of Espressif 8266 development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version
    [env:latest_stable]
    platform = espressif8266
    board = ...

    ; Custom stable version
    [env:custom_stable]
    platform = espressif8266@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-espressif8266.git
    board = ...


Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-arduinoespressif8266 <https://github.com/esp8266/Arduino.git?utm_source=platformio.org&utm_medium=docs>`__
      - Arduino Wiring-based Framework for Espressif ESP8266 microcontrollers

    * - `framework-esp8266-nonos-sdk <https://github.com/espressif/ESP8266_NONOS_SDK.git?utm_source=platformio.org&utm_medium=docs>`__
      - Espressif ESP8266 Non-OS SDK

    * - `framework-esp8266-rtos-sdk <https://github.com/espressif/ESP8266_RTOS_SDK.git?utm_source=platformio.org&utm_medium=docs>`__
      - Espressif ESP8266 SDK based on FreeRTOS

    * - `framework-simba <https://github.com/eerimoq/simba.git?utm_source=platformio.org&utm_medium=docs>`__
      - Simba is an Embedded Programming Platform. It aims to make embedded programming easy and portable

    * - `tool-esptool <https://github.com/igrr/esptool-ck.git?utm_source=platformio.org&utm_medium=docs>`__
      - Espressif ESP8266 build/flash helper tool

    * - `tool-esptoolpy <https://github.com/espressif/esptool.git?utm_source=platformio.org&utm_medium=docs>`__
      - Espressif ESP8266 and ESP32 serial bootloader utility

    * - `tool-mklittlefs <https://github.com/earlephilhower/mklittlefs.git?utm_source=platformio.org&utm_medium=docs>`__
      - Utility for creating littlefs images for upload on the ESP8266

    * - `tool-mkspiffs <https://github.com/igrr/mkspiffs.git?utm_source=platformio.org&utm_medium=docs>`__
      - Tool to build and unpack SPIFFS images

    * - `toolchain-xtensa <https://github.com/jcmvbkbc/gcc-xtensa.git?utm_source=platformio.org&utm_medium=docs>`__
      - GCC Toolchain for Xtensa processor

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

    * - :ref:`framework_esp8266-nonos-sdk`
      - The non-OS SDK provides a set of application programming interfaces (APIs) for core ESP8266 functionalities such as data reception/transmission over Wi-Fi, TCP/IP stack functions, hardware interface functions and basic system management functions

    * - :ref:`framework_esp8266-rtos-sdk`
      - ESP8266 SDK based on FreeRTOS, a truly free professional grade RTOS for microcontrollers

    * - :ref:`framework_simba`
      - Simba is an RTOS and build framework with aims to make embedded programming easy and portable

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll the tables below by
      horizontally.

4D Systems
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_gen4iod`
      - No
      - ESP8266
      - 80MHz
      - 512KB
      - 80KB

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
    * - :ref:`board_espressif8266_huzzah`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

Amperka
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_wifi_slot`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

DigiStump
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_oak`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

Doit
~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_espmxdevkit`
      - No
      - ESP8266
      - 80MHz
      - 1MB
      - 80KB
    * - :ref:`board_espressif8266_espduino`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

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
    * - :ref:`board_espressif8266_espectro`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

ESPert
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_espresso_lite_v1`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_espressif8266_espresso_lite_v2`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

ESPino
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_espino`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

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
    * - :ref:`board_espressif8266_esp_wroom_02`
      - No
      - ESP8266
      - 80MHz
      - 2MB
      - 80KB
    * - :ref:`board_espressif8266_esp12e`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_espressif8266_esp01_1m`
      - No
      - ESP8266
      - 80MHz
      - 1MB
      - 80KB
    * - :ref:`board_espressif8266_esp01`
      - No
      - ESP8266
      - 80MHz
      - 512KB
      - 80KB
    * - :ref:`board_espressif8266_esp07`
      - No
      - ESP8266
      - 80MHz
      - 1MB
      - 80KB
    * - :ref:`board_espressif8266_esp07s`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_espressif8266_esp8285`
      - No
      - ESP8266
      - 80MHz
      - 1MB
      - 80KB
    * - :ref:`board_espressif8266_phoenix_v1`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_espressif8266_phoenix_v2`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_espressif8266_wifinfo`
      - No
      - ESP8266
      - 80MHz
      - 1MB
      - 80KB

Heltec
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_heltec_wifi_kit_8`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

ITEAD
~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_sonoff_basic`
      - No
      - ESP8266
      - 80MHz
      - 1MB
      - 80KB
    * - :ref:`board_espressif8266_sonoff_s20`
      - No
      - ESP8266
      - 80MHz
      - 1MB
      - 80KB
    * - :ref:`board_espressif8266_sonoff_sv`
      - No
      - ESP8266
      - 80MHz
      - 1MB
      - 80KB
    * - :ref:`board_espressif8266_sonoff_th`
      - No
      - ESP8266
      - 80MHz
      - 1MB
      - 80KB

Invent One
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_inventone`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

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
    * - :ref:`board_espressif8266_nodemcu`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_espressif8266_nodemcuv2`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

Olimex
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_modwifi`
      - No
      - ESP8266
      - 80MHz
      - 2MB
      - 80KB

Schirmilabs
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_eduinowifi`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

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
    * - :ref:`board_espressif8266_wio_link`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_espressif8266_wio_node`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

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
    * - :ref:`board_espressif8266_sparkfunBlynk`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_espressif8266_thing`
      - No
      - ESP8266
      - 80MHz
      - 512KB
      - 80KB
    * - :ref:`board_espressif8266_thingdev`
      - No
      - ESP8266
      - 80MHz
      - 512KB
      - 80KB

SweetPea
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_esp210`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

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
    * - :ref:`board_espressif8266_espinotee`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

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
    * - :ref:`board_espressif8266_d1`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_espressif8266_d1_mini`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_espressif8266_d1_mini_lite`
      - No
      - ESP8266
      - 80MHz
      - 1MB
      - 80KB
    * - :ref:`board_espressif8266_d1_mini_pro`
      - No
      - ESP8266
      - 80MHz
      - 16MB
      - 80KB

WifiDuino
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_wifiduino`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

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
    * - :ref:`board_espressif8266_xinabox_cw01`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
