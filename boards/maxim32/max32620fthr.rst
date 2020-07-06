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

.. _board_maxim32_max32620fthr:

MAX32620FTHR
============

.. contents::

Hardware
--------

Platform :ref:`platform_maxim32`: Maxim's microcontrollers provide low-power, efficient, and secure solutions for challenging embedded applications. Maxim's processors embed cutting-edge technologies to secure data and intellectual property, proven analog circuitry for real-world applications, and battery-conserving low power operation.

.. list-table::

  * - **Microcontroller**
    - MAX32620FTHR
  * - **Frequency**
    - 96MHz
  * - **Flash**
    - 2MB
  * - **RAM**
    - 256KB
  * - **Vendor**
    - `Maxim <https://www.maximintegrated.com/en/products/microcontrollers/MAX32620FTHR.html?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``max32620fthr`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:max32620fthr]
  platform = maxim32
  board = max32620fthr

You can override default MAX32620FTHR settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `max32620fthr.json <https://github.com/platformio/platform-maxim32/blob/master/boards/max32620fthr.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:max32620fthr]
  platform = maxim32
  board = max32620fthr

  ; change microcontroller
  board_build.mcu = max32620fthr

  ; change MCU frequency
  board_build.f_cpu = 96000000L


Uploading
---------
MAX32620FTHR supports the next uploading protocols:

* ``jlink``
* ``mbed``

Default protocol is ``mbed``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:max32620fthr]
  platform = maxim32
  board = max32620fthr

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

MAX32620FTHR does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_jlink`
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