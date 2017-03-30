..  Copyright 2014-present PlatformIO <contact@platformio.org>
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

.. _framework_pumbaa:

Framework ``pumbaa``
====================
Pumbaa is Python on top of Simba. The implementation is a port of MicroPython, designed for embedded devices with limited amount of RAM and code memory.

For more detailed information please visit `vendor site <http://pumbaa.readthedocs.org/>`_.

.. contents::

Platforms
---------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`platform_espressif32`
      - Espressif Systems is a privately held fabless semiconductor company. They provide wireless communications and Wi-Fi chips which are widely used in mobile devices and the Internet of Things applications.

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <http://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by horizontal.

MakerAsia
~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``nano32``
      - `MakerAsia Nano32 <http://iot-bits.com/nano32-esp32-development-board>`_
      - ESP32
      - 240 MHz
      - 1024 Kb
      - 288 Kb
