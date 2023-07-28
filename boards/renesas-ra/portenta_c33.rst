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

.. _board_renesas-ra_portenta_c33:

Arduino Portenta C33
====================

.. contents::

Hardware
--------

Platform :ref:`platform_renesas-ra`: Renesas Advanced (RA) 32-bit microcontrollers with the Arm Cortex-M33, -M23 and -M4 processor cores deliver key advantages compared to competitive Arm Cortex-M MCUs by providing stronger embedded security, superior CoreMark performance and ultra-low power operation.

.. list-table::

  * - **Microcontroller**
    - R7FA6M5BH2CBG
  * - **Frequency**
    - 200MHz
  * - **Flash**
    - 2MB
  * - **RAM**
    - 511.35KB
  * - **Vendor**
    - `Arduino <https://www.arduino.cc/pro/hardware-product-portenta-c33?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``portenta_c33`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:portenta_c33]
  platform = renesas-ra
  board = portenta_c33

You can override default Arduino Portenta C33 settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `portenta_c33.json <https://github.com/platformio/platform-renesas-ra/blob/master/boards/portenta_c33.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:portenta_c33]
  platform = renesas-ra
  board = portenta_c33

  ; change microcontroller
  board_build.mcu = r7fa6m5bh2cbg

  ; change MCU frequency
  board_build.f_cpu = 200000000L


Uploading
---------
Arduino Portenta C33 supports the following uploading protocols:

* ``dfu``
* ``jlink``

Default protocol is ``dfu``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:portenta_c33]
  platform = renesas-ra
  board = portenta_c33

  upload_protocol = dfu

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further
    instructions and configuration information.

You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` option in :ref:`projectconf`.

Arduino Portenta C33 does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

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

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences.

    * - :ref:`framework_cmsis`
      - Vendor-independent hardware abstraction layer for the Cortex-M processor series

    * - :ref:`framework_fsp`
      - The Renesas Flexible Software Package (FSP) is an enhanced software package designed to provide easy-to-use, scalable, high-quality software for embedded system designs using Renesas RA family of Arm Microcontrollers.