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

.. _framework_artik-sdk:

ARTIK SDK
=========
:ref:`projectconf_env_framework` = ``artik-sdk``

ARTIK SDK is a C/C++ SDK targeting Samsung ARTIK platforms. It exposes a set of APIs to ease up development of applications. These APIs cover hardware buses such as GPIO, SPI, I2C, UART, connectivity links like Wi-Fi, Bluetooth, Zigbee, and network protocols such as HTTP, Websockets, MQTT, and others.

For more detailed information please visit `vendor site <http://www.artik.io?utm_source=platformio&utm_medium=docs>`_.


.. contents:: Contents
    :local:
    :depth: 1

Examples
--------

* `ARTIK SDK for Linux ARM <https://github.com/platformio/platform-linux_arm/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_

Platforms
---------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`platform_linux_arm`
      - Linux ARM is a Unix-like and mostly POSIX-compliant computer operating system (OS) assembled under the model of free and open-source software development and distribution. Using host OS (Mac OS X, Linux ARM) you can build native application for Linux ARM platform.

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <https://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by horizontal.

RushUp
~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``kitra_520``
      - `RushUp Kitra 520 <https://www.rushup.tech/kitra?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Linux ARM <platform_linux_arm>`
      - No
      - EXYNOS3250
      - 1000MHz
      - 4GB
      - 512MB

Samsung
~~~~~~~

.. list-table::
    :header-rows:  1

    * - ID
      - Name
      - Platform
      - Debug
      - MCU
      - Frequency
      - Flash
      - RAM
    * - ``artik_1020``
      - `Samsung ARTIK 1020 <https://www.artik.io?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Linux ARM <platform_linux_arm>`
      - No
      - EXYNOS5422
      - 1500MHz
      - 16GB
      - 2GB
    * - ``artik_520``
      - `Samsung ARTIK 520 <https://www.artik.io?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Linux ARM <platform_linux_arm>`
      - No
      - EXYNOS3250
      - 1000MHz
      - 4GB
      - 512MB
    * - ``artik_530``
      - `Samsung ARTIK 530 <https://www.artik.io?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Linux ARM <platform_linux_arm>`
      - No
      - S5P4418
      - 1200MHz
      - 4GB
      - 512MB
    * - ``artik_710``
      - `Samsung ARTIK 710 <https://www.artik.io?utm_source=platformio&utm_medium=docs>`_
      - :ref:`Linux ARM <platform_linux_arm>`
      - No
      - S5P6818
      - 1400MHz
      - 4GB
      - 1GB
