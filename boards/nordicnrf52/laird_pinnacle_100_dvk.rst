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

.. _board_nordicnrf52_laird_pinnacle_100_dvk:

Laird Connectivity Pinnacle 100 DVK
===================================

.. contents::

Hardware
--------

Platform :ref:`platform_nordicnrf52`: The nRF52 Series are built for speed to carry out increasingly complex tasks in the shortest possible time and return to sleep, conserving precious battery power. They have a Cortex-M4F processor and are the most capable Bluetooth Smart SoCs on the market.

.. list-table::

  * - **Microcontroller**
    - NRF52840
  * - **Frequency**
    - 64MHz
  * - **Flash**
    - 1MB
  * - **RAM**
    - 256KB
  * - **Vendor**
    - `Laird Connectivity <https://www.lairdconnect.com/wireless-modules/cellular-solutions/pinnacle-100-cellular-modem?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``laird_pinnacle_100_dvk`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:laird_pinnacle_100_dvk]
  platform = nordicnrf52
  board = laird_pinnacle_100_dvk

You can override default Laird Connectivity Pinnacle 100 DVK settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `laird_pinnacle_100_dvk.json <https://github.com/platformio/platform-nordicnrf52/blob/master/boards/laird_pinnacle_100_dvk.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:laird_pinnacle_100_dvk]
  platform = nordicnrf52
  board = laird_pinnacle_100_dvk

  ; change microcontroller
  board_build.mcu = nrf52840

  ; change MCU frequency
  board_build.f_cpu = 64000000L


Uploading
---------
Laird Connectivity Pinnacle 100 DVK supports the next uploading protocols:

* ``blackmagic``
* ``cmsis-dap``
* ``jlink``
* ``mbed``
* ``nrfjprog``
* ``stlink``

Default protocol is ``jlink``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:laird_pinnacle_100_dvk]
  platform = nordicnrf52
  board = laird_pinnacle_100_dvk

  upload_protocol = jlink

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further
    instructions and configuration information.

You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` option in :ref:`projectconf`.

Laird Connectivity Pinnacle 100 DVK does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_blackmagic`
    - 
    - Yes
  * - :ref:`debugging_tool_cmsis-dap`
    - 
    - 
  * - :ref:`debugging_tool_jlink`
    - 
    - 
  * - :ref:`debugging_tool_stlink`
    - 
    - 

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_zephyr`
      - The Zephyr Project is a scalable real-time operating system (RTOS) supporting multiple hardware architectures, optimized for resource constrained devices, and built with safety and security in mind