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

.. _board_espressif32_ttgo-t-watch:

TTGO T-Watch
============

.. contents::

Hardware
--------

Platform :ref:`platform_espressif32`: Espressif Systems is a privately held fabless semiconductor company. They provide wireless communications and Wi-Fi chips which are widely used in mobile devices and the Internet of Things applications.

.. list-table::

  * - **Microcontroller**
    - ESP32
  * - **Frequency**
    - 240MHz
  * - **Flash**
    - 16MB
  * - **RAM**
    - 320KB
  * - **Vendor**
    - `TTGO <https://github.com/Xinyuan-LilyGO/TTGO-T-Watch?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``ttgo-t-watch`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:ttgo-t-watch]
  platform = espressif32
  board = ttgo-t-watch

You can override default TTGO T-Watch settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `ttgo-t-watch.json <https://github.com/platformio/platform-espressif32/blob/master/boards/ttgo-t-watch.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:ttgo-t-watch]
  platform = espressif32
  board = ttgo-t-watch

  ; change microcontroller
  board_build.mcu = esp32

  ; change MCU frequency
  board_build.f_cpu = 240000000L


Uploading
---------
TTGO T-Watch supports the next uploading protocols:

* ``espota``
* ``esptool``

Default protocol is ``esptool``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:ttgo-t-watch]
  platform = espressif32
  board = ttgo-t-watch

  upload_protocol = esptool

Debugging
---------
:ref:`piodebug` currently does not support TTGO T-Watch board.

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