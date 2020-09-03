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

.. _board_espressif32_m5stack-grey:

M5Stack GREY ESP32
==================

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
    - 520KB
  * - **Vendor**
    - `M5Stack <http://www.m5stack.com?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``m5stack-grey`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:m5stack-grey]
  platform = espressif32
  board = m5stack-grey

You can override default M5Stack GREY ESP32 settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `m5stack-grey.json <https://github.com/platformio/platform-espressif32/blob/master/boards/m5stack-grey.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:m5stack-grey]
  platform = espressif32
  board = m5stack-grey

  ; change microcontroller
  board_build.mcu = esp32

  ; change MCU frequency
  board_build.f_cpu = 240000000L


Uploading
---------
M5Stack GREY ESP32 supports the next uploading protocols:

* ``espota``
* ``esptool``

Default protocol is ``esptool``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:m5stack-grey]
  platform = espressif32
  board = m5stack-grey

  upload_protocol = esptool

Debugging
---------
:ref:`piodebug` currently does not support M5Stack GREY ESP32 board.

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