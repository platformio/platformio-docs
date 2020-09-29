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

.. _board_espressif8266_heltec_wifi_kit_8:

Heltec Wifi kit 8
=================

.. contents::

Hardware
--------

Platform :ref:`platform_espressif8266`: Espressif Systems is a privately held fabless semiconductor company. They provide wireless communications and Wi-Fi chips which are widely used in mobile devices and the Internet of Things applications.

.. list-table::

  * - **Microcontroller**
    - ESP8266
  * - **Frequency**
    - 80MHz
  * - **Flash**
    - 4MB
  * - **RAM**
    - 80KB
  * - **Vendor**
    - `Heltec <http://www.heltec.cn/project/wifi_kit_8/?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``heltec_wifi_kit_8`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:heltec_wifi_kit_8]
  platform = espressif8266
  board = heltec_wifi_kit_8

You can override default Heltec Wifi kit 8 settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `heltec_wifi_kit_8.json <https://github.com/platformio/platform-espressif8266/blob/master/boards/heltec_wifi_kit_8.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:heltec_wifi_kit_8]
  platform = espressif8266
  board = heltec_wifi_kit_8

  ; change microcontroller
  board_build.mcu = esp8266

  ; change MCU frequency
  board_build.f_cpu = 80000000L


Uploading
---------
Heltec Wifi kit 8 supports the next uploading protocols:

* ``espota``
* ``esptool``

Default protocol is ``esptool``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:heltec_wifi_kit_8]
  platform = espressif8266
  board = heltec_wifi_kit_8

  upload_protocol = esptool

Debugging
---------
:ref:`piodebug` currently does not support Heltec Wifi kit 8 board.

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