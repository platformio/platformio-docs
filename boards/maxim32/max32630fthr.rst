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

.. _board_maxim32_max32630fthr:

Maxim MAX32630FTHR Application Platform
=======================================

.. contents::

Platform :ref:`platform_maxim32`: Maxim's microcontrollers provide low-power, efficient, and secure solutions for challenging embedded applications. Maxim's processors embed cutting-edge technologies to secure data and intellectual property, proven analog circuitry for real-world applications, and battery-conserving low power operation.

System
------

.. list-table::

  * - **Microcontroller**
    - MAX32630
  * - **Frequency**
    - 96Mhz
  * - **Flash**
    - 2MB
  * - **RAM**
    - 512KB
  * - **Vendor**
    - `Maxim <https://developer.mbed.org/platforms/MAX32630FTHR/?utm_source=platformio&utm_medium=docs>`__


Configuration
-------------

Please use ``max32630fthr`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:max32630fthr]
  platform = maxim32
  board = max32630fthr

You can override default Maxim MAX32630FTHR Application Platform settings per build environment using
``board_{JSON.PATH}`` option, where ``{JSON.PATH}`` is a path from
board manifest `max32630fthr.json <https://github.com/platformio/platform-maxim32/blob/master/boards/max32630fthr.json>`_. For example,

.. code-block:: ini

  [env:max32630fthr]
  platform = maxim32
  board = max32630fthr

  ; change microcontroller
  board_build.mcu = max32630

  ; change MCU frequency
  board_build.f_cpu = 96000000L

Debugging
---------
:ref:`piodebug` currently does not support Maxim MAX32630FTHR Application Platform board.

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_mbed`
      - The mbed framework The mbed SDK has been designed to provide enough hardware abstraction to be intuitive and concise, yet powerful enough to build complex projects. It is built on the low-level ARM CMSIS APIs, allowing you to code down to the metal if needed. In addition to RTOS, USB and Networking libraries, a cookbook of hundreds of reusable peripheral and module libraries have been built on top of the SDK by the mbed Developer Community.