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

.. _framework_esp8266-nonos-sdk:

ESP8266 Non-OS SDK
==================

:Configuration:
  :ref:`projectconf_env_framework` = ``esp8266-nonos-sdk``

The non-OS SDK provides a set of application programming interfaces (APIs) for core ESP8266 functionalities such as data reception/transmission over Wi-Fi, TCP/IP stack functions, hardware interface functions and basic system management functions

For more detailed information please visit `vendor site <https://github.com/espressif/ESP8266_NONOS_SDK?utm_source=platformio.org&utm_medium=docs>`_.


.. contents:: Contents
    :local:
    :depth: 1

Examples
--------

* `ESP8266 Non-OS SDK for Espressif 8266 <https://github.com/platformio/platform-espressif8266/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_

Platforms
---------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`platform_espressif8266`
      - Espressif Systems is a privately held fabless semiconductor company. They provide wireless communications and Wi-Fi chips which are widely used in mobile devices and the Internet of Things applications.

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll the tables below by horizontally.

4D Systems
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
    * - :ref:`board_espressif8266_gen4iod`
      - :ref:`platform_espressif8266`
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

Amperka
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
    * - :ref:`board_espressif8266_wifi_slot`
      - :ref:`platform_espressif8266`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_espmxdevkit`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 1MB
      - 80KB
    * - :ref:`board_espressif8266_espduino`
      - :ref:`platform_espressif8266`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_espectro`
      - :ref:`platform_espressif8266`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_espresso_lite_v1`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_espressif8266_espresso_lite_v2`
      - :ref:`platform_espressif8266`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_espino`
      - :ref:`platform_espressif8266`
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
    * - :ref:`board_espressif8266_esp01_1m`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 1MB
      - 80KB
    * - :ref:`board_espressif8266_esp01`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 512KB
      - 80KB
    * - :ref:`board_espressif8266_esp07`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 1MB
      - 80KB
    * - :ref:`board_espressif8266_esp07s`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_espressif8266_esp8285`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 1MB
      - 80KB
    * - :ref:`board_espressif8266_phoenix_v1`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_espressif8266_phoenix_v2`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_espressif8266_wifinfo`
      - :ref:`platform_espressif8266`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_heltec_wifi_kit_8`
      - :ref:`platform_espressif8266`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_sonoff_basic`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 1MB
      - 80KB
    * - :ref:`board_espressif8266_sonoff_s20`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 1MB
      - 80KB
    * - :ref:`board_espressif8266_sonoff_sv`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 1MB
      - 80KB
    * - :ref:`board_espressif8266_sonoff_th`
      - :ref:`platform_espressif8266`
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

Olimex
~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_modwifi`
      - :ref:`platform_espressif8266`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_eduinowifi`
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
    * - :ref:`board_espressif8266_wio_link`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_espressif8266_wio_node`
      - :ref:`platform_espressif8266`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_sparkfunBlynk`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_espressif8266_thing`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 512KB
      - 80KB
    * - :ref:`board_espressif8266_thingdev`
      - :ref:`platform_espressif8266`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_esp210`
      - :ref:`platform_espressif8266`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_espinotee`
      - :ref:`platform_espressif8266`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_d1`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_espressif8266_d1_mini`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
    * - :ref:`board_espressif8266_d1_mini_pro`
      - :ref:`platform_espressif8266`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_wifiduino`
      - :ref:`platform_espressif8266`
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
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - :ref:`board_espressif8266_xinabox_cw01`
      - :ref:`platform_espressif8266`
      - No
      - ESP8266
      - 80MHz
      - 4MB
      - 80KB
