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

.. _framework_wiringpi:

WiringPi
========

:Configuration:
  :ref:`projectconf_env_framework` = ``wiringpi``

WiringPi is a PIN based GPIO access library written in C for the BCM2835, BCM2836 and BCM2837 SoC devices used in all Raspberry Pi

.. contents:: Contents
    :local:
    :depth: 1

Platforms
---------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`platform_linux_arm`
      - Linux ARM is a Unix-like and mostly POSIX-compliant computer operating system (OS) assembled under the model of free and open-source software development and distribution. Using host OS (Mac OS X, Linux ARM) you can build native application for Linux ARM platform.

Examples
--------

* `WiringPi for Linux ARM <https://github.com/platformio/platform-linux_arm/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command
    * For more detailed ``board`` information please scroll the tables below by horizontally.

Raspberry Pi
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
    * - :ref:`board_linux_arm_raspberrypi_1b`
      - :ref:`platform_linux_arm`
      - No
      - BCM2835
      - 700MHz
      - 512MB
      - 512MB
    * - :ref:`board_linux_arm_raspberrypi_2b`
      - :ref:`platform_linux_arm`
      - No
      - BCM2836
      - 900MHz
      - 1GB
      - 1GB
    * - :ref:`board_linux_arm_raspberrypi_3b`
      - :ref:`platform_linux_arm`
      - No
      - BCM2837
      - 1200MHz
      - 1GB
      - 1GB
    * - :ref:`board_linux_arm_raspberrypi_zero`
      - :ref:`platform_linux_arm`
      - No
      - BCM2835
      - 1000MHz
      - 512MB
      - 512MB
