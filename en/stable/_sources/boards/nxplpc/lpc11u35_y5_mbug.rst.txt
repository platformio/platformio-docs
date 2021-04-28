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

.. _board_nxplpc_lpc11u35_y5_mbug:

y5 LPC11U35 mbug
================

.. contents::

Hardware
--------

Platform :ref:`platform_nxplpc`: The NXP LPC is a family of 32-bit microcontroller integrated circuits by NXP Semiconductors. The LPC chips are grouped into related series that are based around the same 32-bit ARM processor core, such as the Cortex-M4F, Cortex-M3, Cortex-M0+, or Cortex-M0. Internally, each microcontroller consists of the processor core, static RAM memory, flash memory, debugging interface, and various peripherals.

.. list-table::

  * - **Microcontroller**
    - LPC11U35
  * - **Frequency**
    - 48MHz
  * - **Flash**
    - 64KB
  * - **RAM**
    - 10KB
  * - **Vendor**
    - `y5 design <https://developer.mbed.org/platforms/Y5-LPC11U35-MBUG/?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``lpc11u35_y5_mbug`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:lpc11u35_y5_mbug]
  platform = nxplpc
  board = lpc11u35_y5_mbug

You can override default y5 LPC11U35 mbug settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `lpc11u35_y5_mbug.json <https://github.com/platformio/platform-nxplpc/blob/master/boards/lpc11u35_y5_mbug.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:lpc11u35_y5_mbug]
  platform = nxplpc
  board = lpc11u35_y5_mbug

  ; change microcontroller
  board_build.mcu = lpc11u35

  ; change MCU frequency
  board_build.f_cpu = 48000000L


Uploading
---------
y5 LPC11U35 mbug supports the next uploading protocols:

* ``blackmagic``
* ``jlink``
* ``mbed``

Default protocol is ``mbed``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:lpc11u35_y5_mbug]
  platform = nxplpc
  board = lpc11u35_y5_mbug

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

y5 LPC11U35 mbug does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_blackmagic`
    - 
    - Yes
  * - :ref:`debugging_tool_jlink`
    - 
    - 

Frameworks
----------
.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_mbed`
      - Arm Mbed OS is an open source embedded operating system designed specifically for the 'things' in the Internet of Things. It includes all the features you need to develop a connected product based on an Arm Cortex-M microcontroller, including security, connectivity, an RTOS and drivers for sensors and I/O devices