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

.. _board_atmelsam_sainSmartDueUSB:

SainSmart Due (USB Native Port)
===============================

.. contents::

Hardware
--------

Platform :ref:`platform_atmelsam`: Atmel | SMART offers Flash- based ARM products based on the ARM Cortex-M0+, Cortex-M3 and Cortex-M4 architectures, ranging from 8KB to 2MB of Flash including a rich peripheral and feature mix.

.. list-table::

  * - **Microcontroller**
    - AT91SAM3X8E
  * - **Frequency**
    - 84MHz
  * - **Flash**
    - 512KB
  * - **RAM**
    - 96KB
  * - **Vendor**
    - `SainSmart <http://www.sainsmart.com/arduino/control-boards/sainsmart-due-atmel-sam3x8e-arm-cortex-m3-board-black.html?utm_source=platformio.org&utm_medium=docs>`__


Configuration
-------------

Please use ``sainSmartDueUSB`` ID for :ref:`projectconf_env_board` option in :ref:`projectconf`:

.. code-block:: ini

  [env:sainSmartDueUSB]
  platform = atmelsam
  board = sainSmartDueUSB

You can override default SainSmart Due (USB Native Port) settings per build environment using
``board_***`` option, where ``***`` is a JSON object path from
board manifest `sainSmartDueUSB.json <https://github.com/platformio/platform-atmelsam/blob/master/boards/sainSmartDueUSB.json>`_. For example,
``board_build.mcu``, ``board_build.f_cpu``, etc.

.. code-block:: ini

  [env:sainSmartDueUSB]
  platform = atmelsam
  board = sainSmartDueUSB

  ; change microcontroller
  board_build.mcu = at91sam3x8e

  ; change MCU frequency
  board_build.f_cpu = 84000000L


Uploading
---------
SainSmart Due (USB Native Port) supports the following uploading protocols:

* ``atmel-ice``
* ``blackmagic``
* ``jlink``
* ``sam-ba``
* ``stlink``

Default protocol is ``sam-ba``

You can change upload protocol using :ref:`projectconf_upload_protocol` option:

.. code-block:: ini

  [env:sainSmartDueUSB]
  platform = atmelsam
  board = sainSmartDueUSB

  upload_protocol = sam-ba

Debugging
---------

:ref:`piodebug` - "1-click" solution for debugging with a zero configuration.

.. warning::
    You will need to install debug tool drivers depending on your system.
    Please click on compatible debug tool below for the further
    instructions and configuration information.

You can switch between debugging :ref:`debugging_tools` using
:ref:`projectconf_debug_tool` option in :ref:`projectconf`.

SainSmart Due (USB Native Port) does not have on-board debug probe and **IS NOT READY** for debugging. You will need to use/buy one of external probe listed below.

.. list-table::
  :header-rows:  1

  * - Compatible Tools
    - On-board
    - Default
  * - :ref:`debugging_tool_atmel-ice`
    - 
    - Yes
  * - :ref:`debugging_tool_blackmagic`
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

    * - :ref:`framework_arduino`
      - Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences.