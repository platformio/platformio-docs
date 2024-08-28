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

.. _board_espressif32_esp32-c6-devkitc-1:

Espressif ESP32-C6-DevKitC-1
============================

.. contents::

Hardware
--------

Platform :ref:`platform_espressif32`: ESP32 is a series of low-cost, low-power system on a chip microcontrollers with integrated Wi-Fi and Bluetooth. ESP32 integrates an antenna switch, RF balun, power amplifier, low-noise receive amplifier, filters, and power management modules.

.. list-table::

  * - **Microcontroller**
    - ESP32C6
  * - **Frequency**
    - 160MHz
  * - **Flash**
    - 8MB
  * - **RAM**
    - 320KB
  * - **Vendor**
    - `Espressif <https://docs.espressif.com/projects/espressif-esp-dev-kits/en/latest/esp32c6/esp32-c6-devkitc-1/index.html?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``esp32-c6-devkitc-1`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:esp32-c6-devkitc-1]
  platform = espressif32
  board = esp32-c6-devkitc-1

You can override default Espressif ESP32-C6-DevKitC-1 settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `esp32-c6-devkitc-1.json <https://github.com/platformio/platform-espressif32/blob/master/boards/esp32-c6-devkitc-1.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:esp32-c6-devkitc-1]
  platform = espressif32
  board = esp32-c6-devkitc-1

  ; change microcontroller
  board_build.mcu = esp32c6

  ; change MCU frequency
  board_build.f_cpu = 160000000L


Uploading
---------
Espressif ESP32-C6-DevKitC-1 supports the following uploading protocols:

* ``espota``
* ``esptool``

Default protocol is ``esptool``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:esp32-c6-devkitc-1]
  platform = espressif32
  board = esp32-c6-devkitc-1

  upload_protocol = esptool

Debugging
---------
:ref:`piodebug` currently does not support Espressif ESP32-C6-DevKitC-1 board.

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_espidf`
      - Espressif IoT Development Framework. Official development framework for ESP32 chip