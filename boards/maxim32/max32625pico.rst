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

.. _board_maxim32_max32625pico:

MAX32625PICO
============

.. contents::

Hardware
--------

Platform :ref:`platform_maxim32`: Maxim's microcontrollers provide low-power, efficient, and secure solutions for challenging embedded applications. Maxim's processors embed cutting-edge technologies to secure data and intellectual property, proven analog circuitry for real-world applications, and battery-conserving low power operation.

.. list-table::

  * - **Microcontroller**
    - MAX32625
  * - **Frequency**
    - 96MHz
  * - **Flash**
    - 512KB
  * - **RAM**
    - 160KB
  * - **Vendor**
    - `Maxim <https://www.maximintegrated.com/en/products/microcontrollers/MAX32625PICO.html?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``max32625pico`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:max32625pico]
  platform = maxim32
  board = max32625pico

You can override default MAX32625PICO settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `max32625pico.json <https://github.com/platformio/platform-maxim32/blob/master/boards/max32625pico.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:max32625pico]
  platform = maxim32
  board = max32625pico

  ; change microcontroller
  board_build.mcu = max32625

  ; change MCU frequency
  board_build.f_cpu = 96000000L

Debugging
---------
:ref:`piodebug` currently does not support MAX32625PICO board.

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_mbed`
      - Arm Mbed OS is an open source embedded operating system designed specifically for the 'things' in the Internet of Things. It includes all the features you need to develop a connected product based on an Arm Cortex-M microcontroller, including security, connectivity, an RTOS and drivers for sensors and I/O devices