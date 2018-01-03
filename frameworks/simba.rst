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

.. _framework_simba:

Simba
=====
:ref:`projectconf_env_framework` = ``simba``

Simba is an RTOS and build framework. It aims to make embedded programming easy and portable.

For more detailed information please visit `vendor site <http://simba-os.readthedocs.org>`_.


.. contents:: Contents
    :local:

Platforms
---------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`platform_atmelavr`
      - Atmel AVR 8- and 32-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industrys most code-efficient architecture for C and assembly programming.

    * - :ref:`platform_atmelsam`
      - Atmel | SMART offers Flash- based ARM products based on the ARM Cortex-M0+, Cortex-M3 and Cortex-M4 architectures, ranging from 8KB to 2MB of Flash including a rich peripheral and feature mix.

    * - :ref:`platform_espressif32`
      - Espressif Systems is a privately held fabless semiconductor company. They provide wireless communications and Wi-Fi chips which are widely used in mobile devices and the Internet of Things applications.

    * - :ref:`platform_espressif8266`
      - Espressif Systems is a privately held fabless semiconductor company. They provide wireless communications and Wi-Fi chips which are widely used in mobile devices and the Internet of Things applications.

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <http://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by horizontal.

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

Arduino
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

    * - ``due``
      - `Arduino Due (Programming Port) <https://www.arduino.cc/en/Main/ArduinoBoardDue>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - 
      - AT91SAM3X8E
      - 84 MHz
      - 512 Kb
      - 32 Kb

    * - ``dueUSB``
      - `Arduino Due (USB Native Port) <https://www.arduino.cc/en/Main/ArduinoBoardDue>`_
      - :ref:`Atmel SAM <platform_atmelsam>`
      - 
      - AT91SAM3X8E
      - 84 MHz
      - 512 Kb
      - 32 Kb

    * - ``megaatmega2560``
      - `Arduino Mega or Mega 2560 ATmega2560 (Mega 2560) <https://www.arduino.cc/en/Main/ArduinoBoardMega2560>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA2560
      - 16 MHz
      - 256 Kb
      - 8 Kb

    * - ``nanoatmega328``
      - `Arduino Nano ATmega328 <https://www.arduino.cc/en/Main/ArduinoBoardNano>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 16 MHz
      - 32 Kb
      - 2 Kb

    * - ``uno``
      - `Arduino Uno <https://www.arduino.cc/en/Main/ArduinoBoardUno>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 16 MHz
      - 32 Kb
      - 2 Kb

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

    * - ``esp12e``
      - `Espressif ESP8266 ESP-12E <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

    * - ``esp_wroom_02``
      - `ESP-WROOM-02 <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family>`_
      - :ref:`Espressif 8266 <platform_espressif8266>`
      - 
      - ESP8266
      - 80 MHz
      - 4096 Kb
      - 80 Kb

MakerAsia
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

    * - ``nano32``
      - `MakerAsia Nano32 <http://iot-bits.com/nano32-esp32-development-board>`_
      - :ref:`Espressif 32 <platform_espressif32>`
      - 
      - ESP32
      - 240 MHz
      - 1280 Kb
      - 288 Kb

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

    * - ``seeeduino``
      - `Seeeduino <https://www.seeedstudio.com/Seeeduino-V4.2-p-2517.html>`_
      - :ref:`Atmel AVR <platform_atmelavr>`
      - 
      - ATMEGA328P
      - 16 MHz
      - 32 Kb
      - 2 Kb

.. include:: simba_extra.rst
