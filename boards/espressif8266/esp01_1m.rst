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

.. _board_espressif8266_esp01_1m:

Espressif Generic ESP8266 ESP-01 1M
===================================

.. contents::

Hardware
--------

Platform :ref:`platform_espressif8266`: ESP8266 is a cost-effective and highly integrated Wi-Fi MCU with built-in TCP/IP networking software for IoT applications. ESP8266 integrates an enhanced version of Tensilica’s L106 Diamond series 32-bit processor and on-chip SRAM.

.. list-table::

  * - **Microcontroller**
    - ESP8266
  * - **Frequency**
    - 80MHz
  * - **Flash**
    - 1MB
  * - **RAM**
    - 80KB
  * - **Vendor**
    - `Espressif <http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family&utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``esp01_1m`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:esp01_1m]
  platform = espressif8266
  board = esp01_1m

You can override default Espressif Generic ESP8266 ESP-01 1M settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `esp01_1m.json <https://github.com/platformio/platform-espressif8266/blob/master/boards/esp01_1m.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:esp01_1m]
  platform = espressif8266
  board = esp01_1m

  ; change microcontroller
  board_build.mcu = esp8266

  ; change MCU frequency
  board_build.f_cpu = 80000000L


Uploading
---------
Espressif Generic ESP8266 ESP-01 1M supports the following uploading protocols:

* ``espota``
* ``esptool``

Default protocol is ``esptool``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:esp01_1m]
  platform = espressif8266
  board = esp01_1m

  upload_protocol = esptool

Debugging
---------
:ref:`piodebug` currently does not support Espressif Generic ESP8266 ESP-01 1M board.

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences.

    * - :ref:`framework_esp8266-nonos-sdk`
      - Espressif ESP8266 Non-OS SDK

    * - :ref:`framework_esp8266-rtos-sdk`
      - Espressif ESP8266 SDK based on FreeRTOS