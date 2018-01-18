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
:ref:`projectconf_env_platform` = ``espressif8266``

Espressif Systems is a privately held fabless semiconductor company. They provide wireless communications and Wi-Fi chips which are widely used in mobile devices and the Internet of Things applications.

For more detailed information please visit `vendor site <https://espressif.com/>`_.

.. contents:: Contents
    :local:

Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-arduinoespressif8266 <https://github.com/esp8266/Arduino>`__
      - Arduino Wiring-based Framework (ESP8266 Core)

    * - `framework-esp8266-nonos-sdk <https://github.com/espressif/ESP8266_NONOS_SDK>`__
      - ESP8266 Non-OS SDK

    * - `framework-esp8266-rtos-sdk <https://github.com/espressif/ESP8266_RTOS_SDK>`__
      - ESP8266 SDK based on FreeRTOS

    * - `framework-simba <https://github.com/eerimoq/simba>`__
      - Simba Framework

    * - `sdk-esp8266 <http://bbs.espressif.com>`__
      - ESP8266 SDK

    * - `tool-espotapy <https://github.com/esp8266/Arduino/blob/master/tools/espota.py>`__
      - ESP8266 OTA utility

    * - `tool-esptool <https://github.com/igrr/esptool-ck>`__
      - esptool-ck

    * - `tool-mkspiffs <https://github.com/igrr/mkspiffs>`__
      - Tool to build and unpack SPIFFS images

    * - `toolchain-xtensa <https://github.com/jcmvbkbc/gcc-xtensa>`__
      - xtensa-gcc

.. warning::
    **Linux Users**:

        * Install "udev" rules file `99-platformio-udev.rules <https://github.com/platformio/platformio-core/blob/develop/scripts/99-platformio-udev.rules>`_
          (an instruction is located inside a file).
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

    * - :ref:`framework_esp8266-nonos-sdk`
      - The non-OS SDK provides a set of application programming interfaces (APIs) for core ESP8266 functionalities such as data reception/transmission over Wi-Fi, TCP/IP stack functions, hardware interface functions and basic system management functions.

    * - :ref:`framework_esp8266-rtos-sdk`
      - ESP8266 SDK based on FreeRTOS, a truly free professional grade RTOS for microcontrollers

    * - :ref:`framework_simba`
      - Simba is an RTOS and build framework. It aims to make embedded programming easy and portable.

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <http://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by
      horizontal.

4D Systems
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``gen4iod``
      - `4D Systems gen4 IoD Range <http://www.4dsystems.com.au/product/gen4_IoD/>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 512 Kb
      - 80 Kb

Adafruit
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``huzzah``
      - `Adafruit HUZZAH ESP8266 <https://www.adafruit.com/products/2471>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

DigiStump
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``oak``
      - `DigiStump Oak <http://digistump.com/category/22>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

Doit
~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``espduino``
      - `ESPDuino (ESP-13 Module) <https://www.tindie.com/products/doit/espduinowifi-uno-r3/>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

DycodeX
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``espectro``
      - `ESPectro Core <https://shop.makestro.com/en/product/espectro-core/>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

ESPert
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``espresso_lite_v1``
      - `ESPresso Lite 1.0 <http://www.espert.co>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

    * - ``espresso_lite_v2``
      - `ESPresso Lite 2.0 <http://www.espert.co>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

ESPino
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``espino``
      - `ESPino <http://www.espino.io>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

Espressif
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``esp01``
      - `Espressif Generic ESP8266 ESP-01 512k <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 512 Kb
      - 80 Kb

    * - ``esp01_1m``
      - `Espressif Generic ESP8266 ESP-01 1M <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 1024 Kb
      - 80 Kb

    * - ``esp07``
      - `Espressif Generic ESP8266 ESP-07 <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family#esp-07>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

    * - ``esp12e``
      - `Espressif ESP8266 ESP-12E <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

    * - ``esp8285``
      - `Generic ESP8285 Module <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 448 Kb
      - 80 Kb

    * - ``esp_wroom_02``
      - `ESP-WROOM-02 <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

    * - ``phoenix_v1``
      - `Phoenix 1.0 <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

    * - ``phoenix_v2``
      - `Phoenix 2.0 <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

    * - ``wifinfo``
      - `WifInfo <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 1024 Kb
      - 80 Kb

Heltec
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``heltec_wifi_kit_8``
      - `Heltec Wifi kit 8 <http://www.heltec.cn/project/wifi_kit_8/>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

NodeMCU
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``nodemcu``
      - `NodeMCU 0.9 (ESP-12 Module) <http://www.nodemcu.com/>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

    * - ``nodemcuv2``
      - `NodeMCU 1.0 (ESP-12E Module) <http://www.nodemcu.com/>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

Olimex
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``modwifi``
      - `Olimex MOD-WIFI-ESP8266(-DEV) <https://www.olimex.com/Products/IoT/MOD-WIFI-ESP8266-DEV/open-source-hardware>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 2048 Kb
      - 80 Kb

SeeedStudio
~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``wio_node``
      - `Wio Node <https://www.seeedstudio.com/Wio-Node-p-2637.html>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

SparkFun
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``sparkfunBlynk``
      - `SparkFun Blynk Board <https://www.sparkfun.com/products/13794>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

    * - ``thing``
      - `SparkFun ESP8266 Thing <https://www.sparkfun.com/products/13231>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 512 Kb
      - 80 Kb

    * - ``thingdev``
      - `SparkFun ESP8266 Thing Dev <https://www.sparkfun.com/products/13231>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 512 Kb
      - 80 Kb

SweetPea
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``esp210``
      - `SweetPea ESP-210 <http://wiki.sweetpeas.se/index.php?title=ESP-210>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

ThaiEasyElec
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``espinotee``
      - `ThaiEasyElec ESPino <http://www.thaieasyelec.com/products/wireless-modules/wifi-modules/espino-wifi-development-board-detail.html>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

WEMOS
~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``d1``
      - `WEMOS D1 R1 (Retired) <https://wiki.wemos.cc/products:d1:d1>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

    * - ``d1_mini``
      - `WeMos D1 R2 & mini <https://wiki.wemos.cc/products:d1:d1_mini>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

    * - ``d1_mini_lite``
      - `WeMos D1 mini Lite <https://wiki.wemos.cc/products:d1:d1_mini_lite>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 1024 Kb
      - 80 Kb

    * - ``d1_mini_pro``
      - `WeMos D1 mini Pro <https://wiki.wemos.cc/products:d1:d1_mini>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 16384 Kb
      - 80 Kb

.. include:: espressif8266_extra.rst
