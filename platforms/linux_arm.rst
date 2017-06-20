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

.. _platform_linux_arm:

Linux ARM
=========
:ref:`projectconf_env_platform` = ``linux_arm``

Linux ARM is a Unix-like and mostly POSIX-compliant computer operating system (OS) assembled under the model of free and open-source software development and distribution. Using host OS (Mac OS X, Linux ARM) you can build native application for Linux ARM platform.

For more detailed information please visit `vendor site <http://platformio.org/platforms/linux_arm>`_.

.. contents:: Contents
    :local:

Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-artik-sdk <http://www.artik.io>`__
      - ARTIK SDK is a C/C++ SDK targeting Samsung ARTIK platforms

    * - `framework-wiringpi <http://wiringpi.com>`__
      - GPIO Interface library for the Raspberry Pi

    * - `toolchain-gccarmlinuxgnueabi <https://gcc.gnu.org>`__
      - GCC for Linux ARM GNU EABI

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_artik-sdk`
      - ARTIK SDK is a C/C++ SDK targeting Samsung ARTIK platforms. It exposes a set of APIs to ease up development of applications. These APIs cover hardware buses such as GPIO, SPI, I2C, UART, connectivity links like Wi-Fi, Bluetooth, Zigbee, and network protocols such as HTTP, Websockets, MQTT, and others.

    * - :ref:`framework_wiringpi`
      - WiringPi is a GPIO access library written in C for the BCM2835 used in the Raspberry Pi. It's designed to be familiar to people who have used the Arduino "wiring" system.

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <http://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by
      horizontal.

Raspberry Pi
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``raspberrypi_1b``
      - `Raspberry Pi 1 Model B <https://www.raspberrypi.org>`_
      - :ref:`Linux ARM <platform_linux_arm>`
      - 
      - BCM2835
      - 700 MHz
      - 524288 Kb
      - 524288 Kb

    * - ``raspberrypi_2b``
      - `Raspberry Pi 2 Model B <https://www.raspberrypi.org>`_
      - :ref:`Linux ARM <platform_linux_arm>`
      - 
      - BCM2836
      - 900 MHz
      - 1048576 Kb
      - 1048576 Kb

    * - ``raspberrypi_3b``
      - `Raspberry Pi 3 Model B <https://www.raspberrypi.org>`_
      - :ref:`Linux ARM <platform_linux_arm>`
      - 
      - BCM2837
      - 1200 MHz
      - 1048576 Kb
      - 1048576 Kb

    * - ``raspberrypi_zero``
      - `Raspberry Pi Zero <https://www.raspberrypi.org>`_
      - :ref:`Linux ARM <platform_linux_arm>`
      - 
      - BCM2835
      - 1000 MHz
      - 524288 Kb
      - 524288 Kb

Samsung
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - Microcontroller
      - Frequency
      - Flash
      - RAM

    * - ``artik_1020``
      - `Samsung ARTIK 1020 <https://www.artik.io>`_
      - :ref:`Linux ARM <platform_linux_arm>`
      - 
      - EXYNOS5422
      - 1500 MHz
      - 16777216 Kb
      - 2097152 Kb

    * - ``artik_520``
      - `Samsung ARTIK 520 <https://www.artik.io>`_
      - :ref:`Linux ARM <platform_linux_arm>`
      - 
      - EXYNOS3250
      - 1000 MHz
      - 4194304 Kb
      - 524288 Kb

    * - ``artik_530``
      - `Samsung ARTIK 530 <https://www.artik.io>`_
      - :ref:`Linux ARM <platform_linux_arm>`
      - 
      - S5P4418
      - 1200 MHz
      - 4194304 Kb
      - 524288 Kb

    * - ``artik_710``
      - `Samsung ARTIK 710 <https://www.artik.io>`_
      - :ref:`Linux ARM <platform_linux_arm>`
      - 
      - S5P6818
      - 1400 MHz
      - 4194304 Kb
      - 1048576 Kb
