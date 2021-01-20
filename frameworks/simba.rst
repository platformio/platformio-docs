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

:Configuration:
  :ref:`projectconf_env_framework` = ``simba``

Simba is an RTOS and build framework with aims to make embedded programming easy and portable

For more detailed information please visit `vendor site <http://simba-os.readthedocs.org?utm_source=platformio.org&utm_medium=docs>`_.


.. contents:: Contents
    :local:
    :depth: 1

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
      - Platform
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_megaatmega2560`
      - :ref:`platform_atmelavr`
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_nanoatmega328`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_uno`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
    * - :ref:`board_atmelavr_seeeduino`
      - :ref:`platform_atmelavr`
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB


External Debug Tools
^^^^^^^^^^^^^^^^^^^^

Boards listed below are compatible with :ref:`piodebug` but **DEPEND ON**
external debug probe. They **ARE NOT READY** for debugging.
Please click on board name for the further details.


.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelsam_due`
      - :ref:`platform_atmelsam`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_atmelsam_dueUSB`
      - :ref:`platform_atmelsam`
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB


Examples
--------

* `Simba for Atmel AVR <https://github.com/platformio/platform-atmelavr/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_
* `Simba for Atmel SAM <https://github.com/platformio/platform-atmelsam/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_
* `Simba for Espressif 32 <https://github.com/platformio/platform-espressif32/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_
* `Simba for Espressif 8266 <https://github.com/platformio/platform-espressif8266/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_

Platforms
---------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`platform_atmelavr`
      - Atmel AVR 8-bit MCUs deliver a unique combination of performance, power efficiency and design flexibility. Optimized to speed time to market-and easily adapt to new ones-they are based on the industry's most code-efficient architecture for C and assembly programming

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
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll the tables below by horizontally.

Adafruit
~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_huzzah`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

Arduino
~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelsam_due`
      - :ref:`platform_atmelsam`
      - External
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_atmelsam_dueUSB`
      - :ref:`platform_atmelsam`
      - External
      - AT91SAM3X8E
      - 84MHz
      - 512KB
      - 96KB
    * - :ref:`board_atmelavr_megaatmega2560`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA2560
      - 16MHz
      - 248KB
      - 8KB
    * - :ref:`board_atmelavr_nanoatmega328`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 30KB
      - 2KB
    * - :ref:`board_atmelavr_uno`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB

Espressif
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_esp_wroom_02`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 2MB
      - 80KB
    * - :ref:`board_espressif8266_esp12e`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_espressif8266_esp01`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 512KB
      - 80KB

Invent One
~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_inventone`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB

MakerAsia
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif32_nano32`
      - :ref:`platform_espressif32`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_nodemcu`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_espressif8266_nodemcuv2`
      - :ref:`platform_espressif8266`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_atmelavr_seeeduino`
      - :ref:`platform_atmelavr`
      - On-board
      - ATMEGA328P
      - 16MHz
      - 31.50KB
      - 2KB
