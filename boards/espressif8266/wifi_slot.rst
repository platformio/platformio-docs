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

.. _board_espressif8266_wifi_slot:

WiFi Slot
=========

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
    - `Amperka <https://amperka.ru/product/wifi-slot>`__


Configuration
-------------

Please use ``wifi_slot`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:wifi_slot]
  platform = espressif8266
  board = wifi_slot

You can override default WiFi Slot settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `wifi_slot.json <https://github.com/platformio/platform-espressif8266/blob/master/boards/wifi_slot.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:wifi_slot]
  platform = espressif8266
  board = wifi_slot

  ; change microcontroller
  board_build.mcu = esp8266

  ; change MCU frequency
  board_build.f_cpu = 80000000L


Uploading
---------
WiFi Slot supports the following uploading protocols:

* ``espota``
* ``esptool``

Default protocol is ``esptool``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:wifi_slot]
  platform = espressif8266
  board = wifi_slot

  upload_protocol = esptool

Debugging
---------
:ref:`piodebug` currently does not support WiFi Slot board.

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
