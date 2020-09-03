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

.. _board_maxim32_maxwsnenv:

Maxim Wireless Sensor Node Demonstrator
=======================================

.. contents::

Hardware
--------

Platform :ref:`platform_maxim32`: Maxim's microcontrollers provide low-power, efficient, and secure solutions for challenging embedded applications. Maxim's processors embed cutting-edge technologies to secure data and intellectual property, proven analog circuitry for real-world applications, and battery-conserving low power operation.

.. list-table::

  * - **Microcontroller**
    - MAX32610
  * - **Frequency**
    - 24MHz
  * - **Flash**
    - 256KB
  * - **RAM**
    - 32KB
  * - **Vendor**
    - `Maxim <https://developer.mbed.org/platforms/MAXWSNENV/?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``maxwsnenv`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:maxwsnenv]
  platform = maxim32
  board = maxwsnenv

You can override default Maxim Wireless Sensor Node Demonstrator settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `maxwsnenv.json <https://github.com/platformio/platform-maxim32/blob/master/boards/maxwsnenv.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:maxwsnenv]
  platform = maxim32
  board = maxwsnenv

  ; change microcontroller
  board_build.mcu = max32610

  ; change MCU frequency
  board_build.f_cpu = 24000000L


Uploading
---------
Maxim Wireless Sensor Node Demonstrator supports the next uploading protocols:

* ``cmsis-dap``
* ``mbed``

Default protocol is ``mbed``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:maxwsnenv]
  platform = maxim32
  board = maxwsnenv

  upload_protocol = mbed

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further
    instructions and configuration information.

You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` option in :ref:`projectconf`.

Maxim Wireless Sensor Node Demonstrator does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_cmsis-dap`
    - 
    - Yes

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_mbed`
      - Arm Mbed OS is an open source embedded operating system designed specifically for the 'things' in the Internet of Things. It includes all the features you need to develop a connected product based on an Arm Cortex-M microcontroller, including security, connectivity, an RTOS and drivers for sensors and I/O devices