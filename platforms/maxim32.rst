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

.. _platform_maxim32:

Platform ``maxim32``
====================
Maxim's microcontrollers provide low-power, efficient, and secure solutions for challenging embedded applications. Maxim's processors embed cutting-edge technologies to secure data and intellectual property, proven analog circuitry for real-world applications, and battery-conserving low power operation.

For more detailed information please visit `vendor site <https://www.maximintegrated.com/en/products/digital/microcontrollers.html>`_.

.. contents::

Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `framework-mbed <http://mbed.org>`__
      - mbed Framework

    * - `tool-openocd <http://openocd.org>`__
      - OpenOCD

    * - `toolchain-gccarmnoneeabi <https://launchpad.net/gcc-arm-embedded>`__
      - gcc-arm-embedded

.. warning::
    **Linux Users**:

    * Ubuntu/Debian users may need to add own "username" to the "dialout"
      group if they are not "root", doing this issuing a
      ``sudo usermod -a -G dialout yourusername``.
    * Install "udev" rules file `99-platformio-udev.rules <https://github.com/platformio/platformio-core/blob/develop/scripts/99-platformio-udev.rules>`_
      (an instruction is located in the file).
    * Raspberry Pi users, please read this article
      `Enable serial port on Raspberry Pi <https://hallard.me/enable-serial-port-on-raspberry-pi/>`__.


    **Windows Users:** Please check that you have correctly installed USB
    driver from board manufacturer



Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_mbed`
      - The mbed framework The mbed SDK has been designed to provide enough hardware abstraction to be intuitive and concise, yet powerful enough to build complex projects. It is built on the low-level ARM CMSIS APIs, allowing you to code down to the metal if needed. In addition to RTOS, USB and Networking libraries, a cookbook of hundreds of reusable peripheral and module libraries have been built on top of the SDK by the mbed Developer Community.

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command or
      `PlatformIO Boards Explorer <http://platformio.org/boards>`_
    * For more detailed ``board`` information please scroll tables below by
      horizontal.

Maxim
~~~~~

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

    * - ``max32600mbed``
      - `Maxim ARM mbed Enabled Development Platform for MAX32600 <https://developer.mbed.org/platforms/MAX32600mbed/>`_
      - :ref:`Maxim 32 <platform_maxim32>`
      - 
      - MAX32600
      - 24 MHz
      - 256 Kb
      - 32 Kb

    * - ``max32620hsp``
      - `Maxim Health Sensor Platform <https://developer.mbed.org/platforms/MAX32620HSP/>`_
      - :ref:`Maxim 32 <platform_maxim32>`
      - 
      - MAX32620
      - 96 MHz
      - 2048 Kb
      - 256 Kb

    * - ``max32630fthr``
      - `Maxim MAX32630FTHR Application Platform <https://developer.mbed.org/platforms/MAX32630FTHR/>`_
      - :ref:`Maxim 32 <platform_maxim32>`
      - 
      - MAX32630
      - 96 MHz
      - 2048 Kb
      - 512 Kb

    * - ``maxwsnenv``
      - `Maxim Wireless Sensor Node Demonstrator <https://developer.mbed.org/platforms/MAXWSNENV/>`_
      - :ref:`Maxim 32 <platform_maxim32>`
      - 
      - MAX32610
      - 24 MHz
      - 256 Kb
      - 32 Kb
