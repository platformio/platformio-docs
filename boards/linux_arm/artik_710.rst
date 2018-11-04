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

.. _board_linux_arm_artik_710:

Samsung ARTIK 710
=================

.. contents::

Hardware
--------

Platform :ref:`platform_linux_arm`: Linux ARM is a Unix-like and mostly POSIX-compliant computer operating system (OS) assembled under the model of free and open-source software development and distribution. Using host OS (Mac OS X, Linux ARM) you can build native application for Linux ARM platform.

.. list-table::

  * - **Microcontroller**
    - S5P6818
  * - **Frequency**
    - 1400MHz
  * - **Flash**
    - 4GB
  * - **RAM**
    - 1GB
  * - **Vendor**
    - `Samsung <https://www.artik.io?utm_source=platformio&utm_medium=docs>`__


Configuration
-------------

Please use ``artik_710`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:artik_710]
  platform = linux_arm
  board = artik_710

You can override default Samsung ARTIK 710 settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `artik_710.json <https://github.com/platformio/platform-linux_arm/blob/master/boards/artik_710.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:artik_710]
  platform = linux_arm
  board = artik_710

  ; change microcontroller
  board_build.mcu = s5p6818

  ; change MCU frequency
  board_build.f_cpu = 1400000000L

Debugging
---------
:ref:`piodebug` currently does not support Samsung ARTIK 710 board.

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_artik-sdk`
      - ARTIK SDK is a C/C++ SDK targeting Samsung ARTIK platforms. It exposes a set of APIs to ease up development of applications. These APIs cover hardware buses such as GPIO, SPI, I2C, UART, connectivity links like Wi-Fi, Bluetooth, Zigbee, and network protocols such as HTTP, Websockets, MQTT, and others.